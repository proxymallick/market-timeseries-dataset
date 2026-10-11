"""Inventory local files without copying or transforming them."""
import csv, json, os, re, hashlib
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlsplit
import pandas as pd
import pyarrow.parquet as pq

BASE = Path(__file__).resolve().parents[1]
WORK = BASE.parent
HOME = Path.home()
FIELDS = 'original_path,file_name,format,size_bytes,row_count,date_start,date_end,frequency,columns,units_currency,instruments,timezone_adjustments,category,source,source_evidence,notes'.split(',')
SKIP = {'.git','.venv','venv','node_modules','__pycache__','.cache','Library','.ssh','.codex','.config','.Trash'}
EXT = {'.csv','.tsv','.parquet','.feather','.h5','.hdf5','.json','.jsonl','.xlsx','.xls','.sqlite','.sqlite3','.db','.duckdb','.zip','.gz','.xz','.tar','.bin','.txt','.raw'}
roots = [HOME/'Documents', HOME/'Downloads', HOME/'Desktop',HOME/'Public', HOME/'Models',HOME/'.qlib']
errors=[]; candidates=[]; exclusions=[]
for root in roots:
    if not root.exists(): continue
    for d, dirs, files in os.walk(root, onerror=lambda e: errors.append(str(e))):
        dirs[:] = [n for n in dirs if n not in SKIP and Path(d,n)!=BASE and not re.search(r'credential|secret',n,re.I)]
        for name in files:
            p=Path(d,name)
            if name.startswith('.env') or re.search(r'credential|secret|private.?key|token',name,re.I): continue
            if p.suffix.lower() not in EXT: continue
            # Names are enough to exclude personal documents without opening them.
            relevant = (WORK in p.parents or HOME/'.qlib' in p.parents or 'ML model futures contracts' in p.parts or name in {'ADA_1min.csv','ADA_1min.csv.zip'})
            if relevant: candidates.append(p)
            else: exclusions.append(str(p))

raw_sources={}
idx=WORK/'data/raw/economic_events/index.json'
if idx.exists():
    for url, entries in json.loads(idx.read_text()).items():
        u=urlsplit(url); safe=f'{u.scheme}://{u.hostname}{u.path}'
        for entry in entries: raw_sources[entry['file']]=safe

def provenance(p):
    s=str(p).lower()
    rules=[('fincast', 'FinCast-Paper-test','https://huggingface.co/datasets/Vincent05R/FinCast-Paper-test'),('binance','Binance','https://data.binance.vision/'),('futures_daily','Yahoo Finance via yfinance','local data/manifests/futures_daily_21_v1.yaml'),('hyperliquid','Hyperliquid Open Book','https://doi.org/10.5281/zenodo.18184441'),('cftc','CFTC','local data/manifests and data/raw/macro/README.md'),('treasury','US Treasury','local data/manifests/us_treasury_curve_daily_2006_2025_v1.yaml'),('rba_f2','Reserve Bank of Australia','local data/manifests/rba_f2_government_yields_2013_2025_v1.yaml')]
    if p.name in raw_sources: return urlsplit(raw_sources[p.name]).hostname,raw_sources[p.name]
    if 'economic_events' in s: return 'ABS; Federal Reserve; AOFM; USDA (partition-dependent)','local economic_events/sources.md; source field in table'
    for token,src,evidence in rules:
        if token in s: return src,evidence
    return 'UNKNOWN','UNKNOWN'

rows=[]
for p in candidates:
    if 'ML model futures contracts' in p.parts: continue # independently inventoried
    if p.relative_to(WORK).parts[0] in {'output','runs','tmp','submission_full_verified','reports'} if WORK in p.parents else False: continue
    # Keep configuration visible in the audit without treating it as data.
    if p.suffix=='.json' and 'data' not in p.parts: continue
    if p.suffix=='.txt' and HOME/'.qlib' not in p.parents and 'data' not in p.parts: continue
    r={k:'UNKNOWN' for k in FIELDS}
    r.update(original_path=str(p),file_name=p.name,format=p.suffix[1:],size_bytes=p.stat().st_size,category='markets',notes='Licensing UNVERIFIED; original retained')
    r['source'],r['source_evidence']=provenance(p)
    if 'economic_events' in str(p): r['category']='economic events'
    elif 'macro' in p.parts or any(x in str(p) for x in ['wasde','cftc','treasury','rba_f2']): r['category']='time series'
    df=None
    try:
        if p.suffix=='.parquet':
            pf=pq.ParquetFile(p); names=pf.schema_arrow.names
            r['row_count']=pf.metadata.num_rows; r['columns']=json.dumps(names)
            wanted=[n for n in names if n.lower() in {'timestamp','date','datetime','event_timestamp_utc','item_id','symbol','source','frequency','unit','currency','event_time_utc','country','release_timestamp_utc'}]
            df=pf.read(columns=wanted).to_pandas() if wanted else None
            r['notes']+='; row count exact Parquet metadata'
        elif p.suffix in {'.csv','.tsv'} and p.stat().st_size<100_000_000:
            df=pd.read_csv(p,sep='\t' if p.suffix=='.tsv' else ',',low_memory=False)
            r['row_count']=len(df); r['columns']=json.dumps(list(df.columns));r['notes']+='; row count exact parsed table'
        elif p.suffix in {'.zip','.xz','.gz','.tar'}:
            r['notes']+='; archive not expanded; overlaps extracted files where present'
        elif p.suffix=='.raw':
            r['notes']+='; immutable source response, not observation rows'
        elif p.suffix=='.bin':
            r['notes']+='; Qlib binary feature storage; count/date mapping requires provider decoder'
        elif p.suffix=='.json':
            r['notes']+='; JSON sidecar/metadata candidate; not counted as independent observations'
        if df is not None:
            for c in df.columns:
                lc=str(c).lower()
                if lc in {'timestamp','date','datetime','event_timestamp_utc','event_time_utc','release_timestamp_utc'}:
                    dt=pd.to_datetime(df[c],errors='coerce',utc=True)
                    if dt.notna().any():
                        r['date_start']=str(dt.min());r['date_end']=str(dt.max())
                        r['timezone_adjustments']='Date comparison normalized to UTC; source timezone UNVERIFIED'
                        if lc.endswith('_utc'):r['timezone_adjustments']='UTC field in schema'
                if lc in {'symbol','item_id'}:r['instruments']=json.dumps(sorted(map(str,df[c].dropna().unique())))
                if lc in {'source','frequency','unit','currency'}:
                    vals='; '.join(map(str,df[c].dropna().unique()))
                    if lc=='source' and vals:r['source']=vals
                    elif lc=='frequency' and vals:r['frequency']=vals
                    elif vals:r['units_currency']=vals
    except Exception as e:r['notes']+=f'; extraction incomplete: {type(e).__name__}'
    rows.append(r)

BASE.joinpath('docs').mkdir(parents=True,exist_ok=True)
with (BASE/'docs/primary_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
(BASE/'docs/discovery_scope.json').write_text(json.dumps({'roots':list(map(str,roots)),'candidate_count':len(candidates),'excluded_nonproject_candidates':len(exclusions),'errors':errors,'mounted_volumes':[p.name for p in Path('/Volumes').iterdir()],'excluded_directories':sorted(SKIP),'notes':'Macintosh HD is current filesystem; GitHub Copilot volume is an app installer. No external dataset volume found. Personal files not opened; archives not extracted; credentials excluded. Hidden tool caches excluded. JSON outside data dirs treated as config, not datasets.'},indent=2))
print(json.dumps({'primary_files':len(rows),'candidate_count':len(candidates),'errors':errors}))

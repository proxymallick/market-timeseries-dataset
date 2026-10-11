import csv,json,hashlib,re,struct
from pathlib import Path
from collections import Counter,defaultdict
import pandas as pd
import pyarrow.parquet as pq
BASE=Path(__file__).resolve().parents[1]; WORK=BASE.parent
files=['primary_inventory.csv','futures_inventory.csv','derived_and_copies_inventory.csv']
rows=[]
for name in files:
    with (BASE/'docs'/name).open() as f: rows.extend(csv.DictReader(f))
fields=list(rows[0])+['dataset_role','duplicate_group','overlap_group','metadata_status']
seen=set(); unique=[]
cal=Path.home()/'.qlib/qlib_data/cn_data/calendars/day.txt'
dates=cal.read_text().splitlines() if cal.exists() else []
hashes=defaultdict(list)
for r in rows:
    p=Path(r['original_path']); s=str(p).lower()
    if str(p) in seen:continue
    seen.add(str(p))
    for k in list(r):
        if not r[k]:r[k]='UNKNOWN'
    if r['category'] not in {'markets','time series','economic events'}:
        r['category']='time series' if any(t in s for t in ['cftc','wasde','treasury','rba_f2']) else 'markets'
    r['dataset_role']='observations'
    if any(t in p.parts for t in ['runs','reports','paper']) or '__splits' in p.name or any(t in p.name for t in ['coverage','quality','validation','metrics']):r['dataset_role']='analysis_or_model_artifact'
    if 'output' in p.parts or ('tmp' in p.parts and 'economic_events_initial_unvalidated' not in s):r['dataset_role']='packaged_copy_or_analysis'
    if r['dataset_role'] in {'analysis_or_model_artifact','packaged_copy_or_analysis'}:r['category']='time series'
    if p.suffix in {'.zip','.gz','.xz','.tar'} and r['dataset_role']=='observations':r['dataset_role']='archive'
    if p.suffix=='.raw':r['dataset_role']='raw_source_document'
    if p.suffix=='.json':r['dataset_role']='metadata_sidecar'
    if p.name.endswith('_items.parquet'):r['dataset_role']='instrument_metadata'
    if r['dataset_role']=='observations' and p.suffix=='.parquet' and 'macro' in p.parts:
        pf=pq.ParquetFile(p);names=pf.schema_arrow.names
        cols=[n for n in ['observation_timestamp','instrument'] if n in names]
        df=pf.read(columns=cols).to_pandas()
        if 'observation_timestamp' in df:
            r['date_start']=str(df.observation_timestamp.min());r['date_end']=str(df.observation_timestamp.max())
            r['timezone_adjustments']='UTC observation and separate availability timestamps in Arrow schema; availability methodology in source manifest'
        if 'instrument' in df:r['instruments']=json.dumps(sorted(df.instrument.unique()))
        r['frequency']='weekly' if 'cftc' in s else 'daily observed dates'
        r['units_currency']='contracts' if 'cftc' in s else 'yield percent'
    manifest=WORK/'data/manifests'/f'{p.stem}.yaml'
    if manifest.exists():
        text=manifest.read_text()
        for key,dest in [('frequency','frequency'),('timezone','timezone_adjustments')]:
            match=re.search(r'^'+key+r':\s*(.+)$',text,re.M)
            if match:r[dest]='Manifest: '+match.group(1)
    if r['frequency']=='UNKNOWN':
        match=re.search(r'(?:_|/)(1m|5min|1h|1d|1wk)(?:_|\.|/|$)',s)
        if match:r['frequency']='Filename granularity: '+match.group(1)+'; observed gaps UNVERIFIED'
    if 'source_policy_snapshots' in s:r['dataset_role']='source_policy_document'
    if 'economic_events_initial_unvalidated' in s:r['dataset_role']='superseded_unvalidated'
    if 'economic_events' in s:r['category']='economic events'
    if 'futures_daily' in s:
        r['source']='Yahoo Finance via yfinance';r['source_evidence']=str(WORK/'data/manifests/futures_daily_21_v1.yaml')
        r['frequency']='daily observed bars';r['timezone_adjustments']='Manifest: UTC, back-adjusted continuous futures; roll procedure UNVERIFIED'
    if '/.qlib/' in s:
        r['source']='UNKNOWN';r['source_evidence']='Local Qlib cn_data provider directory; upstream vendor UNVERIFIED'
        r['frequency']='daily provider calendar';r['overlap_group']='qlib_cn_daily'
        if p.suffix=='.bin' and int(r['size_bytes'])>=4 and int(r['size_bytes'])%4==0:
            with p.open('rb') as f: start=int(struct.unpack('<f',f.read(4))[0])
            count=int(r['size_bytes'])//4-1;r['row_count']=count
            r['columns']=p.name;r['instruments']=p.parent.name
            if 0<=start<len(dates) and start+count<=len(dates):r['date_start']=dates[start];r['date_end']=dates[start+count-1]
            r['notes']+='; Qlib float32 layout: leading calendar offset, then stored feature slots (including missing values); not trades'
    if 'fincast-fts/datasets' in s:
        r['source']='FinCast-Paper-test';r['source_evidence']=str(WORK/'FinCast-fts/README.md')+'; https://huggingface.co/datasets/Vincent05R/FinCast-Paper-test'
    groups=['economic_events','futures_daily','fincast','binance','hyperliquid','coinbase','fi2010','cftc','treasury','rba_f2','wasde']
    r.setdefault('overlap_group',next((t for t in groups if t in s),'UNVERIFIED'))
    r['duplicate_group']='UNVERIFIED';r['metadata_status']='Partial metadata; UNKNOWN fields require verification; licenses UNVERIFIED'
    # Large archives are excluded so this pass stays bounded.
    if p.is_file() and int(r['size_bytes'])<=2_000_000 and r['dataset_role'] not in {'analysis_or_model_artifact','packaged_copy_or_analysis'}:
        digest=hashlib.sha256(p.read_bytes()).hexdigest();hashes[digest].append(r)
    unique.append(r)
for digest, members in hashes.items():
    if len(members)>1:
        for r in members:r['duplicate_group']='sha256:'+digest
with (BASE/'docs/dataset_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(unique)
summary={}
for cat in ['markets','time series','economic events']:
    rr=[r for r in unique if r['category']==cat]
    summary[cat]={'physical_files':len(rr),'size_bytes':sum(int(r['size_bytes']) for r in rr),'roles':dict(Counter(r['dataset_role'] for r in rr)),'unknown_row_counts':sum(r['row_count']=='UNKNOWN' for r in rr)}
summary['duplicate_groups_verified']=sum(len(v)>1 for v in hashes.values())
summary['total_files']=len(unique)
(BASE/'docs/inventory_summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))

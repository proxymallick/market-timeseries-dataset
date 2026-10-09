"""Local-only curated selection and independent restricted copies; no network/upload."""
import csv,json,hashlib,re
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from copy_data import copy_without_overwrite
from release_selection import require_public_sources
from release_companions import add_lossless_parquet_companion

BASE=Path(__file__).resolve().parents[1];WORK=BASE.parent;HOME=Path.home()
audit=list(csv.DictReader((BASE/'docs/license_audit.csv').open()))
inventory={r['original_path']:r for r in csv.DictReader((BASE/'docs/dataset_inventory.csv').open())}
registry=json.loads((BASE/'docs/source_license_registry.json').read_text())
require_public_sources(['abs','fed','aofm','rba_events','usda','hyperliquid_hourly','cftc','rba_f2'],registry,True)
for directory in ['data/markets','data/timeseries','data/events','data_restricted','metrics','hosting','paper']:(BASE/directory).mkdir(parents=True,exist_ok=True)
manifest=[];transforms=[];stats=[];public_originals=set()

def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
    return h.hexdigest()

def add_copy(source,target,families,conditions,description):
    require_public_sources(families,registry,bool(conditions))
    source=Path(source);target=BASE/target
    method=copy_without_overwrite(source,target)
    sha=digest(target)
    assert sha==digest(source)
    public_originals.add(str(source))
    entry={'path':str(target.relative_to(BASE)),'bytes':target.stat().st_size,'sha256':sha,'source_dependencies':families,'licenses':[registry[k]['license_name'] for k in families],'conditions_satisfied':conditions,'description':description,'source_locator':str(source.relative_to(HOME))}
    if target.suffix=='.parquet':entry['row_count']=pq.ParquetFile(target).metadata.num_rows
    manifest.append(entry)
    transforms.append({'output':entry['path'],'operation':'byte-preserving independent copy','copy_method':method,'source_sha256':sha,'output_sha256':sha,'rows_removed':0,'values_changed':0})

def table_statistics(dataset_id,path,category,description,source_ids,frequency,units,temporal_field):
    path=Path(path)
    if path.suffix=='.csv':
        # Raw CFTC wide table: compute count/date facts using two documented fields.
        df=pd.read_csv(path,usecols=['Report_Date_as_YYYY-MM-DD','Market_and_Exchange_Names'],low_memory=False)
        full_cols=next(csv.reader(path.open()))
        timestamp=pd.to_datetime(df['Report_Date_as_YYYY-MM-DD'],errors='raise')
        nitems=int(df['Market_and_Exchange_Names'].nunique())
        schema={'format':'CSV','columns':full_cols,'units':'Contract_Units column; not one common unit','timezone':'date-only weekly observation dates','adjustment':'Futures and options combined; published positioning, not price bars'}
        nulls={c:int(df[c].isna().sum()) for c in df.columns}
    else:
        table=pq.read_table(path);df=table.to_pandas();timestamp=df[temporal_field] if temporal_field in df else pd.Series([],dtype='datetime64[ns]')
        if temporal_field in df:timestamp=pd.to_datetime(df[temporal_field],utc=True,errors='raise')
        key=next((k for k in ['item_id','instrument'] if k in df),None)
        nitems=int(df[key].nunique()) if key else None
        nulls={c:int(df[c].isna().sum()) for c in df.columns}
        schema={'format':'Parquet','fields':[{'name':f.name,'arrow_type':str(f.type),'nullable':f.nullable} for f in table.schema]}
    date_start=str(timestamp.min()) if len(timestamp) and timestamp.notna().any() else None
    date_end=str(timestamp.max()) if len(timestamp) and timestamp.notna().any() else None
    entry={'dataset_id':dataset_id,'path':str(path.relative_to(BASE)),'category':category,'description':description,'row_count':len(df),'column_count':len(full_cols) if path.suffix=='.csv' else len(df.columns),'frequency':frequency,'units':units,'timezone':'UTC if typed timestamps; date-only CFTC records stay dates','date_start':date_start,'date_end':date_end,'instrument_count':nitems,'size_bytes':sum(p.stat().st_size for p in path.rglob('*.parquet')) if path.is_dir() else path.stat().st_size,'source_dependencies':source_ids,'null_counts':nulls,'null_count_scope':'all columns' if path.suffix!='.csv' else 'two source/date columns only; other CSV columns UNVERIFIED'}
    if 'source_name' in df:entry['source_counts']=df.source_name.value_counts().to_dict()
    if 'event_category' in df:entry['event_category_counts']=df.event_category.value_counts().to_dict()
    if 'quality_status' in df:entry['quality_status_counts']=df.quality_status.value_counts().to_dict()
    if 'event_timestamp_utc' in df:
        dated=pd.to_datetime(df['event_date'],errors='raise')
        entry['publication_date_start']=str(dated.min().date());entry['publication_date_end']=str(dated.max().date())
        entry['timestamped_rows']=int(df.event_timestamp_utc.notna().sum());entry['year_counts']=dated.dt.year.value_counts().sort_index().to_dict()
    stats.append(entry)
    (BASE/f'docs/schema_{dataset_id}.json').write_text(json.dumps(schema,indent=2,default=str))

agency_conditions='Structured agency-origin factual release metadata only; no logos, imagery or third-party attachments. Agency attribution/license URLs in THIRD_PARTY_LICENSES.md; changes logged; source URLs and hashes retained.'
events=WORK/'data/processed/economic_events'
for source in sorted(events.rglob('events.parquet')):
    families=['abs'] if 'country=AU' in str(source) else ['fed']
    add_copy(source,Path('data/events/economic_events')/source.relative_to(events),families,agency_conditions,'Verified-time agency economic-event records; source values preserved')
table_statistics('economic_events',BASE/'data/events/economic_events','economic events','Release/document versions with explicit source release times',['abs','fed'],'event-level','Per-row currency/unit; most scalar values missing','event_timestamp_utc')

source=WORK/'data/processed/economic_events_quarantine.parquet'
table=pq.read_table(source);df=table.to_pandas()
allowed={'ABS','Federal Reserve','AOFM','RBA','USDA'}
mask=df.source_name.isin(allowed)
assert set(df.loc[mask,'source_name'].unique())==allowed
filtered=table.filter(pa.array(mask.tolist()))
target=BASE/'data/events/economic_events_review.parquet'
if target.exists():raise FileExistsError(target)
pq.write_table(filtered,target,compression='zstd')
manifest.append({'path':str(target.relative_to(BASE)),'bytes':target.stat().st_size,'sha256':digest(target),'row_count':filtered.num_rows,'source_dependencies':['abs','fed','aofm','rba_events','usda'],'licenses':[registry[k]['license_name'] for k in ['abs','fed','aofm','rba_events','usda']],'conditions_satisfied':agency_conditions,'description':'Separate review-only records; excludes unresolved FDIC source; not timestamp-eligible training data','source_locator':str(source.relative_to(HOME))})
transforms.append({'output':str(target.relative_to(BASE)),'operation':'Filter independently attributable agency rows; exclude FDIC rows with unresolved redistribution rights; Parquet ZSTD rewrite','source_sha256':digest(source),'output_sha256':digest(target),'rows_before':len(df),'rows_after':filtered.num_rows,'rows_removed':int((~mask).sum()),'removed_source_counts':df.loc[~mask,'source_name'].value_counts().to_dict(),'values_changed':0,'columns_changed':0})
assert filtered.equals(table.filter(pa.array(mask.tolist())))
table_statistics('economic_events_review',target,'economic events','Date-only or revision-review agency rows; separate from verified release-time data',['abs','fed','aofm','rba_events','usda'],'event-level / review only','Per-row currency/unit','event_timestamp_utc')

selections=[
 ('hyperliquid_hourly',WORK/'data/processed/hyperliquid_perp_hourly_2025_12_v1.parquet','data/markets/hyperliquid_hourly.parquet',['hyperliquid_hourly'],'Hourly OHLCVA derived from BTC/ETH/SOL perpetual trades','1 hour','Venue price/size units; amount=sum(price*size); no fiat conversion','timestamp'),
 ('cftc_tff',WORK/'data/processed/macro/cftc_tff_treasury_positions_2006_2025_v1.parquet','data/timeseries/cftc_tff.parquet',['cftc'],'Weekly Treasury futures TFF positioning','weekly observed reports','contracts','observation_timestamp'),
 ('rba_f2',WORK/'data/processed/macro/rba_f2_government_yields_2013_2025_v1.parquet','data/timeseries/rba_f2.parquet',['rba_f2'],'Daily interpolated Australian Government Security cash yields','daily observations; weekly publication schedule','yield percent','observation_timestamp'),
 ('cftc_disaggregated',HOME/'Documents/ML model futures contracts/datasets/cftc_cot/cftc_disaggregated_fut_and_opt_2018_2024.csv','data/timeseries/cftc_disaggregated_2018_2024.csv',['cftc'],'Published CFTC disaggregated futures-and-options combined positioning','weekly observed reports','Contract_Units source field; heterogeneous units','Report_Date_as_YYYY-MM-DD')]
for dataset_id,source,target,families,description,frequency,units,time_field in selections:
    if dataset_id=='hyperliquid_hourly':
        df=pq.read_table(source).to_pandas()
        assert not any(re.search(r'user|wallet|address|oid|cloid',c,re.I) for c in df.columns)
        conditions='Address-free aggregate fields verified; DataCite publisher-registered CC-BY-4.0 confirmed live; Albers et al. credit, DOI/license link and prior aggregation notice retained.'
    elif dataset_id=='rba_f2':conditions='RBA origin of F2 series confirmed by official CSV metadata; attribution and free-source disclosure; no endorsement; retain Financial Data section 5 terms and third-party caveat. Cash yields are not an RBA-administered benchmark.'
    else:conditions='Agency-origin numeric positioning table; no third-party images/seals; CFTC credit and source policy link; transforms documented.'
    add_copy(source,target,families,conditions,description)
    table_statistics(dataset_id,BASE/target,'markets' if dataset_id=='hyperliquid_hourly' else 'time series',description,families,frequency,units,time_field)
    if dataset_id=='cftc_disaggregated':
        companion_path=BASE/'data/timeseries/cftc_disaggregated_2018_2024.parquet'
        require_public_sources(families,registry,bool(conditions))
        companion,companion_manifest,companion_transform=add_lossless_parquet_companion(
            source_csv=source,
            release_csv=BASE/target,
            destination=companion_path,
            base=BASE,
            source_locator=str(source.relative_to(HOME)),
            source_dependencies=families,
            licenses=[registry[k]['license_name'] for k in families],
            conditions_satisfied=conditions,
            description='Lossless field-text Parquet companion to raw CFTC CSV; numbers, NA markers and empty strings not coerced',
        )
        assert companion.num_rows==stats[-1]['row_count']==83019
        manifest.append(companion_manifest)
        transforms.append(companion_transform)
        companion_schema={'fields':[{'name':field.name,'arrow_type':str(field.type),'nullable':field.nullable} for field in companion.schema]}
        (BASE/'docs/schema_cftc_disaggregated_parquet.json').write_text(json.dumps(companion_schema,indent=2,default=str))
        stats[-1].update({
            'companion_path':str(companion_path.relative_to(BASE)),
            'companion_size_bytes':companion_path.stat().st_size,
            'companion_dtype_policy':'all fields UTF-8 strings; empty fields remain empty strings',
        })

(BASE/'docs/release_manifest.json').write_text(json.dumps({'created_at_utc':datetime.now(timezone.utc).isoformat(),'status':'local preparation only; not published','files':manifest},indent=2))
(BASE/'docs/transformation_log.json').write_text(json.dumps(transforms,indent=2))
(BASE/'docs/dataset_statistics.json').write_text(json.dumps(stats,indent=2,default=str))
restricted=[]
excluded_roles={'analysis_or_model_artifact','packaged_copy_or_analysis','superseded_unvalidated','source_policy_document','metadata_sidecar'}
for row in audit:
    source=Path(row['original_path'])
    if str(source) in public_originals or row['dataset_role'] in excluded_roles:continue
    relative=source.relative_to(HOME)
    destination=BASE/'data_restricted/original_copies'/relative
    method=copy_without_overwrite(source,destination)
    assert destination.stat().st_size==source.stat().st_size
    restricted.append({'original_path':str(source),'copy_path':str(destination.relative_to(BASE)),'bytes':source.stat().st_size,'copy_method':method,'classification':row['classification'],'source_dependencies':row['source_dependencies'],'reason':'Unresolved rights, unmet artifact/privacy conditions or source copy not selected; do not publish'})
(BASE/'data_restricted/restricted_manifest.json').write_text(json.dumps(restricted,indent=2))
(BASE/'docs/local_preparation_summary.json').write_text(json.dumps({'public_files':len(manifest),'public_bytes':sum(r['bytes'] for r in manifest),'public_table_rows':{s['dataset_id']:s['row_count'] for s in stats},'restricted_copy_files':len(restricted),'restricted_logical_bytes':sum(r['bytes'] for r in restricted),'restricted_copy_methods':dict(Counter(r['copy_method'] for r in restricted))},indent=2))
print((BASE/'docs/local_preparation_summary.json').read_text())

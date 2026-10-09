"""Generate per-file audit and human-readable family report from verified evidence."""
import csv,json,hashlib,shutil
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
from release_selection import classify_dependencies
BASE=Path(__file__).resolve().parents[1]
IDS={'government':['cftc','treasury','usda','fed','fdic'],'australia':['abs','rba_events','rba_f2','aofm'],'academic':['fi2010','hyperliquid','hyperliquid_hourly','coinbase'],'markets':['yahoo','binance','fincast','qlib','unknown']}
registry={}
for group,ids in IDS.items():
    entries=json.loads((BASE/f'docs/audit_{group}.json').read_text())
    assert len(entries)==len(ids)
    for key,value in zip(ids,entries):registry[key]=value
for key in ['hyperliquid','hyperliquid_hourly']:
    r=registry[key]
    r['terms_urls'].append('https://api.datacite.org/dois/10.5281/zenodo.18184441')
    r['verification_status']+='; fresh authoritative DOI registry HTTP 200 confirms CC-BY-4.0, creators and title'
    r['evidence_summary']+=' Primary-agent follow-up captured current DataCite DOI metadata, which confirms the publisher-registered CC-BY-4.0 grant. Zenodo record UI/API availability remains unverified.'
    r['accessed_at_utc']='2026-10-09T12:42:45Z'
registry['yahoo']['verification_status']='Official Yahoo Terms HTML captured HTTP 200 by public GET; sections 6(b), API license and automated-collection restrictions inspected. Direct web tool returned 999; acquisition-specific entitlements remain unverified.'
registry['yahoo']['restrictions']='Yahoo/provider IP and API terms apply; no written permission supplied. yfinance software license does not license data. Source exchange entitlements and historical terms remain unverified.'
registry['yahoo']['accessed_at_utc']='2026-10-09T12:42:45Z'
for key,entry in registry.items():
    entry['commercial_permitted']=key in {'abs','fed','cftc','usda','rba_events','rba_f2','aofm','hyperliquid','hyperliquid_hourly'}
(BASE/'docs/source_license_registry.json').write_text(json.dumps(registry,indent=2))

def dependencies(row):
    path=row['original_path'].lower();src=(row['source']+' '+row['source_evidence']).lower()
    if row['dataset_role'] in {'analysis_or_model_artifact','packaged_copy_or_analysis'}:return ['unknown']
    if 'economic_events' in path:
        if '/country=au/' in path:return ['abs']
        if '/country=us/' in path:return ['fed']
        if 'quarantine' in path:return ['abs','fed','aofm','rba_events','usda','fdic']
        for token,key in [('federalreserve.gov','fed'),('abs.gov.au','abs'),('aofm.gov.au','aofm'),('rba.gov.au','rba_events'),('fdic.gov','fdic'),('usda.gov','usda')]:
            if token in src:return [key]
        return ['abs','fed'] if row['file_name']=='sample.csv' else ['unknown']
    if '/.qlib/' in path:return ['qlib']
    if 'futures_a1_s1' in path:return ['yahoo','treasury']
    if 'futures_a1_s2' in path:return ['yahoo','treasury','cftc']
    if 'futures_a1_s3' in path:return ['yahoo','treasury','cftc','usda']
    if 'futures_daily' in path or 'yahoo' in src:return ['yahoo']
    if 'fincast' in path:return ['fincast']
    if 'binance' in path:return ['binance']
    if 'hyperliquid' in path:return ['hyperliquid_hourly'] if 'hourly' in path else ['hyperliquid']
    if 'fi2010' in path:return ['fi2010']
    if 'coinbase' in path:return ['coinbase']
    if 'rba_f2' in path:return ['rba_f2']
    if 'treasury' in path:return ['treasury']
    if 'cftc' in path:return ['cftc']
    if 'wasde' in path:return ['usda']
    return ['unknown']

inventory=list(csv.DictReader((BASE/'docs/dataset_inventory.csv').open()))
fields=['original_path','file_name','category','dataset_role','source_dependencies','classification','license_name','spdx','redistribution','commercial_use','attribution','share_alike','derived_data_rules','restrictions','terms_urls','date_accessed_utc','verification_status','conditions_satisfied','release_decision','alternative']
out=[]
for row in inventory:
    deps=dependencies(row); entries=[registry[k] for k in deps]
    r={k:row[k] for k in ['original_path','file_name','category','dataset_role']}
    r['source_dependencies']=';'.join(deps);r['classification']=classify_dependencies([e['classification'] for e in entries])
    for key in ['license_name','spdx','redistribution','commercial_use','attribution','share_alike','derived_data_rules','restrictions','terms_urls','verification_status','alternative']:
        r[key]=' | '.join(json.dumps(e.get(key),ensure_ascii=False) if isinstance(e.get(key),(list,dict)) else str(e.get(key) or 'UNVERIFIED') for e in entries)
    r['date_accessed_utc']=';'.join(sorted(set(e['accessed_at_utc'] for e in entries)))
    r['conditions_satisfied']='not yet evaluated for this artifact'
    r['release_decision']='exclude until separately reviewed and recorded in release manifest'
    if row['dataset_role'] in {'analysis_or_model_artifact','packaged_copy_or_analysis','superseded_unvalidated'}:r['release_decision']='exclude: model artifact, copy or superseded development data'
    out.append(r)
with (BASE/'docs/license_audit.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(out)
families=Counter(k for r in out for k in r['source_dependencies'].split(';'))
labels={'safe':'✅ Safe to redistribute','conditional':'⚠️ Redistribute with conditions','restricted':'❌ Do not redistribute','unclear':'❓ Unclear'}
lines=['# Licensing audit — local preparation','', 'Accessed 2026-10-09 UTC. This is a technical rights review, not legal advice. Official dataset grants, API/service terms and venue policies were checked separately. Current venue policy does not conclusively establish historical contractual applicability; unresolved cases are excluded rather than asserted illegal.','', 'Every inventoried physical file is mapped in the private per-file CSV. Decisions are source-family classifications; they do not automatically clear every artifact. Release eligibility requires a separate conditions check. Original data are not moved.','', '| Source family | Status | Applicable license/terms | Affected files* |','|---|---|---|---:|']
for key,r in registry.items():lines.append(f"| {r['source_family']} | {labels[r['classification']]} | {r['license_name'] or 'UNVERIFIED'} | {families[key]} |")
lines+=['','* A multi-source file may appear in more than one family. Counts are physical files, not independent datasets.','', '## Evidence and obligations']
for key,r in registry.items():
    lines += ['',f"### {key}: {r['provider']}",'',r['evidence_summary'],'',f"- Redistribution: {r['redistribution']}",f"- Commercial use: {r['commercial_use']}",f"- Attribution: {r['attribution']}",f"- Share-alike: {r['share_alike']}",f"- Derived data: {r['derived_data_rules']}",f"- Restrictions: {json.dumps(r['restrictions'],ensure_ascii=False) if isinstance(r['restrictions'],list) else r['restrictions']}",f"- Verification: {r['verification_status']}; accessed {r['accessed_at_utc']}", '- Official sources: '+', '.join(f'[source {i+1}]({u})' for i,u in enumerate(r['terms_urls'])),f"- Alternative: {r['alternative']}"]
lines+=['','## Compatibility and release policy','', 'MIT is recommended for original code, curation logic and documentation only. It is concise and permissive; Apache-2.0 adds an express patent grant and NOTICE obligations, while GPL imposes software copyleft. None can replace upstream data rights. Upstream CC-BY attribution must remain even when curation code is MIT. RBA Financial Data terms are separate and must not be mislabeled CC-BY. Public-domain agency material remains identified as such, without asserting a worldwide statutory result for every inclusion.','', 'Binance NC/SA cannot be presented as a commercially reusable, permissively licensed combined dataset. Its derivative bars stay excluded from the main selection; an optional separately licensed noncommercial package is an owner decision. Yahoo, unresolved venue rights, unknown provenance and mixed tables with restricted inputs stay excluded. Filtering a mixed event file by independently attributable agency rows is logged and does not carry excluded FDIC records into the output. Aggregation alone is not presumed to cure restrictions.','', 'Raw HTML/PDF source bodies and wallet-linked archives require artifact/notice or privacy review before inclusion; attribution alone does not satisfy those checks. The processed selection will include only structured agency facts and address-free aggregates with checked source identities, license notices and documented changes. A readable release manifest records which conditions have actually been satisfied.','', '## Audit checkpoint','', 'The owner instructed completion of all requested local deliverables after approving discovery. This report is the audit checkpoint; remaining preparation is local only. No external push/upload or provider contact is approved. Permission-request drafts are unsent.']
(BASE/'docs/license_audit.md').write_text('\n'.join(lines)+'\n')
# Store agency evidence within the requested LICENSES directory too.
src=BASE/'docs/audit_evidence/government'
if src.exists():shutil.copytree(src,BASE/'LICENSES/government',dirs_exist_ok=True)
captures=[]
for p in sorted((BASE/'LICENSES').rglob('*')):
    if p.is_file() and p.name!='capture_manifest.json':captures.append({'path':str(p.relative_to(BASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
(BASE/'LICENSES/capture_manifest.json').write_text(json.dumps(captures,indent=2))
print(json.dumps({'files_audited':len(out),'families':len(registry),'classification_counts':dict(Counter(r['classification'] for r in out)),'license_evidence_files':len(captures)},indent=2))

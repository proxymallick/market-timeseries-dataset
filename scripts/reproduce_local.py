"""Rebuild the release from hash-pinned local inputs without overwriting them."""
import argparse,json,hashlib
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq
from copy_data import copy_without_overwrite
from csv_to_lossless_parquet import convert
from release_selection import require_public_sources
BASE=Path(__file__).resolve().parents[1]

def sha256(path):
    digest=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda:stream.read(8*1024*1024),b''):digest.update(chunk)
    return digest.hexdigest()

def reproduce(manifest,transforms,registry,source_home,output):
    output=Path(output).resolve();source_home=Path(source_home).resolve()
    if output.exists():raise FileExistsError(output)
    operations={r['output']:r for r in transforms}
    planned=[]
    for entry in manifest['files']:
        require_public_sources(entry['source_dependencies'],registry,bool(entry.get('conditions_satisfied')))
        source=(source_home/entry['source_locator']).resolve();destination=(output/entry['path']).resolve()
        if not source.is_relative_to(source_home) or not destination.is_relative_to(output):raise ValueError('Manifest path escapes its declared root')
        if source.suffix not in {'.csv','.parquet'}:raise ValueError('Only explicit CSV/Parquet inputs are accepted')
        if output.is_relative_to(source) or output==source:raise ValueError('Output must be separate from inputs')
        op=operations.get(entry['path'],{})
        expected=op.get('source_sha256',entry['sha256'])
        if sha256(source)!=expected:raise ValueError('Input bytes differ from pinned source; review before reproduction')
        planned.append((entry,source,destination))
    output.mkdir(parents=True)
    for entry,source,destination in planned:
        destination.parent.mkdir(parents=True,exist_ok=True)
        if entry['path'].endswith('economic_events_review.parquet'):
            table=pq.read_table(source);allowed={'ABS','Federal Reserve','AOFM','RBA','USDA'}
            mask=pa.array([x.as_py() in allowed for x in table['source_name']])
            pq.write_table(table.filter(mask),destination,compression='zstd')
        elif source.suffix=='.csv' and destination.suffix=='.parquet':convert(source,destination)
        else:copy_without_overwrite(source,destination)
        if sha256(destination)!=entry['sha256']:raise ValueError('Output hash differs; inspect dependency versions and transformation')
    return len(planned)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-home',type=Path,required=True,help='Root containing source_locator paths; source files must be lawfully held')
    parser.add_argument('--output',type=Path,required=True,help='New, nonexistent directory')
    args=parser.parse_args()
    n=reproduce(json.loads((BASE/'docs/release_manifest.json').read_text()),json.loads((BASE/'docs/transformation_log.json').read_text()),json.loads((BASE/'docs/source_license_registry.json').read_text()),args.source_home,args.output)
    print(f'Reproduced {n} hash-verified files locally; no upload performed.')

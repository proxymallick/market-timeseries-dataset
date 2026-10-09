"""Re-create independent private copies from an owner-held manifest; no downloads."""
import argparse
import json
from pathlib import Path
from copy_data import copy_without_overwrite

def reproduce(rows, output):
    output=Path(output).resolve()
    if output.exists():raise FileExistsError(output)
    checked=[]
    for row in rows:
        relative=Path(row['copy_path'])
        if relative.is_absolute() or '..' in relative.parts or not relative.parts or relative.parts[0]!='data_restricted':
            raise ValueError('Private copy path must remain inside data_restricted')
        source=Path(row['original_path'])
        if source.is_symlink() or not source.is_file():raise ValueError('Input must be a regular local file')
        if source.stat().st_size!=row['bytes']:raise ValueError('Input size changed; review original acquisition')
        checked.append((source,output/relative))
    output.mkdir(parents=True)
    for source,destination in checked:
        copy_without_overwrite(source,destination)
        if destination.stat().st_size!=source.stat().st_size:raise ValueError('Copy size mismatch')
    return len(checked)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    print(f'Created {reproduce(json.loads(args.manifest.read_text()),args.output)} private copies; not licensed for publication.')

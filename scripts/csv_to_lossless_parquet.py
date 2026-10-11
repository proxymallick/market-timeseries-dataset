"""Copy CSV fields to Parquet without type or null inference."""
import argparse,csv
from pathlib import Path
import pyarrow as pa
import pyarrow.csv as arrow_csv
import pyarrow.parquet as pq

def convert(source,destination):
    source=Path(source);destination=Path(destination)
    if destination.exists():raise FileExistsError(destination)
    with source.open(newline='',encoding='utf-8-sig') as stream:names=next(csv.reader(stream))
    if len(names)!=len(set(names)):raise ValueError('Duplicate CSV field names need an explicit mapping')
    options=arrow_csv.ConvertOptions(column_types={name:pa.string() for name in names},strings_can_be_null=False,null_values=[])
    table=arrow_csv.read_csv(source,convert_options=options)
    destination.parent.mkdir(parents=True,exist_ok=True)
    with destination.open('xb') as stream:pq.write_table(table,stream,compression='zstd')
    restored=pq.read_table(destination)
    if not restored.equals(table):raise ValueError('Parquet round-trip changed CSV field text')
    return table

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('source',type=Path);parser.add_argument('destination',type=Path)
    args=parser.parse_args();convert(args.source,args.destination)

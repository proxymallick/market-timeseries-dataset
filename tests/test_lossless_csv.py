import sys
from pathlib import Path
import pytest
import pyarrow.parquet as pq
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
try:
    from csv_to_lossless_parquet import convert
except ImportError:
    convert=None

def test_field_text_and_empty_values_survive_conversion(tmp_path):
    assert convert is not None,'CSV converter missing'
    source=tmp_path/'source.csv';source.write_text('code,value,note\n001,NA,"a,b"\n002,,"quoted text"\n')
    before=source.read_bytes();target=tmp_path/'out.parquet'
    convert(source,target)
    assert pq.read_table(target).to_pylist()==[{'code':'001','value':'NA','note':'a,b'},{'code':'002','value':'','note':'quoted text'}]
    assert source.read_bytes()==before
    with pytest.raises(FileExistsError):convert(source,target)

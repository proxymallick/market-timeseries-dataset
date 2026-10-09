import sys,json,hashlib
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
try:
    from reproduce_local import reproduce
except ImportError:
    reproduce=None

def test_reproduction_checks_source_integrity_and_refuses_existing_output(tmp_path):
    assert reproduce is not None,'reproduction tool missing'
    home=tmp_path/'inputs';home.mkdir();source=home/'table.csv';source.write_text('date,value\n2026-01-01,001\n')
    sha=hashlib.sha256(source.read_bytes()).hexdigest()
    m={'files':[{'path':'data/timeseries/table.csv','source_locator':'table.csv','sha256':sha,'source_dependencies':['cftc'],'conditions_satisfied':'Agency numeric facts and attribution'}]}
    reg={'cftc':{'classification':'conditional','commercial_permitted':True}}
    dest=tmp_path/'output';reproduce(m,[],reg,home,dest)
    assert (dest/'data/timeseries/table.csv').read_bytes()==source.read_bytes()
    with pytest.raises(FileExistsError):reproduce(m,[],reg,home,dest)
    source.write_text('changed input')
    with pytest.raises(ValueError):reproduce(m,[],reg,home,tmp_path/'changed')

def test_reproduction_rejects_path_escape_and_uncleared_source(tmp_path):
    assert reproduce is not None,'reproduction tool missing'
    reg={'cftc':{'classification':'conditional','commercial_permitted':True}}
    m={'files':[{'path':'../../escape.csv','source_locator':'table.csv','sha256':'0'*64,'source_dependencies':['cftc'],'conditions_satisfied':'checked'}]}
    with pytest.raises(ValueError):reproduce(m,[],reg,tmp_path,tmp_path/'output')
    m['files'][0].update(path='data/timeseries/table.csv',source_dependencies=['yahoo'])
    with pytest.raises(ValueError):reproduce(m,[],reg,tmp_path,tmp_path/'output2')

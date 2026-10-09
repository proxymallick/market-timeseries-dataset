import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))

def test_restricted_copy_preserves_input_and_rejects_escape(tmp_path):
    from reproduce_restricted import reproduce
    source=tmp_path/'source.csv';source.write_text('value\n001\n')
    rows=[{'original_path':str(source),'copy_path':'data_restricted/original_copies/source.csv','bytes':10}]
    output=tmp_path/'copy';reproduce(rows,output)
    copied=output/rows[0]['copy_path']
    assert copied.read_bytes()==source.read_bytes()
    assert copied.stat().st_ino!=source.stat().st_ino
    with pytest.raises(FileExistsError):reproduce(rows,output)
    rows[0]['copy_path']='../escape.csv'
    with pytest.raises(ValueError):reproduce(rows,tmp_path/'bad')

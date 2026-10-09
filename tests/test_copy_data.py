import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
try:
    from copy_data import copy_without_overwrite
except ImportError:
    copy_without_overwrite=None

def test_copy_is_independent_and_existing_destination_is_protected(tmp_path):
    assert copy_without_overwrite is not None, 'copy implementation missing'
    source=tmp_path/'source';source.write_bytes(b'original observation bytes')
    dest=tmp_path/'release'/'copy'
    copy_without_overwrite(source,dest)
    assert dest.read_bytes()==source.read_bytes()
    dest.write_bytes(b'changed independent copy')
    assert source.read_bytes()==b'original observation bytes'
    with pytest.raises(FileExistsError):copy_without_overwrite(source,dest)

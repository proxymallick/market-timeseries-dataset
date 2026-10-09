import shutil
import sys
from pathlib import Path

import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from release_companions import add_lossless_parquet_companion


def test_lossless_companion_registers_second_representation_without_new_rows(tmp_path):
    source = tmp_path / 'source.csv'
    release = tmp_path / 'release' / 'source.csv'
    destination = tmp_path / 'release' / 'source.parquet'
    source.parent.mkdir(exist_ok=True)
    source.write_text('code,value,marker\n0012,1.00,NA\n0007,,text\n', encoding='utf-8')
    release.parent.mkdir()
    shutil.copyfile(source, release)

    table, manifest, transform = add_lossless_parquet_companion(
        source_csv=source,
        release_csv=release,
        destination=destination,
        base=tmp_path,
        source_locator='source.csv',
        source_dependencies=['cftc'],
        licenses=['agency policy'],
        conditions_satisfied='attribution retained',
        description='Field-text companion',
    )

    restored = pq.read_table(destination)
    assert table.num_rows == restored.num_rows == 2
    assert restored.column('code').to_pylist() == ['0012', '0007']
    assert restored.column('value').to_pylist() == ['1.00', '']
    assert restored.column('marker').to_pylist() == ['NA', 'text']
    assert manifest['row_count'] == 2
    assert manifest['source_locator'] == 'source.csv'
    assert transform['rows_before'] == transform['rows_after'] == 2
    assert transform['values_changed'] == 0
    assert transform['representation_changed'] is True

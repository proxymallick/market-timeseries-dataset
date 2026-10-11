"""Record lossless companion formats in the release manifest."""
import hashlib
from pathlib import Path

from csv_to_lossless_parquet import convert


def _digest(path):
    hasher = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def add_lossless_parquet_companion(
    *, source_csv, release_csv, destination, base, source_locator,
    source_dependencies, licenses, conditions_satisfied, description,
):
    """Write a text-preserving Parquet companion and its audit records.

    The release CSV must match the source. The returned rows describe another
    format of the same data, so callers must not count it as a new dataset.
    """
    source_csv = Path(source_csv)
    release_csv = Path(release_csv)
    destination = Path(destination)
    base = Path(base)
    source_hash = _digest(source_csv)
    if _digest(release_csv) != source_hash:
        raise ValueError('Release CSV differs from original source bytes')

    table = convert(release_csv, destination)
    output_hash = _digest(destination)
    relative_output = str(destination.relative_to(base))
    manifest_entry = {
        'path': relative_output,
        'bytes': destination.stat().st_size,
        'sha256': output_hash,
        'source_dependencies': list(source_dependencies),
        'licenses': list(licenses),
        'conditions_satisfied': conditions_satisfied,
        'description': description,
        'source_locator': source_locator,
        'row_count': table.num_rows,
    }
    transform_entry = {
        'output': relative_output,
        'operation': 'CSV to Parquet ZSTD; preserve each CSV field as string, including literal NA/leading zeros/empty values; no numeric/date inference',
        'source_sha256': source_hash,
        'output_sha256': output_hash,
        'rows_before': table.num_rows,
        'rows_after': table.num_rows,
        'values_changed': 0,
        'representation_changed': True,
    }
    return table, manifest_entry, transform_entry

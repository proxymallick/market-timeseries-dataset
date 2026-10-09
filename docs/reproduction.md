# Reproducing the local selection

Install the pinned dependencies in a new virtual environment. The owner-provided source files remain immutable. `scripts/reproduce_local.py` rebuilds all proposed payload files using only lawfully held local inputs, with source SHA-256 checks, eligibility guards, a nonexisting output directory and output hash checks:

```sh
python scripts/reproduce_local.py --source-home /path/to/source-root --output /path/to/new-reproduction
```

`source_locator` in the release manifest is relative to that root. It is an input locator, not a download URL. The current locators describe the owner's directory layout; another researcher supplies a matching tree or reviews and updates locators while retaining source hashes. Missing or changed input bytes fail closed. In addition to byte-preserving copies, the rebuild filters the review-event table to independently attributable agency rows and reproduces the CFTC field-text Parquet companion. No value imputation, timestamp guessing, back-adjustment or resampling is performed here.

The upstream Hyperliquid hourly aggregation was already present and hash-pinned before this curation; this command preserves it rather than claiming to re-create raw trade aggregation from unpublished processing dependencies. Its source and previous aggregation operation are documented in the manifest and paper.

Restricted datasets can be reconstructed locally by retaining or independently copying the lawful inputs recorded in gitignored `data_restricted/restricted_manifest.json`. The independent copied source layer already exists in this preparation. The public package provides input-handling code and original-source links, not a downloader that bypasses vendor terms. Yahoo, FinCast, Coinbase, FI-2010, unknown Qlib provenance and detailed wallet-linked archives need their listed rights/privacy decisions before any public inclusion. Because unknown-source rows have no verified vendor, no acquisition URL is invented for them.

For an additional private reconstruction, run `python scripts/reproduce_restricted.py --manifest data_restricted/restricted_manifest.json --output /path/to/new-private-copy`. This uses only existing local inputs, checks recorded sizes, rejects path escapes and symlinks, and refuses an existing output directory. On APFS it creates independent copy-on-write files; elsewhere it may require the full logical disk space. Most large held inputs have no verified content hash, so size checks do not establish their acquisition authenticity or detect same-size alterations. This command grants no new reuse rights.

Official source endpoints and source-specific policies appear in `THIRD_PARTY_LICENSES.md` and the source license registry. Re-downloading current agency data may return revisions rather than the pinned snapshot; do not label a newly downloaded series byte-identical without comparing hashes. Original event source retrieval code remains in the owner's sibling economic_events project; this release records exact hashes and event-level provenance instead of promising access to every previously retrieved historical response.

The wide CFTC CSV additionally has a string-preserving Parquet representation. `scripts/csv_to_lossless_parquet.py source.csv new.parquet` preserves leading zeros, literal NA markers and empty field text. This prevents silent numeric/null inference. Researchers can explicitly type selected positioning columns after consulting the source units. The original CSV is retained.

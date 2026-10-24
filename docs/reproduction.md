# Reproducing the local selection

Install the pinned dependencies in a new virtual environment. `scripts/reproduce_local.py` rebuilds the payload from local inputs without writing to them. It verifies source hashes and eligibility, requires a new output directory, and checks the result:

```sh
python scripts/reproduce_local.py --source-home /path/to/source-root --output /path/to/new-reproduction
```

Each `source_locator` is relative to that root; it is not a download URL. The locators reflect my source layout. Another user must supply a matching tree or update the locators while retaining the recorded hashes. Missing or changed inputs fail closed. The rebuild also filters the review table to attributable agency rows and recreates the CFTC text-preserving Parquet companion. It does not impute values, guess timestamps, back-adjust, or resample.

The Hyperliquid hourly aggregation already existed and was hash-pinned before this curation. The command copies it; it does not claim to rebuild the bars from raw trades. The manifest and paper record the source and earlier aggregation.

The private Drive backup contains `data_restricted/restricted_manifest.json`, which can rebuild private copies from locally held inputs. I removed the redundant local backup on 2026-10-24 after verifying the Drive upload, so restore the manifest from the restricted folder before running the private-copy command. I provide input-handling code and source links, not a downloader that bypasses vendor terms. Yahoo, FinCast, Coinbase, FI-2010, unknown Qlib material, and detailed wallet-linked data remain out of any public selection until their rights or privacy questions are resolved. I do not invent acquisition URLs for unknown sources.

For another private copy, run `python scripts/reproduce_restricted.py --manifest /path/to/restored/restricted_manifest.json --output /path/to/new-private-copy`. It checks recorded sizes, rejects path escapes and symlinks, and refuses to overwrite a directory. On APFS it creates independent copy-on-write files; elsewhere it may need the full logical disk space. Most large held inputs have no verified content hash, so a size match cannot prove authenticity or detect a same-size change. Reconstructing a file grants no new reuse rights.

`THIRD_PARTY_LICENSES.md` and the source registry list the official endpoints and policies. A fresh agency download may contain revisions, so compare hashes before calling it identical to the pinned snapshot. The original event-retrieval code remains in the sibling `economic_events` project; this repository records exact hashes and event-level provenance instead of promising every historical response.

The wide CFTC CSV also has a text-preserving Parquet representation. `scripts/csv_to_lossless_parquet.py source.csv new.parquet` keeps leading zeroes, literal `NA` markers, and empty fields instead of inferring numbers or nulls. Convert individual fields only after checking their units and meaning. I retain the original CSV.

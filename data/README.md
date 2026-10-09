# Local data payload

Only the selection in `docs/release_manifest.json` belongs to the proposed public data payload. Files are local copies, not uploaded. Data bytes are gitignored: after approval, distribute them through Hugging Face or a versioned external host and archive a citable metadata/release snapshot on Zenodo. Source code, checksums, source-specific licenses and schemas remain in Git.

`markets/` contains address-free hourly aggregates. `timeseries/` contains yield and positioning observations with their own units and calendars. `events/` keeps timestamp-eligible events separate from date-only/revision-review records. Do not combine all tables as independent samples. Parquet is authoritative for typed nested event values; CSV retains the raw wide CFTC field text.

Uncleared or unselected source copies live only in gitignored `data_restricted/`, never in this payload. No original files were moved or overwritten.

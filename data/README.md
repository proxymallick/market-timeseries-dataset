# Prepared data

This directory contains only the 54 files listed in `docs/release_manifest.json`. I keep the actual data bytes out of Git and store private review archives separately. If I publish the collection later, the tables will need a versioned data host and a citable metadata release.

`events/` separates timestamp-verified releases from date-only and revision-review records. `timeseries/` contains yield and positioning data with source-specific units and calendars. `markets/` contains hourly aggregates without account addresses. These tables do not form one independent sample.

Parquet is the typed format for the event tables. For the wide CFTC data, the CSV is the source representation and the Parquet companion preserves every field as text. Restricted or unresolved source copies remain in the gitignored `data_restricted/` tree. I did not move or overwrite any original file when preparing this payload.

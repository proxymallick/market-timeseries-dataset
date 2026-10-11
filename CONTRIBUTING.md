# Contributing

I welcome corrections to the documentation, provenance records, schemas, and reproduction steps. This is still a private preparation. Do not publish data, contact a provider, create a DOI, or change repository visibility as part of a contribution.

Useful changes include fixing a source URL, documenting a verified term or attribution requirement, clarifying a transformation, or improving the explanation of availability timing. Keep restricted and unresolved sources out of `data/`. Never add credentials, private files, or local absolute paths.

## Data and provenance changes

Every data change must be reproducible. Update `docs/release_manifest.json`, `docs/dataset_statistics.json`, the relevant schema, and `docs/transformation_log.json` together. Record the source family, source locator, known retrieval or release date, terms, attribution, transformation, byte size, row count, and SHA-256 hash.

Preserve the source's date semantics. Observation time and public availability are different fields, and a date-only record must not be given an invented intraday timestamp. A null value is not zero.

Check `THIRD_PARTY_LICENSES.md` and `docs/license_audit.md` before proposing a source. A public download, repository license, or downloader's software license does not establish rights in the data itself. If the rights chain is unclear, keep the source held and record what evidence would resolve it. The audit documents evidence and uncertainty; it does not make legal findings.

## Writing style

Use direct language and measured figures from the current manifest and statistics. Explain incomplete scans, uncertain dates, and overlap where they matter. Keep source creators separate from my role as curator. Do not invent a DOI, affiliation, contact address, repository, or publication claim.

Before committing, check that:

- the change stays within the private preparation scope;
- rights, provenance, attribution, timestamps, units, and null semantics remain accurate;
- data changes include regenerated statistics and hashes; and
- local links point to the intended evidence or source.

Describe the evidence and affected files in the commit message or review note. There is no public issue tracker yet.

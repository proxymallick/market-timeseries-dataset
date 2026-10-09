# Contributing

Thank you for helping improve the documentation, provenance, or reproducibility of this local dataset preparation.

## Scope and current status

This checkout is a local, unpublished preparation snapshot. Do not upload data, create a public release, contact a provider, or push to a remote as part of a contribution. A repository owner must explicitly authorize a later external release. The six table products in `docs/release_manifest.json` are proposed selections, not blanket permission to redistribute all source material.

Useful contributions include correcting source URLs, documenting a verified license or attribution condition, explaining a transformation, adding a schema clarification, and improving time-availability guidance. Keep restricted or unresolved records out of `data/` and do not add credentials, local absolute paths, or private user files.

## Provenance and data changes

Every data change must be reproducible and must update `docs/release_manifest.json`, `docs/dataset_statistics.json`, the applicable schema, and `docs/transformation_log.json`. Record the source family, source locator, retrieval or release date when known, license/terms, attribution, changes, byte size, row count, and a cryptographic hash. Preserve source-provided date semantics and distinguish observation time from public availability time. Never invent intraday timestamps for date-only records or infer zeros from null values.

Before proposing a source for inclusion, check the applicable entries in `THIRD_PARTY_LICENSES.md` and `docs/license_audit.md`. A dataset-host license label, downloader's code license, or public download link does not itself establish the data rights chain. If a source is unclear, keep it held and document what evidence would resolve it. Do not write that a use is illegal unless a qualified legal determination supports that conclusion; the audit records evidence and unresolved scope, not legal advice.

## Documentation style

Use measured figures from the current machine-readable statistics and manifest. Qualify incomplete scans, null-count scope, source overlap, and uncertain dates explicitly. Distinguish source creators from this project's curator. Do not invent DOI, affiliation, repository, contact, or publication details.

## Review checklist

- The proposed change stays within the local preparation scope and does not publish, transmit, or push anything.
- Rights, provenance, attribution, and source-specific restrictions are accurately represented.
- Timestamps, units, missing values, frequencies, and coverage are described without changing their meaning.
- Statistics and hashes are regenerated or reconciled when data change.
- Links point to the local evidence files or the exact upstream source being described.

Open a local change for review with a concise explanation of its source evidence and the files affected. There is no public issue tracker or contribution URL at this stage.

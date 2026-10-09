# Owner checkpoint and remaining gates

## Local authorization and audit checkpoint

The owner authorized completion of all requested **local** preparation after discovery, including the licensing audit and draft publication documentation. The earlier discovery-only confirmation pause is complete and is not a remaining prerequisite for local work. The source-family audit was reviewed on 2026-10-09 UTC and is recorded in [`license_audit.md`](license_audit.md), the machine-readable [`source_license_registry.json`](source_license_registry.json), and supporting evidence under `LICENSES/`.

This is the audit checkpoint: 18 source-family decisions are recorded, every inventoried file has a local source-family mapping in the private file-level audit CSV, and proposed table products are separately named in the 54-file [`release_manifest.json`](release_manifest.json). The prepared tables total 106,875,828 bytes. This count is for the proposed table files, not the entire discovery inventory. The CFTC disaggregated table has a source CSV and a same-row-count text Parquet companion; the companion adds a representation, not another table. The selected set preserves uncertainty explicitly and does not claim blanket rights clearance. The detailed audit has limitations, including unresolved historical contract scope, product-level exceptions and incomplete scans described in the audit and dataset card.

All work documented here is local. No upload, remote push, external publication, DOI registration, or provider contact has occurred. Permission-request text in [`permission_requests.md`](permission_requests.md) is unsent. This checkpoint is not an approval to publish or a legal opinion.

## Local deliverables

- [x] Inventory original holdings without changing them; distinguish source records, copies, archives, and model/analysis artifacts.
- [x] Review available official source terms and record evidence/access dates, source-family classifications, conditions, and unresolved questions.
- [x] Prepare a proposed, hash-bearing release manifest, table statistics, and schemas. Keep restricted holdings out of the selected data products.
- [x] Document the collection in the README and dataset card; add loading guidance, source-specific attribution/rights notes, unsent permission-request drafts, and contribution instructions.
- [x] Add MIT terms for original project code, curation, and documentation only; clarify that no monolithic license applies to the data.
- [x] Add curator citation metadata without inventing a DOI, affiliation, public URL, or claim of source ownership.

## Completed local verification

These are execution and accuracy checks, not requests to re-authorize the audit:

- [x] Reconcile every proposed manifest path against the actual files, regenerate SHA-256 and size/row statistics after any data change, and confirm no held source, restricted copy, credential, local absolute path, or model artifact is in the selected set.
- [x] Run the repository's existing local validation and review scripts; record failures and scope limitations accurately. Do not claim tests passed without output evidence.
- [x] Recheck documentation links, license wording, citation metadata, and the measured figures against machine-readable artifacts.
- [x] Complete the dataset-only paper and figure/PDF visual inspection if those deliverables remain in scope; use no model performance claims.
- [x] Complete the host-metrics implementation/configuration checks if those deliverables remain in scope; no credentials should be stored.

## Owner decisions required before any external release

- [ ] Recheck all source terms and acquisition-date rights. In particular resolve or continue to hold Treasury and FDIC data; FI-2010 source-venue rights; the Coinbase CC0/source-terms conflict; FinCast vendor provenance; Qlib's original provider/license; and the Yahoo restricted exports/derivatives. Binance is not part of the proposed commercial-use selection under the audited NC-SA terms.
- [ ] Decide whether any separately scoped non-commercial Binance release is desired and verify all NC-SA and venue conditions before preparing it.
- [ ] Reassess the Hyperliquid source record's current license metadata and complete a privacy/linkability review before distributing detailed account/order data. The proposed hourly aggregate requires attribution and a check that no identifiers are present.
- [ ] Confirm author display name is accurate and optionally provide affiliation and a verified public contact channel; none is invented here. The known curator citation identifies Prakash Mallick but does not imply upstream data ownership.
- [ ] Select and verify public repository, release hosting, dataset hosting, and metrics identities. No GitHub repository, Hugging Face dataset, Zenodo record, DOI, Kaggle dataset, or identifier has been invented.
- [ ] Review the finished local package and provide a separate explicit instruction before any public push, upload, provider email, DOI registration, or release publication.

## Status

Current publication state is `not_published` in `hosting/config.local.json` and the local downloads badge data. No public hosting metrics are configured. The absence of a public identifier is intentional until one is selected and verified.

Local verification is recorded in [verification_report.md](verification_report.md). The local Git branch is `prepare-release`; it has no remote.

## Subsequent private hosting authorization

The owner authorized private GitHub and Google Drive copies on 2026-10-10 Sydney. The repository was created and pushed using the signed-in browser and GitHub Desktop. Ten prepared files were uploaded to the new Drive folder. See [private_hosting.md](private_hosting.md) for destinations. This supersedes the historical local-only boundary for these private copies; public publication, DOI registration and unresolved rights remain pending.

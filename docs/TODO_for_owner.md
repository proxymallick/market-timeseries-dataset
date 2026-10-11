# My release checklist

## Audit checkpoint

I completed the local preparation, licensing audit, and draft publication material after reviewing the discovery results. The source-family audit was checked on 2026-10-09 UTC and is recorded in [`license_audit.md`](license_audit.md), [`source_license_registry.json`](source_license_registry.json), and `LICENSES/`.

The audit records 18 source-family decisions and maps every inventoried file to a family in the private file-level CSV. The 54-file [`release_manifest.json`](release_manifest.json) names the prepared products, totaling 106,875,828 bytes. The CFTC CSV and text-preserving Parquet companion contain the same rows and count as one product. I preserve unresolved rights and incomplete scans instead of claiming blanket clearance.

Private GitHub and Drive copies now exist, but I have not published the dataset, registered a DOI, or contacted a provider. The drafts in [`permission_requests.md`](permission_requests.md) remain unsent. This checkpoint is neither publication approval nor a legal opinion.

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

## Decisions before a public release

- [ ] Recheck all source terms and acquisition-date rights. In particular resolve or continue to hold Treasury and FDIC data; FI-2010 source-venue rights; the Coinbase CC0/source-terms conflict; FinCast vendor provenance; Qlib's original provider/license; and the Yahoo restricted exports/derivatives. Binance is not part of the proposed commercial-use selection under the audited NC-SA terms.
- [ ] Decide whether any separately scoped non-commercial Binance release is desired and verify all NC-SA and venue conditions before preparing it.
- [ ] Reassess the Hyperliquid source record's current license metadata and complete a privacy/linkability review before distributing detailed account/order data. The proposed hourly aggregate requires attribution and a check that no identifiers are present.
- [ ] Confirm author display name is accurate and optionally provide affiliation and a verified public contact channel; none is invented here. The known curator citation identifies Prakash Mallick but does not imply upstream data ownership.
- [ ] Select and verify public repository, release hosting, dataset hosting, and metrics identities. No GitHub repository, Hugging Face dataset, Zenodo record, DOI, Kaggle dataset, or identifier has been invented.
- [ ] Review the finished local package and provide a separate explicit instruction before any public push, upload, provider email, DOI registration, or release publication.

## Status

The status is `private_preparation` in `hosting/config.local.json`. Private GitHub metrics are configured; public dataset-host metrics are not. I will add public identifiers only after selecting and verifying them.

Local verification is recorded in [verification_report.md](verification_report.md). The local Git branch is `prepare-release`; its origin is the private GitHub repository.

## Subsequent private hosting authorization

On 2026-10-10 Sydney, I authorized private GitHub and Google Drive copies. I created and pushed the repository through the signed-in browser and GitHub Desktop, then uploaded ten prepared files to Drive. [private_hosting.md](private_hosting.md) records the locations. Public release, DOI registration, and unresolved rights remain pending.

## Repository analytics access

Visitor and clone totals are unavailable on the current plan. Collecting them would require a plan that supports private Traffic Insights and repository Administration read access through the optional secret described in [github_analytics.md](github_analytics.md). I have not changed the plan or repository visibility.

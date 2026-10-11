# Preparation record

I completed the local inventory, audit, documentation, and prepared selection after the discovery review. I later authorized private GitHub and Drive copies, but not a public release, provider contact, or DOI registration. [`TODO_for_owner.md`](TODO_for_owner.md) records the remaining public-release decisions.

- [x] Inventory original datasets without modifying them; distinguish archives, copies, source documents and experiment/model outputs.
- [x] Verify current official licensing/source terms where available; retain evidence, access dates and family-level decisions. Unmatched source provenance remains UNKNOWN/unclear.
- [x] Prepare a local audit with conditions, compatibility notes and unsent permission-request drafts.
- [x] Prepare a local repository and MIT license for original code, curation and documentation only; preserve upstream terms.
- [x] Prepare a public-metadata-form catalog, table schemas, statistics and file-level manifest. Local absolute-path inventory and restricted source references must not be included in any future public package.
- [x] Build only the proposed conditional selection in `data/`, recording hashes, source dependencies, attribution and transformations. The selection remains unpublished and each upstream license continues to control.
- [x] Add a dataset card, citation files, loading and contribution guidance, and a local hosting setup. No DOI, repository URL, organization, or affiliation has been invented.
- [x] Prepare the dataset-only paper with verified references and measured statistics/figures; compile and visually inspect the PDF. No model benchmark results.
- [x] Implement or verify weekly host metrics collection with aggregate counts, unavailable values distinct from zero, traffic-window semantics, deduplication and offline checks. Do not store credentials.
- [x] Complete local file-coverage, restricted-data-exclusion, transformation/hash, documentation-link, citation, paper-build and relevant script checks before declaring the local package complete.

I kept source-specific tables and terms separate rather than pooling unlike frequencies and rights. I also kept the large restricted holdings out of Git: mirroring hundreds of gigabytes with Git LFS would be costly and would not solve the licensing questions. A permissive software license on a downloader does not make its data eligible.

## Publication boundary

The prepared selection contains 54 files totaling 106,875,828 bytes. The CFTC CSV and text-preserving Parquet file contain the same 83,019 rows and count as one product in two formats. I excluded held and restricted families and recorded the unresolved questions. A public host, provider contact, DOI, or release still requires a separate decision after those issues are reviewed.

Verification is recorded in [verification_report.md](verification_report.md). The `prepare-release` branch tracks the private GitHub repository.

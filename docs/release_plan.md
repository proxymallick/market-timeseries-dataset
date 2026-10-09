# Authorized local preparation plan

The owner authorized completion of all requested local preparation after discovery. The discovery-only approval pause is complete: the current licensing audit and local documentation work are authorized and have been prepared. This file records the work status and remaining local verification. **No external release, upload, remote push, provider contact, or DOI registration is authorized by that local instruction.** See [`TODO_for_owner.md`](TODO_for_owner.md) for the audit checkpoint and separate external-release gates.

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

Approach: retain separate source-specific tables and terms rather than pooling unlike frequencies and rights. Git LFS would make hundreds of gigabytes costly to mirror; a later host-manifest design can preserve provenance with a smaller Git history. A monolithic permissive data license cannot override third-party restrictions. A source is not eligible merely because a downloader's code is permissively licensed.

## Publication boundary

The local preparation summary reports 54 data files / 106,875,828 bytes in the proposed selection. All are status `local preparation only; not published`. The CFTC CSV and lossless field-text Parquet companion represent the same 83,019 rows; they are one table product in two formats. Held or restricted source families are excluded from that selection, with unresolved source and rights questions documented. Any later public hosting, push, external contact, DOI registration, or release requires a separate owner instruction after review of the concrete completed package and unresolved rights issues.

Local verification is recorded in [verification_report.md](verification_report.md). The local Git branch is `prepare-release`; it has no remote.

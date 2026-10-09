# Local preparation verification

Verified on 2026-10-09 UTC / 2026-10-10 Sydney. This report covers local preparation, not publication or legal clearance.

- The discovery inventory contains 56,653 physical files, 241,884,028,581 bytes across all categories. Counts include packages, copies and analysis artifacts; they are not unique datasets.
- The proposed selection contains 54 payload files, 106,875,828 bytes, across six table products. All 54 stored sizes and SHA-256 hashes match the manifest. A complete offline reconstruction produced the same 54 hashes.
- The CFTC CSV and Parquet companion agree field-for-field across 83,019 rows and 191 columns. The companion preserves strings, empty field text and leading zeros; it does not add observations.
- Independent review verified all 32,653 restricted copies: matching sizes, independent file identities, no symlinks and no overlap with selected original inputs. Their logical size is 237,154,298,717 bytes; APFS copy-on-write avoids allocating that entire amount immediately. Large held inputs were not all content-hashed.
- The review-event output contains 4,219 rows after removal of 577 FDIC rows whose redistribution rights remain unresolved. Retained source values agree with the filtered original. Review-only rows remain separate from timestamp-qualified events.
- `python -m pytest tests -q`: **19 passed**. Tests cover source eligibility, independent copies, lossless conversion and companion recording, manifest-based reproduction, private path containment, metrics pagination, windows and unavailable counters. `python -m compileall -q scripts` also passed.
- The original preparation builder was updated to include the companion and its metadata. It intentionally refuses existing outputs and was not rerun over the finished package. Its companion integration helper was tested separately.
- No broken local Markdown links or owner absolute paths were found in staged text files. CITATION.cff parses as YAML and has the required reviewed dataset identity fields; no full external CFF schema validator was run.
- All 17 paper citation keys resolve in references.bib. The self-contained LaTeX paper compiled with Tectonic into a five-page PDF. Every page was rendered and visually inspected; there are no LaTeX errors or overfull boxes. Remaining underfull notices concern table spacing. The initial built-in editor compile timed out fetching dependencies; the exported PDF was independently verified.
- The local Git repository excludes payload data, restricted copies, private file-level inventories, raw policy captures, credentials patterns, temporary reproductions and rendering images. The largest staged file is the portable inventory CSV, about 9.1 MB. Data hosting is configured as unpublished; no remote is configured.
- Metrics tests use deterministic API fixtures. No hosting identifiers exist, so no real download, star, view or clone measurements are claimed. GitHub owner traffic requires authorized authentication; keyless traffic requests correctly report unavailable. Zenodo record and all-version counters remain distinct.

The licensing audit identifies conditions and unresolved rights; it is a technical review, not a legal opinion. No original dataset was moved or overwritten. No provider was contacted, and nothing was pushed, uploaded, published or assigned a DOI. Owner decisions remain in TODO_for_owner.md.

## Repository analytics verification, 2026-10-09 UTC

All 25 local tests passed. A live authenticated CLI collection returned unavailable for this private repository (the existing CLI credential cannot access it); no visitor counts were invented. The rendered report preserves these unavailable values. Weekly Actions collection is configured to retain history and render the summary.

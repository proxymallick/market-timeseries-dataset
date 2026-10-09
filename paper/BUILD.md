# Dataset paper build

`main.tex` is intentionally self-contained so it can be opened and compiled by the built-in Codex LaTeX editor without extra project files. Its bibliography is embedded with `thebibliography`; `references.bib` is a parallel canonical BibTeX record set for archival and for later venue-template migration. Keep the citation keys and records aligned when editing either file.

For a local TeX installation with PGFPlots available:

```sh
pdflatex main.tex
pdflatex main.tex
```

The second pass resolves references. No BibTeX/Biber pass is required for this self-contained source. The row-count chart is drawn inline using PGFPlots, so no chart image or generated file is needed. The source states that the preparation is local and unpublished; do not add a DOI, repository link, release claim, or author affiliation until the owner confirms it.

The delivered five-page `main.pdf` was compiled with Tectonic (`tectonic --keep-logs main.tex`) and all pages were rendered for visual inspection. The build has no LaTeX errors or overfull boxes; remaining underfull-box notices concern table spacing. An initial built-in editor compile timed out while fetching TeX dependencies; the exported PDF was verified separately.

The measured statistics cited in the paper come from `../docs/dataset_statistics.json`, `../docs/inventory_summary.json`, `../docs/local_preparation_summary.json`, `../docs/transformation_log.json`, the corresponding schema JSON files, and the license audit/registry as of 9 October 2026. The current preparation manifest contains 54 files totaling 106,875,828 bytes. It includes both the 88 MB CFTC disaggregated CSV and its 16,201,232-byte lossless field-text Parquet companion; these are two representations of the same 83,019 records, counted once among the six table products. Regenerate the manifest and statistics before updating any counts or availability statements.

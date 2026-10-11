# Dataset paper build

I keep `main.tex` self-contained so it compiles without extra project files. The paper embeds its bibliography with `thebibliography`; `references.bib` is the parallel BibTeX record for archival use and a possible venue template. Keep their citation keys aligned.

For a local TeX installation with PGFPlots available:

```sh
pdflatex main.tex
pdflatex main.tex
```

The second pass resolves references. The build does not need BibTeX or Biber, and PGFPlots draws the row-count figure inline. Do not add a DOI, public download, release claim, or affiliation until it has been verified.

The current PDF is built with Tectonic (`tectonic --keep-logs main.tex`) and rendered page by page for inspection. Treat LaTeX errors, unresolved references, overfull boxes, clipping, and unreadable tables as build failures. Minor underfull table-spacing notices are acceptable after visual review.

The paper's measured figures come from `../docs/dataset_statistics.json`, `../docs/inventory_summary.json`, `../docs/local_preparation_summary.json`, `../docs/transformation_log.json`, the schemas, and the rights audit as of 9 October 2026. The manifest contains 54 files totaling 106,875,828 bytes. The 88 MB CFTC CSV and 16,201,232-byte text-preserving Parquet file contain the same 83,019 rows and count once. Regenerate the manifest and statistics before changing any count or availability statement.

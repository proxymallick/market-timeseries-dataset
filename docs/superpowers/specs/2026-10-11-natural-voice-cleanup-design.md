# Natural voice cleanup

## Goal

Rewrite the repository's hand-written prose so it sounds like Prakash Mallick wrote it: direct, specific, and consistent. The cleanup will remove generic boilerplate, repeated explanations, marketing language, and comments that merely restate the code.

## Voice

The README and supporting guides will use first person where authorship or a project decision matters: "I prepared", "I kept", and "I excluded". Instructions will stay direct. The dataset paper will remain academic, but it will use first person for the curator's work and decisions instead of an anonymous institutional voice.

The rewrite will avoid filler, excessive headings, dense bullet lists, and repeated disclaimers. It will not make the prose casual where legal, licensing, provenance, or temporal details require precision.

## Files in scope

The cleanup covers the hand-written repository documentation, including:

- `README.md`
- `DATASET_CARD.md`
- `CONTRIBUTING.md`
- `data/README.md`
- `THIRD_PARTY_LICENSES.md`
- hand-written guides under `docs/`
- `metrics/README.md`
- `paper/BUILD.md`
- comments and docstrings in project-authored Python and workflow files
- `paper/main.tex` and the rebuilt `paper/main.pdf`

Generated JSON, CSV, manifests, measured audit outputs, copied upstream licenses, source-policy evidence, and source datasets will not be rewritten. Fact-heavy generated Markdown reports will also remain unchanged when their wording is produced from measured evidence rather than maintained as narrative documentation.

## Editing rules

The rewrite will preserve every measured count, byte total, date, hash, path, URL, citation, license condition, status label, schema fact, code example, and data-availability distinction. It will not broaden redistribution rights, imply publication, invent affiliations or contact details, or soften unresolved provenance and licensing findings.

Comments will remain only when they explain a reason that is not obvious from the code, especially safeguards around timestamps, data fidelity, non-overwrite behavior, credentials, and rights. Module and function docstrings will be short descriptions of purpose or a non-obvious contract.

The main README will remain the entry point. Supporting documents will retain their current roles and links, so the cleanup will not reorganize the repository or change data-processing behavior.

## PDF workflow

The paper source will be rewritten in place and compiled to `paper/main.pdf`. The final PDF will retain its citations, tables, figures, page numbering, and measured facts. Every rendered page will be inspected for clipping, overlap, broken references, missing glyphs, and inconsistent layout.

## Verification

The final review will include:

1. the existing automated test suite;
2. a LaTeX build and log check;
3. page-by-page PDF rendering and visual inspection;
4. a diff review focused on factual and legal changes;
5. a scan for stale boilerplate, overlong comments, placeholders, and broken local links.

The completed cleanup will be committed locally in one implementation commit. It will not be pushed.

# Natural Voice Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the repository's hand-written prose and paper in Prakash Mallick's direct first-person voice without changing technical facts, legal conditions, or program behavior.

**Architecture:** Keep the existing file structure and documentation roles. Edit narrative prose in place, trim comments and docstrings to non-obvious intent, rebuild the LaTeX paper, and verify both content and rendering against the unchanged machine-readable evidence.

**Tech Stack:** Markdown, Python, GitHub Actions YAML, LaTeX, pytest, Poppler PDF rendering.

---

### Task 1: Establish the editing inventory

**Files:**
- Read: `README.md`
- Read: `DATASET_CARD.md`
- Read: `CONTRIBUTING.md`
- Read: `THIRD_PARTY_LICENSES.md`
- Read: `data/README.md`
- Read: `docs/*.md`
- Read: `metrics/README.md`
- Read: `paper/BUILD.md`
- Read: `paper/main.tex`
- Read: `scripts/*.py`

- [x] **Step 1: List all narrative Markdown, Python, workflow, and paper source files.**

Run: `rg --files -g '*.md' -g '*.py' -g '*.yml' -g '*.yaml' -g '*.tex'`

Expected: a complete list of hand-written candidates and generated evidence files.

- [x] **Step 2: Separate generated evidence from hand-written prose.**

Keep JSON, CSV, manifests, source evidence, generated audit reports, and copied licenses out of the edit set. Treat `docs/license_audit.md`, `docs/inventory_summary.md`, and `docs/verification_report.md` as measured reports unless a manually maintained note clearly requires correction.

### Task 2: Rewrite the main documentation

**Files:**
- Modify: `README.md`
- Modify: `DATASET_CARD.md`
- Modify: `CONTRIBUTING.md`
- Modify: `THIRD_PARTY_LICENSES.md`
- Modify: `data/README.md`

- [x] **Step 1: Rewrite the README as the direct project entry point.**

Use first person for curation decisions, preserve the six-product table and loading examples, remove stale publication boilerplate, and keep licensing and timing warnings concise.

- [x] **Step 2: Rewrite the dataset card in an academic first-person voice.**

Preserve every measured value and source qualification while replacing anonymous phrases such as “the collection” and “the curator” where personal authorship is clearer.

- [x] **Step 3: Rewrite contribution and data guidance.**

Use direct instructions, convert long checklists to prose where scanning does not improve, and retain safeguards around provenance, timestamps, restricted data, and source rights.

- [x] **Step 4: Tighten third-party license notes without changing their meaning.**

Keep source-specific rights, attribution, exclusions, and unresolved findings exact. Change only surrounding voice and repeated boilerplate.

### Task 3: Rewrite supporting guides and code annotations

**Files:**
- Modify: `docs/data_loading.md`
- Modify: `docs/github_analytics.md`
- Modify: `docs/hosting_and_metrics.md`
- Modify: `docs/permission_requests.md`
- Modify: `docs/private_hosting.md`
- Modify: `docs/release_plan.md`
- Modify: `docs/reproduction.md`
- Modify: `docs/TODO_for_owner.md`
- Modify: `metrics/README.md`
- Modify: `paper/BUILD.md`
- Modify: `scripts/*.py`

- [x] **Step 1: Rewrite hand-written guides in a concise first-person voice.**

Keep commands, paths, access states, GitHub limitations, Drive locations, and unsent permission drafts accurate.

- [x] **Step 2: Shorten comments and docstrings.**

Delete annotations that restate a function name or obvious assignment. Retain short explanations for overwrite prevention, timestamp eligibility, lossless text conversion, credential handling, and audit boundaries.

- [x] **Step 3: Scan for canned language.**

Run: `rg -n 'This repository contains|The collection|The curator|Thank you for|In particular|deliberately|intentionally|proposed public selection' README.md DATASET_CARD.md CONTRIBUTING.md THIRD_PARTY_LICENSES.md data docs metrics paper scripts`

Expected: remaining matches are factual terms or deliberate academic wording, not boilerplate.

### Task 4: Rewrite and rebuild the paper

**Files:**
- Modify: `paper/main.tex`
- Modify: `paper/main.pdf`
- Modify: `paper/qa/page-*.png`

- [x] **Step 1: Mark the PDF edit operation.**

Run: `node container_tools/mark_artifact_operation_started.mjs --operation-kind edit --expected-output-count 1 --output-format pdf`

Expected: successful artifact-operation acknowledgement.

- [x] **Step 2: Rewrite the paper source.**

Keep the academic structure, bibliography, tables, figures, and all measured facts. Use first person for the work performed and direct prose for limitations and release status.

- [x] **Step 3: Compile the PDF from `paper/main.tex`.**

Follow `paper/BUILD.md`, rerunning LaTeX as required for references and page numbers.

Expected: `paper/main.pdf` builds without errors or unresolved references.

- [x] **Step 4: Render and inspect every page.**

Run: `pdftoppm -png paper/main.pdf tmp/pdfs/main`

Expected: every page is legible with no clipped text, overlaps, missing glyphs, broken tables, or bad page transitions.

### Task 5: Verify and commit

**Files:**
- Verify: all modified files

- [x] **Step 1: Run automated checks.**

Run: `../economic_events/.venv/bin/python -m pytest tests -q`

Expected: all tests pass.

- [x] **Step 2: Check formatting and links.**

Run: `git diff --check`

Expected: no whitespace errors.

Run a local-link scan over edited Markdown and verify every repository-relative target exists.

Expected: no broken local links introduced by the rewrite.

- [x] **Step 3: Review factual changes.**

Compare dates, counts, byte totals, source names, status labels, citations, and legal conditions in the diff against the unchanged manifests and statistics.

Expected: style changes only, except for corrections required by the repository's current private-hosting status.

- [x] **Step 4: Commit the implementation.**

Run: `git add <edited files> && git commit -m "Rewrite documentation in a natural first-person voice"`

Expected: one local implementation commit on `prepare-release`; no push.

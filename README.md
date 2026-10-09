# Market Timeseries

**Local release preparation, version 0.1.0-local. Not published.** This repository contains a small, documented selection of public-source and derived market and macro-financial tables prepared for research and reproducible analysis. It is not a mirror of every dataset found in the source workspace. The preparation manifest contains 54 data files (106,875,828 bytes, about 106.9 MB); original datasets were not moved or modified.

Private review hosting has subsequently been authorized: see [private repository and Drive dataset locations](docs/private_hosting.md). Public release and DOI registration remain pending.

Repository usage is documented in the [analytics summary](metrics/README.md), [traffic history](metrics/metrics_log.csv) and [analytics definitions/access notes](docs/github_analytics.md). GitHub currently disables Traffic Insights for this private repository's account plan; unavailable visitors are not reported as zero.

[![Downloads: not published](https://img.shields.io/badge/downloads-not%20published-lightgrey)](hosting/downloads_badge.json)
[![Stars: not published](https://img.shields.io/badge/stars-not%20published-lightgrey)](docs/hosting_and_metrics.md)

<!-- Replace this commented template only after an owner-selected repository URL exists:
[![GitHub stars](https://img.shields.io/github/stars/OWNER/REPOSITORY?style=social)](https://github.com/OWNER/REPOSITORY)
-->

> This is a local preparation snapshot. There is no public repository, release, DOI, hosting identifier, or download endpoint yet. A `not published` badge is intentional.

## Proposed public selection

The table below describes the six prepared table products. “Conditional” means that the proposed selection is limited to the documented material and carries source-specific terms and notices; it is not a universal clearance of every source artifact. Review [the source-by-source terms](THIRD_PARTY_LICENSES.md) and [the machine-readable manifest](docs/release_manifest.json) before reuse.

| Dataset | Coverage and frequency | Rows | Approx. bytes | Units / interpretation | Rights and caveats |
|---|---|---:|---:|---|---|
| Economic release events, verified-time directory (`data/events/economic_events/`) | 2000-01-28 to 2026-09-16; event-level; ABS (Australia) and Federal Reserve Board (US) | 2,465 | 1,202,070 | Per-row currency and unit where a numeric release value exists; most event rows are metadata-only | Conditional agency-origin factual release metadata; attribution, release-level exception checks, and source/hash provenance apply. UTC publication/availability timestamps are retained where established. |
| Economic release events, review-only (`data/events/economic_events_review.parquet`) | Publication-date span 2000-01-05 to 2026-09-18; event/revision-level; AOFM, USDA, Federal Reserve, RBA, ABS | 4,219 | 472,240 | Per-row currency/unit; not every record contains a numeric value | Separate, review-only table. 4,129 rows have unknown release time; 90 are marked `source_revision_requires_review`. Do not treat as timestamp-eligible training data. Source rights are conditional and attribution-dependent. |
| Hyperliquid hourly OHLCVA (`data/markets/hyperliquid_hourly.parquet`) | 2025-11-30 23:00 to 2025-12-31 23:00 UTC; hourly; BTC, ETH and SOL perpetuals | 2,233 | 112,591 | Venue price and size units; `amount` is sum(price × size), not fiat-converted | Derived aggregation of the Albers et al. CC BY 4.0 Open Book data; attribute the source, link the license, identify changes. This table is intended to omit account identifiers. |
| CFTC TFF Treasury futures (`data/timeseries/cftc_tff.parquet`) | 2006-06-13 to 2025-12-30; weekly observed reports; four instruments | 4,084 | 429,245 | Contracts, as reported | CFTC agency public-domain statement supports copying of agency-created material; acknowledge CFTC and check for third-party inclusions. Date/report availability semantics matter. |
| RBA F2 government bond yields (`data/timeseries/rba_f2.parquet`) | 2013-05-20 to 2025-12-31; daily observations on a weekly publication schedule | 3,196 | 125,336 | Yield percent; five Australian Government Security yield series | RBA Financial Data section 5 terms, not the general RBA CC BY grant. Credit RBA, avoid endorsement, and disclose if charging for access to material RBA publishes free. |
| CFTC disaggregated futures-and-options positioning: source CSV plus lossless field-text Parquet companion (`data/timeseries/cftc_disaggregated_2018_2024.csv`, `data/timeseries/cftc_disaggregated_2018_2024.parquet`) | 2018-01-02 to 2024-12-31; weekly; 543 markets | 83,019 (same rows in each format) | 104,534,346 combined: CSV 88,333,114; Parquet 16,201,232 | Heterogeneous source `Contract_Units`; do not assume a common unit across markets. The Parquet companion stores all 191 fields as UTF-8 strings. | CFTC agency public-domain statement supports copying of agency-created information with acknowledgment; check artifact-level exceptions. The two format files are one dataset product, not separate observations. The inventory null scan verified the market-name and report-date columns only; other source CSV null counts are unverified. |

Sizes are exact bytes from the local preparation statistics and are not rounded storage promises. In total, the six prepared table products account for 106,875,828 bytes across 54 files and 99,216 product rows (the CFTC CSV and Parquet files contain the same 83,019 rows and do not add a table). These are not 99,216 independent events or observations; rows may represent releases, revisions, or reports, and datasets have different sampling units. Summing field counts across unlike schemas—or counting the companion's fields twice—does not produce a meaningful dataset-wide column count.

The source inventory identified 18 families. This selected set does not include every family: the [full family decision table](THIRD_PARTY_LICENSES.md) distinguishes proposed inclusion from held, denied, conditional, and unresolved sources. In particular, Binance's NC-SA material is excluded from the commercially reusable selection; FI-2010's CC BY label does not settle its exchange-data rights chain; and the Coinbase CC0 label conflicts with unresolved Coinbase market-data terms. Those are unresolved rights questions, not categorical legal findings about all possible uses.

### Coverage and interpretation limits

Availability is not the same as observation time. For timestamped macro events, use the provided availability/publication timestamp to avoid seeing information before it was public. The verified-time event set uses 2,465 rows with UTC timestamps and source evidence. The review set is deliberately separate: most of its rows do not have a verified release instant, and a source revision may require review. A date-only record remains a date; it must not be assigned an invented intraday time.

The time-series tables also have distinct reporting schedules. CFTC positioning is weekly and refers to report dates; RBA F2 values are daily observations published on a weekly schedule. A model or analysis must respect the actual release/availability fields rather than backfill a value into an earlier information set. CFTC disaggregated contracts have heterogeneous contract units. Hyperliquid rows are venue-native perpetual-market values and are not converted to fiat.

The two event sources shown in the verified-time table are not a consensus calendar. Release selection and historic timestamp evidence vary by source, country and event. An empty scalar value means the field was not supplied or established in this dataset, not zero, unchanged, or “no surprise.” Dataset-specific null counts and quality flags are in [dataset statistics](docs/dataset_statistics.json) and [schemas](#schemas).

This is research data, not investment, trading, legal, accounting, or tax advice. It makes no recommendation and carries no promise of completeness, timeliness, fitness, or future availability. No financial recommendations or model performance claims are made.

## Quick loading

Install Python with `pandas` and a Parquet engine such as `pyarrow`. CSV can be read with pandas directly. The examples below assume the repository root is the current directory.

```python
import pandas as pd

# Partitioned event directory (Parquet files under year=.../country=...)
events = pd.read_parquet("data/events/economic_events")
events["available_timestamp"] = pd.to_datetime(
    events["available_timestamp"], utc=True, errors="coerce"
)

# Keep the separate review set out of timestamp-sensitive evaluation.
review = pd.read_parquet("data/events/economic_events_review.parquet")
timestamp_eligible = events.dropna(subset=["available_timestamp"])

# Weekly CFTC TFF and daily-observation / weekly-publication RBA series.
tff = pd.read_parquet("data/timeseries/cftc_tff.parquet")
rba = pd.read_parquet("data/timeseries/rba_f2.parquet")
rba["available_timestamp"] = pd.to_datetime(rba["available_timestamp"], utc=True)

# CFTC source CSV: keep source fields as text to preserve literal NA, empty
# fields, and leading zeroes. Do not let parser inference change field values.
cftc_csv = pd.read_csv(
    "data/timeseries/cftc_disaggregated_2018_2024.csv",
    dtype="string", keep_default_na=False, na_filter=False,
)

# Field-text Parquet companion: same 83,019 rows and 191 fields, with text
# values preserved. Numeric/date conversion is deliberately left to the user.
cftc_parquet = pd.read_parquet(
    "data/timeseries/cftc_disaggregated_2018_2024.parquet"
)

# Hourly venue-native perpetual OHLCVA.
hourly = pd.read_parquet("data/markets/hyperliquid_hourly.parquet")
hourly["timestamp"] = pd.to_datetime(hourly["timestamp"], utc=True)
```

For time-aware joins, select the latest value whose **availability** timestamp is no later than the simulated decision time. Do not join only on calendar date if an event can occur after the decision time. Do not infer a missing observation as zero. Read the relevant schema and rights notes before combining or republishing tables.

## Schemas and provenance

Schema files document the published field names, types and nullability. The two event products have separate schemas because their timing and review status differ.

- [Economic events schema](docs/schema_economic_events.json)
- [Economic events review schema](docs/schema_economic_events_review.json)
- [CFTC TFF schema](docs/schema_cftc_tff.json)
- [CFTC disaggregated CSV schema](docs/schema_cftc_disaggregated.json)
- [CFTC disaggregated Parquet companion schema](docs/schema_cftc_disaggregated_parquet.json)
- [RBA F2 schema](docs/schema_rba_f2.json)
- [Hyperliquid hourly schema](docs/schema_hyperliquid_hourly.json)

Hashes, source dependencies, per-file byte sizes, descriptions and conditions are in [`docs/release_manifest.json`](docs/release_manifest.json). The CFTC field-text Parquet conversion is logged as retaining 83,019 rows and all field values with no numeric/date inference or value changes. The transformation notes are in [`docs/transformation_log.json`](docs/transformation_log.json). A portable 56,653-file inventory is available at [`docs/public_inventory.csv`](docs/public_inventory.csv); the public family-level rights table is [`docs/license_audit_families.csv`](docs/license_audit_families.csv). The path-bearing `docs/dataset_inventory.csv` and `docs/license_audit.csv` are private, gitignored local artifacts and are not linked here. Inventory entries do not grant rights.

## Citation

For this local prepared collection, cite:

> Mallick, Prakash (curator). *Market Timeseries: Local Release Preparation*. Version 0.1.0-local, 2026. Local preparation snapshot; not published. Cite the originating provider and applicable license for each table as described in `THIRD_PARTY_LICENSES.md`.

Use [`CITATION.cff`](CITATION.cff) or [`docs/citation.bib`](docs/citation.bib) for machine-readable metadata. No DOI, affiliation, public repository URL, or source ownership is claimed. Dataset-source attributions are required independently of this curator citation.

## Licensing

[`LICENSE`](LICENSE) is the MIT License for original project code, curation, and documentation only. It does not relicense upstream data. Upstream terms and attribution requirements remain attached to the corresponding rows and derived material; see [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md). In brief:

- **MIT** is short and permissive for project-authored code/docs, but supplies no express patent grant and cannot solve data rights.
- **Apache-2.0** is also permissive and adds express patent language and NOTICE handling, at the cost of more conditions and text. It still cannot authorize data rights the licensor does not control.
- **GPL-3.0** requires covered derivative software to remain under GPL and includes stronger copyleft/patent provisions; it is a poor fit for a small curation package that needs to preserve varied upstream data terms.

These comparisons concern original project material only. They do not decide whether an upstream provider permits redistribution, commercial use, derived datasets, or machine-learning use.

## Status and planned layout

This work was prepared locally on 2026-10-09. It remains unpublished to the public and has no DOI. The owner subsequently authorized the private repository push and Drive copies described in [private_hosting.md](docs/private_hosting.md). A 32,653-file local restricted copy is under `data_restricted/`, totaling 237,154,298,717 logical bytes. These are independent APFS copy-on-write clones, not hardlinks; their initial physical allocation was metadata-only, so the logical-byte total does not mean an additional 237 GB of content blocks. Restricted holdings are not part of this proposed public table selection. No original source holdings were modified.

```text
data/       selected, manifest-listed table products only
docs/       schemas, inventories, statistics, rights audit, manifests, guidance
LICENSES/   locally retained source-policy evidence; upstream terms remain controlling
metrics/    tested collection tooling; no public metric sources configured
paper/      compiled dataset-only draft; no benchmark results
scripts/    local preparation and validation utilities
tests/      local checks
```

For planned work and release gates, see [`docs/TODO_for_owner.md`](docs/TODO_for_owner.md). Contributions and corrections should follow [`CONTRIBUTING.md`](CONTRIBUTING.md). Data redistribution or publication must wait until source terms and all owner release gates are satisfied.

## Funding, affiliation, and acknowledgements

No funding, institutional affiliation, endorsement, or organizational sponsorship is claimed. Add these only if verified and supplied by the curator. Third-party dataset creators are credited in the source-specific notices.

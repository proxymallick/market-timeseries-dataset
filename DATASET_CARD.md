# Dataset card: Market Timeseries

**Prepared:** 2026-10-09 · **Snapshot:** 0.1.0-local · **Status:** private preparation, not published

**Curator:** Prakash Mallick · **Scope:** six prepared table products, not the full local inventory
**License:** MIT covers my code, curation, and documentation. Each data source keeps its own terms, recorded in [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md).

I curated this snapshot, but I do not claim ownership or authorship of the upstream data.

## 1. Motivation

I assembled selected macroeconomic releases, public futures positioning, Australian government bond yields, and hourly crypto perpetual-market bars into documented tables. My aim is to make provenance and availability timing easy to inspect, especially for research that joins data with different frequencies.

This is a narrow research collection, not a complete history of the markets or providers it samples. It is not investment advice, a forecast, or a trading recommendation. I report no benchmark or predictive-performance result.

## 2. Composition

I prepared 54 files totaling 106,875,828 bytes (about 106.9 MB). The six products contain 99,216 rows after counting the two CFTC formats once. That arithmetic total mixes events, review records, weekly reports, daily yields, and market bars, so it is not a common sample size.

| Product | Rows | Coverage / frequency | Size | Source and measured notes |
|---|---:|---|---:|---|
| Verified-time economic events | 2,465 | 2000-01-28–2026-09-16; event-level | 1,202,070 B | 1,581 ABS and 884 Federal Reserve rows; all are marked `eligible`; all have `available_timestamp`. Scalar `actual_value`, `unit`, and related evidence fields are null in 2,395 rows. `region`, `reference_period`, `importance`, forecasts, previous values and surprise fields are null throughout this extracted dataset. |
| Economic events review set | 4,219 | Publication-date span 2000-01-05–2026-09-18; event/revision-level | 472,240 B | 3,307 AOFM, 323 USDA, 312 Federal Reserve, 240 RBA and 37 ABS rows. 4,129 have unknown release time; 90 need source-revision review. Only 90 rows have a non-null `event_timestamp_utc` and `available_timestamp`. |
| Hyperliquid hourly OHLCVA | 2,233 | 2025-11-30 23:00–2025-12-31 23:00 UTC; hourly | 112,591 B | BTC, ETH and SOL perpetuals. Nine fields; no nulls in the prepared table. Price/size units are venue-native; `amount` is summed price × size, not a fiat valuation. |
| CFTC TFF Treasury futures | 4,084 | 2006-06-13–2025-12-30; weekly observed reports | 429,245 B | Four instruments; 20 fields; no nulls in the measured fields. Units are contracts. |
| RBA F2 government bond yields | 3,196 | 2013-05-20–2025-12-31; daily observations, weekly publication schedule | 125,336 B | Yield percent; 7 fields. Nulls: 98 each for 2y, 3y and 5y; 20 for 10y; 413 for 10y indexed yield. Observation and availability timestamps are populated. |
| CFTC disaggregated futures and options (CSV plus field-text Parquet companion) | 83,019 in each format | 2018-01-02–2024-12-31; weekly; 543 markets | 104,534,346 B combined (CSV 88,333,114 B; Parquet 16,201,232 B) | 191 source fields; units vary by market. Every Parquet field is stored as UTF-8 text, preserving source spellings such as literal `NA`, empty values, and leading zeroes. The conversion did not infer numeric/date types or change field values. The inventory null scan verified the market-name and report-date fields only; other CSV null counts are unverified. |

[`docs/dataset_statistics.json`](docs/dataset_statistics.json) contains the measured statistics, and [`docs/release_manifest.json`](docs/release_manifest.json) contains file sizes and hashes. The transformation log records equal CFTC row counts and zero field-value changes. A manifest entry documents provenance and conditions; it is not proof that every upstream record is cleared for every use. Column counts across unrelated products should not be added together.

### Time and missing-value semantics

A null scalar means I could not establish a value. It does not mean zero, unchanged, “no release,” or “no surprise.” Most verified-event rows contain identity and timing without a numeric actual value. I kept 4,129 unknown-time records in the review table; their dates must not be treated as exact intraday availability times.

`event_timestamp_utc` records an event or release instant when I could verify one. Use `available_timestamp` when reconstructing the information available at a point in time. A date-only observation remains a date. RBA F2 observations are daily but published weekly, and a CFTC report date is not necessarily its public release time.

## 3. Collection process

I inventoried the workspace recursively and mapped local files to source families. Where available, I checked current official policies and retained the evidence in `LICENSES/`. The results are summarized in [`docs/license_audit.md`](docs/license_audit.md), [`docs/source_license_registry.json`](docs/source_license_registry.json), and [`docs/license_audit_families.csv`](docs/license_audit_families.csv). The portable inventory lists 56,653 files without exposing local absolute paths. Path-bearing audit files stay gitignored. I did not modify the original holdings.

I assembled the tables from source material already held locally: ABS and Federal Reserve release metadata, agency records kept for review, CFTC reports, RBA Table F2, and the Hyperliquid Open Book source used for hourly aggregation. `docs/transformation_log.json` and `docs/release_manifest.json` record the dependencies and transformations. I did not freshly fetch every archive, and this snapshot does not represent every provider's full history.

I left unresolved and restricted raw sources out of the selection. The registry contains 18 source families, while the inventory also includes duplicates, archives, documents, derived panels, and model outputs. File counts therefore are not counts of independent datasets. I also distinguish known sources with unclear rights from unknown provenance: the FDIC product is known but its reuse terms remain unclear, while the original provider of the Qlib-compatible archive is unknown.

## 4. Preprocessing, validation, and provenance

I kept the outputs in Parquet or CSV and recorded schemas, dependencies, byte sizes, SHA-256 hashes, and transformations. `docs/transformation_log.json` describes conversions and aggregations; `docs/schema_*.json` documents the products, including the [CFTC field-text Parquet schema](docs/schema_cftc_disaggregated_parquet.json).

The event directory is partitioned by year and country. I retained source URLs and hashes, evidence and quality fields, and separate event and availability timestamps. The review table stays separate from timestamp-verified data. Hyperliquid bars aggregate trade timestamps, prices, and sizes; CFTC data keep source classifications and units; RBA F2 values remain yield percentages with observation and availability fields.

I verified 1,072 small-file duplicate groups. I did not fully hash large archives or establish every possible overlap. CFTC disaggregated null statistics cover only two columns, and I did not stream every FI-2010 matrix or archive for complete row, date, and unit metadata. I did not normalize values, invent timezones, or overwrite source data.

## 5. Uses and limitations

The tables may be useful for research on disclosure timing, public positioning, yields, event-aware pipelines, and provenance-aware joins. Choose the product that matches the question and check its timing, transformations, source rights, and coverage independently.

Known limitations and biases include:

- **Selection and coverage:** the source discovery is broad, but the selected tables are narrow and non-random. Missing periods, products, instruments, or event types are possible.
- **Provider and geography concentration:** the verified event table covers ABS and Federal Reserve source rows; it is not a global release calendar. The review table adds selected Australian agency sources but has unresolved timing.
- **No consensus calendar:** multiple providers do not independently confirm a universal event schedule or release instant. Source selection and historical timestamp evidence vary.
- **Point-in-time risk:** report dates, observation dates, and actual availability can differ. A backtest that ignores publication time may leak future information.
- **Missing values:** nulls can reflect unavailable source values, absent fields, or deliberate lack of a value; they do not encode numeric zero. Some null scans are incomplete as identified above.
- **Measurement differences:** contract units vary in CFTC disaggregated reports; RBA yields are percentages; Hyperliquid price/size and amount are venue-native and not converted to fiat.
- **Revisions:** agency data and release values may be revised. The review table includes rows requiring revision review; historical-vintage completeness is not guaranteed.
- **Market structure:** a single month of hourly Hyperliquid bars and a limited selection of public reports cannot represent all venues, instruments, liquidity conditions, or current market state.
- **Overlap and duplicates:** source families and local derivatives may overlap. Summed row/file counts are not independent sample sizes.
- **Rights and policy:** the local audit records known terms and uncertainties, not legal advice. Current terms may not settle historic acquisition terms or third-party rights.

Do not use this release as the sole basis for a financial, investment, trading, legal, accounting, or tax decision. No suitability, accuracy, completeness, or future-availability guarantee is made.

## 6. Distribution and licensing

I have not published this directory. The prepared selection exists to make a later release review concrete; it has no DOI or public dataset identifier. `data_restricted/` contains 32,653 independent APFS copy-on-write clones totaling 237,154,298,717 logical bytes. They are not hardlinks, and the logical total does not represent another 237 GB of copied blocks. The restricted tree is outside the prepared selection.

The root MIT `LICENSE` covers only the code, curation, and documentation I wrote. It does not supersede source-specific conditions. The six products have conditional source status; other families remain held, restricted, or unresolved. “Conditional” is not approval for unrestricted commercial redistribution. `docs/permission_requests.md` contains drafts for questions that still need written answers.

Attribution remains source-specific. Credit the relevant agencies, follow CC BY 4.0 attribution and change notices where they apply, use the RBA Financial Data section 5 conditions for F2, and cite the Hyperliquid creators and DOI for hourly derivatives. My curator citation does not replace those source credits.

## 7. Maintenance and contact

I am Prakash Mallick, the curator. I have not added an affiliation, ORCID, public contact address, or public dataset host. I checked the source terms on 2026-10-09 UTC; they may change. Before any public release I will recheck them, update evidence dates, regenerate hashes and statistics, reconcile the file list, and confirm that no held material or credentials are included.

Remaining decisions are in [`docs/TODO_for_owner.md`](docs/TODO_for_owner.md). The permission requests are drafts; I have not sent them. Any data or rights change must be reflected in the manifest, audit, statistics, schemas, and this card. If a source disappears or changes terms, I will record the change and reassess the affected products.

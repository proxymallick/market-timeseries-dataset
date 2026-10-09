# Dataset card: Market Timeseries

**Prepared:** 2026-10-09 · **Snapshot:** 0.1.0-local · **Status:** local preparation only, not published.  
**Curator:** Prakash Mallick. The curator is not the owner or original author of upstream source data.  
**Scope:** six prepared table products in a source-aware selection; not the full local discovery inventory.  
**License:** no single data license applies to the collection. Original project code, curation and documentation are offered under MIT; each table retains its upstream terms and conditions in [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md).

## 1. Motivation

The collection organizes selected historical macroeconomic release events, public futures positioning, Australian government bond yields, and a derived hourly crypto perpetual-market series in documented, machine-readable tables. The goal is to make provenance and data availability easier to inspect and to support research workflows that need time-aware joins across unlike frequencies.

The selected records are not a complete view of financial markets, macroeconomic releases, or source-provider histories. This is not an investment product and should not be interpreted as a recommendation to trade, a forecast, or advice. No model benchmark, predictive performance, or representativeness claim is made.

## 2. Composition

The prepared selection contains 54 data files with a combined size of 106,875,828 bytes (about 106.9 MB). The six table products contain 99,216 rows in total, but that arithmetic total combines incompatible units of observation: events, review records, weekly reports, daily yields, market bars, and market-instrument rows. The CFTC disaggregated CSV and Parquet companion are two representations of the same 83,019 rows, not separate products or observations.

| Product | Rows | Coverage / frequency | Size | Source and measured notes |
|---|---:|---|---:|---|
| Verified-time economic events | 2,465 | 2000-01-28–2026-09-16; event-level | 1,202,070 B | 1,581 ABS and 884 Federal Reserve rows; all are marked `eligible`; all have `available_timestamp`. Scalar `actual_value`, `unit`, and related evidence fields are null in 2,395 rows. `region`, `reference_period`, `importance`, forecasts, previous values and surprise fields are null throughout this extracted dataset. |
| Economic events review set | 4,219 | Publication-date span 2000-01-05–2026-09-18; event/revision-level | 472,240 B | 3,307 AOFM, 323 USDA, 312 Federal Reserve, 240 RBA and 37 ABS rows. 4,129 have unknown release time; 90 need source-revision review. Only 90 rows have a non-null `event_timestamp_utc` and `available_timestamp`. |
| Hyperliquid hourly OHLCVA | 2,233 | 2025-11-30 23:00–2025-12-31 23:00 UTC; hourly | 112,591 B | BTC, ETH and SOL perpetuals. Nine fields; no nulls in the prepared table. Price/size units are venue-native; `amount` is summed price × size, not a fiat valuation. |
| CFTC TFF Treasury futures | 4,084 | 2006-06-13–2025-12-30; weekly observed reports | 429,245 B | Four instruments; 20 fields; no nulls in the measured fields. Units are contracts. |
| RBA F2 government bond yields | 3,196 | 2013-05-20–2025-12-31; daily observations, weekly publication schedule | 125,336 B | Yield percent; 7 fields. Nulls: 98 each for 2y, 3y and 5y; 20 for 10y; 413 for 10y indexed yield. Observation and availability timestamps are populated. |
| CFTC disaggregated futures and options (CSV plus field-text Parquet companion) | 83,019 in each format | 2018-01-02–2024-12-31; weekly; 543 markets | 104,534,346 B combined (CSV 88,333,114 B; Parquet 16,201,232 B) | 191 source fields; units vary by market. Every Parquet field is stored as UTF-8 text, preserving source spellings such as literal `NA`, empty values, and leading zeroes. The conversion did not infer numeric/date types or change field values. The inventory null scan verified the market-name and report-date fields only; other CSV null counts are unverified. |

Statistics are taken from [`docs/dataset_statistics.json`](docs/dataset_statistics.json); file-level sizes and hashes are recorded in [`docs/release_manifest.json`](docs/release_manifest.json). The transformation log records the CFTC CSV-to-Parquet conversion, equal row counts, and zero value changes. The proposed release manifest also includes source attribution/conditions. It is not evidence that all upstream records are rights-cleared for every use. Field counts across different products, or across the two representations of the same CFTC data, should not be summed into a purported collection-wide column count.

### Time and missing-value semantics

An empty or null scalar is missing information, not zero, unchanged, “no release,” or “no surprise.” For the verified event table, most rows carry event identity and timing without a numeric actual value. The review table explicitly segregates records for which a trustworthy release instant or revision interpretation has not been established. Do not use its 4,129 unknown-time rows as if their dates were exact intraday availability times.

`event_timestamp_utc` describes an event or release instant when one was established; `available_timestamp` is the field to use when simulating the information set available to a consumer. A date-only observation remains a date. RBA F2 observations are daily but the source publication schedule is weekly; CFTC reports are weekly and their report date is not necessarily the public release time. Avoid joins that make a value visible before it could have been observed.

## 3. Collection process

The original workspace was recursively inventoried and source families were mapped to local files. Current official policies and dataset terms were reviewed where available, with evidence retained in `LICENSES/` and summarized in [`docs/license_audit.md`](docs/license_audit.md), [`docs/source_license_registry.json`](docs/source_license_registry.json), and the portable 18-family table [`docs/license_audit_families.csv`](docs/license_audit_families.csv). A portable file-level inventory of 56,653 discovered files is [`docs/public_inventory.csv`](docs/public_inventory.csv); it avoids private local absolute paths. Path-bearing `docs/dataset_inventory.csv` and `docs/license_audit.csv` remain gitignored local artifacts for privacy. Discovery was local; this preparation did not modify original data holdings.

The selected public-table candidates were assembled from already available local source material: ABS and Federal Reserve release metadata, agency event records retained for review, CFTC reports, RBA Table F2, and the Hyperliquid Open Book source for hourly aggregation. File-level transformations and dependencies are recorded in `docs/transformation_log.json` and `docs/release_manifest.json`. This card does not claim that all source archives were freshly fetched or that every provider's full history is represented.

The release selection deliberately omits unresolved or restricted raw sources. There are 18 identified source families in the registry; the local discovery inventory also separates analysis/model artifacts from source observations. A physical file may be a duplicate, copy, archive, document, derived panel, or model output. Inventory counts therefore are not counts of independent datasets or unique observations. “Known source, unclear rights” is distinct from “unknown provenance”: the FDIC Failed Bank List source is identified, but its dataset-specific reuse terms remain unclear; the original provider for the Qlib-compatible Chinese-equity archive remains unknown.

## 4. Preprocessing, validation, and provenance

Prepared outputs are retained in Parquet or CSV with explicit schemas, source dependencies, byte size, SHA-256, and transformation descriptions. The output manifest is `local preparation only; not published`. `docs/transformation_log.json` describes the conversions and aggregations; `docs/schema_*.json` documents the six tabular products, including the [CFTC field-text Parquet schema](docs/schema_cftc_disaggregated_parquet.json).

The event directory is partitioned by year and country. Its schema retains source URLs and hashes, evidence/confidence/quality fields, and separate event and availability timestamps. The review dataset is separate and quality-marked; it has not been silently promoted to timestamp-verified data. The Hyperliquid hourly output is an aggregation from trade timestamps, prices, and sizes. CFTC data retain source-reported classifications/units. RBA F2 yields remain yield percentages and keep observation and availability fields.

The inventory records 1,072 verified small-file duplicate groups; large-file identity and all potential overlap are not fully established. Discovery statistics warn that archives, extracted copies, and analysis outputs overlap. CFTC disaggregated null statistics are limited to two columns. FI-2010 matrices and archives were not comprehensively streamed to establish complete row/date/unit metadata. No value normalization, invented timezone, or source-data overwrite is claimed.

## 5. Uses and limitations

Potential uses include research on the timing of historical macroeconomic disclosures, descriptive analysis of public positioning and yield series, event-aware data engineering, and examples of provenance-aware joins. Users should choose the product appropriate to their question and independently validate the time semantics, transformations, source rights, and coverage.

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

This directory is not published. The prepared selection is listed to make a later release review concrete; it has no DOI or public repository identifier. Under `data_restricted/` there are 32,653 independent APFS copy-on-write clones with a combined 237,154,298,717 logical bytes. They are not hardlinks, and initial physical allocation was metadata-only; the logical total does not represent an additional 237 GB of copied data blocks. The restricted tree is not part of the proposed public selection.

The root MIT `LICENSE` applies only to original code, curation, and documentation authored for this project. It does not supersede source-specific conditions. The six proposed products currently have conditional source status and are documented with conditions in `THIRD_PARTY_LICENSES.md`. Other source families are held, restricted, or unresolved. Do not treat a “conditional” registry status as approval for unrestricted commercial redistribution. See `docs/permission_requests.md` for unsent requests intended to resolve specific questions.

Attribution is source-specific. In particular, credit the relevant agencies for government/agency tables, follow CC BY 4.0 attribution and change notices for covered ABS/RBA/AOFM material, apply RBA Financial Data section 5 conditions to F2, and cite the Hyperliquid source creators and DOI for hourly derivatives. This collection's curator citation is supplemental, not a replacement for source attribution.

## 7. Maintenance and contact

The curator is Prakash Mallick. No affiliation, ORCID, public contact address, issue tracker, or hosting identity is asserted. The source audit was accessed on 2026-10-09 UTC; terms and hosting status may change. Before any external release, recheck source terms, record evidence/access dates, regenerate hashes and statistics, reconcile all file paths against the selection, and confirm that no held material or credentials are included.

Known owner tasks are listed in [`docs/TODO_for_owner.md`](docs/TODO_for_owner.md). `docs/permission_requests.md` contains drafts only; no requests have been sent. Changes to data or rights decisions should be reflected in the manifest, audit, statistics, schemas, and this card. If a source disappears or changes terms, record the event and reassess affected products rather than assuming continued access or permission.

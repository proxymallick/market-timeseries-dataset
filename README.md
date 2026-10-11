# Market Timeseries

I built this repository as a small, traceable selection of market and macro-financial data for research. It contains 54 prepared files (106,875,828 bytes, about 106.9 MB), drawn from public-agency sources and one documented crypto-market source. I left the original datasets unchanged.

The project is at version `0.1.0-local`. I have stored review copies in a [private GitHub repository and restricted Google Drive folder](docs/private_hosting.md). I have not published the dataset or registered a DOI.

Repository activity is recorded in the [analytics summary](metrics/README.md) and [CSV history](metrics/metrics_log.csv). GitHub does not expose Traffic Insights for this private repository on the current plan, so visitor fields are marked unavailable rather than zero.

There is no public download or DOI yet.

## Prepared selection

I prepared six table products. “Conditional” means I reviewed the named material under the stated source terms; it does not clear every file from that source. Read the [source-by-source terms](THIRD_PARTY_LICENSES.md) and [release manifest](docs/release_manifest.json) before reuse.

| Dataset | Coverage and frequency | Rows | Approx. bytes | Units / interpretation | Rights and caveats |
|---|---|---:|---:|---|---|
| Economic release events, verified-time directory (`data/events/economic_events/`) | 2000-01-28 to 2026-09-16; event-level; ABS (Australia) and Federal Reserve Board (US) | 2,465 | 1,202,070 | Per-row currency and unit where a numeric release value exists; most event rows are metadata-only | Conditional agency-origin factual release metadata; attribution, release-level exception checks, and source/hash provenance apply. UTC publication/availability timestamps are retained where established. |
| Economic release events, review-only (`data/events/economic_events_review.parquet`) | Publication-date span 2000-01-05 to 2026-09-18; event/revision-level; AOFM, USDA, Federal Reserve, RBA, ABS | 4,219 | 472,240 | Per-row currency/unit; not every record contains a numeric value | Separate, review-only table. 4,129 rows have unknown release time; 90 are marked `source_revision_requires_review`. Do not treat as timestamp-eligible training data. Source rights are conditional and attribution-dependent. |
| Hyperliquid hourly OHLCVA (`data/markets/hyperliquid_hourly.parquet`) | 2025-11-30 23:00 to 2025-12-31 23:00 UTC; hourly; BTC, ETH and SOL perpetuals | 2,233 | 112,591 | Venue price and size units; `amount` is sum(price × size), not fiat-converted | Derived aggregation of the Albers et al. CC BY 4.0 Open Book data; attribute the source, link the license, identify changes. This table is intended to omit account identifiers. |
| CFTC TFF Treasury futures (`data/timeseries/cftc_tff.parquet`) | 2006-06-13 to 2025-12-30; weekly observed reports; four instruments | 4,084 | 429,245 | Contracts, as reported | CFTC agency public-domain statement supports copying of agency-created material; acknowledge CFTC and check for third-party inclusions. Date/report availability semantics matter. |
| RBA F2 government bond yields (`data/timeseries/rba_f2.parquet`) | 2013-05-20 to 2025-12-31; daily observations on a weekly publication schedule | 3,196 | 125,336 | Yield percent; five Australian Government Security yield series | RBA Financial Data section 5 terms, not the general RBA CC BY grant. Credit RBA, avoid endorsement, and disclose if charging for access to material RBA publishes free. |
| CFTC disaggregated futures-and-options positioning: source CSV plus lossless field-text Parquet companion (`data/timeseries/cftc_disaggregated_2018_2024.csv`, `data/timeseries/cftc_disaggregated_2018_2024.parquet`) | 2018-01-02 to 2024-12-31; weekly; 543 markets | 83,019 (same rows in each format) | 104,534,346 combined: CSV 88,333,114; Parquet 16,201,232 | Heterogeneous source `Contract_Units`; do not assume a common unit across markets. The Parquet companion stores all 191 fields as UTF-8 strings. | CFTC agency public-domain statement supports copying of agency-created information with acknowledgment; check artifact-level exceptions. The two format files are one dataset product, not separate observations. The inventory null scan verified the market-name and report-date columns only; other source CSV null counts are unverified. |

The sizes above are exact. Together the products use 106,875,828 bytes across 54 files and contain 99,216 rows after counting the CFTC CSV and Parquet companion once. That total mixes releases, revisions, reports, yields, and market bars. It is not a sample size, and summing columns across these unrelated schemas would not be meaningful.

My inventory identified 18 source families, but only six prepared products are included here. The [family decision table](THIRD_PARTY_LICENSES.md) explains what I included, held back, or could not resolve. I excluded Binance's NC-SA material from the commercially reusable selection. I also held FI-2010 and Coinbase-derived material because their dataset labels do not settle the underlying market-data rights. These are unresolved rights questions, not legal conclusions about every possible use.

### Coverage and interpretation limits

Availability is not the same as observation time. For macro events, use the availability or publication timestamp so a backtest cannot see information before it was public. I kept 2,465 events with UTC timestamps and source evidence in the verified set. I kept date-only records and uncertain revisions in a separate review table. A date-only record must stay date-only.

CFTC positioning is weekly and refers to report dates. RBA F2 contains daily observations published on a weekly schedule. Respect the release and availability fields instead of backfilling values into an earlier information set. CFTC contract units vary by market, and the Hyperliquid values remain in venue-native units.

The verified event table is not a consensus calendar. It covers selected ABS and Federal Reserve records, and the timestamp evidence varies by source and event. An empty scalar means I could not establish a value; it does not mean zero, unchanged, or “no surprise.” See the [dataset statistics](docs/dataset_statistics.json) and [schemas](#schemas-and-provenance) for null counts and quality flags.

I prepared this for research, not as investment, trading, legal, accounting, or tax advice. I make no claim that it is complete, current, or suitable for a particular decision, and I report no model-performance results.

## Quick loading

Install Python with `pandas` and a Parquet engine such as `pyarrow`. CSV can be read with pandas directly. The examples below assume the repository root is the current directory.

```python
import pandas as pd

# Partition columns come from the year=.../country=... directory layout.
events = pd.read_parquet("data/events/economic_events")
events["available_timestamp"] = pd.to_datetime(
    events["available_timestamp"], utc=True, errors="coerce"
)

# This table contains records whose timing or revision status still needs review.
review = pd.read_parquet("data/events/economic_events_review.parquet")
timestamp_eligible = events.dropna(subset=["available_timestamp"])

tff = pd.read_parquet("data/timeseries/cftc_tff.parquet")
rba = pd.read_parquet("data/timeseries/rba_f2.parquet")
rba["available_timestamp"] = pd.to_datetime(rba["available_timestamp"], utc=True)

# Disable inference because literal NA, empty fields, and leading zeroes matter.
cftc_csv = pd.read_csv(
    "data/timeseries/cftc_disaggregated_2018_2024.csv",
    dtype="string", keep_default_na=False, na_filter=False,
)

# The Parquet companion stores the same 83,019 rows and 191 fields as text.
cftc_parquet = pd.read_parquet(
    "data/timeseries/cftc_disaggregated_2018_2024.parquet"
)

hourly = pd.read_parquet("data/markets/hyperliquid_hourly.parquet")
hourly["timestamp"] = pd.to_datetime(hourly["timestamp"], utc=True)
```

For time-aware joins, select the latest value whose **availability** timestamp is no later than the simulated decision time. A calendar-date join can leak an event that occurred later that day. Keep missing values as missing, and read the relevant schema and rights notes before combining or republishing tables.

## Schemas and provenance

Each schema records field names, types, and nullability. The event products have separate schemas because their timing evidence and review status differ.

- [Economic events schema](docs/schema_economic_events.json)
- [Economic events review schema](docs/schema_economic_events_review.json)
- [CFTC TFF schema](docs/schema_cftc_tff.json)
- [CFTC disaggregated CSV schema](docs/schema_cftc_disaggregated.json)
- [CFTC disaggregated Parquet companion schema](docs/schema_cftc_disaggregated_parquet.json)
- [RBA F2 schema](docs/schema_rba_f2.json)
- [Hyperliquid hourly schema](docs/schema_hyperliquid_hourly.json)

Hashes, source dependencies, per-file byte sizes, descriptions and conditions are in [`docs/release_manifest.json`](docs/release_manifest.json). The CFTC field-text Parquet conversion is logged as retaining 83,019 rows and all field values with no numeric/date inference or value changes. The transformation notes are in [`docs/transformation_log.json`](docs/transformation_log.json). A portable 56,653-file inventory is available at [`docs/public_inventory.csv`](docs/public_inventory.csv); the public family-level rights table is [`docs/license_audit_families.csv`](docs/license_audit_families.csv). The path-bearing `docs/dataset_inventory.csv` and `docs/license_audit.csv` are private, gitignored local artifacts and are not linked here. Inventory entries do not grant rights.

## Citation

Please cite this preparation as:

> Mallick, Prakash (curator). *Market Timeseries: Local Release Preparation*. Version 0.1.0-local, 2026. Local preparation snapshot; not published. Cite the originating provider and applicable license for each table as described in `THIRD_PARTY_LICENSES.md`.

[`CITATION.cff`](CITATION.cff) and [`docs/citation.bib`](docs/citation.bib) contain the same metadata. I do not claim a DOI, affiliation, public repository, or ownership of the source data. Source attribution still applies separately.

## Licensing

[`LICENSE`](LICENSE) applies MIT to the code, curation, and documentation I wrote. It does not relicense upstream data. The original terms and attribution requirements remain attached to each source; see [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md).

I chose MIT because it is short and suitable for this small code and documentation package. Apache-2.0 would add patent and NOTICE provisions; GPL-3.0 would add copyleft requirements. None of these licenses can grant rights in data I do not own.

## Status and planned layout

I prepared this snapshot on 2026-10-09 and later copied it to the private locations listed in [private_hosting.md](docs/private_hosting.md). It is still unpublished and has no DOI. The local `data_restricted/` tree contains 32,653 APFS copy-on-write files totaling 237,154,298,717 logical bytes. They are independent clones rather than hardlinks, and the logical total does not mean another 237 GB was physically duplicated. These restricted files are outside the prepared selection. I did not modify the source holdings.

```text
data/       selected, manifest-listed table products only
docs/       schemas, inventories, statistics, rights audit, manifests, guidance
LICENSES/   locally retained source-policy evidence; upstream terms remain controlling
metrics/    tested collection tooling; no public metric sources configured
paper/      compiled dataset-only draft; no benchmark results
scripts/    local preparation and validation utilities
tests/      local checks
```

See [`docs/TODO_for_owner.md`](docs/TODO_for_owner.md) for remaining release decisions and [`CONTRIBUTING.md`](CONTRIBUTING.md) for corrections. I will not publish or redistribute the data until the source terms and release gates are resolved.

## Funding, affiliation, and acknowledgements

I received no declared funding or institutional sponsorship for this preparation, and I claim no organizational endorsement. Third-party creators are credited in the source-specific notices.

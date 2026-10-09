# Loading the prepared tables

This guide describes the **local, unpublished** preparation snapshot. Files and row counts are recorded in [`release_manifest.json`](release_manifest.json); all table schemas are linked from the [README](../README.md#schemas). The examples use pandas and PyArrow and assume the repository root is the current working directory.

```bash
python -m pip install pandas pyarrow
```

Do not copy the MIT code license onto the data. Before reusing or redistributing a product, read [`../THIRD_PARTY_LICENSES.md`](../THIRD_PARTY_LICENSES.md), source notices, and upstream terms.

## Partitioned verified-time event directory

The main event set is Parquet files partitioned under `data/events/economic_events/year=.../country=.../`. `pandas.read_parquet` with a dataset-capable engine reads the directory and normally materializes `year` and `country` partition values as columns when available from the dataset layout. Field presence may vary if reading a single partition file directly.

```python
import pandas as pd

events = pd.read_parquet("data/events/economic_events")
for field in ("event_timestamp_utc", "available_timestamp", "ingested_at_utc"):
    if field in events:
        events[field] = pd.to_datetime(events[field], utc=True, errors="coerce")

# Inspect the time evidence and quality fields before choosing rows.
print(events[["event_name", "event_timestamp_utc", "available_timestamp",
              "timestamp_evidence", "confidence", "quality_status"]].head())
```

`available_timestamp` is the conservative point-in-time field for historical simulation. It represents when the information was available to a consumer, where established. Do not treat event date or a value's reference period as the publication instant. `timestamp_evidence`, `confidence`, and `quality_status` help identify how the timestamp was established. If a value is null, do not replace it with zero.

## Separate review-only event table

`data/events/economic_events_review.parquet` is intentionally separate from verified-time data. The measured statistics report 4,129 of 4,219 rows with unknown release time and 90 rows requiring source-revision review. Load it for provenance inspection and manual review, not as timestamp-eligible model input by default.

```python
review = pd.read_parquet("data/events/economic_events_review.parquet")
review["available_timestamp"] = pd.to_datetime(
    review["available_timestamp"], utc=True, errors="coerce"
)
review["event_timestamp_utc"] = pd.to_datetime(
    review["event_timestamp_utc"], utc=True, errors="coerce"
)

unknown_time = review[review["available_timestamp"].isna()]
needs_revision_review = review[
    review["quality_status"].eq("source_revision_requires_review")
]
```

Only 90 review rows have a typed event/availability timestamp in the measured summary. That fact does not promote the other 4,129 rows; use row-level quality and evidence fields. A publication **date** is not an intraday timestamp. The review table includes AOFM, USDA, Federal Reserve, RBA, and ABS records; there is no FDIC source in this release table.

## Weekly CFTC reports

The prepared Parquet TFF table is a four-instrument subset of Treasury futures weekly reports. The disaggregated futures-and-options table covers 543 markets and is available as the source CSV plus a Parquet companion. Both contain the same 83,019 rows and 191 fields; the companion is a second representation, not another table or added observations. `Contract_Units` is not homogeneous across the disaggregated markets.

```python
tff = pd.read_parquet("data/timeseries/cftc_tff.parquet")
tff["observation_timestamp"] = pd.to_datetime(
    tff["observation_timestamp"], utc=True, errors="coerce"
)
tff["available_timestamp"] = pd.to_datetime(
    tff["available_timestamp"], utc=True, errors="coerce"
)

# Source CSV: preserve every field as text, including literal "NA", empty
# fields, and leading zeroes. Disable pandas' default NA/type inference.
disaggregated_csv = pd.read_csv(
    "data/timeseries/cftc_disaggregated_2018_2024.csv",
    dtype="string",
    keep_default_na=False,
    na_filter=False,
)

# Lossless field-text Parquet companion: all columns are UTF-8 strings.
disaggregated_parquet = pd.read_parquet(
    "data/timeseries/cftc_disaggregated_2018_2024.parquet"
)
```

The source CSV remains unchanged. The Parquet companion was created by parsing all CSV fields as UTF-8 text: literal `NA`, empty strings, leading zeroes, and source text spellings are preserved; no number/date inference or field-value conversion was performed. Its schema is [`schema_cftc_disaggregated_parquet.json`](schema_cftc_disaggregated_parquet.json); the CSV schema is [`schema_cftc_disaggregated.json`](schema_cftc_disaggregated.json). Any numeric or date conversion is a downstream user choice. Convert only after checking meaning, units, and missing-value spellings, and preserve the original text field. For example, an explicit conversion of a verified numeric field could be `pd.to_numeric(disaggregated_csv["Open_Interest_All"], errors="raise")`; this raises if source spellings are not numeric instead of silently coercing them.

Retain source report dates and do not assume that a Tuesday report date alone records when a user could first have known its values. For TFF use `available_timestamp` when populated. The inventory's CFTC disaggregated null scan covered only the market-name and report-date fields; other source CSV null counts remain unverified. Consult the source CFTC schema and terms before interpreting columns or combining markets.

## RBA F2 yields

The F2 table stores daily observed Australian Government Security yields in percent, with both observation and availability timestamps. Its official publication schedule is weekly, and it can contain missing yield fields. Preserve the distinction between the value's observation date and when the table became available.

```python
rba = pd.read_parquet("data/timeseries/rba_f2.parquet")
rba["observation_timestamp"] = pd.to_datetime(
    rba["observation_timestamp"], utc=True
)
rba["available_timestamp"] = pd.to_datetime(
    rba["available_timestamp"], utc=True
)
yield_columns = [c for c in rba if c.endswith("_yield_pct")]
print(rba[yield_columns].isna().sum())
```

Do not fill missing yields without a documented rule and a separate derived output. The F2 series has separate RBA Financial Data conditions; see [`../THIRD_PARTY_LICENSES.md`](../THIRD_PARTY_LICENSES.md#family-decisions).

## Hyperliquid hourly bars

The Hyperliquid table has hourly BTC, ETH, and SOL perpetual-market bars for the prepared period. Prices, volume, and amount are venue-native. The aggregation's `amount` is sum(price × size); no fiat conversion is made.

```python
bars = pd.read_parquet("data/markets/hyperliquid_hourly.parquet")
bars["timestamp"] = pd.to_datetime(bars["timestamp"], utc=True)
bars = bars.sort_values(["item_id", "timestamp"])
```

The table has no nulls in the nine measured fields. A single month of hourly observations is not a complete historical or current-market representation. The source Open Book data carries a CC BY 4.0 attribution requirement; this aggregation should be cited as a modified hourly derivative. The raw account/order data are not included here.

## Availability-aware joins

For an as-of join, sort both the decision observations and provider data by their timestamps. Use each provider's availability field, not the event's reference period, observation date, or eventual revised value. The simple pattern below demonstrates the direction of a join; it does not certify a complete point-in-time backtest.

```python
decisions = decisions.copy()
decisions["decision_time"] = pd.to_datetime(decisions["decision_time"], utc=True)
available = events.dropna(subset=["available_timestamp"]).copy()

decisions = decisions.sort_values("decision_time")
available = available.sort_values("available_timestamp")
joined = pd.merge_asof(
    decisions,
    available,
    left_on="decision_time",
    right_on="available_timestamp",
    direction="backward",
    allow_exact_matches=True,
)
```

For announcement events, a backward as-of join may need a keyed event/series design rather than a global join, and revisions need a policy for selecting vintages. Verify that all source timestamps represent the same information concept and that your code handles date-only rows, revisions, timezone normalization, and publication lags. A timestamp field does not guarantee a comprehensive historical vintage archive.

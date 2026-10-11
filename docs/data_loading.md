# Loading the prepared tables

These examples load the private preparation with pandas and PyArrow. Run them from the repository root. The [release manifest](release_manifest.json) records files and row counts, and the [README](../README.md#schemas-and-provenance) links every schema.

```bash
python -m pip install pandas pyarrow
```

MIT covers my code and documentation, not the source data. Read [`../THIRD_PARTY_LICENSES.md`](../THIRD_PARTY_LICENSES.md) and the upstream notices before reuse or redistribution.

## Partitioned verified-time event directory

The verified event set is partitioned under `data/events/economic_events/year=.../country=.../`. A dataset-capable Parquet engine reads the full directory and usually materializes `year` and `country` from the path. A single partition file may not contain those fields directly.

```python
import pandas as pd

events = pd.read_parquet("data/events/economic_events")
for field in ("event_timestamp_utc", "available_timestamp", "ingested_at_utc"):
    if field in events:
        events[field] = pd.to_datetime(events[field], utc=True, errors="coerce")

# These fields explain why a timestamp is usable.
print(events[["event_name", "event_timestamp_utc", "available_timestamp",
              "timestamp_evidence", "confidence", "quality_status"]].head())
```

Use `available_timestamp` for point-in-time work. It records when the information became available, where I could establish that time. An event date or reference period is not a publication instant. The evidence, confidence, and quality fields explain each timestamp. Keep null values as null.

## Separate review-only event table

I keep `data/events/economic_events_review.parquet` separate because 4,129 of its 4,219 rows have unknown release times and 90 need source-revision review. Use it for provenance checks and manual review, not as timestamp-eligible model input.

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

Only 90 review rows have typed event and availability timestamps. The other 4,129 remain unknown-time records. A publication **date** is not an intraday timestamp. The table contains AOFM, USDA, Federal Reserve, RBA, and ABS records; it contains no FDIC data.

## Weekly CFTC reports

The TFF Parquet file contains four Treasury-futures instruments. The disaggregated table covers 543 markets and comes as a source CSV plus a Parquet companion. Both formats contain the same 83,019 rows and 191 fields. `Contract_Units` varies by market.

```python
tff = pd.read_parquet("data/timeseries/cftc_tff.parquet")
tff["observation_timestamp"] = pd.to_datetime(
    tff["observation_timestamp"], utc=True, errors="coerce"
)
tff["available_timestamp"] = pd.to_datetime(
    tff["available_timestamp"], utc=True, errors="coerce"
)

# Disable inference because literal NA, empty fields, and leading zeroes matter.
disaggregated_csv = pd.read_csv(
    "data/timeseries/cftc_disaggregated_2018_2024.csv",
    dtype="string",
    keep_default_na=False,
    na_filter=False,
)

# The companion stores every column as UTF-8 text.
disaggregated_parquet = pd.read_parquet(
    "data/timeseries/cftc_disaggregated_2018_2024.parquet"
)
```

I left the CSV unchanged and wrote every Parquet field as UTF-8 text. Literal `NA`, empty strings, leading zeroes, and source spellings are preserved. The [Parquet schema](schema_cftc_disaggregated_parquet.json) and [CSV schema](schema_cftc_disaggregated.json) document the formats. Convert a field only after checking its units and missing-value spellings. For example, `pd.to_numeric(disaggregated_csv["Open_Interest_All"], errors="raise")` fails on non-numeric source text instead of silently coercing it.

A Tuesday report date does not prove when the values became public. Use `available_timestamp` for TFF where present. The disaggregated null scan covered only market name and report date; null counts for other fields remain unverified.

## RBA F2 yields

The F2 table stores daily Australian Government Security yields in percent and records both observation and availability times. The RBA publishes it weekly, so keep those times distinct.

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

Do not fill missing yields in place. Document any imputation in a separate derivative. RBA Financial Data has its own conditions in [`../THIRD_PARTY_LICENSES.md`](../THIRD_PARTY_LICENSES.md#family-decisions).

## Hyperliquid hourly bars

The Hyperliquid table contains hourly BTC, ETH, and SOL perpetual bars. Prices, volume, and amount stay in venue-native units; `amount` is the sum of price times size, not a fiat conversion.

```python
bars = pd.read_parquet("data/markets/hyperliquid_hourly.parquet")
bars["timestamp"] = pd.to_datetime(bars["timestamp"], utc=True)
bars = bars.sort_values(["item_id", "timestamp"])
```

The nine measured fields contain no nulls. One month of hourly bars is not a complete market history. Cite the CC BY 4.0 Open Book source and identify this as a modified hourly derivative. Raw account and order data are not included.

## Availability-aware joins

For an as-of join, sort both sides by time and join on the provider's availability field. Do not use a reference period, observation date, or eventual revised value as a substitute. This example shows the join direction; it does not make a backtest point-in-time complete.

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

Announcements usually need a keyed event or series join rather than one global match, and revisions need an explicit vintage policy. Check that timestamps describe the same information concept and handle date-only rows, timezone normalization, and publication lags. A timestamp column does not imply a complete vintage archive.

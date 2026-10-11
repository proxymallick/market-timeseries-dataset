"""Render repository counters without inventing visitor totals."""

import argparse
import csv
from pathlib import Path


LABELS = [
    ("unique_visitors_14d", "Unique visitors (14 days)"),
    ("views_14d", "Page views (14 days)"),
    ("unique_cloners_14d", "Unique cloners (14 days)"),
    ("clones_14d", "Full clones (14 days)"),
    ("stars", "Stars"),
    ("forks", "Forks"),
    ("watchers", "Watch subscriptions"),
]


def render(rows, repository):
    rows = [
        row
        for row in rows
        if row.get("host") == "github" and row.get("resource_id") == repository
    ]
    latest = {}
    for row in sorted(rows, key=lambda item: item.get("collected_at_utc", "")):
        latest[row["metric"]] = row

    stamp = max(
        (row.get("collected_at_utc", "") for row in rows),
        default="No collection yet",
    )
    lines = [
        "# Repository analytics",
        "",
        f"I collect aggregate activity for [{repository}](https://github.com/{repository}). "
        f"The latest attempt was `{stamp}`.",
        "",
        "| Metric | Latest result |",
        "|---|---:|",
    ]
    for metric, label in LABELS:
        row = latest.get(metric, {})
        value = ""
        if row.get("status") == "ok" and row.get("value") is not None:
            value = str(row["value"])
        lines.append(f'| {label} | {value if value else "Unavailable"} |')

    lines += [
        "",
        f"[Live GitHub Traffic Insights](https://github.com/{repository}/graphs/traffic) · "
        "[CSV history](metrics_log.csv) · "
        "[Definitions and access limits](../docs/github_analytics.md)",
        "",
        "GitHub deduplicates visitors within its 14-day window. That is not an "
        "all-time people count, and daily uniques or overlapping windows cannot be "
        "added together. Views include repeats; clones exclude fetches. Missing "
        "counters stay unavailable.",
        "",
        "The current account plan disables Traffic Insights for this private "
        "repository. Traffic collection needs both a supported plan and "
        "repository-authorized API access. I store no visitor identities, IP "
        "addresses, cookies, or tracking pixels.",
    ]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    base = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repository", default="proxymallick/market-timeseries-dataset"
    )
    parser.add_argument(
        "--input", type=Path, default=base / "metrics/metrics_log.csv"
    )
    parser.add_argument("--output", type=Path, default=base / "metrics/README.md")
    args = parser.parse_args()

    with args.input.open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(rows, args.repository))

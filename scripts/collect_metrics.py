#!/usr/bin/env python3
"""Collect public, keyless repository metrics into a local append/upsert CSV."""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit
from urllib.request import Request, urlopen

FIELDS = ["collected_at_utc", "host", "resource_id", "metric", "value",
          "window_start", "window_end", "status"]
DEFAULT_CONFIG = Path(__file__).resolve().parents[1] / "hosting" / "metrics_config.json"
DEFAULT_LOG = Path(__file__).resolve().parents[1] / "metrics" / "metrics_log.csv"


def metric_row(now, host, resource_id, metric, value, start, end, status="ok"):
    return {"collected_at_utc": now.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
            "host": host, "resource_id": resource_id, "metric": metric,
            "value": value, "window_start": start, "window_end": end, "status": status}


def fetch_json(url, opener=urlopen):
    request = Request(url, headers={"Accept": "application/json", "User-Agent": "local-dataset-metrics/1.0"})
    with opener(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def github_json(url, opener=urlopen, auth=False):
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != "api.github.com":
        raise ValueError("GitHub API mode only supports api.github.com")
    if not auth:
        return fetch_json(url, opener)
    endpoint = parsed.path.lstrip("/")
    if parsed.query:
        endpoint += "?" + parsed.query
    result = subprocess.run(["gh", "api", "--hostname", "github.com", endpoint],
                            check=True, capture_output=True, text=True, timeout=30)
    return json.loads(result.stdout)


def github_release_assets(repository, opener=urlopen, auth=False):
    base = f"https://api.github.com/repos/{repository}/releases"
    releases = _pages(base, opener, auth=auth)
    rows = []
    for release in releases:
        assets = _pages(release["assets_url"], opener, auth=auth)
        for asset in assets:
            rows.append({"resource_id": f'{repository}/releases/{release.get("tag_name", release.get("id"))}/assets/{asset["name"]}',
                         "value": asset.get("download_count")})
    return rows


def _pages(url, opener, auth=False):
    rows, page = [], 1
    while True:
        separator = "&" if "?" in url else "?"
        batch = github_json(f"{url}{separator}per_page=100&page={page}", opener, auth)
        if not batch:
            return rows
        rows.extend(batch)
        if len(batch) < 100:
            return rows
        page += 1


def kaggle_rows(resource_id, metadata, now):
    start = end = now.astimezone(timezone.utc).date().isoformat()
    result = []
    for metric, key in (("views", "viewCount"), ("downloads", "downloadCount")):
        result.append(metric_row(now, "kaggle", resource_id, metric, metadata.get(key), start, end,
                                 "ok" if metadata.get(key) is not None else "unavailable"))
    return result


def _daily_rows(now, host, resource_id, metric, payload):
    uniques_metric = {"views": "unique_visitors", "clones": "unique_cloners"}.get(metric, f"{metric}_uniques")
    values = payload.get("views", payload.get("clones", []))
    out = []
    for item in values:
        timestamp = item.get("timestamp")
        day = timestamp[:10] if isinstance(timestamp, str) else item.get("date")
        count = item.get("count")
        uniques = item.get("uniques")
        out.append(metric_row(now, host, resource_id, metric, count, day, day,
                              "ok" if count is not None else "unavailable"))
        out.append(metric_row(now, host, resource_id, uniques_metric, uniques, day, day,
                              "ok" if uniques is not None else "unavailable"))
    return out


def _traffic_summary_rows(now, resource_id, metric, payload, start, end):
    names = {"views": ("views_14d", "unique_visitors_14d"),
             "clones": ("clones_14d", "unique_cloners_14d")}[metric]
    return [metric_row(now, "github", resource_id, name, payload.get(key), start, end,
                       "ok" if payload.get(key) is not None else "unavailable")
            for name, key in zip(names, ("count", "uniques"))]


def _popular_rows(now, repo, kind, values, start, end):
    rows = []
    for item in values:
        label = item.get("referrer" if kind == "referrers" else "path")
        if not isinstance(label, str):
            continue
        rid = f"{repo}/{kind}/{quote(label, safe='')}"
        for suffix, key in (("count", "count"), ("uniques", "uniques")):
            value = item.get(key)
            rows.append(metric_row(now, "github", rid, f"{kind[:-1]}_{suffix}", value,
                                   start, end, "ok" if value is not None else "unavailable"))
    return rows


def collect(config, log_path=DEFAULT_LOG, opener=urlopen, now=None, github_auth=False):
    now = now or datetime.now(timezone.utc)
    today = now.astimezone(timezone.utc).date()
    rows, failures = [], 0

    def request_rows(host, resource_id, callback):
        nonlocal failures
        try:
            collected = callback()
            rows.extend(collected)
            if any(row.get("status") == "unavailable" for row in collected):
                failures += 1
        except (HTTPError, URLError, TimeoutError, OSError, ValueError, KeyError, TypeError,
                UnicodeDecodeError, subprocess.SubprocessError):
            failures += 1
            rows.append(metric_row(now, host, resource_id, "collection_status", None,
                                   today.isoformat(), today.isoformat(), "unavailable"))

    gh = config.get("github", {})
    for repo in gh.get("repositories", []):
        base = f"https://api.github.com/repos/{repo}"
        def stars(repo=repo, base=base):
            data = github_json(base, opener, github_auth)
            return [metric_row(now, "github", repo, metric, data.get(key), today.isoformat(), today.isoformat(),
                               "ok" if data.get(key) is not None else "unavailable")
                    for metric, key in (("stars", "stargazers_count"), ("forks", "forks_count"),
                                        ("watchers", "subscribers_count"))]
        request_rows("github", repo, stars)
        request_rows("github", repo, lambda: [metric_row(now, "github", asset["resource_id"], "release_asset_downloads",
                                                          asset["value"], today.isoformat(), today.isoformat(),
                                                          "ok" if asset["value"] is not None else "unavailable")
                                                          for asset in github_release_assets(repo, opener, github_auth)])
        for metric, endpoint in (("views", "traffic/views"), ("clones", "traffic/clones")):
            def traffic(endpoint=endpoint, metric=metric):
                start = (today - timedelta(days=13)).isoformat()
                try:
                    payload = github_json(f"{base}/{endpoint}", opener, github_auth)
                except (HTTPError, URLError, TimeoutError, OSError, ValueError, TypeError,
                        UnicodeDecodeError, subprocess.SubprocessError):
                    return _traffic_summary_rows(now, repo, metric, {}, start, today.isoformat())
                output = _daily_rows(now, "github", repo, metric, payload)
                output.extend(_traffic_summary_rows(now, repo, metric, payload, start, today.isoformat()))
                return output
            request_rows("github", repo, traffic)

        for kind in ("referrers", "paths"):
            def popular(kind=kind):
                payload = github_json(f"{base}/traffic/popular/{kind}", opener, github_auth)
                start = (today - timedelta(days=13)).isoformat()
                return _popular_rows(now, repo, kind, payload, start, today.isoformat())
            request_rows("github", repo, popular)

    for resource_id in config.get("huggingface", {}).get("datasets", []):
        url = f"https://huggingface.co/api/datasets/{quote(resource_id, safe='/')}"
        def hf(resource_id=resource_id, url=url):
            data = fetch_json(url, opener)
            downloads = data.get("downloads")
            value = downloads if downloads is not None else None
            return [metric_row(now, "huggingface", resource_id, "downloads_30d", value,
                               (today - timedelta(days=29)).isoformat(), today.isoformat(),
                               "ok" if value is not None else "unavailable")]
        request_rows("huggingface", resource_id, hf)

    for record in config.get("zenodo", {}).get("records", []):
        rid = str(record)
        def zenodo(rid=rid):
            record_data = fetch_json(f"https://zenodo.org/api/records/{quote(rid)}", opener)
            stats = record_data.get("stats", {})
            output = []
            for key in ("views", "downloads"):
                value = stats.get(key)
                output.append(metric_row(now, "zenodo", rid, key, value,
                                         "cumulative", today.isoformat(),
                                         "ok" if value is not None else "unavailable"))
            for key, metric in (("version_views", "all_version_views"),
                                ("version_downloads", "all_version_downloads")):
                if stats.get(key) is not None:
                    output.append(metric_row(now, "zenodo", rid, metric, stats[key],
                                             "cumulative", today.isoformat(), "ok"))
            versions_url = record_data.get("links", {}).get("versions")
            if versions_url:
                next_url, seen = versions_url, set()
                while next_url and next_url not in seen:
                    seen.add(next_url)
                    versions_data = fetch_json(next_url, opener)
                    version_items = versions_data.get("hits", {}).get("hits", [])
                    for version in version_items:
                        version_id = str(version.get("id", ""))
                        version_stats = version.get("stats", {})
                        for key in ("views", "downloads"):
                            value = version_stats.get(key)
                            output.append(metric_row(now, "zenodo", f"{rid}/versions/{version_id}", key, value,
                                                     "cumulative", today.isoformat(),
                                                     "ok" if value is not None else "unavailable"))
                    next_url = versions_data.get("links", {}).get("next")
            return output
        request_rows("zenodo", rid, zenodo)

    for resource_id in config.get("kaggle", {}).get("datasets", []):
        url = f"https://www.kaggle.com/api/v1/datasets/view/{quote(resource_id, safe='/')}"
        request_rows("kaggle", resource_id,
                     lambda resource_id=resource_id, url=url: kaggle_rows(resource_id, fetch_json(url, opener), now))

    if rows:
        upsert_rows(log_path, rows)
    return 1 if failures else 0


def upsert_rows(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if path.exists():
        with path.open(newline="", encoding="utf-8") as stream:
            existing = list(csv.DictReader(stream))
    keyed = {(r["host"], r["resource_id"], r["metric"], r["window_start"], r["window_end"]): r for r in existing}
    for row in rows:
        key = (row["host"], row["resource_id"], row["metric"], row["window_start"], row["window_end"])
        row = dict(row)
        row["value"] = "" if row["value"] is None else row["value"]
        keyed[key] = row
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(keyed.values())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output", type=Path, default=DEFAULT_LOG)
    parser.add_argument("--github-auth", action="store_true",
                        help="use gh api authentication for GitHub requests")
    args = parser.parse_args(argv)
    try:
        config = json.loads(args.config.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        print("Metrics configuration unavailable or invalid.", file=sys.stderr)
        return 2
    return collect(config, args.output, github_auth=args.github_auth)


if __name__ == "__main__":
    raise SystemExit(main())

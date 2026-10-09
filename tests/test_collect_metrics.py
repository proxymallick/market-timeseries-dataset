import csv
import json
import sys
from urllib.parse import parse_qs, urlparse
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import collect_metrics


class Response:
    def __init__(self, data, headers=None):
        self.data = json.dumps(data).encode()
        self.headers = headers or {}

    def read(self):
        return self.data

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False


def test_github_release_asset_pagination_includes_all_pages():
    calls = []

    def opener(request, timeout=0):
        calls.append(request.full_url)
        if "releases?" in request.full_url:
            return Response([{"id": 1, "tag_name": "v1", "assets_url": "https://api.github.com/repos/o/r/releases/1/assets"}])
        page = int(parse_qs(urlparse(request.full_url).query)["page"][0])
        if page == 1:
            return Response([{"name": f"asset-{n}", "download_count": n} for n in range(100)])
        if page == 2:
            return Response([{"name": "asset-100", "download_count": 100}])
        return Response([])

    rows = collect_metrics.github_release_assets("o/r", opener=opener)
    assert len(rows) == 101
    assert len(calls) == 3


def test_log_upserts_daily_buckets_and_revisions_instead_of_summing_windows(tmp_path):
    path = tmp_path / "metrics_log.csv"
    timestamp = datetime(2026, 10, 9, tzinfo=timezone.utc)
    rows = [collect_metrics.metric_row(timestamp, "github", "o/r", "views", 7,
                                       "2026-10-08", "2026-10-08", "ok")]
    collect_metrics.upsert_rows(path, rows)
    rows[0]["value"] = 9
    collect_metrics.upsert_rows(path, rows)
    with path.open(newline="") as stream:
        stored = list(csv.DictReader(stream))
    assert len(stored) == 1
    assert stored[0]["value"] == "9"


def test_unconfigured_hosts_are_unavailable_and_do_not_emit_zero(tmp_path):
    cfg = {"github": {"repositories": []}, "huggingface": {"datasets": []},
           "zenodo": {"records": []}, "kaggle": {"datasets": []}}
    calls = []
    def opener(request, timeout=0):
        calls.append(request.full_url)
        raise AssertionError("unconfigured hosts must not make network requests")

    result = collect_metrics.collect(cfg, tmp_path / "metrics.csv", opener=opener,
                                    now=datetime(2026, 10, 9, tzinfo=timezone.utc))
    assert result == 0
    assert calls == []
    assert not (tmp_path / "metrics.csv").exists()


def test_configured_failure_is_nonzero_and_records_unavailable_without_leaking_body(tmp_path):
    def opener(request, timeout=0):
        raise collect_metrics.HTTPError(request.full_url, 404, "missing", {}, None)

    cfg = {"github": {"repositories": ["public-owner/private-repo"]}, "huggingface": {"datasets": []},
           "zenodo": {"records": []}, "kaggle": {"datasets": []}}
    status = collect_metrics.collect(cfg, tmp_path / "metrics.csv", opener=opener,
                                    now=datetime(2026, 10, 9, tzinfo=timezone.utc))
    assert status == 1
    contents = (tmp_path / "metrics.csv").read_text()
    assert "unavailable" in contents
    assert "404" not in contents and "missing" not in contents


def test_kaggle_missing_counts_stay_null(tmp_path):
    metadata = {"title": "example", "totalBytes": 42}
    rows = collect_metrics.kaggle_rows("owner/dataset", metadata,
                                       datetime(2026, 10, 9, tzinfo=timezone.utc))
    assert {r["metric"]: r["value"] for r in rows}["views"] is None
    assert {r["metric"]: r["value"] for r in rows}["downloads"] is None


def test_kaggle_missing_metrics_are_null_unavailable_and_fail_collection(tmp_path):
    def opener(request, timeout=0):
        return Response({"title": "example"})

    cfg = {"github": {"repositories": []}, "huggingface": {"datasets": []},
           "zenodo": {"records": []}, "kaggle": {"datasets": ["owner/dataset"]}}
    status = collect_metrics.collect(cfg, tmp_path / "metrics.csv", opener=opener,
                                    now=datetime(2026, 10, 9, tzinfo=timezone.utc))
    assert status == 1
    with (tmp_path / "metrics.csv").open(newline="") as stream:
        stored = list(csv.DictReader(stream))
    assert [row["value"] for row in stored] == ["", ""]
    assert [row["status"] for row in stored] == ["unavailable", "unavailable"]


def test_github_traffic_uses_official_timestamp_field_for_daily_upserts():
    now = datetime(2026, 10, 9, tzinfo=timezone.utc)
    payload = {"count": 25, "uniques": 7, "views": [
        {"timestamp": "2026-10-07T00:00:00Z", "count": 10, "uniques": 3},
        {"timestamp": "2026-10-08T00:00:00Z", "count": 15, "uniques": 4},
    ]}
    rows = collect_metrics._daily_rows(now, "github", "owner/repo", "views", payload)
    assert [(r["window_start"], r["value"]) for r in rows] == [
        ("2026-10-07", 10), ("2026-10-08", 15)]


def test_zenodo_uses_public_record_stats_and_per_version_record_stats(tmp_path):
    now = datetime(2026, 10, 9, tzinfo=timezone.utc)
    calls = []
    record_url = "https://zenodo.org/api/records/1234"
    versions_url = record_url + "/versions"
    def opener(request, timeout=0):
        calls.append(request.full_url)
        if request.full_url == record_url:
            return Response({"id": 1234, "stats": {
                "views": 25, "downloads": 12, "version_views": 40,
                "version_downloads": 20, "unique_views": 24,
                "unique_downloads": 18,
            }, "links": {"versions": versions_url}})
        if request.full_url == versions_url:
            return Response({"hits": {"hits": [{"id": 1234, "stats": {
                "views": 25, "downloads": 12, "version_views": 25,
                "version_downloads": 12,
            }}]}, "links": {"next": versions_url + "?page=2"}})
        if request.full_url == versions_url + "?page=2":
            return Response({"hits": {"hits": [{"id": 1235, "stats": {
                "views": 15, "downloads": 8,
            }}]}, "links": {"next": None}})
        raise AssertionError("unexpected Zenodo URL")

    cfg = {"github": {"repositories": []}, "huggingface": {"datasets": []},
           "zenodo": {"records": ["1234"]}, "kaggle": {"datasets": []}}
    status = collect_metrics.collect(cfg, tmp_path / "metrics.csv", opener=opener, now=now)
    assert status == 0
    assert calls == [record_url, versions_url, versions_url + "?page=2"]
    with (tmp_path / "metrics.csv").open(newline="") as stream:
        stored = list(csv.DictReader(stream))
    values = {(row["resource_id"], row["metric"]): row["value"] for row in stored}
    assert values[("1234", "views")] == "25"
    assert values[("1234", "downloads")] == "12"
    assert values[("1234", "all_version_views")] == "40"
    assert values[("1234", "all_version_downloads")] == "20"
    assert values[("1234/versions/1234", "views")] == "25"
    assert values[("1234/versions/1234", "downloads")] == "12"
    assert values[("1234/versions/1235", "views")] == "15"
    assert values[("1234/versions/1235", "downloads")] == "8"


def test_missing_github_stars_are_unavailable_and_nonzero(tmp_path):
    def opener(request, timeout=0):
        if request.full_url == "https://api.github.com/repos/owner/repo":
            return Response({"name": "repo"})
        if "/releases?" in request.full_url:
            return Response([])
        if "/traffic/" in request.full_url:
            return Response({"views": [], "clones": []})
        raise AssertionError("unexpected URL")

    cfg = {"github": {"repositories": ["owner/repo"]}, "huggingface": {"datasets": []},
           "zenodo": {"records": []}, "kaggle": {"datasets": []}}
    status = collect_metrics.collect(cfg, tmp_path / "metrics.csv", opener=opener,
                                    now=datetime(2026, 10, 9, tzinfo=timezone.utc))
    assert status == 1
    with (tmp_path / "metrics.csv").open(newline="") as stream:
        stored = list(csv.DictReader(stream))
    stars = next(row for row in stored if row["metric"] == "stars")
    assert stars["value"] == ""
    assert stars["status"] == "unavailable"

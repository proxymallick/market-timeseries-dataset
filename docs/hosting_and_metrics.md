# Hosting and metrics preparation

I have completed the private GitHub and Drive setup described in [private hosting](private_hosting.md). The private repository is configured for metrics; public dataset-host identifiers remain empty until redistribution is approved. See the [analytics summary](../metrics/README.md) and [access notes](github_analytics.md).

## Possible public hosting

If I publish later, Hugging Face Datasets is the likely home for versioned data and Zenodo for a citable metadata release. GitHub should hold code and small manifests. The roughly 235 GB local collection is too large for a normal Git repository. GitHub recommends an on-disk repository below 10 GB and caps each release asset at 2 GiB. Hugging Face recommends files below 200 GB, enforces a 500 GB per-file maximum, and applies account quotas. Zenodo documents a 50 GB record/file limit and at most 100 files. A larger release would therefore need deliberate sharding and a confirmed quota before upload.

Hugging Face's public API reports downloads over the previous 30 days; daily organization analytics require a separate plan. GitHub exposes public stars and release-asset downloads, while private traffic needs repository access. Zenodo's record response separates one-version `views` and `downloads` from concept-wide `version_views` and `version_downloads`; the collector stores the latter as `all_version_views` and `all_version_downloads`. Kaggle metadata may omit counters. In every case I record a missing field as `unavailable`, not zero.

## Local collection

Run `python3 scripts/collect_metrics.py` for keyless collection. Configure public IDs in `hosting/metrics_config.json`. The script upserts `metrics/metrics_log.csv` with collection time, host, resource, metric, value, window, and status. It stores GitHub daily buckets separately from 14-day totals and stores Hugging Face's 30-day figure as a rolling window. Stars and host counters are snapshots, never values to add across dates. A failed endpoint writes `unavailable` and returns nonzero; it does not save response bodies or invent a zero.

For this private repository, run `python3 scripts/collect_metrics.py --github-auth` with an existing GitHub CLI login, then `python3 scripts/render_analytics.py`. The collector does not inspect stored credentials. The weekly workflow uses its repository token or an optional `REPO_ANALYTICS_TOKEN` and commits only the CSV and rendered summary. The current plan blocks private Traffic Insights, so traffic remains unavailable.

`hosting/downloads_badge.json` says `not published` by design. I will replace it only when a public dataset and a defensible counter exist.

## Current official references (checked 2026-10-09)

- [GitHub repository limits](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits) — recommended repository on-disk size and general repository guidance.
- [GitHub release storage and bandwidth quotas](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) — per-asset and total release limits; release assets expose download counts.
- [GitHub REST API: repository traffic](https://docs.github.com/en/rest/metrics/traffic) — views and clones are per-day data; availability requires repository access.
- [Hugging Face Hub storage limits](https://huggingface.co/docs/hub/storage-limits) — account quotas and per-repository/file recommendations and limits.
- [Hugging Face dataset API client reference](https://huggingface.co/docs/huggingface_hub/en/package_reference/hf_api) — dataset `downloads` is the prior 30 days.
- [Hugging Face Publisher Analytics](https://huggingface.co/docs/hub/publisher-analytics) — daily breakdown is an organization analytics feature.
- [Zenodo API](https://developers.zenodo.org/) — documents `GET /api/records/:id`; the [statistics implementation](https://github.com/zenodo/zenodo/blob/master/zenodo/modules/stats/utils.py#L655-L719) scopes unprefixed counters to `recid` and `version_*` counters to `conceptrecid`. This distinction matches the [statistics FAQ](https://zenodo.org/help/statistics), which describes aggregate and per-version counts. A [sample public record response](https://zenodo.org/api/records/5109709) inspected on 2026-10-09 contained the corresponding fields. [Zenodo quota guide](https://help.zenodo.org/docs/deposit/manage-quota/) documents default quota details.
- [Kaggle API documentation](https://www.kaggle.com/docs/api) — dataset API access and authentication requirements may vary; this collector does not read Kaggle credentials.

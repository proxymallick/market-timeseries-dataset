# GitHub visitors and analytics

The private repository is <https://github.com/proxymallick/market-timeseries-dataset>. I keep the latest counters in the [summary](../metrics/README.md) and retain each collection in the [CSV history](../metrics/metrics_log.csv).

On 2026-10-09 UTC, GitHub redirected the signed-in Traffic page to Dependency Insights and disabled Traffic for this private repository. I did not make the repository public or buy an upgrade. Visitor and traffic counts are therefore **unavailable**, not zero. The saved CLI token also returned 404 because it cannot access this repository; GitHub Desktop uses separate authorization.

## What the counters mean

| Counter | Interpretation |
|---|---|
| Unique visitors, 14 days | GitHub's window-level deduplicated visitor count; not identifiable individuals or all-time people |
| Page views, 14 days | Visits to repository pages, including repeat views |
| Daily visitors/views | UTC daily buckets retained in CSV; daily visitors cannot be summed into a unique window count |
| Full clones / unique cloners | Full repository clones and distinct cloners; fetches are excluded |
| Referrers | GitHub's top ten referral sources and their counts/uniques for the available window |
| Popular content | GitHub's top ten repository paths and counts/uniques |
| Stars / forks / watch subscriptions | Repository metadata snapshots, independent of traffic |
| Release asset downloads | Asset counters when actual release assets exist; no repository-file download counter is invented |

I keep GitHub's 14-day totals separate from its daily buckets. Weekly runs preserve what GitHub exposes before the short window expires, but they cannot recover older history or create an all-time count of people. I never add overlapping windows or cumulative snapshots. Referrers and popular paths are top-ten lists, not a full visitor log.

## Collection and access

Run `python scripts/collect_metrics.py --github-auth` to use the existing `gh api` login. The script does not read or print credential files or token values. Without that flag it stays keyless. Authenticated requests are restricted to `api.github.com`, and failed endpoints are recorded as unavailable. Build the summary with `python scripts/render_analytics.py`.

The weekly action uses the repository-scoped `GITHUB_TOKEN` for metadata and asset counters. It can use an optional `REPO_ANALYTICS_TOKEN` secret for traffic. GitHub documents **Administration: read** as the required fine-grained permission; Contents access alone is insufficient. The account plan must also support private traffic. Never place a token in source, CSV, command arguments, or chat.

I keep these reports inside the private repository. They contain aggregate counts and repository or referrer paths, not identities, IP addresses, contact details, cookies, or tracking pixels. The history can still reveal private usage patterns, so it needs review before any public release.

## Official references, checked 2026-10-09 UTC

- [Viewing traffic to a repository](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository): plan availability, 14-day window, UTC timing, update cadence and full-clone semantics.
- [Repository traffic REST endpoints](https://docs.github.com/en/rest/metrics/traffic): views, unique counts, clones, referrers, popular paths and Administration read permission.

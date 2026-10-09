# GitHub visitors and analytics

Repository: https://github.com/proxymallick/market-timeseries-dataset. See [the current summary](../metrics/README.md) and [CSV history](../metrics/metrics_log.csv).

On 2026-10-09 UTC the signed-in GitHub Traffic URL redirected to Dependency Insights. The page explicitly disabled Traffic for this private repository and stated: “Upgrade to GitHub Pro or make this repository public to enable this feature.” No private-to-public change or paid upgrade was performed. Current visitor and traffic counts are **unavailable**, not zero. A CLI traffic request also returned 404 because its saved token does not have access to this new private repository; GitHub Desktop push authorization is separate from GitHub CLI API access.

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

The collection keeps response-level 14-day totals separately from daily counts. Weekly runs preserve observed buckets before GitHub's short retention window expires, but cannot recover earlier history or create an all-time unique-person count. Overlapping windows and cumulative snapshots are never added together. Popular sources/paths are incomplete top-ten lists, not a full visitor log. Empty lists are not individual visitor counts.

## Collection and access

`python scripts/collect_metrics.py --github-auth` delegates authenticated requests to the existing `gh api` client. It does not read or print credential files, passwords or token values. Plain invocation remains keyless. Authenticated GitHub API requests stay on `api.github.com`; other hosts remain public/keyless. Failed endpoints are logged as unavailable. The report is generated with `python scripts/render_analytics.py`.

The weekly GitHub Action uses the existing repository-scoped `GITHUB_TOKEN` through the `gh` client for metadata and asset counters, and can use an optional owner-configured Actions secret named `REPO_ANALYTICS_TOKEN` for traffic. GitHub's documented traffic API fine-grained permission is **Administration: read** on this repository; ordinary Contents access alone does not provide traffic access. An eligible account plan and repository API permissions must both be checked. Do not put a token in source, CSV, command arguments or a chat message. Creating or broadening token access is an owner step; none was performed here.

All reporting remains inside this private repository. Only aggregate counts and repository/referrer paths are stored. No personal visitor identities, IPs, contact details or cross-site tracking are collected. Traffic and popularity fields may disclose private repository usage patterns, so review this history before any later public release.

## Official references, checked 2026-10-09 UTC

- [Viewing traffic to a repository](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository): plan availability, 14-day window, UTC timing, update cadence and full-clone semantics.
- [Repository traffic REST endpoints](https://docs.github.com/en/rest/metrics/traffic): views, unique counts, clones, referrers, popular paths and Administration read permission.

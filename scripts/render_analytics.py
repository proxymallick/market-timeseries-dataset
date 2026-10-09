"""Render a private repository's aggregate counters without inferring people."""
import argparse,csv
from pathlib import Path

LABELS=[('unique_visitors_14d','Unique visitors (14 days)'),('views_14d','Page views (14 days)'),('unique_cloners_14d','Unique cloners (14 days)'),('clones_14d','Full clones (14 days)'),('stars','Stars'),('forks','Forks'),('watchers','Watch subscriptions')]

def render(rows,repository):
    rows=[r for r in rows if r.get('host')=='github' and r.get('resource_id')==repository]
    latest={}
    for row in sorted(rows,key=lambda r:r.get('collected_at_utc','')):latest[row['metric']]=row
    stamp=max((r.get('collected_at_utc','') for r in rows),default='No collection yet')
    lines=['# Repository analytics','',f'Repository: [{repository}](https://github.com/{repository})',f'Latest collection attempt: {stamp}','', '| Metric | Latest result |','|---|---:|']
    for metric,label in LABELS:
        row=latest.get(metric,{})
        value=str(row.get('value','')) if row.get('status')=='ok' and row.get('value') is not None else ''
        lines.append(f'| {label} | {value if value else "Unavailable"} |')
    lines += ['',f'[Live GitHub Traffic Insights](https://github.com/{repository}/graphs/traffic) · [CSV history](metrics_log.csv) · [Definitions and access limits](../docs/github_analytics.md)','', 'GitHub reports unique visitors for the selected 14-day window; this is not an all-time count of people. Daily uniques and overlapping windows must not be summed. Views can include repeat visits; clones exclude fetches. Missing or inaccessible measurements remain unavailable.', '', 'Current private-repository Traffic Insights is disabled by the account plan. A supported private-repository plan and repository-authorized API access are needed for traffic collection. See the access notes before enabling a token. Counts have no visitor identities, IP addresses, cookies or tracking pixels.']
    return '\n'.join(lines)+'\n'

if __name__=='__main__':
    base=Path(__file__).resolve().parents[1]
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--repository',default='proxymallick/market-timeseries-dataset');parser.add_argument('--input',type=Path,default=base/'metrics/metrics_log.csv');parser.add_argument('--output',type=Path,default=base/'metrics/README.md')
    args=parser.parse_args()
    with args.input.open(newline='') as stream:rows=list(csv.DictReader(stream))
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(render(rows,args.repository))

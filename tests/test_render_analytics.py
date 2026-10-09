import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))

def test_summary_uses_window_uniques_and_distinguishes_zero():
    from render_analytics import render
    def row(metric,value,status='ok',stamp='2026-10-09T14:00:00Z'):
        return dict(host='github',resource_id='o/r',metric=metric,value=value,status=status,collected_at_utc=stamp,window_start='2026-09-26',window_end='2026-10-09')
    text=render([row('unique_visitors',4),row('unique_visitors',7),row('unique_visitors_14d',8),row('views_14d',0),row('clones_14d','', 'unavailable')],'o/r')
    assert '| Unique visitors (14 days) | 8 |' in text
    assert '| Page views (14 days) | 0 |' in text
    assert '| Full clones (14 days) | Unavailable |' in text
    assert '| Unique visitors (14 days) | 11 |' not in text

def test_new_failure_does_not_show_old_count_as_current():
    from render_analytics import render
    rows=[dict(host='github',resource_id='o/r',metric='unique_visitors_14d',value=8,status='ok',collected_at_utc='2026-10-08T00:00:00Z'),dict(host='github',resource_id='o/r',metric='unique_visitors_14d',value='',status='unavailable',collected_at_utc='2026-10-09T00:00:00Z')]
    assert '| Unique visitors (14 days) | Unavailable |' in render(rows,'o/r')

import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
try:
    from release_selection import classify_dependencies, release_allowed, require_public_sources
except ImportError:
    classify_dependencies = release_allowed = require_public_sources = None

def test_mixed_source_table_inherits_blocked_dependency():
    assert classify_dependencies is not None, 'release selection implementation missing'
    assert classify_dependencies(['conditional','restricted']) == 'restricted'
    assert classify_dependencies(['conditional','unclear']) == 'unclear'

def test_conditional_data_requires_actual_conditions_and_commercial_permission():
    assert release_allowed is not None, 'release selection implementation missing'
    assert not release_allowed('conditional', False, True, 'observations')
    assert not release_allowed('conditional', True, False, 'observations')
    assert release_allowed('conditional', True, True, 'observations')

def test_unknown_dependencies_and_experiment_artifacts_are_excluded():
    assert classify_dependencies is not None, 'release selection implementation missing'
    assert classify_dependencies([]) == 'unclear'
    assert not release_allowed('safe', True, True, 'analysis_or_model_artifact')

def test_changed_or_incomplete_source_audit_blocks_public_builder():
    assert require_public_sources is not None, 'registry guard missing'
    allowed={'agency':{'classification':'conditional','commercial_permitted':True}}
    require_public_sources(['agency'],allowed,True)
    with pytest.raises(ValueError):require_public_sources(['missing'],allowed,True)
    with pytest.raises(ValueError):require_public_sources(['agency'],allowed,False)
    for classification,commercial in [('restricted',True),('unclear',True),('conditional',False),('conditional','UNKNOWN')]:
        with pytest.raises(ValueError):require_public_sources(['agency'],{'agency':{'classification':classification,'commercial_permitted':commercial}},True)

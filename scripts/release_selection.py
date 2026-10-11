"""Decide which local sources can enter the release."""
def classify_dependencies(classifications):
    values=set(classifications)
    if 'restricted' in values:
        return 'restricted'
    if not values or 'unclear' in values or values-{'safe','conditional'}:
        return 'unclear'
    return 'conditional' if 'conditional' in values else 'safe'

def release_allowed(classification, conditions_satisfied, commercial_permitted, role):
    return (classification in {'safe','conditional'} and conditions_satisfied
            and commercial_permitted and role in {'observations','archive','instrument_metadata'})

def require_public_sources(source_ids, registry, conditions_satisfied, role='observations'):
    if not source_ids:raise ValueError('A public output needs verified source dependencies')
    for key in source_ids:
        entry=registry.get(key,{})
        commercial=entry.get('commercial_permitted') is True
        if not release_allowed(entry.get('classification','unclear'), conditions_satisfied, commercial, role):
            raise ValueError(f'Source {key} is not cleared for this public output')

"""Compatibility command dispatcher; domain services migrate in later tasks."""

from ._legacy import *  # noqa: F401,F403 - preserve the established CLI surface

# Focused service modules are exported from the compatibility facade so direct
# imports can migrate without changing the executable command contract.
from .metadata import (  # noqa: F401
    MetadataResolver,
    default_metadata_cache_dir,
    normalize_name,
    normalize_rate_limit,
    select_named,
)
from .reports import (  # noqa: F401
    event_request,
    hydrate_discovery_report,
    iter_event_pages,
    parse_report_reference,
    report_data,
    report_request,
    write_event_jsonl,
)

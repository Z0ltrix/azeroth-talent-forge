"""Report references, report payloads, and event export service boundary.

The compatibility implementation remains in ``_legacy`` during this migration;
these lazy delegates keep the public behavior stable while callers move to the
focused module.
"""


def _legacy():
    from . import _legacy
    return _legacy


def parse_report_reference(value):
    return _legacy().parse_report_reference(value)


def report_request(args):
    return _legacy().report_request(args)


def report_data(payload, kind):
    return _legacy().report_data(payload, kind)


def hydrate_discovery_report(client, code, filters, fight_id=None):
    return _legacy().hydrate_discovery_report(client, code, filters, fight_id)


def iter_event_pages(client, code, variables, max_pages=10):
    return _legacy().iter_event_pages(client, code, variables, max_pages)


def write_event_jsonl(path, metadata, events):
    return _legacy().write_event_jsonl(path, metadata, events)


def event_request(args):
    return _legacy().event_request(args)

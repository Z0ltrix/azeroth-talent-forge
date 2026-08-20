#!/usr/bin/env python3
"""Opt-in, bounded live contract and public-report smoke check."""

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from warcraftlogs_core.credentials import resolve_credentials
from warcraftlogs_core.models import ApiError, Credentials
from warcraftlogs_core.reports import parse_report_reference
from warcraftlogs_core.transport import GRAPHQL_URL, WarcraftLogsClient, load_query, sanitize_graphql_errors

OPT_IN = "WARCRAFTLOGS_LIVE_CHECK"
CLIENT_ID = "WARCRAFTLOGS_CLIENT_ID"
CLIENT_SECRET = "WARCRAFTLOGS_CLIENT_SECRET"
TEST_REPORT = "WARCRAFTLOGS_TEST_REPORT"
TEST_FIGHT = "WARCRAFTLOGS_TEST_FIGHT"
INTROSPECTION_QUERY = """
query WarcraftLogsLiveCheckSchema {
  __type(name: "Report") {
    fields {
      name
      args { name type { kind name ofType { kind name ofType { kind name } } } }
    }
  }
}
""".strip()


class LiveCheckError(RuntimeError):
    pass


def build_parser():
    parser = argparse.ArgumentParser(description="Opt-in Warcraft Logs schema/report smoke check")
    parser.add_argument("--report", help="public report code or Warcraft Logs report URL")
    parser.add_argument("--fight", type=int, help="public fight ID")
    return parser


def required_schema_fixture():
    """Small fake-client schema used by local tests; live responses use __type."""
    return {"contracts": {
        "fights": {"fightIDs": "[Int]", "translate": "Boolean"},
        "playerDetails": {"includeCombatantInfo": "Boolean"},
        "events": {"fightIDs": "[Int!]", "abilityID": "Float", "hostilityType": "HostilityType", "limit": "Int"},
        "table": {"fightIDs": "[Int]", "viewOptions": "Int"},
        "graph": {"fightIDs": "[Int]", "viewOptions": "Int"},
    }}


def _type_name(type_info):
    if not isinstance(type_info, dict):
        return ""
    kind = type_info.get("kind")
    name = type_info.get("name")
    if kind == "NON_NULL":
        return _type_name(type_info.get("ofType")) + "!"
    if kind == "LIST":
        return "[" + _type_name(type_info.get("ofType")) + "]"
    return name or ""


def _schema_fields(payload):
    contracts = payload.get("contracts") if isinstance(payload, dict) else None
    if isinstance(contracts, dict):
        return contracts
    try:
        fields = payload["data"]["__type"]["fields"]
    except (KeyError, TypeError):
        raise LiveCheckError("schema response missing Report fields")
    result = {}
    for field in fields or []:
        if not isinstance(field, dict) or not isinstance(field.get("name"), str):
            continue
        result[field["name"]] = {
            arg["name"]: _type_name(arg.get("type"))
            for arg in field.get("args", [])
            if isinstance(arg, dict) and isinstance(arg.get("name"), str)
        }
    return result


def validate_schema(client):
    if isinstance(client, WarcraftLogsClient):
        payload = _execute_document(client, INTROSPECTION_QUERY, {})
    else:
        payload = client.execute("__introspection__", {})
    fields = _schema_fields(payload)
    expected = {
        "fights": {"fightIDs": "[Int]"},
        "playerDetails": {"includeCombatantInfo": "Boolean"},
        "events": {"abilityID": "Float", "hostilityType": "HostilityType", "limit": "Int"},
        "table": {},
        "graph": {},
    }
    for field, arguments in expected.items():
        if field not in fields:
            raise LiveCheckError("schema drift: Report.%s is unavailable" % field)
        for name, type_name in arguments.items():
            if fields[field].get(name) != type_name:
                raise LiveCheckError("schema drift: Report.%s.%s has unexpected type" % (field, name))
    for field in ("table", "graph"):
        if "viewOptions" in load_query("report-" + field) and "viewOptions" not in fields[field]:
            raise LiveCheckError("schema drift: Report.%s.viewOptions is unavailable" % field)
    for field in ("table", "graph"):
        for obsolete in ("sourcePetType", "sourceSpec", "targetPetType", "targetSpec"):
            if obsolete in fields[field]:
                raise LiveCheckError("schema contract unexpectedly exposes obsolete %s" % obsolete)
    events_query = load_query("report-events")
    if "$abilityID: Float" not in events_query or "hostilityType" not in events_query:
        raise LiveCheckError("query contract drift: events filters")
    if "includeCombatantInfo: true" not in load_query("report-player-details"):
        raise LiveCheckError("query contract drift: combatant info")
    return True


def _execute_document(client, document, variables):
    body = json.dumps({"query": document, "variables": dict(variables)}, separators=(",", ":")).encode("utf-8")
    request = urllib.request.Request(
        GRAPHQL_URL, data=body,
        headers={"Authorization": "Bearer " + client.access_token(), "Content-Type": "application/json"},
        method="POST",
    )
    return client._open_json(request)


def _make_client(credentials):
    return WarcraftLogsClient(credentials)


def _payload_errors(payload):
    errors = payload.get("errors") if isinstance(payload, dict) else None
    if errors:
        safe = sanitize_graphql_errors(errors)
        message = safe[0].get("message") if safe else "GraphQL request failed"
        raise LiveCheckError("API error: " + str(message))


def _count(payload, command):
    try:
        report = payload["data"]["reportData"]["report"]
    except (KeyError, TypeError):
        return 0
    if command == "report-fights":
        value = report.get("fights", [])
    elif command == "report-events":
        value = report.get("events", {}).get("data", [])
    elif command == "report-player-details":
        value = report.get("playerDetails", {})
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except (TypeError, ValueError):
                return 1 if value else 0
        value = value.get("players", value) if isinstance(value, dict) else value
    else:
        value = report.get(command[7:], {})
        value = value.get("data", value) if isinstance(value, dict) else value
    return len(value) if isinstance(value, (list, dict)) else (1 if value else 0)


def _safe_message(error, secrets):
    message = str(error).splitlines()[0][:240]
    message = re.split(r"[\[{]", message, maxsplit=1)[0].rstrip()
    for secret in secrets:
        if secret:
            message = message.replace(secret, "[redacted]")
    message = re.sub(r"(access_token|client_secret|client_id)\s*[:=]\s*[^,}\s]+", r"\1=[redacted]", message, flags=re.I)
    return message


def smoke(client, report, fight):
    common = {"code": report, "allowUnlisted": False, "fightIDs": [fight]}
    calls = [
        ("report-fights", {"code": report, "allowUnlisted": False, "translate": True}),
        ("report-player-details", dict(common, translate=True)),
        ("report-table", dict(common, dataType="Summary")),
        ("report-graph", dict(common, dataType="DamageDone")),
        ("report-events", dict(common, limit=100)),
    ]
    for command, variables in calls:
        payload = client.execute(command, variables)
        _payload_errors(payload)
        print("OK %s count=%d" % (command, _count(payload, command)))


def run(environment=None, client=None, args=None):
    environment = dict(os.environ if environment is None else environment)
    if environment.get(OPT_IN) != "1":
        print("not enabled: set %s=1" % OPT_IN)
        return 0
    args = args or build_parser().parse_args([])
    report_value = args.report or environment.get(TEST_REPORT)
    fight_value = args.fight if args.fight is not None else environment.get(TEST_FIGHT)
    if not report_value or not fight_value:
        print("not enabled: %s and %s are required" % (TEST_REPORT, TEST_FIGHT))
        return 2
    try:
        reference = parse_report_reference(report_value)
        fight = int(fight_value)
        if fight < 1:
            raise ValueError
        if client is None:
            credentials = resolve_credentials(None, None, None, Path.cwd(), environment)
            client = _make_client(credentials)
        validate_schema(client)
        smoke(client, reference.code, fight)
        print("live check passed: report=%s fight=%d" % (reference.code, fight))
        return 0
    except Exception as error:
        secrets = [environment.get(CLIENT_ID), environment.get(CLIENT_SECRET)]
        prefix = "API error: " if isinstance(error, ApiError) else ""
        print(prefix + _safe_message(error, secrets))
        return 1


def main(argv=None):
    args = build_parser().parse_args(argv)
    return run(args=args)


if __name__ == "__main__":
    raise SystemExit(main())

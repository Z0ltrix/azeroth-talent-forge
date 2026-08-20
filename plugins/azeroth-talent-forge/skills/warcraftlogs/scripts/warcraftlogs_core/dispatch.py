"""CLI command dispatch and output handling."""
import json
import os
import sys
from pathlib import Path
from typing import Optional, Sequence
from .credentials import resolve_credentials
from .transport import WarcraftLogsClient
from .metadata import MetadataResolver, normalize_rate_limit
from .models import *
from .reports import *
from .discovery import *
from .discovery import _identity_variables, _discovery_filters, _filters_dict, _global_filters, _expansion_variables
from .parser import build_parser

def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command not in ("rate-limit", "metadata", "report", "find"):
        return 0
    try:
        credentials = resolve_credentials(
            args.client_id,
            args.client_secret,
            args.env_file,
            Path.cwd(),
            os.environ,
        )
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2
    client = WarcraftLogsClient(credentials)
    if args.command == "find":
        if args.find_command == "global":
            try:
                if not 1 <= args.top <= GLOBAL_TOP_MAX:
                    raise ValueError("Global top must be between 1 and 100")
                if args.page < 1 or args.max_pages < 1 or args.max_pages > GLOBAL_MAX_PAGES:
                    raise ValueError("Global page and max pages must be between 1 and 5")
                if args.leaderboard is not None:
                    raise ValueError("Global leaderboard filtering is not supported by the public Warcraft Logs API")
                filters = _global_filters(args, client)
                result = discover_global(
                    client, filters, args.top, args.page, args.max_pages,
                    metric=args.metric, leaderboard=args.leaderboard,
                    server_region=args.server_region, server_slug=args.server_slug,
                    expansion_id=args.expansion_id,
                )
            except AuthenticationError as error:
                print(json.dumps(make_global_result([], args.top, {}, errors=[{"message": str(error)}]), ensure_ascii=True))
                return 3
            except ValueError as error:
                print(str(error), file=sys.stderr)
                return 2
            except (ApiError, KeyError, TypeError, OSError):
                print(json.dumps(make_global_result([], args.top, {}, errors=[{"message": "Warcraft Logs API response did not contain global discovery data"}]), ensure_ascii=True))
                return 4
            print(json.dumps(result, ensure_ascii=True))
            return 0
        if args.find_command not in ("character", "guild"):
            return 0
        try:
            identity = _identity_variables(args.name, args.server, args.region)
            filters = _discovery_filters(args)
            if args.page < 1 or args.max_pages < 1:
                raise ValueError("Discovery page and max pages must be positive")
            if not 1 <= args.limit <= 100:
                raise ValueError("Discovery limit must be between 1 and 100")
            result = discover_reports(
                client, args.find_command, identity, filters, args.page, args.limit, args.max_pages
            )
        except AuthenticationError as error:
            print(str(error), file=sys.stderr)
            return 3
        except ValueError as error:
            print(str(error), file=sys.stderr)
            return 2
        except (ApiError, KeyError, TypeError, OSError):
            print("Warcraft Logs API response did not contain discovery data", file=sys.stderr)
            return 4
        scope = {
            "name": identity["name"],
            "server": identity["serverSlug"],
            "region": identity["serverRegion"],
        }
        if result.get("character") is not None:
            scope["character"] = result["character"].get("name")
        envelope = make_envelope(
            "find " + args.find_command, scope, _filters_dict(filters), "api_collection",
            result["data"], pagination=result["pagination"],
            candidate_count=result["candidate_count"],
            hydrated_count=result["hydrated_count"],
            matched_count=result["matched_count"],
            excluded_count=result["excluded_count"],
            exclusion_reasons=result["exclusion_reasons"],
        )
        print(json.dumps(envelope, ensure_ascii=True))
        return 0
    if args.command == "report":
        if args.report_command == "events":
            try:
                unused, variables, scope, filters = event_request(args)
            except ValueError as error:
                print(str(error), file=sys.stderr)
                return 2
            try:
                pages = list(iter_event_pages(client, unused.code, variables, args.max_pages))
            except AuthenticationError as error:
                print(str(error), file=sys.stderr)
                return 3
            except PublicReportError as error:
                print(str(error), file=sys.stderr)
                return 4
            except RuntimeError as error:
                print(str(error), file=sys.stderr)
                return 4
            except (ApiError, KeyError, TypeError, OSError, ValueError):
                print("Warcraft Logs API response did not contain event data", file=sys.stderr)
                return 4
            data = [event for page in pages for event in page["data"]]
            last_cursor = pages[-1]["nextPageTimestamp"] if pages else None
            truncated = bool(
                pages and last_cursor is not None and
                (args.end_time is None or last_cursor < args.end_time) and
                len(pages) >= args.max_pages
            )
            pagination = {"pages_fetched": len(pages), "truncated": truncated}
            errors = [error for page in pages for error in page.get("errors", [])]
            envelope = make_envelope(
                "report events", scope, filters, "api_collection", data,
                pagination=pagination, errors=errors,
            )
            try:
                if args.output:
                    write_event_jsonl(args.output, envelope, data)
            except OSError:
                print("Could not write event output file", file=sys.stderr)
                return 4
            print(json.dumps(envelope, ensure_ascii=True))
            return 0
        if args.report_command not in REPORT_KINDS:
            return 0
        try:
            unused, variables, scope, filters = report_request(args)
        except ValueError as error:
            print(str(error), file=sys.stderr)
            return 2
        try:
            payload = client.execute("report-" + args.report_command, variables)
            data = report_data(
                payload,
                args.report_command,
                getattr(args, "absolute_start_time", None),
                getattr(args, "absolute_end_time", None),
                getattr(args, "time_mode", None) or "started",
            )
        except AuthenticationError as error:
            print(str(error), file=sys.stderr)
            return 3
        except PublicReportError as error:
            print(str(error), file=sys.stderr)
            return 4
        except (ApiError, KeyError, TypeError, OSError, ValueError):
            print("Warcraft Logs API response did not contain a public report", file=sys.stderr)
            return 4
        print(
            json.dumps(
                make_envelope(
                    "report " + args.report_command,
                    scope,
                    filters,
                    "single_report",
                    data,
                    errors=payload.get("errors"),
                ),
                ensure_ascii=True,
            )
        )
        return 0
    if args.command == "metadata":
        resolver = MetadataResolver(client, no_cache=args.no_cache)
        try:
            if args.kind == "realms":
                data, provenance = resolver.realm(args.region, args.name)
                scope = {"region": args.region}
                filters = {"name": args.name}
            elif args.kind in ("regions", "zones", "encounters", "seasons"):
                world, provenance = resolver.world(_expansion_variables(args.expansion_id))
                scope = {"expansion_id": args.expansion_id}
                filters = {}
                if args.kind == "regions":
                    data = world["regions"]
                elif args.kind == "zones":
                    data = world["zones"]
                elif args.kind == "encounters":
                    data = [
                        dict(encounter, zone={"id": zone["id"], "name": zone["name"]})
                        for zone in world["zones"]
                        for encounter in zone["encounters"]
                    ]
                else:
                    data = [
                        dict(partition, zone={"id": zone["id"], "name": zone["name"]})
                        for zone in world["zones"]
                        for partition in zone["partitions"]
                    ]
            else:
                game, provenance = resolver.game({"abilityLimit": args.ability_limit, "abilityPage": args.ability_page})
                scope = {}
                filters = {"limit": args.ability_limit, "page": args.ability_page} if args.kind == "abilities" else {}
                if args.kind == "classes":
                    data = [{field: value for field, value in item.items() if field != "specs"} for item in game["classes"]]
                elif args.kind == "specs":
                    data = [
                        dict(spec, game_class={"id": game_class["id"], "name": game_class["name"], "slug": game_class["slug"]})
                        for game_class in game["classes"]
                        for spec in game_class["specs"]
                    ]
                else:
                    data = game[args.kind]
        except AuthenticationError as error:
            print(str(error), file=sys.stderr)
            return 3
        except ValueError as error:
            print(str(error), file=sys.stderr)
            return 2
        except (ApiError, KeyError, TypeError, OSError):
            print("Warcraft Logs API response did not contain metadata", file=sys.stderr)
            return 4
        print(
            json.dumps(
                make_envelope(
                    "metadata " + args.kind,
                    scope,
                    filters,
                    "api_collection",
                    data,
                    errors=resolver.errors,
                    cache=provenance,
                ),
                ensure_ascii=True,
            )
        )
        return 0
    try:
        payload = client.execute("rate-limit", {})
    except AuthenticationError as error:
        print(str(error), file=sys.stderr)
        return 3
    except (ApiError, OSError, ValueError):
        print("Warcraft Logs API request failed", file=sys.stderr)
        return 4
    try:
        data = normalize_rate_limit(payload)
    except (KeyError, TypeError):
        print("Warcraft Logs API response did not contain rate limit data", file=sys.stderr)
        return 4
    print(
        json.dumps(
            make_envelope(
                "rate-limit",
                {},
                {},
                "api_collection",
                data,
                errors=payload.get("errors"),
            ),
            ensure_ascii=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

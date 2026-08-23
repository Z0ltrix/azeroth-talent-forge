"""Offline JSON CLI for Retail Blizzard talent strings."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

try:
    from talent_engine.assets import AssetIntegrityError, AssetLoader
    from talent_engine.codec import decode_build, decode_header, encode_build
    from talent_engine.errors import TalentError
    from talent_engine.graph_store import GraphStore
    from talent_engine.models import BuildRequest
    from talent_engine.operations import compare_builds, inspect_build, modify_build
    from talent_engine.presets import PresetStore
    from talent_engine.solver import generate_build
    from talent_engine.validator import validate_build
except ModuleNotFoundError:  # Imported as scripts.talents by repository tests.
    from scripts.talent_engine.assets import AssetIntegrityError, AssetLoader
    from scripts.talent_engine.codec import decode_build, decode_header, encode_build
    from scripts.talent_engine.errors import TalentError
    from scripts.talent_engine.graph_store import GraphStore
    from scripts.talent_engine.models import BuildRequest
    from scripts.talent_engine.operations import compare_builds, inspect_build, modify_build
    from scripts.talent_engine.presets import PresetStore
    from scripts.talent_engine.solver import generate_build
    from scripts.talent_engine.validator import validate_build


SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSETS_ROOT = SKILL_ROOT / "assets"
SHARE_PREFIX = "https://www.wowhead.com/talent-calc/blizzard/"


def share_url(code: str) -> str:
    return SHARE_PREFIX + code


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Offline Retail WoW talent string operations")
    sub = parser.add_subparsers(dest="command", required=True)
    assets = sub.add_parser("assets")
    assets_sub = assets.add_subparsers(dest="assets_command", required=True)
    assets_info = assets_sub.add_parser("info")
    assets_info.add_argument("--build")
    for command in ("inspect", "validate"):
        item = sub.add_parser(command)
        item.add_argument("--code", required=True)
        item.add_argument("--build")
        item.add_argument("--level", type=int, default=90)
    compare = sub.add_parser("compare")
    compare.add_argument("--left", required=True)
    compare.add_argument("--right", required=True)
    compare.add_argument("--build")
    compare.add_argument("--level", type=int, default=90)
    modify = sub.add_parser("modify")
    modify.add_argument("--code", required=True)
    modify.add_argument("--build")
    modify.add_argument("--level", type=int, default=90)
    modify.add_argument("--set", dest="set_ranks", action="append", default=[])
    modify.add_argument("--clear", action="append", default=[])
    modify.add_argument("--choice", action="append", default=[])
    modify.add_argument("--hero")
    modify.add_argument("--cascade", action="store_true")
    generate = sub.add_parser("generate")
    generate.add_argument("--spec", required=True, type=int)
    generate.add_argument("--build")
    generate.add_argument("--level", type=int, default=90)
    generate.add_argument("--hero", type=int)
    generate.add_argument("--require", action="append", default=[])
    generate.add_argument("--forbid", action="append", default=[])
    generate.add_argument("--prefer", action="append", default=[])
    presets = sub.add_parser("presets")
    presets_sub = presets.add_subparsers(dest="presets_command", required=True)
    list_parser = presets_sub.add_parser("list")
    list_parser.add_argument("--build")
    list_parser.add_argument("--spec", type=int)
    list_parser.add_argument("--category")
    show_parser = presets_sub.add_parser("show")
    show_parser.add_argument("--id", required=True)
    show_parser.add_argument("--build")
    return parser


def _load_graph(code: str, build: str | None, level: int = 90):
    _version, spec_id, _tree_hash = decode_header(code)
    bundle = AssetLoader(ASSETS_ROOT).open(build)
    graph = GraphStore(bundle).load_spec(spec_id)
    return bundle, graph, decode_build(code, graph, level=level)


def _build_result(operation: str, build, graph, *, diff=None) -> dict:
    code = encode_build(build, graph)
    validation = validate_build(build, graph)
    if not validation.valid:
        raise TalentError("ILLEGAL_BUILD", "build is invalid", violations=[asdict(item) for item in validation.violations])
    return {"status": "ok", "operation": operation, "snapshot": {"valid_for_build": build.snapshot.game_build, "source_patch_verified": build.snapshot.source_patch_verified}, "validation": {"valid": True, "violations": []}, "diff": [asdict(item) for item in (diff or [])], "export_string": code, "share_url": share_url(code), "export_hash_policy": "third-party-zero", "warnings": []}


def run(args: argparse.Namespace) -> dict:
    if args.command == "assets":
        bundle = AssetLoader(ASSETS_ROOT).open(args.build)
        return {"status": "ok", "operation": "assets-info", "manifest": bundle.manifest, "preset_count": len(bundle.presets)}
    if args.command == "presets":
        bundle = AssetLoader(ASSETS_ROOT).open(args.build)
        store = PresetStore(bundle.presets)
        if args.presets_command == "list":
            return {"status": "ok", "operation": "presets-list", "presets": store.list(spec_id=args.spec, category=args.category)}
        graph = GraphStore(bundle).load_spec(decode_header(next(item["code"] for item in bundle.presets if item.get("preset_id") == args.id))[1])
        preset, build = store.show(args.id, graph)
        return {"status": "ok", "operation": "presets-show", "preset": preset, "build": inspect_build(build, graph)}
    if args.command == "inspect":
        _bundle, graph, build = _load_graph(args.code, args.build, args.level)
        result = inspect_build(build, graph)
        result.update({"status": "ok", "operation": "inspect", "share_url": share_url(args.code)})
        return result
    if args.command == "validate":
        _bundle, graph, build = _load_graph(args.code, args.build, args.level)
        result = validate_build(build, graph)
        return {"status": "ok", "operation": "validate", "snapshot": {"valid_for_build": build.snapshot.game_build, "source_patch_verified": build.snapshot.source_patch_verified}, "validation": {"valid": result.valid, "violations": [asdict(item) for item in result.violations]}}
    if args.command == "compare":
        _bundle, graph, left = _load_graph(args.left, args.build, args.level)
        _bundle, graph_right, right = _load_graph(args.right, args.build, args.level)
        if graph_right.spec_id != graph.spec_id:
            raise TalentError("UNSUPPORTED_SPEC", "comparison specs differ")
        return {"status": "ok", "operation": "compare", "diff": [asdict(item) for item in compare_builds(left, right, graph)]}
    if args.command == "modify":
        _bundle, graph, build = _load_graph(args.code, args.build, args.level)
        set_ranks = []
        for item in args.set_ranks:
            if "=" not in item:
                raise TalentError("INVALID_IMPORT_STRING", "--set requires ENTRY=RANK")
            token, rank = item.split("=", 1)
            set_ranks.append((token, int(rank)))
        choices = []
        for item in args.choice:
            if "=" not in item:
                raise TalentError("CHOICE_CONFLICT", "--choice requires ENTRY=INDEX")
            token, choice = item.split("=", 1)
            choices.append((token, int(choice)))
        modified, diff = modify_build(build, graph, set_ranks=set_ranks, clear=args.clear, choices=choices, cascade=args.cascade)
        return _build_result("modify", modified, graph, diff=diff)
    if args.command == "generate":
        bundle = AssetLoader(ASSETS_ROOT).open(args.build)
        graph = GraphStore(bundle).load_spec(args.spec)
        required = frozenset(resolve for resolve in (int(item) for item in args.require))
        forbidden = frozenset(resolve for resolve in (int(item) for item in args.forbid))
        preferences = tuple((int(item.split("=", 1)[0]), int(item.split("=", 1)[1])) for item in args.prefer)
        request = BuildRequest(args.spec, args.level, args.hero, required, forbidden, preferences)
        return _build_result("generate", generate_build(request, graph), graph)
    raise TalentError("INVALID_COMMAND", "unknown command")


def main(argv: list[str] | None = None) -> int:
    try:
        result = run(_parser().parse_args(argv))
    except (TalentError, AssetIntegrityError, KeyError, ValueError) as exc:
        error = exc.as_dict() if isinstance(exc, TalentError) else {"code": "ASSET_INTEGRITY_FAILED" if isinstance(exc, AssetIntegrityError) else "CLI_ERROR", "message": str(exc), "details": {}}
        print(json.dumps({"status": "error", "error": error}, ensure_ascii=False), file=sys.stdout)
        return 5 if isinstance(exc, AssetIntegrityError) else 4
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

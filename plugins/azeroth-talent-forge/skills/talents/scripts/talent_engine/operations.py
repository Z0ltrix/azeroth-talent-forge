"""Pure inspect, resolve, modify, and compare operations."""

from __future__ import annotations

from dataclasses import replace

from .codec import decode_build, encode_build
from .errors import TalentError
from .models import BuildDiff, Selection, SpecGraph, TalentBuild
from .validator import validate_build


def resolve_entry(graph: SpecGraph, token: str) -> int:
    try:
        numeric = int(token)
    except ValueError:
        numeric = None
    if numeric is not None:
        if numeric in graph.entry_by_id:
            return numeric
        raise TalentError("UNKNOWN_ENTRY", f"entry {numeric} is not in this graph")
    matches = [entry_id for entry_id, name in graph.names if name.casefold() == token.casefold()]
    if not matches:
        raise TalentError("UNKNOWN_ENTRY", f"talent name is not in this graph: {token}")
    if len(matches) > 1:
        raise TalentError("AMBIGUOUS_NAME", f"talent name matches multiple entries: {token}", entry_ids=matches)
    return matches[0]


def inspect_build(build: TalentBuild, graph: SpecGraph) -> dict:
    names = graph.name_by_entry
    descriptions = {entry_id: {"description": description, "effect": effect} for entry_id, description, effect in graph.descriptions}
    selections = []
    for selection in build.selections:
        selections.append({"node_id": selection.node_id, "entry_id": selection.entry_id, "name": names.get(selection.entry_id), "purchased_ranks": selection.purchased_ranks, "granted_ranks": selection.observed_granted_ranks, "choice_index": selection.choice_index, **descriptions.get(selection.entry_id, {})})
    validation = validate_build(build, graph)
    return {"class_id": build.class_id, "spec_id": build.spec_id, "level": build.level, "hero_subtree_id": build.hero_subtree_id, "valid_for_build": build.snapshot.game_build, "source_patch_verified": build.snapshot.source_patch_verified, "observed_tree_hash": build.observed_tree_hash.hex() if build.observed_tree_hash else None, "selections": selections, "validation": {"valid": validation.valid, "violations": [violation.__dict__ for violation in validation.violations]}}


def _round_trip(build: TalentBuild, graph: SpecGraph) -> TalentBuild:
    result = validate_build(build, graph)
    if not result.valid:
        raise TalentError("ILLEGAL_BUILD", "operation produced an invalid build", violations=[item.__dict__ for item in result.violations])
    encoded = encode_build(build, graph)
    decoded = decode_build(encoded, graph, level=build.level)
    if decoded.selections != build.selections:
        raise TalentError("ROUND_TRIP_MISMATCH", "encoded build did not decode to the same semantic state")
    return decoded


def modify_build(build: TalentBuild, graph: SpecGraph, *, set_ranks=(), clear=(), choices=(), hero_subtree_id=None, cascade=False) -> tuple[TalentBuild, list[BuildDiff]]:
    current = {selection.node_id: selection for selection in build.selections}
    diffs: list[BuildDiff] = []
    for token, rank in set_ranks:
        entry_id = resolve_entry(graph, token)
        node = graph.entry_by_id[entry_id]
        old = current.get(node.node_id, Selection(node.node_id, entry_id, 0))
        current[node.node_id] = replace(old, entry_id=entry_id, purchased_ranks=int(rank), observed_granted_ranks=0)
    for token in clear:
        entry_id = resolve_entry(graph, token)
        node = graph.entry_by_id[entry_id]
        old = current.get(node.node_id, Selection(node.node_id, entry_id, 0))
        current[node.node_id] = replace(old, purchased_ranks=0, observed_granted_ranks=0)
    for token, choice_index in choices:
        entry_id = resolve_entry(graph, token)
        node = graph.entry_by_id[entry_id]
        old = current.get(node.node_id, Selection(node.node_id, entry_id, 0))
        current[node.node_id] = replace(old, purchased_ranks=max(old.purchased_ranks, 1), choice_index=int(choice_index))
    if cascade:
        selected = {node_id for node_id, selection in current.items() if selection.purchased_ranks > 0 or selection.observed_granted_ranks > 0}
        changed = True
        while changed:
            changed = False
            for source, target in graph.required_edges:
                if target in selected and source not in selected:
                    target_selection = current.get(target)
                    if target_selection and target_selection.purchased_ranks > 0:
                        current[target] = replace(target_selection, purchased_ranks=0)
                        selected.remove(target)
                        changed = True
    result = replace(build, hero_subtree_id=hero_subtree_id if hero_subtree_id is not None else build.hero_subtree_id, selections=tuple(sorted(current.values(), key=lambda item: item.node_id)))
    result = _round_trip(result, graph)
    before = {item.node_id: item for item in build.selections}
    after = {item.node_id: item for item in result.selections}
    for node_id in sorted(set(before) | set(after)):
        left, right = before.get(node_id), after.get(node_id)
        if (left.purchased_ranks if left else 0) != (right.purchased_ranks if right else 0):
            diffs.append(BuildDiff("RANK", node_id, (right or left).entry_id, left.purchased_ranks if left else 0, right.purchased_ranks if right else 0))
        if (left.choice_index if left else 0) != (right.choice_index if right else 0):
            diffs.append(BuildDiff("CHOICE", node_id, (right or left).entry_id, left.choice_index if left else 0, right.choice_index if right else 0))
    return result, diffs


def compare_builds(left: TalentBuild, right: TalentBuild, graph: SpecGraph) -> list[BuildDiff]:
    if left.snapshot.asset_sha256 != right.snapshot.asset_sha256 or left.spec_id != right.spec_id:
        raise TalentError("UNSUPPORTED_SNAPSHOT", "builds do not share the same asset and specialization")
    before = {item.node_id: item for item in left.selections}
    after = {item.node_id: item for item in right.selections}
    diffs = []
    for node_id in sorted(set(before) | set(after)):
        a, b = before.get(node_id), after.get(node_id)
        ar, br = (a.purchased_ranks if a else 0), (b.purchased_ranks if b else 0)
        if ar == 0 and br > 0:
            diffs.append(BuildDiff("ADD", node_id, (b or a).entry_id, ar, br))
        elif ar > 0 and br == 0:
            diffs.append(BuildDiff("REMOVE", node_id, (a or b).entry_id, ar, br))
        elif ar != br:
            diffs.append(BuildDiff("RANK", node_id, (b or a).entry_id, ar, br))
        if (a.choice_index if a else 0) != (b.choice_index if b else 0):
            diffs.append(BuildDiff("CHOICE", node_id, (b or a).entry_id, a.choice_index if a else 0, b.choice_index if b else 0))
    return diffs

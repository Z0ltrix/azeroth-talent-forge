"""Deterministic small-graph build generation."""

from __future__ import annotations

from .errors import TalentError
from .models import BuildRequest, Selection, SpecGraph, TalentBuild
from .validator import validate_build


def generate_build(request: BuildRequest, graph: SpecGraph) -> TalentBuild:
    if request.spec_id != graph.spec_id:
        raise TalentError("UNSUPPORTED_SPEC", "generation request and graph specialization differ")
    weights = dict(request.preferred_entry_weights)
    nodes = graph.nodes
    best: tuple[tuple, TalentBuild] | None = None
    candidates = 0

    def visit(index: int, selections: list[Selection]):
        nonlocal best, candidates
        if candidates > 100_000:
            raise TalentError("NO_FEASIBLE_BUILD", "search limit exceeded; narrow the generation constraints")
        if index == len(nodes):
            candidates += 1
            selected_entries = {item.entry_id for item in selections if item.purchased_ranks > 0}
            if not request.required_entry_ids.issubset(selected_entries) or selected_entries.intersection(request.forbidden_entry_ids):
                return
            build = TalentBuild(graph.snapshot, graph.class_id, graph.spec_id, request.level, request.hero_subtree_id, None, tuple(selections))
            validation = validate_build(build, graph)
            if not validation.valid:
                return
            weighted = sum(weights.get(item.entry_id, 0) * item.purchased_ranks for item in selections)
            filler = sum(item.purchased_ranks for item in selections if weights.get(item.entry_id, 0) == 0)
            prerequisite_cost = sum(1 for _source, target in graph.required_edges if any(item.node_id == target and item.purchased_ranks > 0 for item in selections))
            tie_break = tuple(item.node_id for item in selections)
            score = (-weighted, filler, prerequisite_cost, tie_break)
            if best is None or score < best[0]:
                best = (score, build)
            return
        node = nodes[index]
        for rank in range(0, node.max_ranks + 1):
            if rank == 0:
                visit(index + 1, selections)
                continue
            choices = range(node.choice_count) if node.is_choice and node.choice_count else (0,)
            for choice_index in choices:
                visit(index + 1, selections + [Selection(node.node_id, node.entry_id, rank, 0, choice_index)])

    visit(0, [])
    if best is None:
        raise TalentError("NO_FEASIBLE_BUILD", "no legal build satisfies the requested constraints")
    return best[1]

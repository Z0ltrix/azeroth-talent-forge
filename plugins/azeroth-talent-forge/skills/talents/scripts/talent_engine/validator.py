"""Structural and graph-rule validation for one decoded talent build."""

from __future__ import annotations

from .models import Selection, SpecGraph, TalentBuild, ValidationResult, Violation


def validate_build(build: TalentBuild, graph: SpecGraph) -> ValidationResult:
    violations: list[Violation] = []
    schedule_levels = [level for _currency_id, level, _amount in graph.currency_budgets]
    if schedule_levels and not min(schedule_levels) <= build.level <= max(schedule_levels):
        violations.append(Violation("UNSUPPORTED_LEVEL", f"level {build.level} is outside this asset's supported range {min(schedule_levels)}-{max(schedule_levels)}"))
    nodes = graph.node_by_id
    by_entry = graph.entry_by_id
    by_node = {selection.node_id: selection for selection in build.selections}
    for selection in build.selections:
        node = nodes.get(selection.node_id)
        if node is None or by_entry.get(selection.entry_id) != node:
            violations.append(Violation("UNKNOWN_NODE", f"node {selection.node_id} is not in this graph", selection.node_id, selection.entry_id))
            continue
        if not node.visible:
            violations.append(Violation("UNKNOWN_NODE", f"node {selection.node_id} is not visible", selection.node_id, selection.entry_id))
        if selection.purchased_ranks < 0 or selection.purchased_ranks > node.max_ranks:
            violations.append(Violation("RANK_OUT_OF_RANGE", f"entry {selection.entry_id} has an invalid rank", selection.node_id, selection.entry_id))
        if node.is_choice and selection.choice_index >= max(node.choice_count, 1):
            violations.append(Violation("CHOICE_CONFLICT", f"entry {selection.entry_id} has an invalid choice", selection.node_id, selection.entry_id))
        if node.is_choice and selection.choice_index < len(node.entry_ids) and selection.entry_id != node.entry_ids[selection.choice_index]:
            violations.append(Violation("CHOICE_CONFLICT", f"entry {selection.entry_id} does not match choice {selection.choice_index}", selection.node_id, selection.entry_id))
    selected_nodes = {node_id for node_id, selection in by_node.items() if selection.purchased_ranks > 0 or selection.observed_granted_ranks > 0}
    purchased_nodes = {node_id for node_id, selection in by_node.items() if selection.purchased_ranks > 0}
    for source, target in graph.required_edges:
        if target in selected_nodes and source not in selected_nodes:
            violations.append(Violation("MISSING_PREREQUISITE", f"node {target} requires node {source}", target, nodes.get(target).entry_id if target in nodes else None))
    for target in {target for _source, target in graph.sufficient_edges}:
        alternatives = [source for source, candidate in graph.sufficient_edges if candidate == target]
        if target in selected_nodes and not any(source in selected_nodes for source in alternatives):
            violations.append(Violation("MISSING_PREREQUISITE", f"node {target} has no sufficient prerequisite", target, nodes.get(target).entry_id if target in nodes else None))
    for left, right in graph.exclusions:
        if left in selected_nodes and right in selected_nodes:
            violations.append(Violation("MUTUAL_EXCLUSION", f"nodes {left} and {right} are mutually exclusive", left, nodes[left].entry_id if left in nodes else None))
    purchased = sum(selection.purchased_ranks for selection in build.selections)
    if graph.budgets:
        available = [quantity for level, quantity in graph.budgets if level <= build.level]
        if available:
            maximum = max(available)
            if purchased > maximum:
                violations.append(Violation("BUDGET_MISMATCH", f"build spends {purchased} points but budget is {maximum}"))
    if graph.costs:
        spent_by_currency: dict[int, int] = {}
        costs_by_node: dict[int, list[tuple[int, int]]] = {}
        granted_ranks_by_node: dict[int, int] = {}
        for node_id, currency_id, amount in graph.costs:
            costs_by_node.setdefault(node_id, []).append((currency_id, amount))
        for node_id, ranks in graph.grants:
            granted_ranks_by_node[node_id] = max(granted_ranks_by_node.get(node_id, 0), ranks)
        for selection in build.selections:
            if selection.purchased_ranks <= 0:
                continue
            chargeable_ranks = max(0, selection.purchased_ranks - granted_ranks_by_node.get(selection.node_id, 0))
            for currency_id, amount in costs_by_node.get(selection.node_id, []):
                spent_by_currency[currency_id] = spent_by_currency.get(currency_id, 0) + chargeable_ranks * amount
        for currency_id, spent in sorted(spent_by_currency.items()):
            earned = sum(amount for candidate, level, amount in graph.currency_budgets if candidate == currency_id and level <= build.level)
            if not any(candidate == currency_id for candidate, _level, _amount in graph.currency_budgets):
                violations.append(Violation("CURRENCY_BUDGET_UNAVAILABLE", f"currency {currency_id} has no local level schedule"))
            elif spent > earned:
                violations.append(Violation("CURRENCY_BUDGET_MISMATCH", f"currency {currency_id} spends {spent} points but level {build.level} grants {earned}"))
    violations.sort(key=lambda item: (item.code, item.node_id or -1, item.entry_id or -1))
    return ValidationResult(not violations, tuple(violations))

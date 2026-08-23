"""The sole runtime boundary around Ladybug and Cypher."""

from __future__ import annotations

from pathlib import Path

import ladybug

from .assets import AssetBundle
from .models import CodecNode, SnapshotIdentity, SpecGraph


class GraphStore:
    def __init__(self, bundle: AssetBundle):
        self.bundle = bundle

    def load_spec(self, spec_id: int) -> SpecGraph:
        database = ladybug.Database(str(self.bundle.database_path), read_only=True)
        connection = ladybug.Connection(database)
        try:
            spec_rows = connection.execute(f"MATCH (s:Spec {{id: {int(spec_id)}}}) RETURN s.id, s.class_id").get_all()
            if not spec_rows:
                raise KeyError(f"unsupported spec: {spec_id}")
            spec_value, class_id = spec_rows[0]
            tree_rows = connection.execute(f"MATCH (s:Spec {{id: {int(spec_id)}}})-[r:SERIALIZES]->(n:TraitNode)-[:HAS_ENTRY]->(e:Entry) RETURN n.id, e.id, e.max_ranks, n.type, r.ordinal, e.ordinal ORDER BY r.ordinal, e.ordinal, e.id").get_all()
            if not tree_rows:
                # Backward-compatible fallback for hand-built/test assets
                # predating the per-specialization codec-order relation.
                tree_rows = connection.execute(f"MATCH (s:Spec {{id: {int(spec_id)}}})-[:USES_SPEC_TREE]->(t:Tree)-[:HAS_NODE]->(n:TraitNode)-[:HAS_ENTRY]->(e:Entry) RETURN n.id, e.id, e.max_ranks, n.type, n.codec_ordinal, e.ordinal ORDER BY n.codec_ordinal, n.id, e.ordinal, e.id").get_all()
            entries_by_node: dict[int, list[tuple[int, int, int]]] = {}
            node_types: dict[int, int] = {}
            for node_id, entry_id, max_ranks, node_type, _ordinal, entry_ordinal in tree_rows:
                entries_by_node.setdefault(int(node_id), []).append((int(entry_id), int(max_ranks), int(entry_ordinal)))
                node_types[int(node_id)] = int(node_type)
            nodes = tuple(
                CodecNode(
                    node_id,
                    values[0][0],
                    sum(rank for _entry, rank, _entry_ordinal in values) if node_types.get(node_id) == 2 else max(rank for _entry, rank, _entry_ordinal in values),
                    # Wowhead type 3 is Blizzard's Selection node.  Type 5
                    # is an Apex node: it has several entries but does not
                    # serialize a choice marker.
                    is_choice=node_types.get(node_id) == 3,
                    choice_count=len(values) if node_types.get(node_id) == 3 else 0,
                    entry_ids=tuple(entry_id for entry_id, _rank, _entry_ordinal in values),
                )
                for node_id, values in entries_by_node.items()
            )
            node_ids = {node.node_id for node in nodes}
            required_edges = tuple(
                (int(source), int(target))
                for source, target in connection.execute(f"MATCH (s:Spec {{id: {int(spec_id)}}})-[:SERIALIZES]->(a:TraitNode)-[:REQUIRED_FOR]->(b:TraitNode) RETURN a.id, b.id").get_all()
                if int(source) in node_ids and int(target) in node_ids
            )
            sufficient_edges = tuple(
                (int(source), int(target))
                for source, target in connection.execute(f"MATCH (s:Spec {{id: {int(spec_id)}}})-[:SERIALIZES]->(a:TraitNode)-[:SUFFICIENT_FOR]->(b:TraitNode) RETURN a.id, b.id").get_all()
                if int(source) in node_ids and int(target) in node_ids
            )
            exclusions = tuple(
                (int(source), int(target))
                for source, target in connection.execute(f"MATCH (s:Spec {{id: {int(spec_id)}}})-[:SERIALIZES]->(a:TraitNode)-[:MUTUALLY_EXCLUSIVE]->(b:TraitNode) RETURN a.id, b.id").get_all()
                if int(source) in node_ids and int(target) in node_ids
            )
            try:
                costs = tuple(
                    (int(node_id), int(currency_id), int(amount))
                    for node_id, currency_id, amount in connection.execute(
                        f"MATCH (s:Spec {{id: {int(spec_id)}}})-[:SERIALIZES]->(n:TraitNode)-[cost:COSTS]->(c:Currency) RETURN n.id, c.id, cost.amount"
                    ).get_all()
                )
                currency_budgets = tuple(
                    (int(currency_id), int(level), int(amount))
                    for currency_id, level, amount in connection.execute(
                        "MATCH (c:Currency)-[:UNLOCKS]->(source:CurrencySource) RETURN c.id, source.level, source.amount"
                    ).get_all()
                )
                grants = tuple(
                    (int(node_id), int(ranks))
                    for node_id, ranks in connection.execute(
                        f"MATCH (s:Spec {{id: {int(spec_id)}}})-[grant:GRANTS]->(n:TraitNode) RETURN n.id, grant.ranks"
                    ).get_all()
                    if int(node_id) in node_ids
                )
            except Exception:
                # Pre-1.0 assets intentionally lack the normalized constraint
                # tables. Asset schema validation keeps that fallback from
                # masking a shipped 1.0 asset failure.
                costs = ()
                currency_budgets = ()
                grants = ()
            description_rows = connection.execute(f"MATCH (s:Spec {{id: {int(spec_id)}}})-[:USES_SPEC_TREE]->(:Tree)-[:HAS_NODE]->(:TraitNode)-[:HAS_ENTRY]->(e:Entry)-[:USES_DEFINITION]->(d:Definition) RETURN e.id, d.name, d.description, d.effect ORDER BY e.id").get_all()
            snapshot_rows = connection.execute("MATCH (s:Snapshot) RETURN s.game_build, s.locale").get_all()
            game_build, locale = snapshot_rows[0]
            snapshot = SnapshotIdentity(str(game_build), str(locale), 2, int(spec_id), self.bundle.asset_sha256, False)
            return SpecGraph(snapshot, int(class_id), int(spec_value), nodes, tuple((int(row[0]), str(row[1])) for row in description_rows), tuple((int(row[0]), str(row[2]), str(row[3])) for row in description_rows), required_edges=required_edges, sufficient_edges=sufficient_edges, exclusions=exclusions, grants=grants, costs=costs, currency_budgets=currency_budgets)
        finally:
            connection.close()
            database.close()

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
            tree_rows = connection.execute(f"MATCH (s:Spec {{id: {int(spec_id)}}})-[:USES_SPEC_TREE]->(t:Tree)-[:HAS_NODE]->(n:TraitNode)-[:HAS_ENTRY]->(e:Entry) RETURN n.id, e.id, e.max_ranks ORDER BY n.id").get_all()
            nodes = tuple(CodecNode(int(node_id), int(entry_id), int(max_ranks)) for node_id, entry_id, max_ranks in tree_rows)
            description_rows = connection.execute(f"MATCH (s:Spec {{id: {int(spec_id)}}})-[:USES_SPEC_TREE]->(:Tree)-[:HAS_NODE]->(:TraitNode)-[:HAS_ENTRY]->(e:Entry)-[:USES_DEFINITION]->(d:Definition) RETURN e.id, d.name, d.description, d.effect ORDER BY e.id").get_all()
            snapshot_rows = connection.execute("MATCH (s:Snapshot) RETURN s.game_build, s.locale").get_all()
            game_build, locale = snapshot_rows[0]
            snapshot = SnapshotIdentity(str(game_build), str(locale), 2, int(spec_id), self.bundle.asset_sha256, False)
            return SpecGraph(snapshot, int(class_id), int(spec_value), nodes, tuple((int(row[0]), str(row[1])) for row in description_rows), tuple((int(row[0]), str(row[2]), str(row[3])) for row in description_rows))
        finally:
            connection.close()
            database.close()

import gzip
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from compile_assets import AssetCompileError, compile_assets, verify_assets


def fixture_snapshot():
    return {
        "schema_version": 1,
        "product": "wow",
        "channel": "retail-live",
        "game_build": "12.1.0.69404",
        "locale": "enUS",
        "classes": [{"id": 1, "name": "Warrior"}],
        "specs": [{"id": 73, "name": "Protection", "class_id": 1, "role": "TANK"}],
        "trees": [{"id": 100, "kind": "spec", "spec_id": 73}],
        "nodes": [{"id": 10, "tree_id": 100, "x": 1, "y": 2, "type": 0}],
        "entries": [{"id": 20, "node_id": 10, "definition_id": 30, "max_ranks": 2, "ordinal": 0}],
        "definitions": [{"id": 30, "spell_id": 40, "name": "Shield Block", "description": "Increases block.", "effect": "Increases block.", "source": "fixture"}],
        "effects": [], "edges": [], "conditions": [], "currencies": [],
        "codec_orders": {"73": [10]}, "presets": [], "source_receipts": [],
    }


class CompileAssetTests(unittest.TestCase):
    def test_compiles_manifest_graph_and_hashes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = pathlib.Path(temp_dir)
            snapshot = root / "snapshot.json.gz"
            with snapshot.open("wb") as raw:
                with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as stream:
                    stream.write((json.dumps(fixture_snapshot(), sort_keys=True) + "\n").encode())
            references = root / "references"
            (references / "features").mkdir(parents=True)
            (references / "features" / "inspect.md").write_text("# Inspect\n", encoding="utf-8")
            output = root / "assets"
            manifest = compile_assets(snapshot, output, references)
            self.assertEqual(manifest["game_build"], "12.1.0.69404")
            self.assertEqual(manifest["graph"]["engine_version"], "0.19.1")
            self.assertTrue((output / "talents.lbdb").is_file())
            self.assertTrue((output / "presets.json").is_file())
            self.assertEqual(verify_assets(output / "talents.lbdb", output / "manifest.json", output / "presets.json", references), [])
            database = __import__("ladybug").Database(str(output / "talents.lbdb"), read_only=True)
            connection = __import__("ladybug").Connection(database)
            self.assertEqual(connection.execute("MATCH (n:TraitNode) RETURN n.codec_ordinal").get_all(), [[0]])
            connection.close()
            database.close()

    def test_rejects_wrong_snapshot_product_or_build(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = pathlib.Path(temp_dir)
            snapshot = root / "snapshot.json.gz"
            data = fixture_snapshot()
            data["product"] = "classic"
            with snapshot.open("wb") as raw:
                with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as stream:
                    stream.write((json.dumps(data) + "\n").encode())
            with self.assertRaises(AssetCompileError):
                compile_assets(snapshot, root / "assets", root / "references")


if __name__ == "__main__":
    unittest.main()

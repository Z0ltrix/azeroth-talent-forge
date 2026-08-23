import gzip
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from compile_assets import _hash_tree
from generate_references import generate_references


class ReferenceGenerationTests(unittest.TestCase):
    def test_generates_all_features_and_factual_talent_catalog(self):
        snapshot = {
            "schema_version": 1, "product": "wow", "channel": "retail-live",
            "game_build": "12.1.0.69404", "locale": "enUS",
            "classes": [{"id": 1, "name": "Warrior"}],
            "specs": [{"id": 73, "name": "Protection", "class_id": 1, "role": "TANK"}],
            "trees": [{"id": 100, "kind": "spec", "spec_id": 73}],
            "nodes": [{"id": 10, "tree_id": 100, "x": 1, "y": 2, "type": 0}],
            "entries": [{"id": 20, "node_id": 10, "definition_id": 30, "max_ranks": 2, "ordinal": 0}],
            "definitions": [{"id": 30, "spell_id": 40, "name": "Shield Block", "description": "Increases block.", "effect": "Increases block.", "source": "fixture"}],
            "effects": [], "edges": [], "conditions": [], "currencies": [],
            "codec_orders": {"73": [10]}, "presets": [], "source_receipts": [],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            root = pathlib.Path(temp_dir)
            snapshot_path = root / "snapshot.json.gz"
            with snapshot_path.open("wb") as raw:
                with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as stream:
                    stream.write((json.dumps(snapshot, sort_keys=True) + "\n").encode())
            output = root / "references"
            registry = pathlib.Path(__file__).resolve().parents[1] / "reference_sources" / "features.json"
            notes = pathlib.Path(__file__).resolve().parents[1] / "reference_sources" / "planning_notes.json"
            generate_references(snapshot_path, registry, notes, output)
            feature_files = sorted((output / "features").glob("*.md"))
            self.assertEqual({path.stem for path in feature_files}, {"import-export", "inspect", "validate", "compare", "modify", "generate", "presets", "patch-assets", "errors"})
            protection = output / "classes" / "warrior" / "protection.md"
            self.assertTrue(protection.is_file())
            text = protection.read_text(encoding="utf-8")
            self.assertIn("Entry ID: `20`", text)
            self.assertIn("Shield Block", text)
            self.assertIn("Increases block.", text)
            self.assertTrue((output / "internals" / "data-model.md").is_file())
            self.assertEqual(len(_hash_tree(output)), 64)


if __name__ == "__main__":
    unittest.main()

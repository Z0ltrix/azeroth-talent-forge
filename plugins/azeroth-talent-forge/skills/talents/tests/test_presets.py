import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from scripts.talent_engine.models import CodecNode, SnapshotIdentity, SpecGraph
from scripts.talent_engine.presets import PresetStore


class PresetTests(unittest.TestCase):
    def test_filters_and_reports_missing_preset(self):
        store = PresetStore([{"preset_id": "one", "spec_id": 73, "category": "raid"}])
        self.assertEqual(store.list(spec_id=73)[0]["preset_id"], "one")
        graph = SpecGraph(SnapshotIdentity("12.1.0.69404", "enUS", 2, 73, "a" * 64, False), 1, 73, (CodecNode(10, 20, 1),), ((20, "One"),), ((20, "One", "Effect"),))
        with self.assertRaises(Exception):
            store.show("missing", graph)


if __name__ == "__main__":
    unittest.main()

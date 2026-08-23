import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from scripts.talent_engine.models import CodecNode, Selection, SnapshotIdentity, SpecGraph, TalentBuild
from scripts.talent_engine.operations import compare_builds, inspect_build, modify_build, resolve_entry


class OperationTests(unittest.TestCase):
    def setUp(self):
        identity = SnapshotIdentity("12.1.0.69404", "enUS", 2, 73, "a" * 64, False)
        self.graph = SpecGraph(identity, 1, 73, (CodecNode(10, 20, 2), CodecNode(30, 40, 1)), ((20, "One"), (40, "Two")), ((20, "Description one", "Effect one"), (40, "Description two", "Effect two")), required_edges=((10, 30),))
        self.base = TalentBuild(identity, 1, 73, 80, None, None, (Selection(10, 20, 1),))

    def test_resolve_inspect_and_modify(self):
        self.assertEqual(resolve_entry(self.graph, "one"), 20)
        inspected = inspect_build(self.base, self.graph)
        self.assertEqual(inspected["selections"][0]["description"], "Description one")
        modified, diffs = modify_build(self.base, self.graph, set_ranks=(("Two", 1),))
        self.assertTrue(modified.selections[-1].purchased_ranks)
        self.assertIn("RANK", {item.kind for item in diffs})

    def test_compare_reports_add_and_remove(self):
        right, _ = modify_build(self.base, self.graph, set_ranks=(("Two", 1),))
        diffs = compare_builds(self.base, right, self.graph)
        self.assertEqual(diffs[0].kind, "ADD")


if __name__ == "__main__":
    unittest.main()

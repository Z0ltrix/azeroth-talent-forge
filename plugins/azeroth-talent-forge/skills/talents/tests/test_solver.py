import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from scripts.talent_engine.models import BuildRequest, CodecNode, SnapshotIdentity, SpecGraph
from scripts.talent_engine.solver import generate_build


class SolverTests(unittest.TestCase):
    def setUp(self):
        identity = SnapshotIdentity("12.1.0.69404", "enUS", 2, 73, "a" * 64, False)
        self.graph = SpecGraph(identity, 1, 73, (CodecNode(10, 20, 1), CodecNode(30, 40, 1)), ((20, "One"), (40, "Two")), ((20, "One", "Effect"), (40, "Two", "Effect")), required_edges=((10, 30),))

    def test_prefers_weighted_legal_entry_and_is_deterministic(self):
        request = BuildRequest(73, 80, None, frozenset({40}), frozenset(), ((40, 10),))
        first = generate_build(request, self.graph)
        second = generate_build(request, self.graph)
        self.assertEqual(first, second)
        self.assertEqual([item.entry_id for item in first.selections if item.purchased_ranks], [20, 40])

    def test_reports_no_feasible_build(self):
        request = BuildRequest(73, 80, None, frozenset({20}), frozenset({20}), ())
        with self.assertRaises(Exception):
            generate_build(request, self.graph)


if __name__ == "__main__":
    unittest.main()

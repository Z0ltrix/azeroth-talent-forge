import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from scripts.talent_engine.models import CodecNode, Selection, SnapshotIdentity, SpecGraph, TalentBuild
from scripts.talent_engine.validator import validate_build


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        identity = SnapshotIdentity("12.1.0.69404", "enUS", 2, 73, "a" * 64, False)
        self.graph = SpecGraph(identity, 1, 73, (CodecNode(10, 20, 2), CodecNode(30, 40, 1)), ((20, "One"), (40, "Two")), ((20, "One", "Effect"), (40, "Two", "Effect")), required_edges=((10, 30),), budgets=((80, 2),))

    def _build(self, selections):
        return TalentBuild(self.graph.snapshot, 1, 73, 80, None, None, tuple(selections))

    def test_prerequisite_and_budget(self):
        result = validate_build(self._build([Selection(30, 40, 1)]), self.graph)
        self.assertFalse(result.valid)
        self.assertEqual(result.violations[0].code, "MISSING_PREREQUISITE")
        result = validate_build(self._build([Selection(10, 20, 2), Selection(30, 40, 1)]), self.graph)
        self.assertFalse(result.valid)
        self.assertIn("BUDGET_MISMATCH", {item.code for item in result.violations})

    def test_valid_grant_does_not_consume_budget(self):
        result = validate_build(self._build([Selection(10, 20, 0, 2), Selection(30, 40, 1)]), self.graph)
        self.assertTrue(result.valid)

    def test_currency_budget_uses_the_exact_level_schedule(self):
        graph = SpecGraph(
            self.graph.snapshot, 1, 73, self.graph.nodes, self.graph.names, self.graph.descriptions,
            costs=((10, 500, 1), (30, 500, 1)),
            currency_budgets=((500, 10, 1), (500, 12, 1)),
        )
        build = TalentBuild(graph.snapshot, 1, 73, 10, None, None, (Selection(10, 20, 1), Selection(30, 40, 1)))
        result = validate_build(build, graph)
        self.assertFalse(result.valid)
        self.assertIn("CURRENCY_BUDGET_MISMATCH", {item.code for item in result.violations})

    def test_spec_granted_rank_does_not_consume_currency(self):
        graph = SpecGraph(
            self.graph.snapshot, 1, 73, self.graph.nodes, self.graph.names, self.graph.descriptions,
            costs=((10, 500, 1),), currency_budgets=((500, 10, 0),), grants=((10, 1),),
        )
        result = validate_build(TalentBuild(graph.snapshot, 1, 73, 10, None, None, (Selection(10, 20, 1),)), graph)
        self.assertTrue(result.valid)

    def test_rejects_a_level_outside_the_asset_schedule(self):
        graph = SpecGraph(
            self.graph.snapshot, 1, 73, self.graph.nodes, self.graph.names, self.graph.descriptions,
            currency_budgets=((500, 10, 1), (500, 90, 1)),
        )
        result = validate_build(TalentBuild(graph.snapshot, 1, 73, 91, None, None, ()), graph)
        self.assertFalse(result.valid)
        self.assertIn("UNSUPPORTED_LEVEL", {item.code for item in result.violations})


if __name__ == "__main__":
    unittest.main()

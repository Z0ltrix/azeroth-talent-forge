import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from scripts.talent_engine.codec import decode_build, decode_header, encode_build
from scripts.talent_engine.models import CodecNode, Selection, SnapshotIdentity, SpecGraph, TalentBuild


class CodecTests(unittest.TestCase):
    def setUp(self):
        identity = SnapshotIdentity("12.1.0.69404", "enUS", 2, 73, "a" * 64, False)
        self.graph = SpecGraph(identity, 1, 73, (CodecNode(10, 20, 2), CodecNode(30, 40, 1, True, False, 2)), ((20, "Shield Block"), (40, "Choice")), ((20, "Shield Block", "Increases block."), (40, "Choice", "Chooses one.")))

    def test_round_trip_zero_hash_full_and_partial_choice(self):
        build = TalentBuild(self.graph.snapshot, 1, 73, 80, None, None, (Selection(10, 20, 1), Selection(30, 40, 1, 0, 1)))
        code = encode_build(build, self.graph)
        version, spec_id, tree_hash = decode_header(code)
        self.assertEqual((version, spec_id, tree_hash), (2, 73, None))
        decoded = decode_build(code, self.graph)
        self.assertEqual(decoded.selections, build.selections)

    def test_granted_rank_and_invalid_input(self):
        build = TalentBuild(self.graph.snapshot, 1, 73, 80, None, None, (Selection(10, 20, 0, 2),))
        decoded = decode_build(encode_build(build, self.graph), self.graph)
        self.assertEqual(decoded.selections[0].observed_granted_ranks, 2)
        with self.assertRaises(Exception):
            decode_build("!", self.graph)


if __name__ == "__main__":
    unittest.main()

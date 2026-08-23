import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from scripts.talent_engine.graph_store import GraphStore


class GraphStoreContractTests(unittest.TestCase):
    def test_module_exposes_read_only_graph_adapter(self):
        self.assertTrue(hasattr(GraphStore, "load_spec"))


if __name__ == "__main__":
    unittest.main()

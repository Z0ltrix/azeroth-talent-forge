import importlib.util
import json
import pathlib
import platform
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[5]
REQUIREMENTS = ROOT / "plugins" / "azeroth-talent-forge" / "requirements-talents.txt"


class BackendContractTests(unittest.TestCase):
    def test_python_and_dependency_pin(self):
        version = tuple(int(part) for part in platform.python_version_tuple()[:2])
        self.assertGreaterEqual(version, (3, 10))
        self.assertLess(version, (3, 15))
        self.assertEqual(REQUIREMENTS.read_text(encoding="utf-8").strip(), "ladybug==0.19.1")

    def test_ladybug_can_create_and_reopen_read_only(self):
        spec = importlib.util.find_spec("ladybug")
        self.assertIsNotNone(spec)
        import ladybug

        self.assertEqual(getattr(ladybug, "__version__", None), "0.19.1")
        with tempfile.TemporaryDirectory() as temp_dir:
            database_path = pathlib.Path(temp_dir) / "backend-test.lbdb"
            database = ladybug.Database(str(database_path))
            connection = ladybug.Connection(database)
            connection.execute("CREATE NODE TABLE Marker(id INT64, PRIMARY KEY(id))")
            connection.execute("CREATE (n:Marker {id: 1})")
            connection.close()
            database.close()

            read_only_database = ladybug.Database(str(database_path), read_only=True)
            read_only_connection = ladybug.Connection(read_only_database)
            result = read_only_connection.execute("MATCH (n:Marker) RETURN n.id").get_all()
            self.assertEqual(result, [[1]])
            read_only_connection.close()
            read_only_database.close()


if __name__ == "__main__":
    unittest.main()

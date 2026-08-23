import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from scripts.talent_engine.assets import AssetLoader
from scripts.talent_engine.codec import ALPHABET, decode_build, decode_header, encode_build
from scripts.talent_engine.errors import TalentError
from scripts.talent_engine.graph_store import GraphStore
from scripts.talent_engine.validator import validate_build


ROOT = pathlib.Path(__file__).resolve().parents[1]


def canonical_zero_hash_form(code: str) -> str:
    """Apply Blizzard's supported third-party export canonicalization.

    Imports can carry a live tree hash. Locally generated strings intentionally
    zero that field, and ExportUtil omits a trailing all-zero bit suffix.
    """
    bits = [
        (ALPHABET.index(char) >> bit_offset) & 1
        for char in code
        for bit_offset in range(6)
    ]
    bits[24:152] = [0] * 128
    last_nonzero = max((index for index, bit in enumerate(bits) if bit), default=151)
    length = max(152, last_nonzero + 1)
    return "".join(
        ALPHABET[sum(bit << shift for shift, bit in enumerate(bits[offset:offset + 6]))]
        for offset in range(0, length, 6)
    )


class OnlineStringTests(unittest.TestCase):
    def setUp(self):
        bundle = AssetLoader(ROOT / "assets").open()
        self.store = GraphStore(bundle)
        self.graphs = {}
        self.fixtures = json.loads((ROOT / "tests" / "fixtures" / "online_strings.json").read_text(encoding="utf-8"))

    def graph_for(self, fixture):
        spec_id = fixture["spec_id"]
        if spec_id not in self.graphs:
            self.graphs[spec_id] = self.store.load_spec(spec_id)
        return self.graphs[spec_id]

    def test_wowhead_string_decodes_and_validates(self):
        fixture = next(item for item in self.fixtures if item["source"] == "Wowhead")
        graph = self.graph_for(fixture)
        self.assertGreater(len(graph.sufficient_edges), 0)
        self.assertEqual(len(graph.nodes), 209)
        self.assertEqual({node.node_id for node in graph.nodes} & {99851, 99852, 99853}, {99851, 99852, 99853})
        version, spec_id, _tree_hash = decode_header(fixture["code"])
        self.assertEqual((version, spec_id), (2, fixture["spec_id"]))
        build = decode_build(fixture["code"], graph)
        self.assertTrue(validate_build(build, graph).valid)
        self.assertEqual(decode_build(encode_build(build, graph), graph).selections, build.selections)

    def test_every_manifest_spec_has_a_fixture(self):
        expected = {(spec["class_id"], spec["id"]) for spec in self.store.bundle.manifest["specs"]}
        actual = {(fixture["class_id"], fixture["spec_id"]) for fixture in self.fixtures}
        initial = {
            (spec["class_id"], spec["id"])
            for spec in self.store.bundle.manifest["specs"]
            if spec["name"] == "Initial"
        }
        local_smoke = {
            (fixture["class_id"], fixture["spec_id"])
            for fixture in self.fixtures
            if fixture["source_kind"] == "local-smoke"
        }
        self.assertEqual(actual, expected)
        self.assertEqual(local_smoke, initial)

    def test_every_playable_spec_has_an_external_fixture(self):
        expected = {(spec["class_id"], spec["id"]) for spec in self.store.bundle.manifest["specs"] if spec["name"] != "Initial"}
        external = {(fixture["class_id"], fixture["spec_id"]) for fixture in self.fixtures if fixture["source_kind"] == "external"}
        self.assertEqual(external, expected)

    def test_fixture_provenance_is_complete(self):
        for fixture in self.fixtures:
            with self.subTest(label=fixture["label"]):
                self.assertIn(fixture["source_kind"], {"external", "local-smoke"})
                self.assertTrue(fixture["source"])
                self.assertTrue(fixture["url"])
                self.assertIsInstance(fixture["class_id"], int)
                self.assertIsInstance(fixture["spec_id"], int)
                self.assertTrue(fixture["code"])
                if fixture["source_kind"] == "external":
                    self.assertIn(fixture["expected_status"], {"compatible", "observed-drift"})

    def test_all_strings_decode_and_roundtrip(self):
        for fixture in self.fixtures:
            if fixture["source_kind"] != "external":
                continue
            with self.subTest(label=fixture["label"]):
                graph = self.graph_for(fixture)
                self.assertGreater(len(graph.sufficient_edges), 0)
                try:
                    version, spec_id, _tree_hash = decode_header(fixture["code"])
                    self.assertEqual((version, spec_id), (2, fixture["spec_id"]))
                    build = decode_build(fixture["code"], graph)
                except TalentError as exc:
                    self.assertEqual(fixture["expected_status"], "observed-drift")
                    self.assertEqual(fixture.get("expected_decode_error"), exc.code)
                    continue
                result = validate_build(build, graph)
                if fixture["expected_status"] == "compatible":
                    self.assertTrue(result.valid)
                    self.assertEqual(decode_build(encode_build(build, graph), graph).selections, build.selections)
                else:
                    self.assertFalse(result.valid)
                    self.assertEqual(sorted({violation.code for violation in result.violations}), fixture["expected_violations"])

    def test_external_strings_reexport_to_their_canonical_zero_hash_form(self):
        for fixture in self.fixtures:
            if fixture["source_kind"] != "external":
                continue
            with self.subTest(label=fixture["label"]):
                graph = self.graph_for(fixture)
                if fixture["expected_status"] != "compatible":
                    continue
                build = decode_build(fixture["code"], graph)
                exported = encode_build(build, graph)
                if "expected_export" in fixture:
                    self.assertEqual(exported, fixture["expected_export"])
                self.assertEqual(decode_build(exported, graph).selections, build.selections)

    def test_each_source_covers_every_playable_spec(self):
        expected = {(spec["class_id"], spec["id"]) for spec in self.store.bundle.manifest["specs"] if spec["name"] != "Initial"}
        for source in ("Method", "Icy Veins"):
            actual = {(item["class_id"], item["spec_id"]) for item in self.fixtures if item["source"] == source}
            self.assertEqual(actual, expected)

    def test_each_playable_spec_has_compatible_cross_source_fixture(self):
        expected = {(spec["class_id"], spec["id"]) for spec in self.store.bundle.manifest["specs"] if spec["name"] != "Initial"}
        actual = {(item["class_id"], item["spec_id"]) for item in self.fixtures if item["source_kind"] == "external" and item["expected_status"] == "compatible"}
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

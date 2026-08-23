import gzip
import hashlib
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from normalize_sources import NormalizationError, normalize_bundle


def write_payload(root: pathlib.Path, kind: str, content: str, build: str = "12.1.0.69404") -> None:
    root.mkdir(parents=True, exist_ok=True)
    payload = root / f"{kind}.csv"
    body = content.encode("utf-8")
    payload.write_bytes(body)
    receipt = {
        "kind": kind,
        "url": f"https://wago.tools/db2/{kind}/csv?build={build}&locale=enUS",
        "path": str(payload),
        "game_build": build,
        "locale": "enUS",
        "fetched_at": "2026-08-23T00:00:00Z",
        "content_sha256": hashlib.sha256(body).hexdigest(),
        "parser_version": 1,
        "http_status": 200,
    }
    receipts = root / "receipts.json"
    existing = json.loads(receipts.read_text(encoding="utf-8")) if receipts.exists() else []
    existing.append(receipt)
    receipts.write_text(json.dumps(existing), encoding="utf-8")


class NormalizeTests(unittest.TestCase):
    def _valid_bundle(self, root: pathlib.Path):
        write_payload(root, "ChrClasses", "ID,Name\n1,Warrior\n")
        write_payload(root, "ChrSpecialization", "ID,Name,ClassID\n73,Protection,1\n")
        write_payload(root, "TraitTree", "ID,Type,SpecID\n100,spec,73\n")
        write_payload(root, "TraitNode", "ID,TraitTreeID,PosX,PosY\n10,100,1,2\n")
        write_payload(root, "TraitNodeEntry", "ID,TraitNodeID,TraitDefinitionID,MaxRanks\n20,10,30,2\n")
        write_payload(root, "TraitDefinition", "ID,SpellID,OverrideName_lang,OverrideDescription_lang\n30,40,Shield Block,Increases block.\n")
        write_payload(root, "Spell", "ID,Name_lang,Description_lang\n40,Shield Block,Increases block.\n")
        return root

    def test_normalizes_typed_records_and_sorted_codec_order(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._valid_bundle(pathlib.Path(temp_dir) / "raw")
            output = pathlib.Path(temp_dir) / "snapshot.json.gz"
            normalize_bundle(root, "12.1.0.69404", "enUS", output)
            with gzip.open(output, "rt", encoding="utf-8") as stream:
                snapshot = json.load(stream)
            self.assertEqual(snapshot["game_build"], "12.1.0.69404")
            self.assertEqual(snapshot["classes"][0]["id"], 1)
            self.assertEqual(snapshot["nodes"][0]["id"], 10)
            self.assertEqual(snapshot["codec_orders"]["73"], [10])
            self.assertEqual(snapshot["definitions"][0]["description"], "Increases block.")
            self.assertEqual(snapshot["schema_version"], 1)

    def test_output_is_deterministic_with_zero_gzip_timestamp(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._valid_bundle(pathlib.Path(temp_dir) / "raw")
            first = pathlib.Path(temp_dir) / "one.json.gz"
            second = pathlib.Path(temp_dir) / "two.json.gz"
            normalize_bundle(root, "12.1.0.69404", "enUS", first)
            normalize_bundle(root, "12.1.0.69404", "enUS", second)
            self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_rejects_receipt_build_mismatch_and_bad_hash(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._valid_bundle(pathlib.Path(temp_dir) / "raw")
            receipts = json.loads((root / "receipts.json").read_text(encoding="utf-8"))
            receipts[0]["game_build"] = "12.0.0.00000"
            (root / "receipts.json").write_text(json.dumps(receipts), encoding="utf-8")
            with self.assertRaises(NormalizationError):
                normalize_bundle(root, "12.1.0.69404", "enUS", pathlib.Path(temp_dir) / "bad.json.gz")

    def test_rejects_duplicate_codec_node_and_missing_required_description(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._valid_bundle(pathlib.Path(temp_dir) / "raw")
            (root / "TraitNode.csv").write_text("ID,TraitTreeID,PosX,PosY\n10,100,1,2\n10,100,3,4\n", encoding="utf-8")
            body = (root / "TraitNode.csv").read_bytes()
            receipts = json.loads((root / "receipts.json").read_text(encoding="utf-8"))
            for receipt in receipts:
                if receipt["kind"] == "TraitNode":
                    receipt["content_sha256"] = hashlib.sha256(body).hexdigest()
            (root / "receipts.json").write_text(json.dumps(receipts), encoding="utf-8")
            with self.assertRaises(NormalizationError):
                normalize_bundle(root, "12.1.0.69404", "enUS", pathlib.Path(temp_dir) / "bad.json.gz")


if __name__ == "__main__":
    unittest.main()

import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from scripts.talent_engine.assets import AssetIntegrityError, AssetLoader


class AssetTests(unittest.TestCase):
    def _manifest(self, root: pathlib.Path):
        asset = root / "retail" / "12.1.0.69404"
        asset.mkdir(parents=True)
        (asset / "talents.lbdb").write_bytes(b"graph")
        (asset / "presets.json").write_text("[]\n", encoding="utf-8")
        (asset / "manifest.json").write_text(json.dumps({
            "asset_schema_version": 1, "product": "wow", "channel": "retail-live",
            "game_build": "12.1.0.69404", "locale": "enUS",
            "serialization_versions": [2], "codec_node_order": "ascending-node-id",
            "export_tree_hash": "zero", "graph": {"engine": "ladybug", "engine_version": "0.19.1", "file": "talents.lbdb", "sha256": ""},
            "presets": {"file": "presets.json", "sha256": ""}, "references_sha256": ""}, indent=2), encoding="utf-8")
        return asset

    def test_rejects_missing_or_corrupt_asset(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaises(AssetIntegrityError):
                AssetLoader(pathlib.Path(temp_dir)).open()


if __name__ == "__main__":
    unittest.main()

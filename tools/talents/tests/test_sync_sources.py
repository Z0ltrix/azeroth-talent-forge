import hashlib
import json
import pathlib
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from sync_sources import (
    SourceSyncError,
    build_source_urls,
    extract_build_samples,
    load_config,
    sync_url,
)


ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG = ROOT / "sources.toml"
FIXTURES = ROOT / "tests" / "fixtures"


class FakeResponse:
    def __init__(self, body: bytes, status: int = 200, headers=None):
        self.body = body
        self.status = status
        self.headers = headers or {}

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self, _limit=-1):
        return self.body

    def getcode(self):
        return self.status

    def getheaders(self):
        return list(self.headers.items())


class SourceSyncTests(unittest.TestCase):
    def test_loads_explicit_snapshot_and_source_hosts(self):
        config = load_config(CONFIG)
        self.assertEqual(config["snapshot"]["build"], "12.1.0.69404")
        self.assertEqual(config["snapshot"]["locale"], "enUS")
        self.assertIn("TraitTree", config["wago"]["tables"])
        self.assertEqual(config["wowdbdefs"]["base_url"].split("/")[3], "wowdev")

    def test_build_source_urls_is_explicit_and_deterministic(self):
        config = load_config(CONFIG)
        urls = build_source_urls(config, "12.1.0.69404", "enUS")
        self.assertEqual(urls["TraitTree"], "https://wago.tools/db2/TraitTree/csv?build=12.1.0.69404&locale=enUS")
        self.assertIn("TraitDefinition", urls)
        self.assertIn("8d621ba9e7186458489a2b5aab0d2c303b104362", urls["TraitDefinition.dbd"])

    @mock.patch("sync_sources.urllib.request.urlopen")
    def test_sync_writes_payload_and_receipt_with_hash(self, urlopen):
        body = b"ID,Name\n1,Warrior\n"
        urlopen.return_value = FakeResponse(body, headers={"ETag": "abc", "Last-Modified": "today"})
        with tempfile.TemporaryDirectory() as temp_dir:
            payload, receipt = sync_url(
                "https://wago.tools/db2/TraitTree/csv?build=12.1.0.69404&locale=enUS",
                pathlib.Path(temp_dir),
                "12.1.0.69404",
                "enUS",
                kind="wago-db2",
            )
            self.assertEqual(payload.read_bytes(), body)
            self.assertEqual(receipt["content_sha256"], hashlib.sha256(body).hexdigest())
            self.assertEqual(receipt["etag"], "abc")
            self.assertEqual(json.loads(json.dumps(receipt))["game_build"], "12.1.0.69404")
            urlopen.assert_called_once()

    @mock.patch("sync_sources.urllib.request.urlopen")
    def test_sync_rejects_unconfigured_host_and_http_error(self, urlopen):
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaises(SourceSyncError):
                sync_url("https://evil.example/payload", pathlib.Path(temp_dir), "12.1.0.69404", "enUS", kind="test")
            urlopen.side_effect = OSError("offline")
            with self.assertRaises(SourceSyncError):
                sync_url("https://wago.tools/payload", pathlib.Path(temp_dir), "12.1.0.69404", "enUS", kind="test")

    def test_extracts_only_blizzard_strings_and_drops_identity(self):
        html = (FIXTURES / "wowhead-guide.html").read_text(encoding="utf-8")
        samples = extract_build_samples(html, "https://www.wowhead.com/guide", "Wowhead")
        self.assertEqual(len(samples), 1)
        self.assertTrue(samples[0]["code"].startswith("CkE"))
        self.assertNotIn("character", json.dumps(samples[0]).lower())


if __name__ == "__main__":
    unittest.main()

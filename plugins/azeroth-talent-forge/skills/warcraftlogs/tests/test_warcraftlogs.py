import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "warcraftlogs.py"
SPEC = importlib.util.spec_from_file_location("warcraftlogs_cli", SCRIPT)
warcraftlogs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(warcraftlogs)


class CredentialTests(unittest.TestCase):
    def test_cli_over_dotenv_over_environment_per_field(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".env").write_text(
                "WARCRAFTLOGS_CLIENT_ID=dotenv-id\n"
                "WARCRAFTLOGS_CLIENT_SECRET=dotenv-secret\n",
                encoding="utf-8",
            )
            result = warcraftlogs.resolve_credentials(
                client_id="cli-id",
                client_secret=None,
                env_file=None,
                cwd=root,
                environ={
                    "WARCRAFTLOGS_CLIENT_ID": "env-id",
                    "WARCRAFTLOGS_CLIENT_SECRET": "env-secret",
                },
            )
            self.assertEqual(result.client_id, "cli-id")
            self.assertEqual(result.client_secret, "dotenv-secret")

    def test_environment_is_fallback_when_dotenv_missing(self):
        with tempfile.TemporaryDirectory() as directory:
            result = warcraftlogs.resolve_credentials(
                client_id=None,
                client_secret=None,
                env_file=None,
                cwd=Path(directory),
                environ={
                    "WARCRAFTLOGS_CLIENT_ID": "env-id",
                    "WARCRAFTLOGS_CLIENT_SECRET": "env-secret",
                },
            )
            self.assertEqual(result.client_id, "env-id")
            self.assertEqual(result.client_secret, "env-secret")

    def test_missing_secret_raises_sanitized_error(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "WARCRAFTLOGS_CLIENT_SECRET"):
                warcraftlogs.resolve_credentials(
                    client_id="visible-id",
                    client_secret=None,
                    env_file=None,
                    cwd=Path(directory),
                    environ={},
                )

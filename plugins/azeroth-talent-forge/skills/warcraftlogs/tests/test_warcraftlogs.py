import io
import importlib.util
import json
import os
import tempfile
import unittest
import urllib.error
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).parents[1] / "scripts" / "warcraftlogs.py"
SPEC = importlib.util.spec_from_file_location("warcraftlogs_cli", SCRIPT)
warcraftlogs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(warcraftlogs)


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


class FakeOpener:
    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    def __call__(self, request):
        self.requests.append(request)
        response = self.responses.pop(0)
        if isinstance(response, BaseException):
            raise response
        return FakeResponse(response)


class ReadErrorResponse:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def read(self):
        raise OSError("read failed")


class ReadErrorOpener:
    def __call__(self, request):
        return ReadErrorResponse()


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


class TransportTests(unittest.TestCase):
    def test_query_loader_rejects_path_traversal(self):
        with self.assertRaisesRegex(ValueError, "query name"):
            warcraftlogs.load_query("../secret")

    def test_rate_limit_fixture_normalizes_output(self):
        payload = json.loads((Path(__file__).parent / "fixtures" / "rate-limit.json").read_text())
        result = warcraftlogs.normalize_rate_limit(payload)
        self.assertEqual(result["limit_per_hour"], 3600)
        self.assertEqual(result["points_spent_this_hour"], 12.5)
        self.assertEqual(result["points_reset_in"], 1800)

    def test_access_token_posts_client_credentials_form(self):
        opener = FakeOpener([{"access_token": "test-token", "expires_in": 3600}])
        client = warcraftlogs.WarcraftLogsClient(
            warcraftlogs.Credentials("client-id", "client-secret"), opener=opener
        )

        client.access_token()

        request = opener.requests[0]
        self.assertEqual(request.full_url, warcraftlogs.TOKEN_URL)
        self.assertEqual(request.get_method(), "POST")
        self.assertEqual(request.data, b"grant_type=client_credentials")
        self.assertTrue(request.get_header("Authorization").startswith("Basic "))

    def test_execute_posts_graphql_document_and_variables(self):
        opener = FakeOpener(
            [
                {"access_token": "test-token", "expires_in": 3600},
                {"data": {"rateLimitData": {"limitPerHour": 3600}}},
            ]
        )
        client = warcraftlogs.WarcraftLogsClient(
            warcraftlogs.Credentials("client-id", "client-secret"), opener=opener
        )

        result = client.execute("rate-limit", {"region": "US"})

        request = opener.requests[1]
        body = json.loads(request.data.decode("utf-8"))
        self.assertEqual(result["data"]["rateLimitData"]["limitPerHour"], 3600)
        self.assertEqual(request.full_url, warcraftlogs.GRAPHQL_URL)
        self.assertEqual(request.get_method(), "POST")
        self.assertEqual(body["variables"], {"region": "US"})
        self.assertIn("query RateLimit", body["query"])
        self.assertTrue(request.get_header("Authorization").startswith("Bearer "))
        self.assertEqual(request.get_header("Content-type"), "application/json")

    def test_open_json_retries_rate_limit_after_retry_after_seconds(self):
        rate_limited = urllib.error.HTTPError(
            warcraftlogs.TOKEN_URL,
            429,
            "rate limited",
            {"Retry-After": "2"},
            io.BytesIO(b"{}"),
        )
        opener = FakeOpener([rate_limited, {"ok": True}])
        delays = []
        client = warcraftlogs.WarcraftLogsClient(
            warcraftlogs.Credentials("client-id", "client-secret"),
            opener=opener,
            sleep=delays.append,
        )

        self.assertEqual(client._open_json(object()), {"ok": True})
        self.assertEqual(len(opener.requests), 2)
        self.assertEqual(delays, [2])

    def test_open_json_rejects_non_object_response(self):
        client = warcraftlogs.WarcraftLogsClient(
            warcraftlogs.Credentials("client-id", "client-secret"), opener=FakeOpener([["not", "an", "object"]])
        )

        with self.assertRaisesRegex(warcraftlogs.ApiError, "JSON"):
            client._open_json(object())

    def test_envelope_preserves_partial_errors_without_unsafe_fields(self):
        result = warcraftlogs.make_envelope(
            "rate-limit",
            {},
            {},
            "api_collection",
            {"limit_per_hour": 3600},
            errors=[
                {
                    "message": "partial response",
                    "path": ["rateLimitData"],
                    "extensions": {"code": "PARTIAL", "unsafe": "discard"},
                    "unsafe": "discard",
                }
            ],
            request_id="request-123",
        )

        self.assertTrue(result["partial"])
        self.assertEqual(
            result["errors"],
            [{"message": "partial response", "path": ["rateLimitData"], "extensions": {"code": "PARTIAL"}}],
        )
        self.assertEqual(result["request_id"], "request-123")
        self.assertTrue(result["source"]["fetched_at"].endswith("Z"))

    def test_rate_limit_command_prints_partial_envelope(self):
        opener = FakeOpener(
            [
                {"access_token": "test-token", "expires_in": 3600},
                {
                    "data": {
                        "rateLimitData": {
                            "limitPerHour": 3600,
                            "pointsSpentThisHour": 12.5,
                            "pointsResetIn": 1800,
                        }
                    },
                    "errors": [{"message": "partial response", "extensions": {"code": "PARTIAL"}}],
                },
            ]
        )
        output = io.StringIO()
        errors = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            missing_env = str(Path(directory) / "missing.env")
            with patch.dict(os.environ, {}, clear=True), patch.object(
                warcraftlogs.urllib.request, "urlopen", opener
            ), redirect_stdout(output), redirect_stderr(errors):
                exit_code = warcraftlogs.main(
                    [
                        "--client-id",
                        "client-id",
                        "--client-secret",
                        "client-secret",
                        "--env-file",
                        missing_env,
                        "rate-limit",
                    ]
                )

        result = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors.getvalue(), "")
        self.assertEqual(result["command"], "rate-limit")
        self.assertEqual(result["scope"], {})
        self.assertEqual(result["filters"], {})
        self.assertEqual(result["completeness"], "api_collection")
        self.assertTrue(result["partial"])

    def test_rate_limit_command_returns_configuration_error_without_credentials(self):
        output = io.StringIO()
        errors = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            missing_env = str(Path(directory) / "missing.env")
            with patch.dict(os.environ, {}, clear=True), redirect_stdout(output), redirect_stderr(errors):
                exit_code = warcraftlogs.main(["--env-file", missing_env, "rate-limit"])

        self.assertEqual(exit_code, 2)
        self.assertEqual(output.getvalue(), "")
        self.assertIn("Missing credential", errors.getvalue())

    def test_rate_limit_command_maps_oauth_response_read_error_to_auth_exit_code(self):
        output = io.StringIO()
        errors = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            missing_env = str(Path(directory) / "missing.env")
            with patch.dict(os.environ, {}, clear=True), patch.object(
                warcraftlogs.urllib.request, "urlopen", ReadErrorOpener()
            ), redirect_stdout(output), redirect_stderr(errors):
                exit_code = warcraftlogs.main(
                    [
                        "--client-id",
                        "client-id",
                        "--client-secret",
                        "client-secret",
                        "--env-file",
                        missing_env,
                        "rate-limit",
                    ]
                )

        self.assertEqual(exit_code, 3)
        self.assertEqual(output.getvalue(), "")
        self.assertIn("OAuth authentication failed", errors.getvalue())

    def test_rate_limit_command_escapes_unicode_graphql_errors_for_ascii_output(self):
        opener = FakeOpener(
            [
                {"access_token": "test-token", "expires_in": 3600},
                {
                    "data": {
                        "rateLimitData": {
                            "limitPerHour": 3600,
                            "pointsSpentThisHour": 12.5,
                            "pointsResetIn": 1800,
                        }
                    },
                    "errors": [{"message": "unicode error \u2603", "extensions": {"code": "PARTIAL"}}],
                },
            ]
        )
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            missing_env = str(Path(directory) / "missing.env")
            with patch.dict(os.environ, {}, clear=True), patch.object(
                warcraftlogs.urllib.request, "urlopen", opener
            ), redirect_stdout(output):
                exit_code = warcraftlogs.main(
                    [
                        "--client-id",
                        "client-id",
                        "--client-secret",
                        "client-secret",
                        "--env-file",
                        missing_env,
                        "rate-limit",
                    ]
                )

        self.assertEqual(exit_code, 0)
        self.assertTrue(output.getvalue().isascii())

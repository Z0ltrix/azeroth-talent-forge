import io
import ast
import importlib.util
import json
import os
import tempfile
import unittest
import urllib.error
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch


class FoundationImportTests(unittest.TestCase):
    def test_foundation_modules_and_cli_exist(self):
        from warcraftlogs_core import cli, credentials, models, transport

        self.assertTrue(hasattr(cli, "main"))
        self.assertTrue(hasattr(credentials, "resolve_credentials"))
        self.assertTrue(hasattr(models, "Credentials"))
        self.assertTrue(hasattr(transport, "load_query"))

    def test_metadata_and_reports_service_modules_exist(self):
        from warcraftlogs_core import metadata, reports

        self.assertTrue(hasattr(metadata, "MetadataResolver"))
        self.assertTrue(hasattr(metadata, "normalize_name"))
        self.assertTrue(hasattr(reports, "parse_report_reference"))
        self.assertTrue(hasattr(reports, "iter_event_pages"))

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

    def __call__(self, request, **kwargs):
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


class PackagingTests(unittest.TestCase):
    """Exercise package contracts without matching instruction prose."""

    ROOT = SCRIPT.parents[1]
    MANIFEST = SCRIPT.parents[3] / ".codex-plugin" / "plugin.json"

    @staticmethod
    def _read_narrow_yaml(path):
        """Parse the package's deliberately small, mapping-only UI YAML."""
        root = {}
        stack = [(-1, root)]
        for number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not raw_line.strip() or raw_line.lstrip().startswith("#"):
                continue
            indent = len(raw_line) - len(raw_line.lstrip(" "))
            if "\t" in raw_line[:indent]:
                raise AssertionError("tabs are not supported in UI YAML")
            line = raw_line.strip()
            if ":" not in line:
                raise AssertionError("invalid UI YAML line %d" % number)
            key, raw_value = (part.strip() for part in line.split(":", 1))
            if not key or not raw_value and raw_value != "":
                raise AssertionError("invalid UI YAML line %d" % number)
            while stack[-1][0] >= indent:
                stack.pop()
            parent = stack[-1][1]
            if key in parent:
                raise AssertionError("duplicate UI YAML key %s" % key)
            if raw_value == "":
                value = {}
                parent[key] = value
                stack.append((indent, value))
                continue
            if raw_value in ("true", "false"):
                value = raw_value == "true"
            elif raw_value.startswith(("'", '"')):
                try:
                    value = ast.literal_eval(raw_value)
                except (SyntaxError, ValueError) as error:
                    raise AssertionError("invalid UI YAML scalar on line %d" % number) from error
            else:
                value = raw_value
            parent[key] = value
        return root

    def test_skill_frontmatter_declares_exact_runtime_name(self):
        skill = self.ROOT / "SKILL.md"
        self.assertTrue(skill.is_file())
        frontmatter = skill.read_text(encoding="utf-8").split("---", 2)[1]
        fields = {
            line.split(":", 1)[0].strip(): line.split(":", 1)[1].strip()
            for line in frontmatter.splitlines()
            if ":" in line
        }
        self.assertEqual(fields.get("name"), "warcraftlogs")
        self.assertTrue(fields.get("description"))

    def test_manifest_version_and_skill_entry_are_machine_readable(self):
        manifest = json.loads(self.MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], "0.2.0")
        self.assertIn("skills", manifest)

    def test_repo_agents_documents_plugin_release_rules(self):
        repo_root = SCRIPT.parents[5]
        agents_path = repo_root / "AGENTS.md"
        self.assertTrue(agents_path.is_file())
        agents = agents_path.read_text(encoding="utf-8")
        required_phrases = (
            "one version bump per coherent delivery",
            "Semantic Versioning",
            "fixture-backed tests",
            "SKILL.md",
            "applicable reference files",
            "credentials",
        )
        for phrase in required_phrases:
            self.assertIn(phrase, agents)

    def test_ui_metadata_is_present_with_explicit_interface_fields(self):
        metadata = self.ROOT / "agents" / "openai.yaml"
        self.assertTrue(metadata.is_file())
        document = self._read_narrow_yaml(metadata)
        interface = document.get("interface")
        self.assertIsInstance(interface, dict)
        self.assertEqual(interface.get("display_name"), "Warcraft Logs")
        self.assertTrue(interface.get("short_description"))
        self.assertIn("$warcraftlogs", interface.get("default_prompt", ""))
        self.assertIs(document.get("policy", {}).get("allow_implicit_invocation"), True)

    def test_all_bundled_query_documents_remain_loadable(self):
        query_dir = SCRIPT.parent / "graphql"
        names = sorted(path.stem for path in query_dir.glob("*.graphql"))
        self.assertTrue(names)
        for name in names:
            self.assertTrue(warcraftlogs.load_query(name).strip())

    def test_skill_documents_describe_staged_bounded_actor_bound_workflow(self):
        root = self.ROOT
        skill = (root / "SKILL.md").read_text(encoding="utf-8")
        cli = (root / "references" / "cli.md").read_text(encoding="utf-8")
        discovery = (root / "references" / "discovery.md").read_text(encoding="utf-8")
        reports = (root / "references" / "reports.md").read_text(encoding="utf-8")
        evaluation = (root / "references" / "evaluation.md").read_text(encoding="utf-8")
        scenarios = (root / "tests" / "skill-pressure-scenarios.md").read_text(encoding="utf-8")
        prompt = (root / "agents" / "openai.yaml").read_text(encoding="utf-8")

        for phrase in ("discover", "fights", "details", "local evaluation", "matched_actor", "sampled", "truncation", "errors", "report-wide", "fight-specific"):
            self.assertIn(phrase, skill.lower())
        for phrase in ("absolute-start-time", "time-mode", "--output", "--max-pages"):
            self.assertIn(phrase, cli)
        for phrase in ("--latest", "--player", "report details", "--views"):
            self.assertIn(phrase, skill.lower() + cli.lower() + discovery.lower() + reports.lower())
        for phrase in ("absolute-start-time", "started", "timezone", "same-spec/key"):
            self.assertIn(phrase, discovery + reports)
        for phrase in ("combatant", "--fight", "event-limit", "sampled"):
            self.assertIn(phrase, reports + discovery)
        for phrase in ("target actor", "median", "quartile", "percentile", "derived locally", "missing data", "view mapping", "n < 5", "damagedone"):
            self.assertIn(phrase, evaluation.lower())
        self.assertIn("evaluation.md", skill)
        for phrase in ("stale events", "report-level-only", "whole-report", "exhaustive global"):
            self.assertIn(phrase, scenarios.lower())
        self.assertIn("local run evaluation", prompt.lower())
        self.assertIn("comparable public-log cohorts", prompt.lower())

    def test_documented_fight_selector_matches_public_cli(self):
        cli = (self.ROOT / "references" / "cli.md").read_text(encoding="utf-8")
        reports = (self.ROOT / "references" / "reports.md").read_text(encoding="utf-8")
        for command in ("fights", "player-details", "events"):
            args = warcraftlogs.build_parser().parse_args(
                ["report", command, "REPORTCODE", "--fight", "3"]
            )
            self.assertEqual(args.fight, 3)
        self.assertIn("report-wide", reports.lower())
        self.assertIn("not fight-filtered", reports.lower())


class TransportTests(unittest.TestCase):
    def test_query_loader_rejects_path_traversal(self):
        with self.assertRaisesRegex(ValueError, "query name"):
            warcraftlogs.load_query("../secret")

    def test_default_opener_receives_bounded_timeout(self):
        opener = patch.object(
            warcraftlogs.urllib.request,
            "urlopen",
            return_value=FakeResponse({"ok": True}),
        )
        with opener as mocked_urlopen:
            client = warcraftlogs.WarcraftLogsClient(
                warcraftlogs.Credentials("client-id", "client-secret")
            )

            self.assertEqual(client._open_json(object()), {"ok": True})

        mocked_urlopen.assert_called_once_with(
            unittest.mock.ANY, timeout=30
        )

    def test_injected_opener_keeps_single_argument_contract(self):
        opener = FakeOpener([{"ok": True}])
        client = warcraftlogs.WarcraftLogsClient(
            warcraftlogs.Credentials("client-id", "client-secret"), opener=opener
        )

        self.assertEqual(client._open_json(object()), {"ok": True})
        self.assertEqual(len(opener.requests), 1)

    def test_transport_timeout_is_sanitized_to_api_error(self):
        client = warcraftlogs.WarcraftLogsClient(
            warcraftlogs.Credentials("client-id", "client-secret"),
            opener=FakeOpener([TimeoutError("timed out")]),
        )

        with self.assertRaisesRegex(warcraftlogs.ApiError, "Response read failed"):
            client._open_json(object())

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

    def test_rate_limit_command_preserves_errors_only_graphql_message(self):
        output = io.StringIO()
        errors = io.StringIO()
        client = FixtureClient({"rate-limit": {"errors": [{"message": "rate limit unavailable", "extensions": {"secret": "discard"}}]}})
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(warcraftlogs, "WarcraftLogsClient", return_value=client), patch.dict(
                os.environ, {}, clear=True
            ), redirect_stdout(output), redirect_stderr(errors):
                exit_code = warcraftlogs.main(
                    [
                        "--client-id",
                        "client-id",
                        "--client-secret",
                        "client-secret",
                        "--env-file",
                        str(Path(directory) / "missing.env"),
                        "rate-limit",
                    ]
                )

        self.assertEqual(exit_code, 4)
        self.assertEqual(output.getvalue(), "")
        self.assertIn("GraphQL error: rate limit unavailable", errors.getvalue())
        self.assertNotIn("did not contain rate limit data", errors.getvalue())
        self.assertNotIn("discard", errors.getvalue())

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


class MetadataTests(unittest.TestCase):
    def test_normalize_name_casefolds_whitespace_and_hyphens(self):
        self.assertEqual(warcraftlogs.normalize_name("  ThE-Dawnbreaker  "), "the dawnbreaker")

    def test_select_named_prefers_exact_display_name(self):
        items = [{"id": 1, "name": "The Dawnbreaker"}, {"id": 2, "name": "The-Dawnbreaker"}]
        self.assertEqual(warcraftlogs.select_named(items, "The Dawnbreaker", "instance")["id"], 1)

    def test_select_named_rejects_ambiguous_normalized_match(self):
        items = [{"id": 1, "name": "The Dawnbreaker"}, {"id": 2, "name": "The-Dawnbreaker"}]
        with self.assertRaisesRegex(ValueError, "Ambiguous instance"):
            warcraftlogs.select_named(items, "the dawnbreaker", "instance")

    def test_select_named_error_lists_display_names(self):
        items = [{"id": 1, "name": "Alpha"}, {"id": 2, "name": "ALPHA"}]
        with self.assertRaisesRegex(ValueError, "Alpha, ALPHA"):
            warcraftlogs.select_named(items, "alpha", "class")

    def test_realm_lookup_requires_region(self):
        resolver = warcraftlogs.MetadataResolver(FixtureClient({}), Path(tempfile.mkdtemp()))
        with self.assertRaisesRegex(ValueError, "region"):
            resolver.realm(None, "Area 52")

    def test_realm_fixture_uses_region_and_normalized_slug(self):
        client = FixtureClient({"metadata-realm": fixture("metadata-realm.json")})
        resolver = warcraftlogs.MetadataResolver(client, Path(tempfile.mkdtemp()))

        result, provenance = resolver.realm("US", "Area 52")

        self.assertEqual(client.calls, ["metadata-realm"])
        self.assertEqual(result["id"], 3676)
        self.assertEqual(result["name"], "Area 52")
        self.assertEqual(result["normalizedName"], "area-52")
        self.assertEqual(result["region"], {"id": 1, "name": "US", "slug": "us"})
        self.assertEqual(result["subregion"], {"id": 1, "name": "North America"})
        self.assertEqual(provenance["status"], "miss")

    def test_metadata_queries_select_pagination_data_and_realm_object_fields(self):
        game_query = warcraftlogs.load_query("metadata-game")
        realm_query = warcraftlogs.load_query("metadata-realm")

        self.assertIn("abilities(limit: $abilityLimit, page: $abilityPage) { data { id name } }", game_query)
        self.assertIn("region { id name slug }", realm_query)

    def test_world_fixture_normalizes_partition_season_and_encounter_names(self):
        resolver = warcraftlogs.MetadataResolver(
            FixtureClient({"metadata-world": fixture("metadata-world.json")}), Path(tempfile.mkdtemp())
        )

        result, provenance = resolver.world({"expansionId": 11})

        self.assertEqual(result["regions"], [{"id": 1, "name": "US", "slug": "us"}])
        self.assertEqual(result["zones"][0]["partitions"], [{"id": 42, "name": "Season 1"}])
        self.assertEqual(result["zones"][0]["encounters"], [{"id": 2902, "name": "The Dawnbreaker"}])
        self.assertEqual(provenance["status"], "miss")

    def test_game_fixture_normalizes_classes_specs_and_affix_ids(self):
        resolver = warcraftlogs.MetadataResolver(
            FixtureClient({"metadata-game": fixture("metadata-game.json")}), Path(tempfile.mkdtemp())
        )

        result, provenance = resolver.game({"abilityLimit": 100, "abilityPage": 1})

        self.assertEqual(result["classes"][0]["slug"], "paladin")
        self.assertEqual(result["classes"][0]["specs"], [{"id": 66, "name": "Protection", "slug": "protection"}])
        self.assertEqual(result["affixes"], [{"id": 9, "name": "Tyrannical"}])
        self.assertEqual(result["abilities"], [{"id": 20271, "name": "Judgment"}])
        self.assertEqual(provenance["status"], "miss")

    def test_metadata_cache_expires_and_no_cache_does_not_write(self):
        payload = fixture("metadata-world.json")
        client = FixtureClient({"metadata-world": payload})
        clock = [1000]
        with tempfile.TemporaryDirectory() as directory:
            cache = Path(directory)
            resolver = warcraftlogs.MetadataResolver(client, cache, now=lambda: clock[0])
            resolver.world({"expansionId": 11})
            _, hit = resolver.world({"expansionId": 11})
            self.assertEqual(hit["status"], "hit")
            self.assertEqual(client.calls, ["metadata-world"])
            cache_file = next(cache.glob("*.json"))
            cached = json.loads(cache_file.read_text(encoding="utf-8"))
            self.assertEqual(cached["expires_at"] - cached["fetched_at"], 24 * 60 * 60)
            clock[0] = cached["expires_at"]
            _, expired = resolver.world({"expansionId": 11})
            self.assertEqual(expired["status"], "miss")
            self.assertEqual(client.calls, ["metadata-world", "metadata-world"])
            cache_bytes = cache_file.read_bytes()

            no_cache = warcraftlogs.MetadataResolver(client, cache, no_cache=True, now=lambda: clock[0])
            no_cache.world({"expansionId": 11})
            self.assertEqual(client.calls, ["metadata-world", "metadata-world", "metadata-world"])
            self.assertEqual(cache_file.read_bytes(), cache_bytes)
            self.assertEqual(list(cache.glob("*.tmp")), [])

    def test_metadata_command_emits_fixture_backed_collection_envelope(self):
        output = io.StringIO()
        errors = io.StringIO()
        client = FixtureClient({"metadata-game": fixture("metadata-game.json")})
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(warcraftlogs, "WarcraftLogsClient", return_value=client), patch.dict(
                os.environ, {"LOCALAPPDATA": directory}, clear=True
            ), redirect_stdout(output), redirect_stderr(errors):
                exit_code = warcraftlogs.main(
                    [
                        "--client-id",
                        "client-id",
                        "--client-secret",
                        "client-secret",
                        "--env-file",
                        str(Path(directory) / "missing.env"),
                        "metadata",
                        "classes",
                    ]
                )

        result = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors.getvalue(), "")
        self.assertEqual(result["command"], "metadata classes")
        self.assertEqual(result["completeness"], "api_collection")
        self.assertEqual(result["data"], [{"id": 2, "name": "Paladin", "slug": "paladin"}])
        self.assertEqual(result["cache"]["status"], "miss")

    def test_metadata_command_preserves_errors_only_graphql_message(self):
        output = io.StringIO()
        errors = io.StringIO()
        client = FixtureClient({"metadata-game": {"errors": [{"message": "metadata unavailable", "extensions": {"secret": "discard"}}]}})
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(warcraftlogs, "WarcraftLogsClient", return_value=client), patch.dict(
                os.environ, {"LOCALAPPDATA": directory}, clear=True
            ), redirect_stdout(output), redirect_stderr(errors):
                exit_code = warcraftlogs.main(
                    [
                        "--client-id",
                        "client-id",
                        "--client-secret",
                        "client-secret",
                        "--env-file",
                        str(Path(directory) / "missing.env"),
                        "metadata",
                        "classes",
                    ]
                )

        self.assertEqual(exit_code, 4)
        self.assertEqual(output.getvalue(), "")
        self.assertIn("GraphQL error: metadata unavailable", errors.getvalue())
        self.assertNotIn("did not contain metadata", errors.getvalue())
        self.assertNotIn("discard", errors.getvalue())


class ReportReferenceTests(unittest.TestCase):
    def test_raw_report_code(self):
        self.assertEqual(
            warcraftlogs.parse_report_reference("AbCd1234"),
            warcraftlogs.ReportReference("AbCd1234", None),
        )

    def test_parse_report_url_with_fight_fragment(self):
        result = warcraftlogs.parse_report_reference(
            "https://www.warcraftlogs.com/reports/AbCd1234#fight=7&type=damage-done"
        )
        self.assertEqual(result.code, "AbCd1234")
        self.assertEqual(result.fight_id, 7)

    def test_parse_classic_localized_url_with_query_fight(self):
        result = warcraftlogs.parse_report_reference(
            "https://de.classic.warcraftlogs.com/reports/ZyXw9876?fight=12"
        )
        self.assertEqual(result, warcraftlogs.ReportReference("ZyXw9876", 12))

    def test_rejects_lookalike_host_and_malformed_code(self):
        for value in (
            "https://warcraftlogs.com.evil.example/reports/AbCd1234",
            "https://notwarcraftlogs.com/reports/AbCd1234",
            "bad/code",
            "short",
        ):
            with self.subTest(value=value), self.assertRaises(ValueError):
                warcraftlogs.parse_report_reference(value)

    def test_rejects_non_official_or_non_default_port_report_urls(self):
        for value in (
            "https://foo.warcraftlogs.com/reports/AbCd1234",
            "https://warcraftlogs.com:4444/reports/AbCd1234",
            "https://warcraftlogs.com:bogus/reports/AbCd1234",
        ):
            with self.subTest(value=value), self.assertRaises(ValueError):
                warcraftlogs.parse_report_reference(value)

    def test_rejects_empty_or_duplicate_fight_values_in_query_or_fragment(self):
        for value in (
            "https://www.warcraftlogs.com/reports/AbCd1234?fight=",
            "https://www.warcraftlogs.com/reports/AbCd1234#fight=",
            "https://www.warcraftlogs.com/reports/AbCd1234?fight=7&fight=8",
            "https://www.warcraftlogs.com/reports/AbCd1234#fight=7&fight=8",
        ):
            with self.subTest(value=value), self.assertRaises(ValueError):
                warcraftlogs.parse_report_reference(value)


class ReportTests(unittest.TestCase):
    def run_report(self, payloads, *arguments):
        output = io.StringIO()
        errors = io.StringIO()
        client = FixtureClient(payloads)
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(warcraftlogs, "WarcraftLogsClient", return_value=client), patch.dict(
                os.environ, {}, clear=True
            ), redirect_stdout(output), redirect_stderr(errors):
                exit_code = warcraftlogs.main(
                    [
                        "--client-id",
                        "client-id",
                        "--client-secret",
                        "client-secret",
                        "--env-file",
                        str(Path(directory) / "missing.env"),
                        "report",
                    ]
                    + list(arguments)
                )
        return exit_code, output.getvalue(), errors.getvalue(), client

    def test_report_fights_parser_accepts_targeting_filters(self):
        args = warcraftlogs.build_parser().parse_args([
            "report", "fights", "REPORT123",
            "--player", "Ratelka",
            "--encounter", "Den of Nalorakk",
            "--key", "6",
            "--timed",
            "--latest", "1",
        ])
        self.assertEqual(args.encounter, "Den of Nalorakk")
        self.assertEqual(args.key, 6)
        self.assertTrue(args.timed)
        self.assertFalse(args.depleted)
        self.assertEqual(args.latest, 1)

    def test_report_fights_parser_rejects_invalid_targeting_filters(self):
        invalid = (
            ("--timed", "--depleted"),
            ("--key", "0"),
            ("--latest", "0"),
        )
        for options in invalid:
            with self.subTest(options=options), self.assertRaises(SystemExit):
                warcraftlogs.build_parser().parse_args(["report", "fights", "REPORT123", *options])

    def test_report_queries_select_consumed_object_fields(self):
        summary = warcraftlogs.load_query("report-summary")
        fights = warcraftlogs.load_query("report-fights")
        master = warcraftlogs.load_query("report-master-data")

        self.assertIn("archiveStatus { isArchived isAccessible archiveDate }", summary)
        self.assertIn("zone { id name }", summary)
        self.assertIn("owner { id name }", summary)
        self.assertIn("guild { id name }", summary)
        self.assertIn("gameZone { id name }", fights)
        self.assertIn("keystoneAffixes", fights)
        self.assertIn("abilities { gameID icon name type }", master)
        self.assertIn("actors { id gameID icon name petOwner server subType type }", master)

    def test_summary_fixture_emits_public_single_report(self):
        exit_code, output, errors, client = self.run_report(
            {"report-summary": fixture("report-summary.json")}, "summary", "AbCd1234"
        )

        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertEqual(client.calls, ["report-summary"])
        self.assertEqual(client.variables[0], {"code": "AbCd1234", "allowUnlisted": False})
        self.assertEqual(result["command"], "report summary")
        self.assertEqual(result["scope"], {"report_code": "AbCd1234"})
        self.assertEqual(result["completeness"], "single_report")
        self.assertEqual(result["data"]["zone"], {"id": 38, "name": "Nerub-ar Palace"})

    def test_errors_only_report_response_preserves_sanitized_graphql_message(self):
        exit_code, output, errors, unused = self.run_report(
            {"report-table": {"errors": [{"message": "Cannot query field dataType", "path": ["reportData", "report", "table"], "extensions": {"code": "GRAPHQL_VALIDATION", "secret": "discard"}}]}},
            "table", "AbCd1234", "--data-type", "DamageDone"
        )

        self.assertEqual(exit_code, 4)
        self.assertEqual(output, "")
        self.assertIn("Cannot query field dataType", errors)
        self.assertNotIn("did not contain a public report", errors)
        self.assertNotIn("secret", errors)

    def test_report_wide_commands_drop_compatibility_fight_scope(self):
        cases = (
            ("summary", "report-summary.json", "report-summary"),
            ("master-data", "report-master-data.json", "report-master-data"),
        )
        for kind, fixture_name, query_name in cases:
            with self.subTest(kind=kind):
                exit_code, output, errors, client = self.run_report(
                    {query_name: fixture(fixture_name)}, kind, "AbCd1234", "--fight", "3"
                )
                result = json.loads(output)
                self.assertEqual(exit_code, 0)
                self.assertEqual(errors, "")
                self.assertNotIn("fightIDs", client.variables[0])
                self.assertEqual(result["scope"], {"report_code": "AbCd1234"})

    def test_fights_fixture_keeps_empty_and_mythic_plus_fields(self):
        exit_code, output, errors, client = self.run_report(
            {"report-fights": fixture("report-fights.json")},
            "fights",
            "https://classic.warcraftlogs.com/reports/AbCd1234#fight=7",
            "--fight",
            "9",
        )

        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertEqual(result["scope"], {"report_code": "AbCd1234", "fight_id": 9, "time_mode": "started"})
        self.assertEqual(client.variables[0]["fightIDs"], [9])
        self.assertEqual(result["data"][0]["keystoneLevel"], 12)
        self.assertEqual(result["data"][0]["keystoneAffixes"], [9])
        self.assertEqual(result["data"][0]["friendlyPlayers"], [1])

    def test_fights_filters_to_player_using_report_master_data(self):
        exit_code, output, errors, client = self.run_report(
            {
                "report-fights": fixture("report-fights.json"),
                "report-master-data": fixture("report-master-data.json"),
            },
            "fights",
            "AbCd1234",
            "--player",
            "Tankadin",
        )

        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertEqual([fight["id"] for fight in result["data"]], [9])
        self.assertEqual(result["filters"]["player"], "Tankadin")
        self.assertEqual(client.calls, ["report-fights", "report-master-data"])

    def test_filter_enriched_fights_applies_targeting_order(self):
        payload = fixture("report-fights-filterable.json")
        fights = payload["data"]["reportData"]["report"]["fights"]
        enriched = warcraftlogs.select_fights(fights[:5], 1000000, warnings=[])

        selected, metadata = warcraftlogs.filter_enriched_fights(
            enriched,
            encounter="Den of Nalorakk",
            key=6,
            timed=True,
            latest=1,
        )
        self.assertEqual([fight["id"] for fight in selected], [20])
        self.assertEqual(metadata["source_count"], 5)
        self.assertEqual(metadata["selected_count"], 1)
        self.assertEqual(
            metadata["selection_order"],
            ["fight", "player", "absolute_time", "encounter", "key", "completion", "latest"],
        )

        depleted, unused = warcraftlogs.filter_enriched_fights(enriched, key=6, depleted=True)
        self.assertEqual([fight["id"] for fight in depleted], [21])

    def test_filter_enriched_fights_rejects_ambiguous_encounter(self):
        fights = [
            {"id": 1, "name": "Shared Name", "encounterID": 10},
            {"id": 2, "name": "shared name", "encounterID": 11},
        ]
        with self.assertRaises(ValueError):
            warcraftlogs.filter_enriched_fights(fights, encounter="SHARED NAME")

    def test_filter_enriched_fights_unknown_encounter_is_empty(self):
        selected, metadata = warcraftlogs.filter_enriched_fights(
            [{"id": 1, "name": "Known", "encounterID": 10}], encounter="Unknown"
        )
        self.assertEqual(selected, [])
        self.assertEqual(metadata["selected_count"], 0)

    def test_fights_command_applies_targeting_filters_and_selection_metadata(self):
        exit_code, output, errors, client = self.run_report(
            {
                "report-fights": fixture("report-fights-filterable.json"),
                "report-master-data": fixture("report-master-data.json"),
            },
            "fights",
            "AbCd1234",
            "--player", "Tankadin",
            "--encounter", "Den of Nalorakk",
            "--key", "6",
            "--timed",
            "--latest", "1",
        )
        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertEqual([fight["id"] for fight in result["data"]], [20])
        self.assertEqual(result["filters"]["encounter"], "Den of Nalorakk")
        self.assertEqual(result["filters"]["key"], 6)
        self.assertTrue(result["filters"]["timed"])
        self.assertEqual(result["filters"]["latest"], 1)
        self.assertEqual(result["selection"]["source_count"], 6)
        self.assertEqual(result["selection"]["selected_count"], 1)
        self.assertEqual(client.calls, ["report-fights", "report-master-data"])

    def test_fights_player_partial_master_data_error_is_sanitized_without_traceback(self):
        exit_code, output, errors, client = self.run_report(
            {
                "report-fights": fixture("report-fights.json"),
                "report-master-data": {
                    "errors": [{
                        "message": "Master data unavailable",
                        "path": ["reportData", "report", "masterData"],
                        "extensions": {"code": "PARTIAL", "secret": "discard"},
                    }],
                },
            },
            "fights",
            "AbCd1234",
            "--player",
            "Tankadin",
        )

        self.assertEqual(exit_code, 4)
        self.assertEqual(output, "")
        self.assertIn("Master data unavailable", errors)
        self.assertNotIn("discard", errors)
        self.assertNotIn("Traceback", errors)
        self.assertEqual(client.calls, ["report-fights", "report-master-data"])

    def test_player_details_filters_to_named_player(self):
        exit_code, output, errors, client = self.run_report(
            {"report-player-details": fixture("report-player-details.json")},
            "player-details",
            "AbCd1234",
            "--player",
            "Tankadin",
        )

        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertEqual(result["data"], {"players": [{"id": 1, "name": "Tankadin"}]})
        self.assertEqual(client.calls, ["report-player-details"])

    def test_details_fetches_one_fight_and_actor_scoped_default_tables(self):
        exit_code, output, errors, client = self.run_report(
            {
                "report-fights": fixture("report-fights.json"),
                "report-master-data": fixture("report-master-data.json"),
                "report-player-details": fixture("report-player-details.json"),
                "report-table": fixture("report-table.json"),
            },
            "details",
            "AbCd1234",
            "--fight",
            "9",
            "--player",
            "Tankadin",
        )

        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertEqual(result["command"], "report details")
        self.assertEqual(result["data"]["fight"]["id"], 9)
        self.assertEqual(result["data"]["player"]["id"], 1)
        self.assertEqual(result["data"]["player_details"]["players"][0]["name"], "Tankadin")
        self.assertEqual(
            set(result["data"]["tables"]),
            {"DamageDone", "Healing", "DamageTaken", "Deaths", "Interrupts", "Casts"},
        )
        self.assertEqual(result["data"]["tables"]["DamageDone"]["entries"][0]["name"], "Tankadin")
        self.assertEqual(client.calls.count("report-fights"), 1)
        self.assertEqual(client.calls.count("report-master-data"), 1)
        self.assertEqual(client.calls.count("report-player-details"), 1)
        self.assertEqual(client.calls.count("report-table"), 6)
        table_variables = [variables for name, variables in zip(client.calls, client.variables) if name == "report-table"]
        self.assertEqual({variables["dataType"] for variables in table_variables}, {"DamageDone", "Healing", "DamageTaken", "Deaths", "Interrupts", "Casts"})
        self.assertTrue(all(variables.get("sourceID") == 1 for variables in table_variables if variables["dataType"] in {"DamageDone", "Healing", "Interrupts", "Casts"}))
        self.assertTrue(all(variables.get("targetID") == 1 for variables in table_variables if variables["dataType"] in {"DamageTaken", "Deaths"}))

    def test_details_includes_requested_views_in_filters(self):
        exit_code, output, errors, client = self.run_report(
            {
                "report-fights": fixture("report-fights.json"),
                "report-master-data": fixture("report-master-data.json"),
                "report-player-details": fixture("report-player-details.json"),
                "report-table": fixture("report-table.json"),
            },
            "details",
            "AbCd1234",
            "--fight",
            "9",
            "--player",
            "Tankadin",
            "--views",
            "DamageDone,Healing",
        )

        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertEqual(result["filters"]["views"], "DamageDone,Healing")
        self.assertEqual(set(result["data"]["tables"]), {"DamageDone", "Healing"})
        self.assertEqual(client.calls.count("report-table"), 2)

    def test_details_rejects_unknown_player_before_table_requests(self):
        exit_code, output, errors, client = self.run_report(
            {
                "report-fights": fixture("report-fights.json"),
                "report-master-data": fixture("report-master-data.json"),
                "report-player-details": fixture("report-player-details.json"),
                "report-table": fixture("report-table.json"),
            },
            "details",
            "AbCd1234",
            "--fight",
            "9",
            "--player",
            "Missing",
        )

        self.assertEqual(exit_code, 2)
        self.assertEqual(output, "")
        self.assertIn("Report player was not found", errors)
        self.assertEqual(client.calls, ["report-fights", "report-master-data"])

    def test_details_preserves_fight_selection_warnings_in_envelope(self):
        payload = fixture("report-fights.json")
        payload["data"]["reportData"]["report"]["fights"].append(
            {
                "id": 11,
                "encounterID": 2903,
                "difficulty": 10,
                "startTime": 4000,
                "endTime": 3000,
                "kill": False,
                "friendlyPlayers": [1],
                "friendlySpecs": [66],
                "gameZone": {"id": 2335, "name": "The Dawnbreaker"},
                "inProgress": False,
                "keystoneAffixes": [9],
                "keystoneLevel": 12,
                "keystoneTime": 1550000,
                "keystoneBonus": 2,
            }
        )
        exit_code, output, errors, client = self.run_report(
            {
                "report-fights": payload,
                "report-master-data": fixture("report-master-data.json"),
                "report-player-details": fixture("report-player-details.json"),
                "report-table": fixture("report-table.json"),
            },
            "details",
            "AbCd1234",
            "--fight",
            "9",
            "--player",
            "Tankadin",
        )

        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertTrue(result["warnings"])
        self.assertIn("Skipped fight 11 because its relative timestamps are invalid", result["warnings"][0])
        self.assertEqual(client.calls.count("report-table"), 6)

    def test_fights_rejects_report_relative_window(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
            warcraftlogs.build_parser().parse_args(
                ["report", "fights", "AbCd1234", "--start-time", "1000", "--end-time", "2000"]
            )
        self.assertEqual(raised.exception.code, 2)

    def test_fights_accept_absolute_selection_options_without_sending_them_to_api(self):
        args = warcraftlogs.build_parser().parse_args([
            "report", "fights", "AbCd1234", "--absolute-start-time", "1000",
            "--absolute-end-time", "2000", "--time-mode", "overlap",
        ])
        reference, variables, scope, filters = warcraftlogs.report_request(args)

        self.assertEqual(reference.code, "AbCd1234")
        self.assertNotIn("startTime", variables)
        self.assertNotIn("endTime", variables)
        self.assertEqual(scope["absolute_start_time"], 1000.0)
        self.assertEqual(scope["absolute_end_time"], 2000.0)
        self.assertEqual(scope["time_mode"], "overlap")
        self.assertEqual(filters, {"translate": True})

    def test_fights_reject_invalid_absolute_selection_before_request(self):
        for options in (("--absolute-start-time", "-1"), ("--absolute-start-time", "2000", "--absolute-end-time", "1000")):
            args = warcraftlogs.build_parser().parse_args(["report", "fights", "AbCd1234", *options])
            with self.subTest(options=options), self.assertRaises(ValueError):
                warcraftlogs.report_request(args)

    def test_master_data_fixture_preserves_actors_and_abilities(self):
        exit_code, output, errors, client = self.run_report(
            {"report-master-data": fixture("report-master-data.json")},
            "master-data",
            "AbCd1234",
        )

        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertEqual(result["data"]["abilities"][0]["gameID"], 20271)
        self.assertEqual(result["data"]["actors"][0]["name"], "Tankadin")
        self.assertEqual(client.variables[0]["translate"], True)

    def test_json_report_commands_emit_fixture_data_and_window_scope(self):
        cases = (
            ("player-details", "report-player-details.json", {"players": [{"id": 1, "name": "Tankadin"}]}),
            ("table", "report-table.json", {"entries": [{"name": "Tankadin", "total": 12345}]}),
            ("graph", "report-graph.json", {"series": [{"name": "Tankadin", "data": [[0, 10]]}]}),
        )
        for kind, fixture_name, expected in cases:
            arguments = [kind, "AbCd1234", "--start-time", "1000", "--end-time", "2000"]
            if kind in ("table", "graph"):
                arguments.extend(["--data-type", "DamageDone"])
            with self.subTest(kind=kind):
                exit_code, output, errors, client = self.run_report(
                    {"report-" + kind: fixture(fixture_name)}, *arguments
                )
                result = json.loads(output)
                self.assertEqual(exit_code, 0)
                self.assertEqual(errors, "")
                self.assertEqual(result["data"], expected)
                self.assertEqual(
                    result["scope"],
                    {"report_code": "AbCd1234", "start_time": 1000.0, "end_time": 2000.0},
                )
                self.assertEqual(client.variables[0]["startTime"], 1000.0)
                self.assertEqual(client.variables[0]["endTime"], 2000.0)

    def test_rankings_fixture_uses_supported_typed_arguments(self):
        exit_code, output, errors, client = self.run_report(
            {"report-rankings": fixture("report-rankings.json")},
            "rankings",
            "AbCd1234",
            "--fight",
            "7",
            "--compare",
            "Rankings",
            "--player-metric",
            "bossdps",
            "--timeframe",
            "Historical",
        )

        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertEqual(result["data"]["rankedCharacters"][0]["rankPercent"], 95.2)
        self.assertEqual(client.variables[0]["fightIDs"], [7])
        self.assertNotIn("startTime", client.variables[0])

    def test_partial_graphql_errors_survive_report_envelope(self):
        payload = fixture("report-table.json")
        payload["errors"] = [
            {
                "message": "one actor was unavailable",
                "path": ["reportData", "report", "table"],
                "extensions": {"code": "PARTIAL", "unsafe": "discard"},
            }
        ]
        exit_code, output, errors, unused = self.run_report(
            {"report-table": payload}, "table", "AbCd1234", "--data-type", "DamageDone"
        )

        result = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors, "")
        self.assertTrue(result["partial"])
        self.assertEqual(result["errors"][0]["extensions"], {"code": "PARTIAL"})

    def test_table_passes_documented_typed_filters(self):
        exit_code, output, errors, client = self.run_report(
            {"report-table": fixture("report-table.json")},
            "table",
            "AbCd1234",
            "--data-type",
            "DamageDone",
            "--death",
            "2",
            "--filter-expression",
            "ability.id=20271",
            "--source-class",
            "Paladin",
            "--source-instance-id",
            "4",
            "--target-auras-absent",
            "1234.0",
            "--wipe-cutoff",
            "5",
            "--no-translate",
        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(output != "", True)
        self.assertEqual(errors, "")
        self.assertEqual(client.variables[0]["death"], 2)
        self.assertEqual(client.variables[0]["filterExpression"], "ability.id=20271")
        self.assertEqual(client.variables[0]["sourceClass"], "Paladin")
        self.assertEqual(client.variables[0]["sourceInstanceID"], 4)
        self.assertEqual(client.variables[0]["targetAurasAbsent"], "1234.0")
        self.assertEqual(client.variables[0]["wipeCutoff"], 5)
        self.assertEqual(client.variables[0]["translate"], False)

    def test_rejects_non_public_or_inaccessible_report(self):
        cases = (
            ("private", {"visibility": "private"}),
            ("unlisted", {"visibility": "unlisted"}),
            ("archived", {"archiveStatus": {"isArchived": True, "isAccessible": False, "archiveDate": 1700000000000}}),
        )
        for label, changes in cases:
            with self.subTest(label=label):
                payload = fixture("report-summary.json")
                payload["data"]["reportData"]["report"].update(changes)
                exit_code, output, errors, unused = self.run_report(
                    {"report-summary": payload}, "summary", "AbCd1234"
                )
                self.assertEqual(exit_code, 4)
                self.assertEqual(output, "")
                self.assertIn("public", errors.lower())

    def test_rejects_report_without_positive_archive_accessibility(self):
        for label, changes in (
            ("missing", {"archiveStatus": None}),
            ("null", {"archiveStatus": None}),
            ("missing-accessibility", {"archiveStatus": {"isArchived": False, "archiveDate": None}}),
        ):
            with self.subTest(label=label):
                payload = fixture("report-summary.json")
                report = payload["data"]["reportData"]["report"]
                if label == "missing":
                    del report["archiveStatus"]
                else:
                    report.update(changes)
                exit_code, output, errors, unused = self.run_report(
                    {"report-summary": payload}, "summary", "AbCd1234"
                )
                self.assertEqual(exit_code, 4)
                self.assertEqual(output, "")
                self.assertIn("accessible", errors.lower())

    def test_invalid_enum_is_rejected_before_http(self):
        exit_code, output, errors, client = self.run_report(
            {}, "table", "AbCd1234", "--data-type", "DefinitelyNotADataType"
        )

        self.assertEqual(exit_code, 2)
        self.assertEqual(output, "")
        self.assertIn("data type", errors.lower())
        self.assertEqual(client.calls, [])

    def test_rankings_rejects_window_argument_it_does_not_send(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
            warcraftlogs.build_parser().parse_args(
                ["report", "rankings", "AbCd1234", "--start-time", "1000"]
            )
        self.assertEqual(raised.exception.code, 2)


def event_page(events, cursor):
    return {"data": {"reportData": {"report": {"events": {"data": events, "nextPageTimestamp": cursor}}}}}


class SequenceClient:
    def __init__(self, payloads):
        self.payloads = list(payloads)
        self.calls = []
        self.variables = []

    def execute(self, query_name, variables):
        self.calls.append(query_name)
        self.variables.append(dict(variables))
        return self.payloads.pop(0)


class EventTests(unittest.TestCase):
    def test_direct_event_pagination_rejects_malformed_bounds_and_fight_ids_before_execute(self):
        cases = (
            {"startTime": "0", "endTime": 1000},
            {"startTime": float("inf"), "endTime": 1000},
            {"startTime": 0, "endTime": float("nan")},
            {"startTime": -1, "endTime": 1000},
            {"startTime": 0, "endTime": 1000, "fightIDs": "7"},
            {"startTime": 0, "endTime": 1000, "fightIDs": [0]},
        )
        for variables in cases:
            client = SequenceClient([])
            with self.subTest(variables=variables), self.assertRaises(ValueError):
                list(warcraftlogs.iter_event_pages(client, "CODE", variables, 5))
            self.assertEqual(client.calls, [])

    def test_event_pagination_requires_fight_or_complete_window(self):
        with self.assertRaisesRegex(ValueError, "fight ID or both startTime and endTime"):
            list(warcraftlogs.iter_event_pages(SequenceClient([]), "CODE", {}, 5))

    def test_event_pagination_advances_to_returned_cursor(self):
        client = SequenceClient([
            event_page([{"timestamp": 100}], 200),
            event_page([{"timestamp": 200}], None),
        ])

        pages = list(warcraftlogs.iter_event_pages(client, "CODE", {"startTime": 0, "endTime": 1000}, 5))

        self.assertEqual(len(pages), 2)
        self.assertEqual(client.calls, ["report-events", "report-events"])
        self.assertEqual(client.variables[0]["startTime"], 0)
        self.assertEqual(client.variables[1]["startTime"], 200)
        self.assertEqual(client.variables[1]["limit"], 10000)

    def test_event_pagination_stops_at_null_cursor(self):
        client = SequenceClient([event_page([{"timestamp": 100}], None)])

        pages = list(warcraftlogs.iter_event_pages(client, "CODE", {"fightIDs": [7]}, 5))

        self.assertEqual(len(pages), 1)
        self.assertEqual(client.variables[0]["fightIDs"], [7])

    def test_event_pagination_stops_at_end_window(self):
        client = SequenceClient([event_page([{"timestamp": 100}], 1000)])

        pages = list(warcraftlogs.iter_event_pages(client, "CODE", {"startTime": 0, "endTime": 1000}, 5))

        self.assertEqual(len(pages), 1)
        self.assertEqual(len(client.calls), 1)

    def test_repeated_event_cursor_is_rejected(self):
        client = SequenceClient([
            event_page([{"timestamp": 100}], 200),
            event_page([{"timestamp": 200}], 200),
        ])
        with self.assertRaisesRegex(RuntimeError, "did not advance"):
            list(warcraftlogs.iter_event_pages(client, "CODE", {"startTime": 0, "endTime": 1000}, 5))

    def test_events_cli_surfaces_non_advancing_cursor_error(self):
        client = SequenceClient([
            fixture("report-events-page-1.json"),
            fixture("report-events-repeated-cursor.json"),
        ])
        output = io.StringIO()
        errors = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(output), redirect_stderr(errors), patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ):
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                str(Path(directory) / "missing.env"), "report", "events", "CODE1234", "--fight", "7",
            ])
        self.assertEqual(exit_code, 4)
        self.assertEqual(output.getvalue(), "")
        self.assertIn("did not advance", errors.getvalue())

    def test_events_cli_marks_max_page_truncation_and_fixture_round_trip(self):
        client = SequenceClient([fixture("report-events-page-1.json")])
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(output), patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ):
            path = Path(directory) / "events.jsonl"
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                str(Path(directory) / "missing.env"), "report", "events", "CODE1234", "--fight", "7",
                "--max-pages", "1", "--output", str(path),
            ])
            records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        envelope = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(envelope["pages_fetched"], 1)
        self.assertTrue(envelope["truncated"])
        self.assertEqual(records[0]["metadata"]["pagination"], {"pages_fetched": 1, "truncated": True})
        self.assertEqual(records[1]["event"]["timestamp"], 100)

    def test_events_cli_fixture_null_cursor_is_not_truncated(self):
        client = SequenceClient([fixture("report-events-page-2.json")])
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(output), patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ):
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                str(Path(directory) / "missing.env"), "report", "events", "CODE1234", "--fight", "7",
            ])
        envelope = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(envelope["pagination"], {"pages_fetched": 1, "truncated": False})

    def test_events_cli_fixture_end_cursor_is_not_truncated(self):
        client = SequenceClient([fixture("report-events-page-1.json")])
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(output), patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ):
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                str(Path(directory) / "missing.env"), "report", "events", "CODE1234", "--start-time", "0",
                "--end-time", "200",
            ])
        envelope = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(envelope["pagination"], {"pages_fetched": 1, "truncated": False})

    def test_event_pagination_honors_max_pages_and_preserves_partial_pages(self):
        client = SequenceClient([
            event_page([{"timestamp": 100}], 200),
            event_page([{"timestamp": 200}], 300),
            event_page([{"timestamp": 300}], 400),
        ])

        pages = list(warcraftlogs.iter_event_pages(client, "CODE", {"startTime": 0, "endTime": 1000}, 2))

        self.assertEqual([page["data"] for page in pages], [[{"timestamp": 100}], [{"timestamp": 200}]])
        self.assertEqual(len(client.calls), 2)

    def test_event_limit_must_be_between_100_and_10000(self):
        for limit in (99, 10001):
            with self.subTest(limit=limit), self.assertRaisesRegex(ValueError, "100.*10000"):
                list(warcraftlogs.iter_event_pages(
                    SequenceClient([]), "CODE", {"fightIDs": [7], "limit": limit}, 5
                ))

    def test_event_query_contains_documented_variables_and_fields(self):
        query = warcraftlogs.load_query("report-events")
        for value in (
            "$code", "$fightIDs", "$startTime", "$endTime", "$dataType", "$sourceID",
            "$targetID", "$abilityID", "$hostility", "$filterExpression", "$includeResources",
            "$useActorIDs", "$useAbilityIDs", "$limit", "nextPageTimestamp", "data",
        ):
            self.assertIn(value, query)

    def test_event_jsonl_is_metadata_first_and_round_trips(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            metadata = {"command": "report events", "pagination": {"pages_fetched": 2, "truncated": True}}
            events = [{"timestamp": 100, "ability": "é"}, {"timestamp": 200}]

            warcraftlogs.write_event_jsonl(path, metadata, events)

            records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(records[0], {"type": "metadata", "metadata": metadata})
        self.assertEqual([record["type"] for record in records[1:]], ["event", "event"])
        self.assertEqual([record["event"] for record in records[1:]], events)

    def test_events_cli_writes_jsonl_and_stdout_envelope(self):
        client = SequenceClient([event_page([{"timestamp": 100}], None)])
        output = io.StringIO()
        errors = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(output), redirect_stderr(errors), patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ):
            path = Path(directory) / "events.jsonl"
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                str(Path(directory) / "missing.env"), "report", "events", "CODE1234", "--fight", "7",
                "--output", str(path),
            ])
            records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

        envelope = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(errors.getvalue(), "")
        self.assertEqual(envelope["command"], "report events")
        self.assertEqual(envelope["records_written"], 1)
        self.assertEqual(envelope["output"], str(path))
        self.assertNotIn("data", envelope)
        self.assertEqual(records[0]["type"], "metadata")
        self.assertEqual(records[1], {"type": "event", "event": {"timestamp": 100}})

    def test_events_output_preserves_private_report_error(self):
        payload = fixture("report-events-page-2.json")
        report = payload["data"]["reportData"]["report"]
        report["visibility"] = "private"
        report["archiveStatus"] = {"isAccessible": False}
        client = SequenceClient([payload])
        output = io.StringIO()
        errors = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(output), redirect_stderr(errors), patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ):
            path = Path(directory) / "events.jsonl"
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                str(Path(directory) / "missing.env"), "report", "events", "CODE1234", "--fight", "7",
                "--output", str(path),
            ])
            self.assertFalse(path.exists())
        self.assertEqual(exit_code, 4)
        self.assertIn("public", errors.getvalue().lower())
        self.assertNotIn("write event output file", errors.getvalue().lower())
        self.assertEqual(output.getvalue(), "")

    def test_report_output_is_atomic_and_stdout_is_receipt(self):
        client = FixtureClient({"report-summary": fixture("report-summary.json")})
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(output), redirect_stderr(io.StringIO()), patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ):
            path = Path(directory) / "report.json"
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                str(Path(directory) / "missing.env"), "report", "summary", "CODE1234", "--output", str(path),
            ])
            payload = json.loads(path.read_text(encoding="utf-8"))
        receipt = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(payload["command"], "report summary")
        self.assertEqual(receipt, {
            "command": "report summary",
            "output": str(path),
            "records_written": 1,
            "pages_fetched": 1,
            "truncated": False,
        })

    def test_output_parent_must_exist_before_network_access(self):
        client = FixtureClient({"report-summary": fixture("report-summary.json")})
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()), patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ):
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                str(Path(directory) / "missing.env"), "report", "summary", "CODE1234",
                "--output", str(Path(directory) / "missing" / "report.json"),
            ])
        self.assertEqual(exit_code, 2)
        self.assertEqual(client.calls, [])


class DiscoveryTests(unittest.TestCase):
    def test_expansion_filter_defaults_to_unset_for_metadata_and_global(self):
        metadata_args = warcraftlogs.build_parser().parse_args(["metadata", "zones"])
        global_args = warcraftlogs.build_parser().parse_args([
            "find", "global", "--zone", "1300",
        ])
        self.assertIsNone(metadata_args.expansion_id)
        self.assertIsNone(global_args.expansion_id)

        client = FixtureClient({"metadata-world": fixture("metadata-world.json")})
        warcraftlogs._global_filters(global_args, client)
        self.assertEqual(client.variables, [{}])

        explicit_client = FixtureClient({"metadata-world": fixture("metadata-world.json")})
        explicit_args = warcraftlogs.build_parser().parse_args([
            "find", "global", "--zone", "1300", "--expansion-id", "11",
        ])
        warcraftlogs._global_filters(explicit_args, explicit_client)
        self.assertEqual(explicit_client.variables, [{"expansionId": 11}])

    def test_global_results_are_always_sampled(self):
        envelope = warcraftlogs.make_global_result([], sample_size=0, filters={"encounter": 123}, metric="playerspeed")
        self.assertEqual(envelope["completeness"], "sampled")
        self.assertIn("ranking_basis", envelope["scope"])
        self.assertEqual(envelope["scope"]["ranking_basis"], "encounter_rankings")
        self.assertEqual(envelope["scope"]["metric"], "playerspeed")
        self.assertEqual(envelope["ranking_metric"], "playerspeed")
        self.assertEqual(envelope["requested_top"], 0)
        self.assertEqual(envelope["source_rows"], 0)
        self.assertEqual(envelope["unique_candidates"], 0)
        self.assertEqual(envelope["returned_candidates"], 0)
        self.assertIn(
            "Global discovery is ranking-based and not an exhaustive list of public reports.",
            envelope["warnings"],
        )

    def test_global_rankings_query_exposes_documented_encounter_arguments(self):
        query = warcraftlogs.load_query("encounter-rankings")
        for value in ("$encounterID", "$zoneID", "$difficulty", "$partition", "$page", "$serverRegion", "$serverSlug", "$metric", "fightRankings"):
            self.assertIn(value, query)
        self.assertNotIn("$leaderboard", query)
        self.assertNotIn("$hardModeLevel", query)
        self.assertNotIn("leaderboard:", query)
        self.assertNotIn("hardModeLevel:", query)
        self.assertIn("zone(id: $zoneID)", query)
        self.assertNotIn("zoneID: $zoneID", query)
        self.assertNotIn("className: $className", query)
        self.assertNotIn("specName: $specName", query)
        self.assertNotIn("role: $role", query)
        self.assertNotIn("characterRankings", query)

    def test_global_leaderboard_is_rejected_before_api_call(self):
        client = FixtureClient({})
        with self.assertRaisesRegex(ValueError, "leaderboard.*not supported"):
            warcraftlogs.discover_global(
                client,
                warcraftlogs.DiscoveryFilters(encounter=2902, zone=1300),
                top=2,
                page=1,
                leaderboard="all",
            )
        self.assertEqual(client.calls, [])

    def test_global_cli_rejects_leaderboard_before_metadata_call(self):
        client = FixtureClient({})
        with tempfile.TemporaryDirectory() as directory, patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()) as errors:
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret",
                "--env-file", str(Path(directory) / "missing.env"),
                "find", "global", "--encounter", "2902", "--leaderboard", "all",
            ])
        self.assertEqual(exit_code, 2)
        self.assertIn("leaderboard", errors.getvalue().lower())
        self.assertEqual(client.calls, [])

    def test_global_error_only_ranking_is_sampled_with_sanitized_errors(self):
        client = FixtureClient({"encounter-rankings": {"errors": [{"message": "ranking unavailable", "path": ["worldData"], "extensions": {"code": "DOWN"}}]}})
        result = warcraftlogs.discover_global(client, warcraftlogs.DiscoveryFilters(encounter=2902, zone=1300), top=2, page=1)
        self.assertEqual(result["completeness"], "sampled")
        self.assertEqual(result["data"], [])
        self.assertEqual(result["errors"], [{"message": "ranking unavailable", "path": ["worldData"], "extensions": {"code": "DOWN"}}])
        self.assertEqual(result["requested_top"], 2)
        self.assertIn(warcraftlogs.GLOBAL_WARNING, result["warnings"])

    def test_global_ranking_candidates_accept_nested_report_fight_id_and_dedupe(self):
        rows, pagination = warcraftlogs._ranking_page(fixture("global-rankings-nested-report.json"))

        self.assertFalse(pagination["has_more_pages"])
        candidates = warcraftlogs._dedupe_global_candidates(rows)
        self.assertEqual([(item["report_code"], item["fight_id"]) for item in candidates], [("Nested001", 5)])
        self.assertEqual(warcraftlogs._invalid_ranking_key(rows[2]), ("report", "Nested002", "missing-fight"))

    def test_global_partial_hydration_failure_is_sampled(self):
        client = FixtureClient({
            "metadata-world": fixture("metadata-world.json"),
            "metadata-game": fixture("metadata-game.json"),
            "encounter-rankings": fixture("global-rankings-page-1.json"),
            "report-fights": {"errors": [{"message": "fight unavailable", "path": ["reportData"]}]},
        })
        result = warcraftlogs.discover_global(
            client, warcraftlogs.DiscoveryFilters(encounter=2902, key_min=12), top=2, page=1
        )
        self.assertEqual(result["completeness"], "sampled")
        self.assertTrue(result["partial"])
        self.assertEqual(result["errors"], [{"message": "fight unavailable", "path": ["reportData"]}] * 2)

    def test_global_fetches_until_unique_top_not_raw_duplicate_count(self):
        class Pages:
            def __init__(self):
                self.calls = []
                self.pages = [
                    {"data": {"worldData": {"encounter": {"fightRankings": json.dumps({"rankings": [{"reportID": "AbCd1234", "fightID": 9}], "page": 1, "hasMorePages": True})}}}},
                    {"data": {"worldData": {"encounter": {"fightRankings": json.dumps({"rankings": [{"reportID": "AbCd1234", "fightID": 9}, {"reportID": "EfGh5678", "fightID": 4}], "page": 2, "hasMorePages": False})}}}},
                ]

            def execute(self, query_name, variables):
                if query_name == "metadata-world":
                    return fixture("metadata-world.json")
                self.calls.append((query_name, dict(variables)))
                return self.pages.pop(0)

        client = Pages()
        result = warcraftlogs.discover_global(
            client, warcraftlogs.DiscoveryFilters(encounter=2902), top=2, page=1, max_pages=2
        )
        self.assertEqual(len(client.calls), 2)
        self.assertEqual(result["unique_candidates"], 2)
        self.assertEqual([item["report_code"] for item in result["data"]], ["AbCd1234", "EfGh5678"])

    def test_global_fetches_later_pages_after_filtered_first_page(self):
        class FilteredPages:
            def __init__(self):
                self.calls = []
                self.pages = [
                    {"data": {"worldData": {"encounter": {"fightRankings": json.dumps({
                        "rankings": [{"reportID": "Excluded001", "fightID": 1, "class": "Mage", "role": "dps"}],
                        "page": 1, "hasMorePages": True,
                    })}}}},
                    {"data": {"worldData": {"encounter": {"fightRankings": json.dumps({
                        "rankings": [{"reportID": "Allowed001", "fightID": 2, "class": "Paladin", "role": "tank"}],
                        "page": 2, "hasMorePages": False,
                    })}}}},
                ]

            def execute(self, query_name, variables):
                self.calls.append((query_name, dict(variables)))
                if query_name == "encounter-rankings":
                    return self.pages.pop(0)
                if query_name == "report-fights":
                    return {"data": {"reportData": {"report": {
                        "visibility": "public",
                        "archiveStatus": {"isAccessible": True},
                        "fights": [{"id": 2, "gameZone": {"id": 2335}, "friendlyPlayers": [1]}],
                    }}}}
                if query_name == "report-master-data":
                    return fixture("report-master-data.json")
                raise AssertionError(query_name)

        client = FilteredPages()
        result = warcraftlogs.discover_global(
            client,
            warcraftlogs.DiscoveryFilters(encounter=2902, zone=2335, class_name="Paladin", role="tank"),
            top=1, page=1, max_pages=2,
        )

        self.assertEqual([item["report_code"] for item in result["data"]], ["Allowed001"])
        self.assertEqual(len([call for call in client.calls if call[0] == "encounter-rankings"]), 2)

    def test_global_top_is_local_sample_bound_not_raid_size_filter(self):
        class RankingClient:
            def __init__(self):
                self.calls = []

            def execute(self, query_name, variables):
                self.calls.append((query_name, dict(variables)))
                return {
                    "data": {
                        "worldData": {
                            "encounter": {
                                "fightRankings": json.dumps({
                                    "rankings": [{"reportID": "AbCd1234", "fightID": 9}],
                                    "page": 1,
                                    "hasMorePages": False,
                                })
                            }
                        }
                    }
                }

        client = RankingClient()
        result = warcraftlogs.discover_global(
            client, warcraftlogs.DiscoveryFilters(encounter=2902, zone=1300), top=1, page=1
        )

        self.assertEqual(result["requested_top"], 1)
        self.assertEqual(client.calls[0][0], "encounter-rankings")
        self.assertNotIn("size", client.calls[0][1])

    def test_global_stops_hydrating_after_top_matches(self):
        class HydrationCountingClient:
            def __init__(self):
                self.calls = []

            def execute(self, query_name, variables):
                self.calls.append((query_name, dict(variables)))
                if query_name == "encounter-rankings":
                    return {
                        "data": {
                            "worldData": {
                                "encounter": {
                                    "fightRankings": json.dumps({
                                        "rankings": [
                                            {"reportID": "Match001", "fightID": 9},
                                            {"reportID": "Match002", "fightID": 9},
                                            {"reportID": "Match003", "fightID": 9},
                                        ],
                                        "page": 1,
                                        "hasMorePages": False,
                                    })
                                }
                            }
                        }
                    }
                if query_name == "report-fights":
                    return fixture("report-fights.json")
                raise AssertionError("unexpected query %s" % query_name)

        client = HydrationCountingClient()
        result = warcraftlogs.discover_global(
            client, warcraftlogs.DiscoveryFilters(encounter=2902, zone=2335, key_min=12), top=1, page=1
        )

        self.assertEqual(result["returned_candidates"], 1)
        self.assertEqual(result["hydrated_candidates"], 1)
        self.assertEqual(result["excluded_candidates"], 0)
        self.assertEqual([name for name, _ in client.calls if name == "report-fights"], ["report-fights"])

    def test_global_hydration_is_fight_scoped_and_zone_filter_uses_fight_game_zone(self):
        client = FixtureClient({
            "report-fights": fixture("report-fights.json"),
        })
        fights, actors = warcraftlogs.hydrate_discovery_report(
            client, "AbCd1234", warcraftlogs.DiscoveryFilters(zone=2335), fight_id=9
        )
        self.assertEqual(client.variables[0]["fightIDs"], [9])
        self.assertEqual([fight["id"] for fight in fights], [9])
        matched, reasons = warcraftlogs.report_matches(
            {}, fights, actors, warcraftlogs.DiscoveryFilters(zone=2335)
        )
        self.assertTrue(matched)
        self.assertEqual(reasons, [])

    def test_global_numeric_ids_are_scoped_by_metadata(self):
        client = FixtureClient({"metadata-world": fixture("metadata-world.json")})
        valid_args = warcraftlogs.build_parser().parse_args([
            "find", "global", "--zone", "1300", "--partition", "42",
        ])
        filters = warcraftlogs._global_filters(valid_args, client)
        self.assertEqual(filters.zone, 1300)
        self.assertEqual(filters.encounter, 2902)
        self.assertEqual(filters.partition, 42)
        invalid_args = warcraftlogs.build_parser().parse_args([
            "find", "global", "--zone", "1300", "--partition", "999",
        ])
        with self.assertRaisesRegex(ValueError, "partition"):
            warcraftlogs._global_filters(invalid_args, client)

    def test_global_numeric_class_and_spec_ids_are_validated_by_game_metadata(self):
        client = FixtureClient({
            "metadata-world": fixture("metadata-world.json"),
            "metadata-game": fixture("metadata-game.json"),
        })
        args = warcraftlogs.build_parser().parse_args([
            "find", "global", "--encounter", "2902", "--class-name", "2", "--spec-name", "66",
        ])
        filters = warcraftlogs._global_filters(args, client)
        self.assertEqual(filters.class_name, "Paladin")
        self.assertEqual(filters.spec_name, "Protection")

        encounter_args = warcraftlogs.build_parser().parse_args(["find", "global", "--encounter", "2902"])
        encounter_filters = warcraftlogs._global_filters(encounter_args, client)
        self.assertEqual(encounter_filters.encounter, 2902)

    def test_global_invalid_bounds_make_no_metadata_calls(self):
        client = FixtureClient({})
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ), patch.dict(os.environ, {}, clear=True), redirect_stdout(output), redirect_stderr(io.StringIO()):
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                str(Path(directory) / "missing.env"), "find", "global", "--zone", "Midnight Dungeon",
                "--top", "0",
            ])
        self.assertEqual(exit_code, 2)
        self.assertEqual(client.calls, [])

    def test_global_rejects_fightless_candidates_before_hydration(self):
        class NoReportWideHydrationClient(FixtureClient):
            def execute(self, query_name, variables):
                if query_name == "report-fights" and "fightIDs" not in variables:
                    raise AssertionError("global discovery attempted report-wide hydration")
                return super().execute(query_name, variables)

        client = NoReportWideHydrationClient({
            "encounter-rankings": fixture("global-rankings-no-fight.json"),
            "report-fights": fixture("report-fights.json"),
        })
        result = warcraftlogs.discover_global(
            client, warcraftlogs.DiscoveryFilters(encounter=2902, zone=2335, key_min=12), top=2, page=1
        )
        self.assertEqual(result["source_rows"], 2)
        self.assertEqual(result["unique_candidates"], 1)
        self.assertEqual(result["excluded_candidates"], 1)
        self.assertEqual(result["hydrated_candidates"], 1)
        self.assertEqual(client.variables[1]["fightIDs"], [9])

    def test_global_invalid_key_and_time_bounds_make_no_metadata_calls(self):
        for options in (("--key-min", "20", "--key-max", "10"), ("--start-time", "20", "--end-time", "10")):
            client = FixtureClient({})
            with tempfile.TemporaryDirectory() as directory, patch.object(
                warcraftlogs, "WarcraftLogsClient", return_value=client
            ), patch.dict(os.environ, {}, clear=True), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                exit_code = warcraftlogs.main([
                    "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                    str(Path(directory) / "missing.env"), "find", "global", "--zone", "Midnight Dungeon",
                    *options,
                ])
            self.assertEqual(exit_code, 2)
            self.assertEqual(client.calls, [])

    def test_global_duplicate_fightless_rows_count_as_one_excluded_candidate(self):
        client = FixtureClient({
            "encounter-rankings": fixture("global-rankings-duplicate-no-fight.json"),
            "report-fights": fixture("report-fights.json"),
        })
        result = warcraftlogs.discover_global(
            client, warcraftlogs.DiscoveryFilters(encounter=2902, zone=2335), top=2, page=1
        )
        self.assertEqual(result["source_rows"], 3)
        self.assertEqual(result["unique_candidates"], 1)
        self.assertEqual(result["excluded_candidates"], 1)
        self.assertLessEqual(result["excluded_candidates"], result["source_rows"])

    def test_global_cli_requires_zone_instance_or_encounter(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
            warcraftlogs.build_parser().parse_args(["find", "global"])
        self.assertEqual(raised.exception.code, 2)

    def test_global_cli_extracts_candidates_dedupes_and_hydrates_derived_filters(self):
        client = FixtureClient({
            "metadata-world": fixture("metadata-world.json"),
            "metadata-game": fixture("metadata-game.json"),
            "encounter-rankings": fixture("global-rankings-page-1.json"),
            "report-fights": fixture("report-fights.json"),
            "report-master-data": fixture("report-master-data.json"),
        })
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ), patch.dict(os.environ, {}, clear=True), redirect_stdout(output):
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                str(Path(directory) / "missing.env"), "find", "global", "--encounter", "2902",
                "--class-name", "Paladin", "--spec-name", "Protection", "--role", "tank",
                "--partition", "42", "--difficulty", "8", "--key-min", "12", "--top", "2",
                "--page", "1",
            ])
        result = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(client.calls, ["metadata-world", "metadata-game", "metadata-world", "encounter-rankings", "report-fights", "report-master-data"])
        self.assertEqual(client.variables[3]["encounterID"], 2902)
        self.assertEqual(client.variables[3]["partition"], 42)
        self.assertEqual(client.variables[3]["difficulty"], 8)
        self.assertEqual(result["completeness"], "sampled")
        self.assertEqual(result["source_rows"], 3)
        self.assertEqual(result["unique_candidates"], 2)
        self.assertEqual(result["hydrated_candidates"], 1)
        self.assertEqual(result["returned_candidates"], 1)
        self.assertEqual(result["data"][0]["matched_actor"]["name"], "Tankadin")
        self.assertEqual(result["data"][0]["matched_actor"]["match_source"], "unique_group_match")

    def test_global_cli_bounds_top_and_page_before_execute(self):
        for option, value in (("--top", "0"), ("--top", "101"), ("--page", "0")):
            client = FixtureClient({"encounter-rankings": fixture("global-rankings-page-1.json")})
            with tempfile.TemporaryDirectory() as directory, patch.object(
                warcraftlogs, "WarcraftLogsClient", return_value=client
            ), patch.dict(os.environ, {}, clear=True), redirect_stderr(io.StringIO()):
                exit_code = warcraftlogs.main([
                    "--client-id", "client-id", "--client-secret", "client-secret", "--env-file",
                    str(Path(directory) / "missing.env"), "find", "global", "--encounter", "2902",
                    option, value,
                ])
            self.assertEqual(exit_code, 2)
            self.assertEqual(client.calls, [])

    def test_global_latest_is_rejected_before_api_call(self):
        args = warcraftlogs.build_parser().parse_args([
            "find", "global", "--zone", "1300", "--latest", "1",
        ])
        self.assertEqual(args.latest, 1)

        client = FixtureClient({})
        errors = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ), patch.dict(os.environ, {}, clear=True), redirect_stderr(errors):
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret",
                "--env-file", str(Path(directory) / "missing.env"),
                "find", "global", "--zone", "1300", "--latest", "1",
            ])

        self.assertEqual(exit_code, 2)
        self.assertIn("global", errors.getvalue().lower())
        self.assertIn("latest", errors.getvalue().lower())
        self.assertEqual(client.calls, [])

    def test_global_empty_fixture_keeps_sample_contract(self):
        client = FixtureClient({
            "metadata-world": fixture("metadata-world.json"),
            "encounter-rankings": fixture("global-rankings-empty.json"),
        })
        result = warcraftlogs.discover_global(
            client, warcraftlogs.DiscoveryFilters(encounter=2902), top=10, page=1
        )
        self.assertEqual(result["data"], [])
        self.assertEqual(result["completeness"], "sampled")
        self.assertEqual(result["source_rows"], 0)
        self.assertEqual(result["unique_candidates"], 0)
        self.assertEqual(result["pages_fetched"], 1)

    def test_global_zone_name_resolves_through_metadata(self):
        client = FixtureClient({
            "metadata-world": fixture("metadata-world.json"),
            "encounter-rankings": fixture("global-rankings-empty.json"),
        })
        args = warcraftlogs.build_parser().parse_args(["find", "global", "--zone", "Midnight Dungeon"])
        filters = warcraftlogs._global_filters(args, client)
        result = warcraftlogs.discover_global(client, filters, top=1, page=1)
        self.assertEqual(filters.zone, 1300)
        self.assertEqual(filters.encounter, 2902)
        self.assertEqual(client.variables[0], {})
        self.assertEqual(result["completeness"], "sampled")

    def test_report_matches_returns_deterministic_derived_exclusion_reasons(self):
        filters = warcraftlogs.DiscoveryFilters(
            class_name="Paladin", spec_name="Protection", role="tank",
            encounter=2902, difficulty=10, key_min=15, timed=True, kill=True,
        )
        matched, reasons = warcraftlogs.report_matches(
            {"code": "NOPE"},
            [{"encounterID": 1, "difficulty": 3, "kill": False, "keystoneLevel": 12}],
            [{"subType": "FireMage", "type": "Player"}],
            filters,
        )
        self.assertFalse(matched)
        self.assertEqual(
            reasons,
            ["class_name", "spec_name", "role", "encounter", "key_min", "timed", "difficulty", "kill"],
        )

    def test_report_fights_query_requests_scalar_keystone_affixes(self):
        query = warcraftlogs.load_query("report-fights")
        self.assertIn("keystoneAffixes", query)
        self.assertNotIn("keystoneAffixes {", query)

    def test_season_and_partition_are_rejected_before_discovery_query(self):
        for option in ("--season", "--partition"):
            client = FixtureClient({"guild-reports": fixture("find-guild-page-1.json")})
            errors = io.StringIO()
            with tempfile.TemporaryDirectory() as directory, patch.object(
                warcraftlogs, "WarcraftLogsClient", return_value=client
            ), patch.dict(os.environ, {}, clear=True), redirect_stderr(errors):
                exit_code = warcraftlogs.main([
                    "--client-id", "client-id", "--client-secret", "client-secret",
                    "--env-file", str(Path(directory) / "missing.env"), "find", "guild",
                    "--name", "Fixture Guild", "--server", "Area 52", "--region", "us",
                    option, "1",
                ])
            self.assertEqual(exit_code, 2)
            self.assertEqual(client.calls, [])
            self.assertIn("cannot", errors.getvalue().lower())

    def test_discovery_limit_is_between_one_and_one_hundred_before_execute(self):
        for limit in (0, 101):
            client = FixtureClient({"guild-reports": fixture("find-guild-page-1.json")})
            with tempfile.TemporaryDirectory() as directory, patch.object(
                warcraftlogs, "WarcraftLogsClient", return_value=client
            ), patch.dict(os.environ, {}, clear=True), redirect_stderr(io.StringIO()):
                exit_code = warcraftlogs.main([
                    "--client-id", "client-id", "--client-secret", "client-secret",
                    "--env-file", str(Path(directory) / "missing.env"), "find", "guild",
                    "--name", "Fixture Guild", "--server", "Area 52", "--region", "us",
                    "--limit", str(limit),
                ])
            self.assertEqual(exit_code, 2)
            self.assertEqual(client.calls, [])

    def test_keystone_timed_and_depleted_require_level_and_bonus(self):
        filters = warcraftlogs.DiscoveryFilters(timed=True)
        timed, timed_reasons = warcraftlogs.report_matches(
            {}, [{"keystoneLevel": 10, "keystoneBonus": 1, "kill": True, "inProgress": False}], [], filters
        )
        self.assertTrue(timed)
        self.assertEqual(timed_reasons, [])
        depleted, depleted_reasons = warcraftlogs.report_matches(
            {}, [{"keystoneLevel": 10, "keystoneBonus": 0, "kill": True, "inProgress": False}], [], warcraftlogs.DiscoveryFilters(depleted=True)
        )
        self.assertTrue(depleted)
        self.assertEqual(depleted_reasons, [])
        null_bonus, null_reasons = warcraftlogs.report_matches(
            {}, [{"keystoneLevel": 10, "keystoneBonus": None, "kill": True, "inProgress": False}], [], filters
        )
        self.assertFalse(null_bonus)
        self.assertEqual(null_reasons, ["timed"])

    def test_fight_status_requires_completed_positive_key(self):
        from warcraftlogs_core import models

        self.assertEqual(
            models._fight_status({"keystoneLevel": 6, "keystoneBonus": 1, "kill": True, "inProgress": False}),
            (True, False),
        )
        self.assertEqual(
            models._fight_status({"keystoneLevel": 6, "keystoneBonus": 0, "kill": True, "inProgress": False}),
            (False, True),
        )
        for fight in (
            {"keystoneLevel": 6, "keystoneBonus": 1, "kill": False, "inProgress": True},
            {"keystoneLevel": 6, "keystoneBonus": 0, "kill": False, "inProgress": False},
            {"keystoneLevel": 0, "keystoneBonus": 2, "kill": True, "inProgress": False},
        ):
            with self.subTest(fight=fight):
                self.assertEqual(models._fight_status(fight), (False, False))

    def test_character_filters_use_canonical_actor_name(self):
        filters = warcraftlogs.DiscoveryFilters(class_name="Paladin")
        report = {"code": "X"}
        fights = [{"friendlyPlayers": [1, 2]}]
        actors = [
            {"id": 1, "name": "Tankadin", "subType": "ProtectionPaladin"},
            {"id": 2, "name": "Otheradin", "subType": "ProtectionPaladin"},
        ]
        matched, reasons = warcraftlogs.report_matches(report, fights, actors, filters, "Tankadin")
        self.assertTrue(matched)
        self.assertEqual(reasons, [])
        matched, reasons = warcraftlogs.report_matches(report, fights, actors, filters, "Missing")
        self.assertFalse(matched)
        self.assertIn("character_identity", reasons)

    def test_guild_discovery_pushes_direct_filters_and_skips_hydration(self):
        client = FixtureClient({"guild-reports": fixture("find-guild-page-1.json")})
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ), patch.dict(os.environ, {}, clear=True), redirect_stdout(output):
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret",
                "--env-file", str(Path(directory) / "missing.env"), "find", "guild",
                "--name", "Fixture Guild", "--server", "Area 52", "--region", "us",
                "--zone", "2335", "--start-time", "1000", "--end-time", "2000",
                "--page", "2", "--limit", "25",
            ])
        result = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(client.calls, ["guild-reports"])
        self.assertEqual(client.variables[0]["guildName"], "Fixture Guild")
        self.assertEqual(client.variables[0]["guildServerSlug"], "area-52")
        self.assertEqual(client.variables[0]["guildServerRegion"], "us")
        self.assertEqual(client.variables[0]["gameZoneID"], 2335)
        self.assertEqual(client.variables[0]["startTime"], 1000.0)
        self.assertEqual(client.variables[0]["endTime"], 2000.0)
        self.assertEqual(client.variables[0]["page"], 2)
        self.assertEqual(client.variables[0]["limit"], 25)
        self.assertEqual(result["hydrated_count"], 0)
        self.assertEqual(result["pagination"]["current_page"], 2)
        self.assertEqual(result["completeness"], "api_collection")

    def test_character_discovery_requires_all_identity_inputs(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
            warcraftlogs.build_parser().parse_args(["find", "character", "--name", "Tankadin"])
        self.assertEqual(raised.exception.code, 2)

    def test_character_discovery_preserves_report_order_without_latest(self):
        payload = {
            "data": {
                "characterData": {
                    "character": {
                        "name": "Tankadin",
                        "server": {"name": "Area 52", "slug": "area-52", "region": {"name": "US", "slug": "us"}},
                        "recentReports": {
                            "data": [
                                {"code": "Older000", "title": "Older run", "startTime": 1000, "endTime": 2000},
                                {"code": "Newer000", "title": "Newer run", "startTime": 3000},
                            ],
                            "current_page": 1,
                            "last_page": 1,
                            "has_more_pages": False,
                        },
                    }
                }
            }
        }
        client = FixtureClient({"character": payload, "character-reports": payload})
        result = warcraftlogs.discover_reports(
            client,
            "character",
            {"name": "Tankadin", "serverSlug": "area-52", "serverRegion": "us"},
            warcraftlogs.DiscoveryFilters(),
            page=1,
            limit=100,
        )

        self.assertEqual([report["code"] for report in result["data"]], ["Older000", "Newer000"])
        self.assertNotIn("latest", result)

    def test_character_discovery_latest_selects_newest_report_and_stays_local(self):
        payload = {
            "data": {
                "characterData": {
                    "character": {
                        "name": "Tankadin",
                        "server": {"name": "Area 52", "slug": "area-52", "region": {"name": "US", "slug": "us"}},
                        "recentReports": {
                            "data": [
                                {"code": "Older000", "title": "Older run", "startTime": 1000, "endTime": 2000},
                                {"code": "Newer000", "title": "Newer run", "startTime": 3000},
                            ],
                            "current_page": 1,
                            "last_page": 1,
                            "has_more_pages": False,
                        },
                    }
                }
            }
        }
        client = FixtureClient({"character": payload, "character-reports": payload})
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ), patch.dict(os.environ, {}, clear=True), redirect_stdout(output):
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret",
                "--env-file", str(Path(directory) / "missing.env"), "find", "character",
                "--name", "Tankadin", "--server", "Area 52", "--region", "US",
                "--latest", "1",
            ])

        result = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(result["filters"]["latest"], 1)
        self.assertEqual([report["code"] for report in result["data"]], ["Newer000"])
        self.assertEqual(result["matched_count"], 2)
        self.assertEqual(result["excluded_count"], 0)
        self.assertEqual(result["selected_count"], 1)
        self.assertEqual(client.variables[1], {
            "name": "Tankadin", "serverSlug": "area-52", "serverRegion": "us", "limit": 100, "page": 1,
        })
        self.assertNotIn("latest", client.variables[1])

    def test_character_discovery_latest_preserves_match_counts(self):
        payload = {
            "data": {
                "characterData": {
                    "character": {
                        "name": "Tankadin",
                        "server": {"name": "Area 52", "slug": "area-52", "region": {"name": "US", "slug": "us"}},
                        "recentReports": {
                            "data": [
                                {"code": "Older000", "title": "Older run", "startTime": 1000, "endTime": 2000},
                                {"code": "Newer000", "title": "Newer run", "startTime": 3000},
                            ],
                            "current_page": 1,
                            "last_page": 1,
                            "has_more_pages": False,
                        },
                    }
                }
            }
        }
        client = FixtureClient({"character": payload, "character-reports": payload})
        result = warcraftlogs.discover_reports(
            client,
            "character",
            {"name": "Tankadin", "serverSlug": "area-52", "serverRegion": "us"},
            warcraftlogs.DiscoveryFilters(),
            page=1,
            limit=100,
            latest=1,
        )

        self.assertEqual([report["code"] for report in result["data"]], ["Newer000"])
        self.assertEqual(result["matched_count"], 2)
        self.assertEqual(result["excluded_count"], 0)
        self.assertEqual(result["selected_count"], 1)

    def test_character_discovery_uses_canonical_identity_and_report_page(self):
        payload = fixture("find-character-page-1.json")
        client = FixtureClient({"character": payload, "character-reports": payload})
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, patch.object(
            warcraftlogs, "WarcraftLogsClient", return_value=client
        ), patch.dict(os.environ, {}, clear=True), redirect_stdout(output):
            exit_code = warcraftlogs.main([
                "--client-id", "client-id", "--client-secret", "client-secret",
                "--env-file", str(Path(directory) / "missing.env"), "find", "character",
                "--name", "Tankadin", "--server", "Area 52", "--region", "US",
            ])
        result = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(client.calls, ["character", "character-reports"])
        self.assertEqual(client.variables[1], {
            "name": "Tankadin", "serverSlug": "area-52", "serverRegion": "us", "limit": 100, "page": 1,
        })
        self.assertEqual(result["data"][0]["code"], "Char1234")

    def test_derived_filter_hydrates_fights_and_master_data(self):
        client = FixtureClient({
            "report-fights": fixture("report-fights.json"),
            "report-master-data": fixture("report-master-data.json"),
        })
        fights, actors = warcraftlogs.hydrate_discovery_report(
            client, "AbCd1234", warcraftlogs.DiscoveryFilters(class_name="Paladin")
        )
        self.assertEqual(client.calls, ["report-fights", "report-master-data"])
        self.assertEqual(fights[0]["id"], 9)
        self.assertEqual(actors[0]["name"], "Tankadin")


def fixture(name):
    return json.loads((Path(__file__).parent / "fixtures" / name).read_text(encoding="utf-8"))


class FixtureClient:
    def __init__(self, payloads):
        self.payloads = payloads
        self.calls = []
        self.variables = []

    def execute(self, query_name, variables):
        self.calls.append(query_name)
        self.variables.append(dict(variables))
        return self.payloads[query_name]

import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


TESTS = Path(__file__).parent
SCRIPT = TESTS.parent / "scripts" / "warcraftlogs_live_check.py"
SPEC = importlib.util.spec_from_file_location("warcraftlogs_live_check", SCRIPT)
live_check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(live_check)


class NoNetworkClient:
    def __init__(self):
        self.calls = []

    def execute(self, query_name, variables):
        self.calls.append((query_name, variables))
        raise AssertionError("network call attempted")


class LiveCheckArgumentTests(unittest.TestCase):
    def test_parser_accepts_report_and_fight(self):
        args = live_check.build_parser().parse_args(["--report", "Public001", "--fight", "42"])

        self.assertEqual(args.report, "Public001")
        self.assertEqual(args.fight, 42)

    def test_run_refuses_without_explicit_opt_in(self):
        client = NoNetworkClient()
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            status = live_check.run({}, client=client)

        self.assertEqual(status, 0)
        self.assertIn("not enabled", output.getvalue().lower())
        self.assertEqual(client.calls, [])


class LiveCheckSafetyTests(unittest.TestCase):
    def test_api_error_never_prints_credential_or_payload(self):
        secret = "super-secret-client-value"

        class FailingClient:
            def execute(self, query_name, variables):
                raise live_check.ApiError(
                    'HTTP 401: ' + secret + ' {"access_token":"' + secret + '"}'
                )

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = live_check.run(
                {
                    "WARCRAFTLOGS_LIVE_CHECK": "1",
                    "WARCRAFTLOGS_CLIENT_ID": "client-id",
                    "WARCRAFTLOGS_CLIENT_SECRET": secret,
                    "WARCRAFTLOGS_TEST_REPORT": "Public001",
                    "WARCRAFTLOGS_TEST_FIGHT": "42",
                },
                client=FailingClient(),
            )

        text = output.getvalue()
        self.assertNotEqual(status, 0)
        self.assertNotIn(secret, text)
        self.assertNotIn("access_token", text)
        self.assertIn("API error", text)

    def test_smoke_uses_bounded_contract_calls(self):
        client = FakeClient()
        output = io.StringIO()
        environment = {
            "WARCRAFTLOGS_LIVE_CHECK": "1",
            "WARCRAFTLOGS_CLIENT_ID": "client-id",
            "WARCRAFTLOGS_CLIENT_SECRET": "client-secret",
            "WARCRAFTLOGS_TEST_REPORT": "Public001",
            "WARCRAFTLOGS_TEST_FIGHT": "42",
        }

        with contextlib.redirect_stdout(output):
            status = live_check.run(environment, client=client)

        self.assertEqual(status, 0)
        self.assertEqual(
            [call[0] for call in client.calls],
            ["__introspection__", "report-fights", "report-player-details", "report-table", "report-graph", "report-events"],
        )
        events = client.variables["report-events"]
        self.assertEqual(events["fightIDs"], [42])
        self.assertEqual(events["limit"], 100)
        self.assertNotIn("startTime", events)
        self.assertNotIn("endTime", events)


class FakeClient:
    def __init__(self):
        self.calls = []
        self.variables = {}

    def execute(self, query_name, variables):
        self.calls.append((query_name, variables))
        self.variables[query_name] = dict(variables)
        if query_name == "__introspection__":
            return live_check.required_schema_fixture()
        if query_name == "report-fights":
            return {"data": {"reportData": {"report": {"fights": [{"id": 42}]}}}}
        if query_name == "report-player-details":
            return {"data": {"reportData": {"report": {"playerDetails": {"players": [{"id": 1}]}}}}}
        if query_name in ("report-table", "report-graph"):
            return {"data": {"reportData": {"report": {query_name[7:]: {"data": []}}}}}
        if query_name == "report-events":
            return {"data": {"reportData": {"report": {"events": {"data": [], "nextPageTimestamp": None}}}}}
        raise AssertionError(query_name)


if __name__ == "__main__":
    unittest.main()

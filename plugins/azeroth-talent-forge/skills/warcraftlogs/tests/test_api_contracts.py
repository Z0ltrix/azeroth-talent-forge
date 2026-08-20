import json
import importlib.util
import tempfile
import unittest
from pathlib import Path

TESTS = Path(__file__).parent
SCRIPT = TESTS.parent / "scripts" / "warcraftlogs.py"
SPEC = importlib.util.spec_from_file_location("warcraftlogs_contract_cli", SCRIPT)
warcraftlogs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(warcraftlogs)


def agent_analysis_service(test_case):
    service = getattr(warcraftlogs, "agent_analysis", None)
    if service is None:
        test_case.fail("agent-analysis service is not implemented")
    return service


def fixture(name):
    return json.loads((TESTS / "fixtures" / name).read_text(encoding="utf-8"))


class QueryContractTests(unittest.TestCase):
    def test_fights_query_requests_agent_analysis_fields(self):
        query = warcraftlogs.load_query("report-fights")

        for field in (
            "gameZone", "rating", "averageItemLevel", "friendlyItemLevels",
            "dungeonPulls", "maps", "boundingBox", "friendlyPlayers",
            "friendlyPets", "friendlyNPCs",
        ):
            self.assertIn(field, query)

    def test_player_details_query_requests_combatant_info(self):
        query = warcraftlogs.load_query("report-player-details")
        self.assertIn("includeCombatantInfo: true", query)

    def test_events_query_uses_current_filter_contract(self):
        query = warcraftlogs.load_query("report-events")
        self.assertIn("$abilityID: Float", query)
        self.assertIn("hostilityType", query)
        self.assertNotIn("hostility:", query)

    def test_table_and_graph_queries_do_not_request_removed_filters(self):
        for name in ("report-table", "report-graph"):
            with self.subTest(name=name):
                query = warcraftlogs.load_query(name)
                for field in ("sourcePetType", "sourceSpec", "targetPetType", "targetSpec"):
                    self.assertNotIn(field, query)


class AgentAnalysisContractTests(unittest.TestCase):
    def test_fight_times_are_absolute_and_boundary_crossing_fight_is_retained(self):
        payload = fixture("report-fights-rich.json")

        fights = agent_analysis_service(self).normalize_fights(payload, report_start_time=1_000_000)

        self.assertEqual(fights[0]["startTime"], 1_010_000)
        self.assertEqual(fights[0]["endTime"], 1_070_000)
        self.assertEqual(fights[1]["startTime"], 1_065_000)
        self.assertEqual(fights[1]["endTime"], 1_085_000)

    def test_combatant_fields_are_preserved(self):
        payload = fixture("report-player-details-combatant.json")

        players = agent_analysis_service(self).normalize_combatant_details(payload)

        self.assertEqual(
            players[0],
            {
                "id": 7,
                "name": "Shieldbearer",
                "gear": [{"id": 1001, "itemLevel": 639}],
                "stats": {"strength": 1200, "stamina": 2400},
                "specIDs": [73],
                "talentTree": {"class": "Warrior", "spec": "Protection"},
                "talents": [{"id": 8001, "rank": 1}],
            },
        )

    def test_cohort_match_requires_ranked_actor_and_returns_unique_match(self):
        candidates = [
            {"id": 1, "name": "Ranked Mage", "className": "Mage", "role": "DPS", "ranked": True},
            {"id": 2, "name": "Ranked Rogue", "className": "Rogue", "role": "DPS", "ranked": True},
            {"id": 3, "name": "Ranked Priest", "className": "Priest", "role": "Healer", "ranked": True},
            {"id": 4, "name": "Ranked Hunter", "className": "Hunter", "role": "DPS", "ranked": True},
            {"id": 5, "name": "Unranked Warrior", "className": "Warrior", "role": "Tank", "ranked": False},
        ]

        service = agent_analysis_service(self)
        self.assertIsNone(service.match_cohort_actor(candidates, "Warrior", "Tank"))
        candidates[4]["ranked"] = True
        self.assertEqual(
            service.match_cohort_actor(candidates, "Warrior", "Tank"),
            candidates[4],
        )


class JsonlContractTests(unittest.TestCase):
    def test_jsonl_is_metadata_plus_one_record_per_event_without_embedded_events(self):
        metadata = {"report_code": "Rich001", "pagination": {"pages_fetched": 1}}
        events = fixture("report-events-single-page.json")["data"]["reportData"]["report"]["events"]["data"]

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            warcraftlogs.write_event_jsonl(path, metadata, events)
            records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

        self.assertEqual(len(records), 1 + len(events))
        self.assertEqual(records[0]["type"], "metadata")
        self.assertNotIn("events", records[0]["metadata"])
        self.assertEqual([record["type"] for record in records[1:]], ["event"] * len(events))

    def test_jsonl_write_failure_preserves_existing_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            path.write_text("old destination\n", encoding="utf-8")

            def failing_events():
                yield {"timestamp": 1}
                raise OSError("simulated output failure")

            with self.assertRaises(OSError):
                warcraftlogs.write_event_jsonl(path, {"report_code": "Rich001"}, failing_events())
            self.assertEqual(path.read_text(encoding="utf-8"), "old destination\n")


if __name__ == "__main__":
    unittest.main()

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

        fights = warcraftlogs.report_data(payload, "fights")

        self.assertEqual(fights[0]["startTime"], 1_010_000)
        self.assertEqual(fights[0]["endTime"], 1_070_000)
        self.assertEqual(fights[1]["startTime"], 1_065_000)
        self.assertEqual(fights[1]["endTime"], 1_085_000)

    def test_combatant_fields_are_preserved(self):
        payload = fixture("report-player-details-combatant.json")

        players = warcraftlogs.report_data(payload, "player-details")["players"]

        for field in ("gear", "stats", "specIDs", "talentTree", "talents"):
            with self.subTest(field=field):
                self.assertIn(field, players[0])

    def test_cohort_match_requires_ranked_actor_and_returns_unique_match(self):
        candidates = [
            {"id": 1, "name": "Ranked Mage", "className": "Mage", "role": "DPS", "ranked": True},
            {"id": 2, "name": "Ranked Rogue", "className": "Rogue", "role": "DPS", "ranked": True},
            {"id": 3, "name": "Ranked Priest", "className": "Priest", "role": "Healer", "ranked": True},
            {"id": 4, "name": "Ranked Hunter", "className": "Hunter", "role": "DPS", "ranked": True},
            {"id": 5, "name": "Unranked Warrior", "className": "Warrior", "specName": "Protection", "role": "Tank", "ranked": False},
        ]

        filters = warcraftlogs.DiscoveryFilters(
            encounter=1, zone=2335, class_name="Warrior", role="Tank"
        )
        excluded = warcraftlogs.discover_global(DiscoveryClient(discovery_actors(candidates)), filters, top=1, page=1)
        self.assertEqual(excluded["data"], [])
        self.assertGreaterEqual(excluded["excluded_candidates"], 1)

        candidates[4]["ranked"] = True
        matched = warcraftlogs.discover_global(DiscoveryClient(discovery_actors(candidates)), filters, top=1, page=1)
        candidate = matched["data"][0]
        self.assertEqual(candidate["matched_actor"], {
            "id": 5,
            "name": "Unranked Warrior",
            "class": "Warrior",
            "spec": "Protection",
            "role": "Tank",
            "match_source": "ranked_group_member",
        })

        ambiguous_candidates = candidates + [
            {"id": 6, "name": "Second Warrior", "className": "Warrior", "specName": "Protection", "role": "Tank", "ranked": True},
        ]
        ambiguous = warcraftlogs.discover_global(
            DiscoveryClient(discovery_actors(ambiguous_candidates), friendly_players=[1, 2, 3, 4, 5, 6]),
            filters,
            top=1,
            page=1,
        )
        self.assertEqual(ambiguous["data"], [])
        self.assertGreaterEqual(ambiguous["excluded_candidates"], 1)


class DiscoveryClient:
    def __init__(self, actors, friendly_players=None):
        self.actors = actors
        self.friendly_players = friendly_players or [1, 2, 3, 4, 5]

    def execute(self, query_name, variables):
        if query_name == "encounter-rankings":
            rankings = {
                "rankings": [{"rank": 1, "reportID": "Cohort001", "fightID": 7}],
                "page": 1,
                "hasMorePages": False,
            }
            return {"data": {"worldData": {"encounter": {"fightRankings": json.dumps(rankings)}}}}
        if query_name == "report-fights":
            return {"data": {"reportData": {"report": {
                "visibility": "public",
                "archiveStatus": {"isAccessible": True},
                "fights": [{"id": 7, "gameZone": {"id": 2335}, "friendlyPlayers": self.friendly_players}],
            }}}}
        if query_name == "report-master-data":
            return {"data": {"reportData": {"report": {
                "visibility": "public",
                "archiveStatus": {"isAccessible": True},
                "masterData": {"actors": self.actors},
            }}}}
        raise AssertionError(query_name)


def discovery_actors(candidates):
    actors = []
    for index, candidate in enumerate(candidates, 1):
        actor = dict(candidate)
        actor["id"] = index
        actor["subType"] = "ProtectionWarrior" if candidate["className"] == "Warrior" else candidate["className"]
        actors.append(actor)
    return actors


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

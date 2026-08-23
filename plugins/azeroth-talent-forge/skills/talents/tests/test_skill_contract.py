import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class SkillContractTests(unittest.TestCase):
    def test_release_manifest_and_old_skill_migration(self):
        manifest = json.loads((ROOT.parents[1] / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], "1.0.3")
        self.assertFalse((ROOT.parent / "wowhead-talent-planner").exists())

    def test_skill_is_named_talents_and_routes_every_public_operation(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: talents", text)
        self.assertIn("Runtime\nnetwork access is forbidden", text)
        for feature in ("import-export", "inspect", "validate", "compare", "modify", "generate", "presets", "patch-assets", "errors"):
            self.assertIn(f"references/features/", text)
            self.assertTrue(feature in text or feature.replace("-", " ") in text)
        for command in ("assets info", "inspect", "validate", "compare", "modify", "generate", "presets list"):
            self.assertIn(command, text)

    def test_feature_references_are_specific_not_generator_boilerplate(self):
        feature_dir = ROOT / "references" / "features"
        docs = {path.stem: path.read_text(encoding="utf-8") for path in feature_dir.glob("*.md")}
        self.assertEqual(set(docs), {"import-export", "inspect", "validate", "compare", "modify", "generate", "presets", "patch-assets", "errors"})
        self.assertTrue(all(len(body.splitlines()) >= 10 for body in docs.values()))
        self.assertNotEqual(len({body for body in docs.values()}), 1)
        self.assertTrue(any("NO_FEASIBLE_BUILD" in body for body in docs.values()))
        self.assertTrue(any("ASSET_INTEGRITY_FAILED" in body for body in docs.values()))

    def test_every_reference_is_a_filled_markdown_document(self):
        documents = list((ROOT / "references").rglob("*.md"))
        self.assertGreaterEqual(len(documents), 131)
        forbidden = ("TODO", "TBD", "placeholder", "Talent definition", "Unresolved source text")
        for path in documents:
            with self.subTest(path=path.relative_to(ROOT)):
                body = path.read_text(encoding="utf-8")
                if body.startswith("---\nfeature:"):
                    self.assertIn("\n# ", body)
                else:
                    self.assertTrue(body.startswith("# "))
                self.assertGreaterEqual(len(body.splitlines()), 3)
                self.assertFalse(any(token.casefold() in body.casefold() for token in forbidden))


if __name__ == "__main__":
    unittest.main()

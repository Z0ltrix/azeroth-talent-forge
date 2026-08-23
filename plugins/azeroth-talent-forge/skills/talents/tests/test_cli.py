import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from scripts.talents import _parser, share_url


class CliTests(unittest.TestCase):
    def test_parser_covers_public_commands(self):
        self.assertEqual(_parser().parse_args(["inspect", "--code", "ABC"]).command, "inspect")
        self.assertEqual(_parser().parse_args(["generate", "--spec", "73"]).command, "generate")
        self.assertEqual(_parser().parse_args(["presets", "list"]).presets_command, "list")
        self.assertEqual(_parser().parse_args(["generate", "--spec", "73"]).level, 90)
        self.assertEqual(_parser().parse_args(["validate", "--code", "ABC", "--level", "75"]).level, 75)

    def test_share_url_is_inert_local_formatting(self):
        self.assertEqual(share_url("ABC"), "https://www.wowhead.com/talent-calc/blizzard/ABC")


if __name__ == "__main__":
    unittest.main()

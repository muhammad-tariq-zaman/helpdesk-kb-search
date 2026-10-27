import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestKB(unittest.TestCase):
    def test_ranked_by_matches(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "vpn.md"), "w").write("# VPN fix\nvpn vpn vpn\n")
            open(os.path.join(d, "printer.md"), "w").write("# Printer\nvpn once\n")
            open(os.path.join(d, "other.md"), "w").write("# Other\nnothing here\n")
            r = main.search(d, "vpn")
            self.assertEqual([x["file"] for x in r], ["vpn.md", "printer.md"])
            self.assertEqual(r[0]["score"], 4)  # title + 3 mentions


if __name__ == "__main__":
    unittest.main()

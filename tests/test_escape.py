import re
import unittest

import fmtutil.utils as utils


class UtilsFormatEscapeTestCase(unittest.TestCase):

    def test_fmt_group_escape_utils(self):
        rs = utils.escape_fmt_group(
            "+file_{datetime:%Y-%m-%d %H:%M:%S}_{naming:%n_%e}.json"
        )
        self.assertEqual(
            r"\+file_{datetime:%Y-%m-%d %H:%M:%S}_{naming:%n_%e}\.json",
            rs,
        )

    def test_fmt_group_escape_utils_some(self):
        rs = utils.escape_fmt_group(
            r"+file_{datetime:%Y-%m-%d %H:%M:%S}_{naming:%n_%e}\.json"
        )
        self.assertEqual(
            r"\+file_{datetime:%Y-%m-%d %H:%M:%S}_{naming:%n_%e}\\\.json",
            rs,
        )

    def test_fmt_escape_utils_simple(self):
        rs = re.search(utils.escape_fmt_group(r"\w+"), "Test escape")
        self.assertIsNone(rs)
        rs = re.search(utils.escape_fmt_group(r"\w+"), r"Test escape\w+")
        self.assertEqual(r"\w+", rs.group(0))

    def test_fmt_escape_utils_replace(self):
        rs = re.sub(
            utils.escape_fmt_group("$date.data.json"),
            "replace",
            "Test escape: $date.data.json",
        )
        self.assertEqual("Test escape: replace", rs)

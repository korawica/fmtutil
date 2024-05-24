import unittest

import fmtutil.utils as utils


class UtilsTestCase(unittest.TestCase):

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

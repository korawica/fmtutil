import unittest

import fmtutil.version as vs


class BaseVersionTestCase(unittest.TestCase):
    def test_base_ver_init(self):
        version = vs.BaseVersion(0, 1, 15)

        self.assertEqual("0.1.15", str(version))
        self.assertEqual(
            "BaseVersion(major=0, minor=1, patch=15)",
            repr(version),
        )
        self.assertEqual(0, version.major)
        self.assertEqual(1, version.minor)
        self.assertEqual(15, version.patch)

        self.assertEqual(0, version[0])
        self.assertEqual(1, version[1])
        self.assertEqual(15, version[2])
        self.assertTupleEqual((0, 1, 15), version[:5])

    def test_base_ver_validate(self):
        self.assertTrue(vs.BaseVersion.is_valid("0.0.1"))
        self.assertTrue(vs.BaseVersion.is_valid("2.10.1"))
        self.assertFalse(vs.BaseVersion.is_valid("v2.10.1"))
        self.assertFalse(vs.BaseVersion.is_valid("v2.10.1.rc01"))
        self.assertFalse(vs.BaseVersion.is_valid("v2.10"))
        self.assertFalse(vs.BaseVersion.is_valid("2.10"))

    def test_base_ver_match(self):
        self.assertTrue(vs.BaseVersion.parse("2.0.0").match(">=1.0.0"))
        self.assertFalse(vs.BaseVersion.parse("1.0.0").match(">1.0.0"))
        self.assertTrue(vs.BaseVersion.parse("4.0.4").match("4.0.4"))

    def test_base_ver_compatible(self):
        self.assertFalse(
            vs.BaseVersion(1, 1, 0).is_compatible(vs.BaseVersion(1, 0, 0))
        )
        self.assertTrue(
            vs.BaseVersion(1, 0, 0).is_compatible(vs.BaseVersion(1, 1, 0))
        )

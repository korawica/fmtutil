import unittest

import fmtutil.__type as t
import fmtutil.__version as vs


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

    def test_base_ver_replace(self):
        version = vs.BaseVersion(0, 0, 0)
        self.assertEqual("0.1.15", str(version.replace(minor=1, patch=15)))

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

    def test_base_ver_order(self):
        self.assertGreaterEqual(
            vs.BaseVersion(1, 0, 0),
            vs.BaseVersion(1, 0, 0),
        )
        self.assertGreaterEqual(
            vs.BaseVersion(1, 0, 1),
            vs.BaseVersion(1, 0, 0),
        )
        self.assertFalse(vs.BaseVersion(1, 0, 0) >= vs.BaseVersion(1, 0, 1))
        self.assertFalse(vs.BaseVersion(1, 0, 0) > vs.BaseVersion(1, 0, 1))
        self.assertGreater(vs.BaseVersion(2, 10, 0), vs.BaseVersion(1, 10, 99))
        self.assertFalse(vs.BaseVersion(0, 0, 0) > vs.BaseVersion(0, 0, 0))
        self.assertNotEqual(vs.BaseVersion(2, 10, 0), vs.BaseVersion(1, 10, 99))
        self.assertEqual(vs.BaseVersion(0, 0, 0), vs.BaseVersion(0, 0, 0))
        self.assertNotEqual(vs.BaseVersion(2, 10, 0), vs.BaseVersion(1, 10, 99))
        self.assertEqual(vs.BaseVersion(0, 0, 0), vs.BaseVersion(0, 0, 0))
        self.assertLessEqual(vs.BaseVersion(1, 0, 0), vs.BaseVersion(1, 0, 0))
        self.assertFalse(vs.BaseVersion(1, 0, 1) <= vs.BaseVersion(1, 0, 0))
        self.assertLessEqual(vs.BaseVersion(1, 0, 0), vs.BaseVersion(1, 0, 1))
        self.assertLess(vs.BaseVersion(1, 0, 0), vs.BaseVersion(1, 0, 1))
        self.assertFalse(vs.BaseVersion(2, 10, 0) < vs.BaseVersion(1, 10, 99))
        self.assertFalse(vs.BaseVersion(0, 0, 0) < vs.BaseVersion(0, 0, 0))

    def test_base_vs_order_special(self):
        self.assertLess(vs.BaseVersion(0, 0, 0), (1, 0, 0))
        self.assertEqual(vs.BaseVersion(0, 0, 0), (0, 0, 0))
        self.assertGreaterEqual(vs.BaseVersion(0, 15, 1), "0.0.20")

    def test_base_vs_wildcard(self):
        self.assertTupleEqual(
            (vs.BaseVersion(2, 1, 0), vs.BaseVersion(2, 2, 0)),
            vs.BaseVersion.extract_wildcard("2.1.*"),
        )
        self.assertTupleEqual(
            (vs.BaseVersion(0, 0, 0), t.Inf),
            vs.BaseVersion.extract_wildcard("*"),
        )


class VersionSemverTestCase(unittest.TestCase):
    def test_ver_semver_init(self):
        version = vs.VersionSemver(0, 1, 15, "rc.1", "build.10")

        self.assertEqual("0.1.15-rc.1+build.10", str(version))
        self.assertEqual(
            (
                "VersionSemver(major=0, minor=1, patch=15, pre='rc.1', "
                "build='build.10')"
            ),
            repr(version),
        )
        self.assertEqual(
            vs.VersionSemver(0, 1, 15),
            version.finalize_version(),
        )

    def test_ver_semver_bump(self):
        self.assertEqual(
            vs.VersionSemver(0, 1, 1, "rc", None),
            vs.VersionSemver(0, 1, 1, "rc", None).bump_pre(),
        )
        self.assertEqual(
            vs.VersionSemver(0, 1, 1, "rc.1", None),
            vs.VersionSemver(0, 1, 1, None, None).bump_pre(),
        )
        self.assertEqual(
            vs.VersionSemver(0, 1, 1, "rc.1", None),
            vs.VersionSemver(0, 1, 1, None, None).bump_pre(None),
        )
        self.assertEqual(
            vs.VersionSemver(0, 1, 1, "1", None),
            vs.VersionSemver(0, 1, 1, None, None).bump_pre(""),
        )
        self.assertEqual(
            vs.VersionSemver(0, 1, 1, "rc.2", None),
            vs.VersionSemver(0, 1, 1, "rc.1", None).bump_pre(),
        )
        self.assertEqual(
            vs.VersionSemver(0, 1, 1, "rc.1", "build.10"),
            vs.VersionSemver(0, 1, 1, "rc.1", "build.9").bump_build(),
        )

    def test_ver_semver_match(self):
        self.assertTrue(vs.VersionSemver.parse("2.0.0").match(">=1.0.0"))
        self.assertFalse(vs.VersionSemver.parse("1.0.0").match(">1.0.0"))
        self.assertTrue(vs.VersionSemver.parse("4.0.4").match("4.0.4"))
        self.assertTrue(vs.VersionSemver.parse("4.0.4").match("^4.0.4"))
        self.assertTrue(vs.VersionSemver.parse("0.24.25-rc1").match("^0.24.1"))

        self.assertTrue(vs.VersionSemver.parse("1.24.25-rc1").match("~=1.0.0"))
        self.assertTrue(vs.VersionSemver.parse("1.0.1-rc1").match("~=1.0.0"))
        self.assertTrue(vs.VersionSemver.parse("2.4.25-rc1").match("~=2.2.0"))
        self.assertTrue(vs.VersionSemver.parse("3.0.0-rc1").match("~=2.2.0"))

        self.assertFalse(vs.VersionSemver.parse("1.24.25-rc1").match("^0.24.1"))
        self.assertFalse(vs.VersionSemver.parse("0.24.0-rc1").match("^0.24.1"))
        self.assertFalse(vs.VersionSemver.parse("0.25.1-rc1").match("^0.24.1"))

        self.assertFalse(vs.VersionSemver.parse("2.0.1").match("~=1.0.0"))
        self.assertFalse(vs.VersionSemver.parse("2.1.9").match("~=2.2.0"))
        self.assertFalse(vs.VersionSemver.parse("2.2.0-rc").match("~=2.2.0"))
        self.assertFalse(vs.VersionSemver.parse("3.0.0").match("~=2.2.0"))

    def test_ver_semver_compatible(self):
        self.assertFalse(
            vs.VersionSemver(1, 1, 0).is_compatible(vs.VersionSemver(1, 0, 0))
        )
        self.assertTrue(
            vs.VersionSemver(1, 0, 0).is_compatible(vs.VersionSemver(1, 1, 0))
        )
        self.assertTrue(
            vs.VersionSemver(1, 0, 0).is_compatible(vs.VersionSemver(1, 1, 2))
        )

    def test_ver_semver_order(self):
        semver_parse = vs.VersionSemver.parse
        self.assertEqual(
            semver_parse("0.0.0-pre10+build99"),
            semver_parse("0.0.0-pre10"),
        )
        self.assertEqual(semver_parse("0.0.1"), semver_parse("0.0.1"))
        self.assertEqual(semver_parse("0.0.1"), semver_parse("0.0.1+build.21"))
        self.assertEqual(semver_parse("0.0.1"), semver_parse("0.0.1"))
        self.assertLessEqual(semver_parse("0.0.1"), semver_parse("0.0.1"))
        self.assertLessEqual(semver_parse("1.0.0"), semver_parse("4.2.1"))
        self.assertFalse(semver_parse("1.0.0") > semver_parse("4.2.1"))
        self.assertGreater(semver_parse("1.0.0"), semver_parse("1.0.0-pre.1"))
        self.assertGreater(
            semver_parse("0.15.0-rc1"),
            semver_parse("0.0.16-rc"),
        )
        self.assertGreater(
            semver_parse("1.15.0-rc1"),
            semver_parse("1.0.16-rc"),
        )
        self.assertGreaterEqual(
            semver_parse("1.15.0-rc2"),
            semver_parse("1.15.0-rc1"),
        )
        self.assertGreater(
            semver_parse("1.15.0"),
            semver_parse("1.15.0-rc1"),
        )


class VersionPackageTestCase(unittest.TestCase):
    def test_ver_package_init(self):
        version = vs.VersionPackage(1, 0, 1, 15, "-a2", "-post2")
        self.assertEqual("1!0.1.15-a2-post2", str(version))
        self.assertEqual(
            (
                "VersionPackage(epoch=1, major=0, minor=1, patch=15, "
                "pre='-a2', post='-post2', dev=None, local=None)"
            ),
            repr(version),
        )

    def test_ver_package_parse(self):
        self.assertEqual(
            "0.0.1.rc1.post2",
            str(vs.VersionPackage.parse("0.0.1.rc1.post2")),
        )
        self.assertEqual(
            "1!1.2.3+abc.dev1",
            str(vs.VersionPackage.parse("1!1.2.3+abc.dev1")),
        )

    def test_ver_package_bump(self):
        self.assertEqual(
            vs.VersionPackage(0, 0, 1, 1, "rc", None),
            vs.VersionPackage(0, 0, 1, 1, "rc", None).bump_pre(),
        )

        self.assertEqual(
            vs.VersionPackage(major=0, minor=0, patch=0).bump_patch(),
            vs.VersionPackage(major=0, minor=0, patch=1),
        )

    def test_ver_package_order(self):
        self.assertGreater(
            vs.VersionPackage.parse("0.15.rc1"),
            vs.VersionPackage.parse("0.0.16.rc"),
        )
        self.assertGreater(
            vs.VersionPackage.parse("1.15.rc1"),
            vs.VersionPackage.parse("1.0.16.rc"),
        )

# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
"""
Test the formatter object.
"""
import datetime
import unittest

import fmtutil.formatter as fmt


class FormatterGroupTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # Create FormatterGroup class
        self.DateName: fmt.FormatterGroupType = fmt.make_group(
            {
                "name": fmt.Naming,
                "datetime": fmt.Datetime,
            }
        )
        self.DateVersion = fmt.make_group(
            {
                "version": fmt.Version,
                "datetime": fmt.Datetime,
            }
        )
        self.Namings = fmt.make_group(
            {
                "name": fmt.Naming,
                "role": fmt.Naming,
            }
        )
        # Create FormatterGroup instance
        self.gp = self.DateName(
            {
                "name": fmt.Naming.parse("data engineer"),
                "datetime": fmt.Datetime.parse("2022_01_01", "%Y_%m_%d"),
            }
        )
        self.gp2 = self.DateVersion(
            {
                "version": fmt.Version.parse("1.2.3", "%m.%n.%c"),
                "datetime": fmt.Datetime.parse("2022_01_01", "%Y_%m_%d"),
            }
        )
        self.gp3 = self.Namings(
            {
                "name": fmt.Naming.parse("foo bar"),
                "role": fmt.Naming.parse("data engineer"),
            }
        )
        self.gp2_default = self.DateVersion(
            {
                "version": fmt.Version(),
                "datetime": fmt.Datetime(),
            }
        )

    def test_fmt_group_init_raise(self):
        with self.assertRaises(fmt.FormatterGroupValueError) as context:
            self.DateVersion(
                {
                    "version": fmt.Version(),
                    "timestamp": fmt.Datetime(),
                }
            )
        self.assertIn(
            (
                "VersionDatetimeGroup does not support for this group name, "
                "'timestamp'."
            ),
            str(context.exception),
        )

        with self.assertRaises(fmt.FormatterGroupArgumentError) as context:
            fmt.make_group(
                {
                    "naming": fmt.make_const(
                        formatter=fmt.Naming.parse("data_engineer", "%s")
                    ),
                    "timestamp": fmt.Naming.parse("demo", "%s"),
                }
            )
        self.assertIn(
            (
                "with 'group', Make group constructor function want group with "
                "type, Dict[str, FormatterType], not instance of 'Naming'."
            ),
            str(context.exception),
        )

        with self.assertRaises(fmt.FormatterGroupValueError) as context:
            fmt.make_group(
                {
                    "naming": fmt.make_const(
                        formatter=fmt.Naming.parse("data_engineer", "%s")
                    ),
                    "timestamp": datetime.datetime,
                }
            )
        self.assertIn(
            (
                "Make group constructor function want group with type, "
                "Dict[str, FormatterType], not 'datetime'"
            ),
            str(context.exception),
        )

    def test_fmt_group_const(self):
        ConstGroup = fmt.make_group(
            {
                "naming": fmt.make_const(
                    formatter=fmt.Naming.parse("data_engineer", "%s")
                ),
                "domain": fmt.make_const(
                    fmt=fmt.Naming,
                    value="demo",
                ),
                "timestamp": fmt.Datetime,
            }
        )
        self.assertEqual(
            "Demo",
            ConstGroup.parse("data_engineer", "{naming:%s}").format(
                "{domain:%p}"
            ),
        )
        self.assertEqual(
            "20210101_data_engineer_demo",
            ConstGroup(
                {
                    "timestamp": datetime.datetime(2021, 1, 1, 12),
                }
            ).format("{timestamp:%Y%m%d}_{naming:%s}_{domain}"),
        )
        self.assertEqual(
            "20210101_data_engineer_demo",
            ConstGroup.from_value(
                {
                    "timestamp": datetime.datetime(2021, 1, 1, 12),
                }
            ).format("{timestamp:%Y%m%d}_{naming:%s}_{domain}"),
        )
        self.assertEqual(
            "20210101_data_engineer_demo",
            ConstGroup.from_formats(
                {
                    "timestamp": {"year": "2021", "month": "01", "day": "01"},
                }
            ).format("{timestamp:%Y%m%d}_{naming:%s}_{domain}"),
        )

        with self.assertRaises(NotImplementedError) as context:
            ConstGroup(
                {
                    "timestamp": datetime.datetime(2021, 1, 1, 12),
                    "naming": ["data", "pipeline"],
                }
            )
        self.assertIn(
            (
                "The Constant class does not support for passing value to "
                "this class initialization."
            ),
            str(context.exception),
        )

        with self.assertRaises(fmt.FormatterGroupValueError) as context:
            ConstGroup.from_value(
                {"timestamps": datetime.datetime(2021, 1, 1, 12)}
            )
        self.assertIn(
            (
                "NamingConstNamingConstDatetimeGroup does not support for this "
                "group name, 'timestamps'."
            ),
            str(context.exception),
        )
        with self.assertRaises(fmt.FormatterGroupValueError) as context:
            ConstGroup.from_formats(
                {
                    "timestamps": {"year": "2021", "month": "01", "day": "01"},
                }
            )
        self.assertIn(
            (
                "NamingConstNamingConstDatetimeGroup does not support for this "
                "group name, 'timestamps'."
            ),
            str(context.exception),
        )

    def test_fmt_group_properties(self):
        self.assertEqual(
            "data engineer, 2022-01-01 00:00:00.000000", self.gp.__str__()
        )
        self.assertEqual(
            hash(self.gp.__str__()),
            self.gp.__hash__(),
        )
        self.assertEqual(
            (
                "<NamingDatetimeGroup.parse(value='data engineer_2022-01-01 "
                "00:00:00.000000', fmt='%n_%Y-%m-%d %H:%M:%S.%f')>"
            ),
            self.gp.__repr__(),
        )

    def test_fmt_group_gen_format(self):
        _fmt, _fmt_getter = self.DateName.gen_format(
            "{name:%s}_in_{datetime:%Y%m%d}_{name:%a}__{datetime:%n}"
        )

    def test_fmt_group_parser(self):
        self.assertEqual(
            {
                "datetime": fmt.Datetime.parse("2022-01-01", "%Y-%m-%d"),
                "name": fmt.Naming.parse("data engineer", "%n"),
            },
            self.DateName.parse(
                "data_engineer_in_20220101_de",
                fmt="{name:%s}_in_{datetime:%Y%m%d}_{name:%a}",
            ).groups,
        )
        self.assertEqual(
            {
                "datetime": fmt.Datetime.parse("2022-01-01", "%Y-%m-%d"),
                "name": fmt.Naming.parse("data engineer", "%n"),
            },
            self.DateName.parse(
                "data_engineer_in_20220101_de",
                fmt="{name:%s}_in_{datetime:%Y%m%d}_{name:%a}",
            ).groups,
        )
        self.assertEqual(
            {
                "datetime": fmt.Datetime.parse("2022-01-01", "%Y-%m-%d"),
                "version": fmt.Version.parse("v1.2.3", "v%m.%n.%c"),
            },
            self.DateVersion.parse(
                "20220101_1_2_3_00",
                fmt="{datetime:%Y%m%d}_{version}_{datetime:%H}",
            ).groups,
        )
        self.assertEqual(
            {
                "name": fmt.Naming.parse("foo bar", "%n"),
                "role": fmt.Naming.parse("data engineer", "%n"),
            },
            self.Namings.parse(
                "foo_bar|data_engineer",
                fmt="{name:%s}\\|{role:%s}",
            ).groups,
        )

        self.assertEqual(
            {
                "datetime": fmt.Datetime.parse("2022-11-21", "%Y-%m-%d"),
                "version": fmt.Version.parse("v1.0.0", "v%m.%n.%c"),
            },
            self.DateVersion.parse(
                "20221121_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ).groups,
        )

    def test_fmt_group_parser_fixed(self):
        self.assertEqual(
            {
                "name": fmt.Naming.parse("foo bar data", "%n"),
                "role": fmt.Naming.parse("engineer", "%n"),
            },
            self.gp3.parse(
                "foo_bar_data_engineer",
                fmt="{name:%s}_{role:%s}",
            ).groups,
        )

    def test_fmt_group_parser_raise(self):
        with self.assertRaises(fmt.FormatterGroupArgumentError) as context:
            self.DateName.parse(
                "data_engineer_in_20220101_de",
                fmt="{name:%s}_in_{datetime:%Y%m%d}_{name:%a}_extension",
            )
        self.assertIn(
            (
                r"with 'format', 'data_engineer_in_20220101_de' does not "
                r"match with the format: '^(?P<name>"
                r"(?P<name___strings_snake>[a-z0-9]+(?:_[a-z0-9]+)*))_in_"
                r"(?P<datetime>(?P<datetime___year>\d{4})"
                r"(?P<datetime___month_pad>01|02|03|04|05|06|07|08|09|10"
                r"|11|12)(?P<datetime___day_pad>[0-3][0-9]))_"
                r"(?P<name__1>(?P<name__1___shorts__1>[a-z0-9]+))_extension$'"
            ),
            str(context.exception),
        )

    def test_fmt_group_format(self):
        self.assertEqual(
            "data engineer_2022_01_01_000000_000000.csv",
            self.gp.format("{name}_{datetime:%Y_%m_%d_%H%M%S_%f}.csv"),
        )
        self.assertEqual(
            "dataEngineer_2022_01_01_000000_000000.csv",
            self.gp.format("{name:%c}_{datetime:%Y_%m_%d_%H%M%S_%f}.csv"),
        )
        self.assertEqual(
            "2022_01_01_000000_000000_v1_2_3.csv",
            self.gp2.format("{datetime:%Y_%m_%d_%H%M%S_%f}_v{version:%f}.csv"),
        )
        self.assertEqual(
            "2022-01-01 00:00:00.000000_1_2_3_2022-01-01 00:00:00.000000.csv",
            self.gp2.format("{datetime}_{version}_{datetime}.csv"),
        )

    def test_fmt_group_format_raise(self):
        with self.assertRaises(fmt.FormatterGroupArgumentError) as context:
            self.gp2.format("{datetime:%Y_%m_%d_%H%M%S_%K}_v{version:%f}.csv")
        self.assertIn(
            (
                "with 'format', the format: '%K' does not support for "
                "'Datetime' in {datetime:%Y_%m_%d_%H%M%S_%K}"
            ),
            str(context.exception),
        )
        with self.assertRaises(fmt.FormatterGroupValueError) as context:
            self.gp2.format("{timestamp:%Y_%m_%d_%H%M%S}")
        self.assertIn(
            "This group, 'timestamp', does not set on `cls.base_groups`.",
            str(context.exception),
        )

    def test_fmt_group_order(self):
        self.assertFalse(
            self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            )
            < self.DateVersion.parse(
                "20220101_0_9_1",
                fmt="{datetime:%Y%m%d}_{version}",
            )
        )
        self.assertLess(
            self.DateVersion.parse(
                "20220105_0_9_1",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
            self.DateVersion.parse(
                "20220111_0_9_1",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
        )
        # Datetime is greater but version is less that other
        self.assertFalse(
            self.DateVersion.parse(
                "20220105_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            )
            > self.DateVersion.parse(
                "20220101_1_0_1",
                fmt="{datetime:%Y%m%d}_{version}",
            )
        )
        (
            self.assertGreater(
                self.DateVersion.parse(
                    "20220101_0_1_0",
                    fmt="{datetime:%Y%m%d}_{version}",
                ),
                self.DateVersion.parse(
                    "20220101_0_0_9",
                    fmt="{datetime:%Y%m%d}_{version}",
                ),
            )
        )
        self.assertNotEqual(
            self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
            self.DateVersion.parse(
                "20220101_0_9_1",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
        )
        self.assertGreaterEqual(
            self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
            self.DateVersion.parse(
                "20220101_0_9_1",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
        )
        self.assertLessEqual(
            self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
            self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
        )

    def test_fmt_group_order_raise(self):
        with self.assertRaises(TypeError) as context:
            _ = self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ) < self.DateName.parse(
                "20220101_test",
                fmt="{datetime:%Y%m%d}_{name}",
            )
        self.assertIn(
            (
                "'<' not supported between instances of 'VersionDatetimeGroup' "
                "and 'NamingDatetimeGroup'"
            ),
            str(context.exception),
        )
        with self.assertRaises(TypeError) as context:
            _ = self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ) > self.DateName.parse(
                "20220101_test",
                fmt="{datetime:%Y%m%d}_{name}",
            )
        self.assertIn(
            (
                "'>' not supported between instances of 'VersionDatetimeGroup' "
                "and 'NamingDatetimeGroup'"
            ),
            str(context.exception),
        )

    def test_fmt_group_max_min(self):
        groups = (
            self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
            self.DateVersion.parse(
                "20220329_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
            self.DateVersion.parse(
                "20220329_1_1_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
        )
        self.assertEqual(
            max(groups),
            self.DateVersion.parse(
                "20220329_1_1_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
        )
        self.assertEqual(
            min(groups),
            self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ),
        )

    def test_fmt_group_operation(self):
        self.assertEqual(
            datetime.datetime(2022, 1, 11),
            self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            )
            .adjust({"datetime": datetime.timedelta(days=10)})
            .groups["datetime"]
            .value,
        )

        with self.assertRaises(fmt.FormatterGroupValueError) as context:
            self.DateVersion.parse(
                "20220101_1_0_0",
                fmt="{datetime:%Y%m%d}_{version}",
            ).adjust({"timestamp": datetime.timedelta(days=10)})
        self.assertEqual(
            "Key of values, 'timestamp', does not support for this "
            "<class 'fmtutil.formatter.VersionDatetimeGroup'>.",
            str(context.exception),
        )

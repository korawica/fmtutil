# -------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# --------------------------------------------------------------------------
"""
Test the formatter object.
"""
import unittest

import dup_fmt.formatter as fmt


class FormatterGroupTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.DateName: fmt.FormatterGroupType = fmt.Group(
            {
                "name": fmt.Naming,
                "datetime": fmt.Datetime,
            }
        )
        self.DateVersion = fmt.Group(
            {
                "version": fmt.Version,
                "datetime": fmt.Datetime,
            }
        )
        self.Namings = fmt.Group(
            {
                "name": fmt.Naming,
                "role": fmt.Naming,
            }
        )
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

    def test_fmt_group_properties(self):
        self.assertEqual(
            (
                "<CustomGroup.parse(value='data engineer_2022-01-01 "
                "00:00:00.000', fmt='%n_%Y-%m-%d %H:%M:%S.%f')>"
            ),
            self.gp.__repr__(),
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
        # # FIXME: parser foo_bar_data to `name` and engineer to `role`
        # # self.assertEqual(
        # #     {
        # #         "name": fmt.Naming.parse("foo bar", "%n"),
        # #         "role": fmt.Naming.parse("data engineer", "%n"),
        # #     },
        # #     self.gp3.parser(
        # #         "foo_bar_data_engineer",
        # #         fmt="{name:%s}_{role:%s}",
        # #         _max=True,
        # #     ),
        # # )
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

    def test_fmt_group_parser_raise(self):
        with self.assertRaises(fmt.FormatterGroupArgumentError) as context:
            self.DateName.parse(
                "data_engineer_in_20220101_de",
                fmt="{name:%s}_in_{datetime:%Y%m%d}_{name:%a}_extension",
            )
        self.assertTrue(
            (
                r"with 'format', 'data_engineer_in_20220101_de' does not "
                r"match with the format: '^(?P<name__0>"
                r"(?P<name__0strings_snake__00>[a-z0-9]+(?:_[a-z0-9]+)*))_in_"
                r"(?P<datetime__0>(?P<datetime__0year__00>\d{4})"
                r"(?P<datetime__0month_pad__00>01|02|03|04|05|06|07|08|09|10"
                r"|11|12)(?P<datetime__0day_pad__00>[0-3][0-9]))_"
                r"(?P<name__1>(?P<name__1shorts__01>[a-z0-9]+))_extension$'"
            )
            in str(context.exception)
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
        self.assertTrue(
            (
                "with 'format', the format: '%K' does not support for "
                "'Datetime' in {datetime:%Y_%m_%d_%H%M%S_%K}"
            )
            in str(context.exception)
        )

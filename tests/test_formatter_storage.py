# -------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# --------------------------------------------------------------------------
"""
Test the Serial formatter object.
"""
import unittest

import dup_fmt.formatter as fmt


class StorageTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.st = fmt.Storage({"bit": "10481"})
        self.st_default: fmt.Formatter = fmt.Storage()
        self.st_p: fmt.Formatter = fmt.Storage.parse("10353B", "%B")
        self.st_p2: fmt.Formatter = fmt.Storage.parse("135005", "%b")

    def test_storage_regex(self):
        self.assertDictEqual(
            {
                "%b": "(?P<bit>[0-9]*)",
                "%B": "(?P<byte>[0-9]*B)",
            },
            fmt.Storage.regex(),
        )

    def test_storage_formatter(self):
        formatter = fmt.Storage.formatter(storage=512)
        regex = fmt.Storage.regex()
        self.assertDictEqual(
            {
                "%B": {"regex": "(?P<byte>[0-9]*B)", "value": "64B"},
                "%b": {"regex": "(?P<bit>[0-9]*)", "value": "512"},
            },
            {
                i: {
                    "regex": regex[i],
                    "value": fmt.caller(formatter[i]["value"]),
                }
                for i in formatter
            },
        )

    def test_storage_properties(self):
        self.assertEqual("<Storage.parse('10481', '%b')>", self.st.__repr__())
        self.assertEqual(hash(self.st.string), self.st.__hash__())

        self.assertEqual(82824, self.st_p.value)
        self.assertEqual("82824", self.st_p.string)

        self.assertEqual(135005, self.st_p2.value)
        self.assertEqual("135005", self.st_p2.string)

        self.assertEqual(0, self.st_default.value)
        self.assertEqual("0", self.st_default.string)

    def test_storage_format(self):
        self.assertEqual("82824", self.st_p.format("%b"))
        self.assertEqual("10353B", self.st_p.format("%B"))

        self.assertEqual("135005", self.st_p2.format("%b"))
        self.assertEqual("16876B", self.st_p2.format("%B"))

        self.assertEqual("0", self.st_default.format("%b"))
        self.assertEqual("0B", self.st_default.format("%B"))

        with self.assertRaises(fmt.FormatterKeyError) as context:
            self.st_default.format("%Z")
        self.assertTrue(
            "the format: '%Z' does not support for 'Storage'"
            in str(context.exception)
        )

    def test_storage_order(self):
        self.assertTrue(self.st_p <= self.st_p2)
        self.assertTrue(self.st_p < self.st_p2)
        self.assertFalse(self.st_p == self.st_p2)
        self.assertFalse(self.st_p >= self.st_p2)
        self.assertFalse(self.st_p > self.st_p2)

    def test_level_compare(self):
        self.assertEqual(1, self.st_p.level.value)
        self.assertEqual(0, self.st_default.level.value)
        self.assertTrue(self.st_p.level == self.st_p2.level)
        self.assertFalse(self.st_default.level == self.st_p2.level)
        self.assertTrue(self.st_default.level < self.st_p2.level)
        self.assertListEqual([True], self.st_p.level.slot)
        self.assertListEqual([False], self.st_default.level.slot)

# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
"""
Test the formatter object examples for Serial.
"""
import unittest

import fmtutil.__assets as fmt


class SerialAssetsExampleTestCase(unittest.TestCase):
    def test_parse_examples(self):
        self.assertEqual(
            11,
            fmt.Serial.parse("00011101 11", "%b %n").value,
        )

    def test_parse_with_strict_examples(self):
        with self.assertRaises(fmt.FormatterValueError):
            fmt.Serial.parse("00011101 11", "%b %n", strict=True)

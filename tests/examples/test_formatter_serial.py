# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
"""
Test the formatter object examples for Serial.
"""
import unittest

import fmtutil.formatter as fmt


class NamingExampleTestCase(unittest.TestCase):
    # FIXME: add validate to serial formatter object.
    def test_parse_examples(self):
        self.assertEqual(
            11,
            fmt.Serial.parse("00001101 11", "%b %n").value,
        )

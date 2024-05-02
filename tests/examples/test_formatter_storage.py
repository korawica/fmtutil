# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
"""
Test the formatter object examples for Storage.
"""
import unittest

import fmtutil.formatter as fmt


class StorageExampleTestCase(unittest.TestCase):
    def test_parse_examples(self):
        self.assertEqual(
            152,
            fmt.Storage.parse("152 19B", "%b %B").value,
        )

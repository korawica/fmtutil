# -------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# --------------------------------------------------------------------------
"""
Test the Constant formatter object.
"""
import unittest
from typing import Type

import dup_fmt.formatter as fmt
from dup_fmt.exceptions import FormatterValueError


class ConstantTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.const: Type["fmt.Constant"] = fmt.Constant(
            {
                "%n": "normal",
                "%s": "special",
            }
        )
        self.ct = self.const.parse("normal_life", "%n_life")

    def test_const_parser_raise(self):
        with self.assertRaises(FormatterValueError) as context:
            self.const.parse("special_job", "%s_life")
        self.assertTrue(
            (
                "value 'special_job' does not match "
                "with format '(?P<constant>special)_life'"
            )
            in str(context.exception)
        )

    def test_const_properties(self):
        self.assertEqual(1, self.ct.level.value)
        self.assertEqual("special", self.ct.format("%s"))
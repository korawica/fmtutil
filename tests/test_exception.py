# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
"""
Test the Exception object.
"""
import unittest

import fmtutil.exceptions as err


class ExceptionsTestCase(unittest.TestCase):
    def setUp(self) -> None: ...

    def test_exception_config_str_arg(self):
        result = err.FormatterArgumentError(
            arg="timestamp",
            message=(
                "order file object does not have `timestamp` in name "
                "formatter"
            ),
        )
        respec: str = (
            "with 'timestamp', order file object does not have `timestamp` "
            "in name formatter"
        )
        self.assertEqual(str(result), respec)

    def test_exception_config_tuple_arg(self):
        result = err.FormatterArgumentError(
            arg=("timestamp", "serial"),
            message=(
                "order file object does not have `timestamp` and `serial` "
                "in name formatter"
            ),
        )
        respec: str = (
            "with 'timestamp', and 'serial', order file object does not have "
            "`timestamp` and `serial` in name formatter"
        )
        self.assertEqual(str(result), respec)

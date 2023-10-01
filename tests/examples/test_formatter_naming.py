# -------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# --------------------------------------------------------------------------
"""
Test the formatter object examples for Naming.
"""
import unittest

import fmtutil.formatter as fmt


class NamingExampleTestCase(unittest.TestCase):
    def test_parse_examples(self):
        self.assertListEqual(
            ["monkey", "d", "luffy"],
            fmt.Naming.parse("monkey-d-luffy", "%k").value,
        )

        # FIXME: shortname does not match with the Kebab name
        self.assertListEqual(
            ["monkey", "d", "luffy"],
            fmt.Naming.parse("monkey-d-luffy ddd", "%k %a").value,
        )

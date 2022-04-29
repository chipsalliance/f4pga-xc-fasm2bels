#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

import unittest
from parameterized import parameterized
import pathlib
from fasm2bels.lib import parse_xdc
import yaml

XDC_PARSING_PATH = pathlib.Path(
    __file__).absolute().parent / "test_data" / "xdc_parsing"
XDC_INPUTS_PATH = XDC_PARSING_PATH / "xdc_inputs"
YAML_GOLDEN_PATH = XDC_PARSING_PATH / "yaml_golden"

TEST_NAMES = ["test_basic", "test_dict"]


class TestXdcParser(unittest.TestCase):
    @parameterized.expand(TEST_NAMES)
    def test_parse_and_compare(self, test_name):
        self.maxDiff = None

        # Get input XDC file
        xdc_path = XDC_INPUTS_PATH / (test_name + ".xdc")
        self.assertTrue(xdc_path.is_file())

        # Get golden YAML file
        yaml_path = YAML_GOLDEN_PATH / (test_name + ".yaml")
        self.assertTrue(yaml_path.is_file())

        with open(xdc_path, 'r') as fp:
            constraints = parse_xdc.parse_simple_xdc(fp)

        with open(yaml_path, 'r') as fp:
            net_props = yaml.safe_load(fp)

        all_constraints = {}
        for constraint in constraints:
            all_constraints[constraint.net] = constraint.params

        self.assertEqual(all_constraints, net_props)

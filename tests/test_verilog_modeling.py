#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2021-2022 F4PGA Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

import unittest
import fasm2bels.models.verilog_modeling
from fasm2bels.models.verilog_modeling import Wire, Constant, Bus, NoConnect
import doctest


class TestVerilogModeling(unittest.TestCase):
    def test_connections(self):
        self.assertEqual("a", Wire("a").to_string())
        self.assertEqual("1'b0", Constant(0).to_string())
        self.assertEqual("1'b1", Constant(1).to_string())
        self.assertEqual("{1'b0, 1'b1}",
                         Bus([Constant(1), Constant(0)]).to_string())
        self.assertEqual("{a, 1'b1}",
                         Bus([Constant(1), Wire('a')]).to_string())
        self.assertEqual("", NoConnect().to_string())

    def test_rename(self):
        self.assertEqual("b", Wire("a").to_string({'a': 'b'}))
        self.assertEqual("{b, 1'b1}",
                         Bus([Constant(1), Wire('a')]).to_string({
                             'a': 'b'
                         }))

    def test_iter_connections(self):
        self.assertEqual(list(Wire('a').iter_wires()), [(None, "a")])
        self.assertEqual(
            list(Bus([Constant(1), Wire('a')]).iter_wires()), [(1, "a")])
        self.assertEqual(
            list(Bus([Wire('b'), Wire('a')]).iter_wires()), [(0, "b"),
                                                             (1, "a")])
        self.assertEqual(list(Constant(0).iter_wires()), [])
        self.assertEqual(list(NoConnect().iter_wires()), [])

    def test_doctest(self):
        doctest.testmod(fasm2bels.models.verilog_modeling)

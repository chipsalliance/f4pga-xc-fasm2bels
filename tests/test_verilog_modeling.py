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

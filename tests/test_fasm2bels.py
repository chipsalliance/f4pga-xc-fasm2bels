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
import os
import sys
import tempfile
import filecmp
import difflib
import itertools
import enum
import tarfile
from fasm2bels.fasm2bels import main


class PinConstraintType(enum.Enum):
    XDC = 0
    PCF = 1


test_names = ["simple_ff", "iddr", "oddr", "mmcm", "gtp", "pcie", "carry4", "pudc"]
pin_constraint_types = [PinConstraintType.XDC, PinConstraintType.PCF]


def unpack_tar(tar_file):
    tar = tarfile.open(name=tar_file, mode="r:gz")
    tar.extractall(path=os.path.dirname(tar_file))


class TestFasm2Bels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.channels_file = tempfile.NamedTemporaryFile(
            suffix='channels.db', delete=False)
        cls.channels_file.close()
        os.unlink(cls.channels_file.name)

    @classmethod
    def tearDownClass(cls):
        os.unlink(cls.channels_file.name)

    @parameterized.expand(itertools.product(test_names, pin_constraint_types))
    def test_fasm2bels(self, test_name, pin_constraint_type):
        cur_dir = os.path.dirname(__file__)
        base_dir = os.path.join(cur_dir, '..')
        db_root = os.path.join(base_dir, 'third_party', 'prjxray-db', 'artix7')
        bitread = os.path.join(base_dir, 'third_party', 'prjxray', 'build',
                               'tools', 'bitread')
        bit_file = os.path.join(cur_dir, 'test_data', test_name,
                                '{}.bit'.format(test_name))
        pcf = os.path.join(cur_dir, 'test_data', test_name,
                           '{}.pcf'.format(test_name))
        xdc_input = os.path.join(cur_dir, 'test_data', test_name,
                                 '{}.xdc'.format(test_name))
        eblif = os.path.join(cur_dir, 'test_data', test_name,
                             '{}.eblif'.format(test_name))

        unpack_tar(os.path.join(cur_dir, 'test_data', test_name, "{}.tar.gz".format(test_name)))

        temp_dir = tempfile.mkdtemp(
            prefix="test_fasm2bels_{}_{}_".format(test_name,
                                                  pin_constraint_type.name),
            dir='/tmp')

        fasm_file = os.path.join(temp_dir, '{}.fasm'.format(test_name))

        iostandard = 'LVCMOS33'
        drive = '12'
        top = 'top'
        part = 'xc7a35tcpg236-1'

        generated_top_v = os.path.join(temp_dir, 'top_bit.v')
        generated_top_xdc = os.path.join(temp_dir, 'top_bit.xdc')
        interchange_netlist = os.path.join(temp_dir, 'top_bit.netlist')
        interchange_phys = os.path.join(temp_dir, 'top_bit.phys')
        interchange_xdc = os.path.join(temp_dir, 'top_bit.inter.xdc')

        sys.argv = [
            'fasm2bels',
            '--db_root',
            db_root,
            '--part',
            part,
            '--bitread',
            bitread,
            '--bit_file',
            bit_file,
            '--fasm_file',
            fasm_file,
            '--eblif',
            eblif,
            '--top',
            top,
            '--iostandard',
            iostandard,
            '--drive',
            drive,
            '--connection_database',
            self.channels_file.name,
            '--verilog_file',
            generated_top_v,
            '--xdc_file',
            generated_top_xdc,
            '--logical_netlist',
            interchange_netlist,
            '--physical_netlist',
            interchange_phys,
            '--interchange_xdc',
            interchange_xdc,
            '--interchange_capnp_schema_dir',
            os.environ['INTERCHANGE_SCHEMA_PATH'],
        ]
        if pin_constraint_type == PinConstraintType.XDC:
            sys.argv.extend(('--input_xdc', xdc_input))
        elif pin_constraint_type == PinConstraintType.PCF:
            sys.argv.extend(('--pcf', pcf))

        main()

        tmp_top_v = os.path.join(temp_dir, generated_top_v)
        tmp_top_xdc = os.path.join(temp_dir, generated_top_xdc)

        # Check if generated files exists
        self.assertTrue(os.path.exists(tmp_top_v))
        self.assertTrue(os.path.exists(tmp_top_xdc))

        # Check if generated files are equal to the golden ones
        def compare(file_a, file_b):
            """
            Compares content of the two given files. When that fails assembles
            an unified diff and writes it to sys.stderr.
            """

            if filecmp.cmp(file_a, file_b) is True:
                return True

            with open(file_a, "r") as fp:
                lines_a = fp.readlines()
            with open(file_b, "r") as fp:
                lines_b = fp.readlines()

            lines = difflib.unified_diff(lines_a, lines_b, "golden", "current")
            sys.stderr.writelines(lines)

            return False

        self.assertTrue(compare(os.path.join(
            cur_dir, 'test_data', test_name, 'top_bit.golden.v'), tmp_top_v))
        self.assertTrue(compare(os.path.join(
            cur_dir, 'test_data', test_name, 'top_bit.golden.xdc'), tmp_top_xdc))


if __name__ == "__main__":
    unittest.main()

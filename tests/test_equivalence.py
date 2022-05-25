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
import itertools
import tarfile
import subprocess
from fasm2bels.fasm2bels import main


test_names = ["add32", "alu"]


def unpack_tar(tar_file):
    tar = tarfile.open(name=tar_file, mode="r:gz")
    tar.extractall(path=os.path.dirname(tar_file))


class TestEquivalence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.channels_file = tempfile.NamedTemporaryFile(
            suffix='channels.db', delete=False)
        cls.channels_file.close()
        os.unlink(cls.channels_file.name)

    @classmethod
    def tearDownClass(cls):
        os.unlink(cls.channels_file.name)

    @parameterized.expand(itertools.product(test_names))
    def test_equivalence(self, test_name):
        cur_dir = os.path.dirname(__file__)
        base_dir = os.path.join(cur_dir, '..')
        db_root = os.path.join(base_dir, 'third_party', 'prjxray-db', 'artix7')
        bitread = os.path.join(base_dir, 'third_party', 'prjxray', 'build',
                               'tools', 'bitread')
        bit_file = os.path.join(cur_dir, 'equivalence_checking_data', test_name,
                                '{}.bit'.format(test_name))
        xdc_input = os.path.join(cur_dir, 'equivalence_checking_data', test_name,
                                 '{}.xdc'.format(test_name))

        unpack_tar(os.path.join(cur_dir, 'equivalence_checking_data', test_name, "{}.tar.gz".format(test_name)))

        temp_dir = tempfile.mkdtemp(
            prefix="test_fasm2bels_equivalence_{}_".format(test_name),
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
            '--input_xdc',
            xdc_input
        ]

        main()

        tmp_top_v = os.path.join(temp_dir, generated_top_v)
        tmp_top_xdc = os.path.join(temp_dir, generated_top_xdc)

        # Check if generated files exists
        self.assertTrue(os.path.exists(tmp_top_v))

        LOG_FILE_NAME = "yosys_log.txt"
        SCRIPT_FILE_NAME = "yosys_compare.ys"

        # Check if generated files are equal to the golden ones
        def compare(file_a, file_b):
            """
            Uses Yosys equivalence checking to compare generated netlist with a
            Vivado generated netlist.
            """

            # Capture path of cells_sim.v from yosys
            cmd = ["yosys-config", "--datdir"]
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,    
            )
            for line in proc.stdout:
                yosys_config_output = line
            proc.communicate()
            if proc.returncode:
                return False
            yosys_share_path = yosys_config_output.strip()

            log_path = os.path.join(temp_dir, LOG_FILE_NAME)

            # Create Yosys script
            script_file_path = os.path.join(temp_dir, SCRIPT_FILE_NAME)

            with open(script_file_path, "w") as fp:
                fp.write("read_verilog " + yosys_share_path + "/xilinx/cells_sim.v" + "\n")
                fp.write("read_verilog " + file_a + "\n")
                fp.write("prep -flatten\n")
                fp.write("hierarchy -auto-top\n")
                fp.write("rename -top gold\n")
                fp.write("splitnets -ports;;\n")
                fp.write("design -stash gold\n")
                fp.write("read_verilog " + yosys_share_path + "/xilinx/cells_sim.v" + "\n")
                fp.write("read_verilog " + file_b + "\n")
                fp.write("prep -flatten\n")
                fp.write("hierarchy -auto-top\n")
                fp.write("rename -top gate\n")
                fp.write("splitnets -ports;;\n")
                fp.write("design -stash gate\n")
                fp.write("read_verilog " + yosys_share_path + "/xilinx/cells_sim.v" + "\n")
                fp.write("design -copy-from gold -as gold gold\n")
                fp.write("design -copy-from gate -as gate gate\n")
                fp.write("equiv_make gold gate equiv\n")
                fp.write("prep -flatten -top equiv\n")
                fp.write("async2sync\n")
                fp.write("equiv_induct\n")
                fp.write("equiv_status -assert\n")

            # Run Yosys
            with open(log_path, "w") as fp:
                cmd = ["yosys", script_file_path]
                proc = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    universal_newlines=True,    
                )
                for line in proc.stdout:
                    fp.write(line)
                    fp.flush()
                proc.communicate()
                if proc.returncode:
                    return False
                
            return True

        self.assertTrue(compare(os.path.join(
            cur_dir, 'equivalence_checking_data', test_name, 'top_bit.golden.v'), tmp_top_v))


if __name__ == "__main__":
    unittest.main()

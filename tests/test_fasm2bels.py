import unittest
from parameterized import parameterized
from unittest.mock import patch
import os
import sys
import tempfile
import filecmp
from fasm2bels.fasm2bels import main


class TestFasm2Bels(unittest.TestCase):
    @parameterized.expand([["simple_ff"], ["iddr"], ["oddr"]])
    def test_simple_ff(self, test_name):
        cur_dir = os.path.dirname(__file__)
        base_dir = os.path.join(cur_dir, '..')
        db_root = os.path.join(base_dir, 'third_party', 'prjxray-db', 'artix7')
        bitread = os.path.join(base_dir, 'third_party', 'prjxray', 'build',
                               'tools', 'bitread')
        bit_file = os.path.join(cur_dir, 'test_data', test_name,
                                '{}.bit'.format(test_name))
        pcf = os.path.join(cur_dir, 'test_data', test_name,
                           '{}.pcf'.format(test_name))
        eblif = os.path.join(cur_dir, 'test_data', test_name,
                             '{}.eblif'.format(test_name))

        temp_dir = tempfile.mkdtemp(
            prefix="test_fasm2bels_{}_".format(test_name), dir='/tmp')

        fasm_file = os.path.join(temp_dir, '{}.fasm'.format(test_name))
        channels_file = os.path.join(temp_dir, 'channels.db')

        iostandard = 'LVCMOS33'
        drive = '12'
        top = 'top'
        part = 'xc7a35tcpg236-1'

        generated_top_v = os.path.join(temp_dir, 'top_bit.v')
        generated_top_xdc = os.path.join(temp_dir, 'top_bit.xdc')

        sys.argv = [
            'fasm2bels', '--db_root', db_root, '--part', part, '--bitread',
            bitread, '--bit_file', bit_file, '--fasm_file', fasm_file, '--pcf',
            pcf, '--eblif', eblif, '--top', top, '--iostandard', iostandard,
            '--drive', drive, '--connection_database', channels_file,
            generated_top_v, generated_top_xdc
        ]

        main()

        tmp_top_v = os.path.join(temp_dir, generated_top_v)
        tmp_top_xdc = os.path.join(temp_dir, generated_top_xdc)

        # Check if generated files exists
        self.assertTrue(os.path.exists(tmp_top_v))
        self.assertTrue(os.path.exists(tmp_top_xdc))

        # Check if generated files are equal to the golden ones
        self.assertTrue(
            filecmp.cmp(
                os.path.join(cur_dir, 'test_data', test_name,
                             'top_bit.golden.v'), tmp_top_v))
        self.assertTrue(
            filecmp.cmp(
                os.path.join(cur_dir, 'test_data', test_name,
                             'top_bit.golden.xdc'), tmp_top_xdc))


if __name__ == "__main__":
    unittest.main()

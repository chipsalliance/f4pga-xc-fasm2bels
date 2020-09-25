import unittest
from parameterized import parameterized
import os
import sys
import tempfile
import filecmp
import itertools
import enum
from fasm2bels.fasm2bels import main


class PinConstraintType(enum.Enum):
    XDC = 0
    PCF = 1


test_names = ["simple_ff", "iddr", "oddr"]
pin_constraint_types = [PinConstraintType.XDC, PinConstraintType.PCF]


class TestFasm2Bels(unittest.TestCase):
    @parameterized.expand(itertools.product(test_names, pin_constraint_types))
    def test_simple_ff(self, test_name, pin_constraint_type):
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

        temp_dir = tempfile.mkdtemp(
            prefix="test_fasm2bels_{}_{}_".format(test_name,
                                                  pin_constraint_type.name),
            dir='/tmp')

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
            bitread, '--bit_file', bit_file, '--fasm_file', fasm_file,
            '--eblif', eblif, '--top', top, '--iostandard', iostandard,
            '--drive', drive, '--connection_database', channels_file,
            '--verilog_file', generated_top_v, '--xdc_file', generated_top_xdc
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

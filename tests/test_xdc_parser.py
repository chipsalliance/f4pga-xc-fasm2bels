import unittest
from parameterized import parameterized
import pathlib
from fasm2bels.lib import parse_xdc
import yaml

xdc_parsing_path = pathlib.Path(__file__).absolute().parent / "test_data" / "xdc_parsing"
xdc_inputs_path = xdc_parsing_path / "xdc_inputs"
yaml_golden_path = xdc_parsing_path / "yaml_golden"

test_names = ["test_basic", "test_dict"]

class TestXdcParser(unittest.TestCase):
    @parameterized.expand(test_names)
    def test_parse_and_compare(self, test_name):
        self.maxDiff = None

        # Get input XDC file
        xdc_path = xdc_inputs_path / (test_name + ".xdc")
        self.assertTrue(xdc_path.is_file())

        # Get golden YAML file
        yaml_path = yaml_golden_path / (test_name + ".yaml")
        self.assertTrue(yaml_path.is_file())

        with open(xdc_path, 'r') as fp:
            constraints = parse_xdc.parse_simple_xdc(fp)

        with open(yaml_path,'r') as fp:
            net_props = yaml.safe_load(fp)

        all_constraints = {}
        for constraint in constraints:
            all_constraints[constraint.net] = constraint.params

        self.assertEqual(all_constraints, net_props)
""" Used to parse XDC files for pin constraints """

from collections import namedtuple
import re

XdcIoConstraint = namedtuple("XdcIoConstraint", "net pad line_str line_num")


def parse_simple_xdc(fp):
    """ Parse a simple XDC file object and yield XdcIoConstraint objects. """

    for line_number, line in enumerate(fp):
        m = re.match(r"^\s*set_property\s+(.*)\[get_ports\s+{(.*)}", line,
                     re.I)
        if not m:
            continue
        properties = m.group(1).strip()
        port = m.group(2).strip()

        # Check for pin property as part of a dictionary, ie:
        # -dict { PACKAGE_PIN N15   IOSTANDARD LVCMOS33 }
        m = re.match(r"-dict\s+{(.*)}", properties)
        if m:
            # Convert tcl dict to python dict
            dict_list = m.group(1).strip().split()
            properties = dict(zip(dict_list[::2], dict_list[1::2]))

            if "PACKAGE_PIN" in properties:
                yield XdcIoConstraint(
                    net=port,
                    pad=properties["PACKAGE_PIN"],
                    line_str=line.strip(),
                    line_num=line_number,
                )
            continue

        # Otherwise, must be a direct set_property, ie:
        # PACKAGE_PIN N15
        property_pair = properties.split()
        assert len(property_pair) == 2, property_pair

        if property_pair[0] == "PACKAGE_PIN":
            yield XdcIoConstraint(
                net=port,
                pad=property_pair[1],
                line_str=line.strip(),
                line_num=line_number,
            )

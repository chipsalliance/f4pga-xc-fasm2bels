""" Used to parse XDC files for pin constraints """

from collections import namedtuple
import re

XdcIoConstraint = namedtuple("XdcIoConstraint",
                             "net pad line_str line_num params")


def parse_simple_xdc(fp):
    """ Parse a simple XDC file object and return list of XdcIoConstraint objects. """

    # For each port, maintain a dictionary of PROPERTIES
    port_to_params = {}

    # For each port, maintain XdcIoConstraint object to return
    port_to_results = {}

    for line_number, line in enumerate(fp):
        m = re.match(r"^\s*set_property\s+(.*)\[\s*get_ports\s+(.*)\]", line,
                     re.I)
        if not m:
            continue
        properties = m.group(1).strip()
        port = m.group(2).strip()

        # Check if port is surrounded by {} braces
        m = re.match(r"{\s*(\S+)\s*}", port)
        if m:
            port = m.group(1).strip()

        if port not in port_to_params:
            # Default DRIVE value is 12.
            port_to_params[port] = {'DRIVE': 12}

        # Check for pin property as part of a dictionary, ie:
        # -dict { PACKAGE_PIN N15   IOSTANDARD LVCMOS33 }
        m = re.match(r"-dict\s+{(.*)}", properties)
        if m:
            # Convert tcl dict to python dict
            dict_list = m.group(1).strip().split()
            properties = dict(zip(dict_list[::2], dict_list[1::2]))

            if "PACKAGE_PIN" in properties:
                port_to_results[port] = XdcIoConstraint(
                    net=port,
                    pad=properties["PACKAGE_PIN"],
                    line_str=line.strip(),
                    line_num=line_number,
                    params=port_to_params[port],
                )

            port_to_params[port].update(properties)
        else:
            # Otherwise, must be a direct set_property, ie:
            # PACKAGE_PIN N15
            property_pair = properties.split()
            assert len(property_pair) == 2, property_pair

            port_to_params[port][property_pair[0]] = property_pair[1]

            if property_pair[0] == "PACKAGE_PIN":
                port_to_results[port] = XdcIoConstraint(
                    net=port,
                    pad=property_pair[1],
                    line_str=line.strip(),
                    line_num=line_number,
                    params=port_to_params[port],
                )

    # Return list of XdcIoConstraint objects
    return [port_to_results[port] for port in port_to_results]

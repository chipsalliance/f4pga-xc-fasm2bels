import re
from .verilog_modeling import Bel, Site, make_inverter_path
from .models_data.gtp_channel_data import ports, params


def get_gtp_channel_site(db, grid, tile, site):
    """ Return the prjxray.tile.Site object for the given GTP site. """
    gridinfo = grid.gridinfo_at_tilename(tile)
    tile_type = db.get_tile_type(gridinfo.tile_type)

    sites = list(tile_type.get_instance_sites(gridinfo))

    for site in sites:
        if "GTPE2_CHANNEL" in site:
            return site

    assert False, (tile, site)


def process_gtp_channel(conn, top, tile_name, features):
    """
    Processes the GTP_CHANNEL tile
    """

    # Filter only GTPE2_CHANNEL related features
    gtp_channel_features = [
        f for f in features if 'GTPE2_CHANNEL.' in f.feature
    ]
    if len(gtp_channel_features) == 0:
        return

    site = get_gtp_channel_site(
        top.db, top.grid, tile=tile_name, site='GTPE2_CHANNEL'
    )

    # Create the site
    gtp_site = Site(gtp_channel_features, site)

    # Create the GTPE2_CHANNEL bel and add its ports
    gtp = Bel('GTPE2_CHANNEL')
    gtp.set_bel('GTPE2_CHANNEL')

    # If the GTPE2_CHANNEL is not used then skip the rest
    if not gtp_site.has_feature("IN_USE"):
        return

    for param, param_info in params.items():
        param_type = param_info["type"]
        param_digits = param_info["digits"]

        value = None
        if param_type == "INT":
            value = gtp_site.decode_multi_bit_feature(
                feature=param, allow_partial_match=False
            )

            encoding_idx = param_info["encoding"].index(value)
            value = param_info["values"][encoding_idx]
        elif param_type == "BIN":
            value = gtp_site.decode_multi_bit_feature(
                feature=param, allow_partial_match=False
            )
            value = "{digits}'b{value:0{digits}b}".format(
                digits=param_digits, value=value
            )
        elif param_type == "BOOL":
            value = '"TRUE"' if gtp_site.has_feature(param) else '"FALSE"'
        elif param_type == "STR":
            for val in param_info["values"]:
                if gtp_site.has_feature(val):
                    value = '"{}"'.format(val)

            if value is None:
                continue

        gtp.parameters[param] = value

    inv_ports = [
        "TXUSRCLK",
        "TXUSRCLK2",
        "TXPHDLYTSTCLK",
        "SIGVALIDCLK",
        "RXUSRCLK",
        "RXUSRCLK2",
        "DRPCLK",
        "DMONITORCLK",
        "CLKRSVD0",
        "CLKRSVD1",
    ]

    for port in inv_ports:
        inv_feature = "INV_{}".format(port)
        if gtp_site.has_feature(inv_feature):
            gtp.parameters["IS_{}_INVERTED".format(port)] = 1

    for in_port, width in ports["inputs"]:
        for i in range(width):
            if width > 1:
                port = "{}[{}]".format(in_port, i)
                wire = "{}{}".format(in_port, i)
            else:
                port = wire = in_port

            gtp_site.add_sink(gtp, port, wire, gtp.bel, wire)

    for out_port, width in ports["outputs"]:
        for i in range(width):
            if width > 1:
                port = "{}[{}]".format(out_port, i)
                wire = "{}{}".format(out_port, i)
            else:
                port = wire = out_port

            gtp_site.add_source(gtp, port, wire, gtp.bel, wire)

    top_wire_tx_p = top.add_top_in_port(tile_name, site.name, "IPAD_TX_P")
    top_wire_tx_n = top.add_top_in_port(tile_name, site.name, "IPAD_TX_N")
    top_wire_rx_p = top.add_top_in_port(tile_name, site.name, "IPAD_RX_P")
    top_wire_rx_n = top.add_top_in_port(tile_name, site.name, "IPAD_RX_N")

    gtp.connections["GTPTXP"] = top_wire_tx_p
    gtp.connections["GTPTXN"] = top_wire_tx_n
    gtp.connections["GTPRXP"] = top_wire_rx_p
    gtp.connections["GTPRXN"] = top_wire_rx_n

    # Add the bel
    gtp_site.add_bel(gtp)

    # Add the sites
    top.add_site(gtp_site)

    top.disable_drc("REQP-47")

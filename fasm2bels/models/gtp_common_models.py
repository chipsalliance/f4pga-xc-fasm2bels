import re
from .verilog_modeling import Bel, Site, make_inverter_path
from .models_data.gtp_common_data import ports, params


def get_gtp_common_site(db, grid, tile, site):
    """ Return the prjxray.tile.Site object for the given GTP site. """
    gridinfo = grid.gridinfo_at_tilename(tile)
    tile_type = db.get_tile_type(gridinfo.tile_type)

    sites = list(tile_type.get_instance_sites(gridinfo))

    for site in sites:
        if "GTPE2_COMMON" in site:
            return site

    assert False, (tile, site)


def ibufds_y(site):
    IBUFDS_RE = re.compile('IBUFDS_GTE2.*Y([0-9]+)')

    m = IBUFDS_RE.fullmatch(site)
    assert m is not None, site

    return int(m.group(1))


def get_ibufds_site(db, grid, tile, generic_site):
    y = ibufds_y(generic_site)

    gridinfo = grid.gridinfo_at_tilename(tile)

    tile = db.get_tile_type(gridinfo.tile_type)

    for site in tile.get_instance_sites(gridinfo):
        if not site.name.startswith("IBUFDS"):
            continue

        instance_y = ibufds_y(site.name)

        if y == (instance_y % 2):
            return site

    assert False, (tile, generic_site)


def process_gtp_common(conn, top, tile_name, features):
    """
    Processes the GTP_COMMON tile
    """

    # Filter only GTPE2_COMMON related features
    gtp_common_features = [f for f in features if 'GTPE2_COMMON.' in f.feature]
    if len(gtp_common_features) == 0:
        return

    # Create the site
    gtp_site = Site(
        gtp_common_features,
        get_gtp_common_site(
            top.db, top.grid, tile=tile_name, site='GTPE2_COMMON'
        )
    )

    # Create the GTPE2_COMMON bel and add its ports
    gtp = Bel('GTPE2_COMMON')
    gtp.set_bel('GTPE2_COMMON')

    # If the GTPE2_COMMON is not used then skip the rest
    if not gtp_site.has_feature("IN_USE"):
        return

    for param, param_info in params.items():
        param_type = param_info["type"]

        value = gtp_site.decode_multi_bit_feature(
            feature=param, allow_partial_match=False
        )

        if param_type == "INT":
            encoding_idx = param_info["encoding"].index(value)
            value = param_info["values"][encoding_idx]

        gtp.parameters[param] = value

    for port in ["DRPCLK", "PLL0LOCKDETCLK", "PLL1LOCKDETCLK"]:
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

    for port in ["GTREFCLK0", "GTREFCLK1"]:
        if gtp_site.has_feature("{}_USED".format(port)):
            gtp_site.add_sink(gtp, port, port, gtp.bel, port)

    # Add the bel
    gtp_site.add_bel(gtp)

    for i in range(2):
        generic_site = 'IBUFDS_GTE2_Y{}'.format(i)

        ibufds_features = [f for f in features if generic_site in f.feature]

        if len(ibufds_features) == 0:
            continue

        site = get_ibufds_site(
            top.db, top.grid, tile=tile_name, generic_site=generic_site
        )
        ibufds_site = Site(ibufds_features, site)

        if not ibufds_site.has_feature("IN_USE"):
            continue

        # Create the IBUFDS_GTE2 bel and add its ports
        ibufds = Bel('IBUFDS_GTE2')
        ibufds.set_bel('IBUFDS_GTE2')

        if ibufds_site.has_feature("CLKCM_CFG"):
            ibufds.parameters["CLKCM_CFG"] = '"TRUE"'
        if ibufds_site.has_feature("CLKRCV_TRST"):
            ibufds.parameters["CLKRCV_TRST"] = '"TRUE"'

        for port in ["O", "ODIV2"]:
            ibufds_site.add_source(ibufds, port, port, ibufds.bel, port)

        ibufds_site.add_sink(ibufds, "CEB", "CEB", ibufds.bel, "CEB")

        top_wire_p = top.add_top_in_port(tile_name, site.name, "IPAD_P")
        top_wire_n = top.add_top_in_port(tile_name, site.name, "IPAD_N")

        ibufds.connections["I"] = top_wire_p
        ibufds.connections["IB"] = top_wire_n

        ibufds_site.add_bel(ibufds)
        top.add_site(ibufds_site)

    # Add the sites
    top.add_site(gtp_site)

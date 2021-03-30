import re
import json
import os
from .verilog_modeling import Bel, Site, make_inverter_path
from .utils import add_bel_attributes, add_site_ports

ZERO_VAL_PARAMS = {
    "CBCC_DATA_SOURCE_SEL": "ENCODED",
    "RXBUF_ADDR_MODE": "FULL",
    "RXOOB_CLK_CFG": "PMA",
    "RXSLIDE_MODE": "OFF",
    "RX_XCLK_SEL": "RXREC",
    "SATA_PLL_CFG": "VCO_3000MHZ",
    "TXPI_PPMCLK_SEL": "TXUSRCLK",
    "TX_DRIVE_MODE": "DIRECT",
    "TX_XCLK_SEL": "TXOUT",
}


def get_gtp_channel_site(db, grid, tile, site_type):
    """ Return the prjxray.tile.Site object for the given GTP site. """
    gridinfo = grid.gridinfo_at_tilename(tile)
    tile_type = db.get_tile_type(gridinfo.tile_type)

    sites = list(tile_type.get_instance_sites(gridinfo))

    gtp_channel_sites = [site for site in sites if site.type == site_type]
    assert len(gtp_channel_sites) == 1

    return gtp_channel_sites[0]


def process_gtp_channel(conn, top, tile_name, features):
    """
    Processes the GTP_CHANNEL tile
    """

    site_name = "GTPE2_CHANNEL"

    # Filter only GTPE2_CHANNEL related features
    gtp_channel_features = [
        f for f in features if '{}.'.format(site_name) in f.feature
    ]
    if len(gtp_channel_features) == 0:
        return

    site = get_gtp_channel_site(
        top.db, top.grid, tile=tile_name, site_type=site_name)

    # Create the site
    gtp_site = Site(gtp_channel_features, site)

    # Create the GTPE2_CHANNEL bel and add its ports
    gtp = Bel(site_name)
    gtp.set_bel(site_name)

    # If the GTPE2_CHANNEL is not used then skip the rest
    if not gtp_site.has_feature("IN_USE"):
        return

    db_root = top.db.db_root

    # Add basic attributes to the GTP bel
    add_bel_attributes(db_root, site_name.lower(), gtp_site, gtp)

    for param, zero_val in ZERO_VAL_PARAMS.items():
        if param not in gtp.parameters:
            gtp.parameters[param] = '"{}"'.format(zero_val)

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

    # Adding ports to the GTP site
    add_site_ports(db_root, site_name.lower(), gtp_site, gtp, ["PLL", "GTP"])

    top_wire_tx_p = top.add_top_out_port(tile_name, site.name, "OPAD_TX_P")
    top_wire_tx_n = top.add_top_out_port(tile_name, site.name, "OPAD_TX_N")
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

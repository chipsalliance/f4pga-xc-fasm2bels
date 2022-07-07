#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2021-2022 F4PGA Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

import re
import json
import os
from .verilog_modeling import Bel, Site, make_inverter_path
from .utils import add_bel_attributes, add_site_ports


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

    site_name = "GTPE2_COMMON"

    # Filter only GTPE2_COMMON related features
    gtp_common_features = [
        f for f in features if '{}.'.format(site_name) in f.feature
    ]
    if len(gtp_common_features) == 0:
        return

    # Create the site
    gtp_site = Site(
        gtp_common_features,
        get_gtp_common_site(top.db, top.grid, tile=tile_name, site=site_name))

    # Create the GTPE2_COMMON bel and add its ports
    gtp = Bel(site_name)
    gtp.set_bel(site_name)

    # If the GTPE2_COMMON is not used then skip the rest
    if not gtp_site.has_feature("IN_USE"):
        return

    db_root = top.db.db_root

    # Add basic attributes to the GTP bel
    add_bel_attributes(db_root, site_name.lower(), gtp_site, gtp)

    for port in ["DRPCLK", "PLL0LOCKDETCLK", "PLL1LOCKDETCLK"]:
        inv_feature = "INV_{}".format(port)
        if gtp_site.has_feature(inv_feature):
            gtp.parameters["IS_{}_INVERTED".format(port)] = 1

    any_gtrefclk_used = False
    for port in ["GTREFCLK0", "GTREFCLK1"]:
        if gtp_site.has_feature("{}_USED".format(port)):
            gtp_site.add_sink(gtp, port, port, gtp.bel, port)
            any_gtrefclk_used = True

    assert any_gtrefclk_used, "ERROR: no GTREFCLK ports is used!"

    # Adding ports to the GTP site
    add_site_ports(db_root, site_name.lower(), gtp_site, gtp, ["GT"])

    # Add the bel
    gtp_site.add_bel(gtp)

    for i in range(2):
        generic_site = 'IBUFDS_GTE2_Y{}'.format(i)

        ibufds_features = [f for f in features if generic_site in f.feature]

        if len(ibufds_features) == 0:
            continue

        site = get_ibufds_site(
            top.db, top.grid, tile=tile_name, generic_site=generic_site)
        ibufds_site = Site(ibufds_features, site)

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

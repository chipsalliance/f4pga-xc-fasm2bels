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

import re
import json
import os
from .verilog_modeling import Bel, Site, make_inverter_path
from .utils import add_bel_attributes, add_site_ports


def get_pcie_site(db, grid, tile, site):
    """ Return the prjxray.tile.Site object for the given PCIE site. """
    gridinfo = grid.gridinfo_at_tilename(tile)
    tile_type = db.get_tile_type(gridinfo.tile_type)

    sites = list(tile_type.get_instance_sites(gridinfo))

    for site in sites:
        if "PCIE_2_1" in site:
            return site

    assert False, (tile, site)


def process_pcie(conn, top, tile_name, features):
    """
    Processes the PCIE_BOT tile
    """

    site_name = "PCIE_2_1"

    # Filter only PCIE_2_1 related features
    pcie_features = [f for f in features if 'PCIE.' in f.feature]
    if len(pcie_features) == 0:
        return

    site = get_pcie_site(top.db, top.grid, tile=tile_name, site=site_name)

    # Create the site
    pcie_site = Site(pcie_features, site)

    # Create the PCIE_2_1 bel and add its ports
    pcie = Bel(site_name)
    pcie.set_bel(site_name)

    db_root = top.db.db_root

    # Add basic attributes to the PCIE bel
    add_bel_attributes(db_root, site_name.lower(), pcie_site, pcie)

    # Add site port to the PCIE bel
    add_site_ports(db_root, site_name.lower(), pcie_site, pcie)

    # Add the bel
    pcie_site.add_bel(pcie)

    # Add the sites to top
    top.add_site(pcie_site)

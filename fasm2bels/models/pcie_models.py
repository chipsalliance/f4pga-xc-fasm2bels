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

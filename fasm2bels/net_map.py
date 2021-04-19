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

from collections import namedtuple
from .lib.parse_route import find_net_sources
import re
""" Utilities for match VPR route names with xc7 site pin sources. """


class Net(namedtuple('Net', 'name wire_pkey tile site_pin')):
    """
    Args:
        name (str): VPR net name
        wire_pkey (int): Wire table primary key.  This is unique in the part.
        tile (str): Name of tile this wire belongs too.  This is redundant
            information wire_pkey uniquely indentifies the tile.
        site_pin (str): Name of site pin this wire belongs. This is redundant
            information wire_pkey uniquely indentifies the site pin.
    """
    pass


# CLBLL_L.CLBLL_LL_A1[0] -> (CLBLL_L, CLBLL_LL_A1)
PIN_NAME_TO_PARTS = re.compile(r'^([^\.]+)\.([^\]]+)\[0\]$')


def create_net_list(conn, graph, route_file, vpr_grid_map):
    """ From connection database, rrgraph and VPR route file, yields net_map.Net.
    """
    c = conn.cursor()

    for net, node in find_net_sources(route_file):
        gridloc = graph.loc_map[(node.x_low, node.y_low)]
        pin_name = graph.pin_ptc_to_name_map[(gridloc.block_type_id, node.ptc)]

        # Do not add synthetic nets to map.
        if pin_name.startswith('SYN-'):
            continue

        m = PIN_NAME_TO_PARTS.match(pin_name)
        assert m is not None, pin_name

        pin = m.group(2)

        canon_loc_list = vpr_grid_map[(node.x_low, node.y_low)]

        wire_found = False

        for can_x, can_y in canon_loc_list:
            c.execute(
                """
WITH tiles(phy_tile_pkey, tile_name, tile_type_pkey) AS (
    SELECT DISTINCT pkey, name, tile_type_pkey FROM phy_tile
    WHERE grid_x = ? AND grid_y = ?
)
SELECT wire_in_tile.pkey, tiles.phy_tile_pkey, tiles.tile_name
FROM wire_in_tile
INNER JOIN tiles
ON tiles.tile_type_pkey = wire_in_tile.phy_tile_type_pkey
WHERE
    name = ?;""", (can_x, can_y, pin))

            results = c.fetchall()

            if len(results) != 1:
                continue

            wire_in_tile_pkey, phy_tile_pkey, tile_name = results[0]
            wire_found = True

            break

        assert wire_found, (node, pin)

        c.execute(
            "SELECT pkey FROM wire WHERE wire_in_tile_pkey = ? AND phy_tile_pkey = ?",
            (wire_in_tile_pkey, phy_tile_pkey))
        wire_pkey = c.fetchone()[0]

        yield Net(name=net, wire_pkey=wire_pkey, tile=tile_name, site_pin=pin)

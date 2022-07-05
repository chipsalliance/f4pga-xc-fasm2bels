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

import os
import datetime
import argparse

from prjxray.db import Database

from fasm2bels.lib import progressbar_utils
from fasm2bels.database.connection_database_cache import DatabaseCache
"""
This file is used to create a basic form of the device database
imported from the prjxray database.

The connection database will hold information on nodes, sites and
tiles that are required when reconstructing the routing tree
of a given FASM file.
"""


def create_tables(conn):
    """ Create connection database scheme. """
    connection_database_sql_file = os.path.join(
        os.path.dirname(__file__), "connection_database.sql")
    with open(connection_database_sql_file, 'r') as f:
        c = conn.cursor()
        c.executescript(f.read())
        conn.commit()


def import_site_type(db, write_cur, site_types, site_type_name):
    assert site_type_name not in site_types
    site_type = db.get_site_type(site_type_name)

    if site_type_name in site_types:
        return

    write_cur.execute("INSERT INTO site_type(name) VALUES (?)",
                      (site_type_name, ))
    site_types[site_type_name] = write_cur.lastrowid

    for site_pin in site_type.get_site_pins():
        pin_info = site_type.get_site_pin(site_pin)

        write_cur.execute(
            """
INSERT INTO site_pin(name, site_type_pkey, direction)
VALUES
  (?, ?, ?)""", (pin_info.name, site_types[site_type_name],
                 pin_info.direction.value))


def build_pss_object_mask(db, tile_type_name):
    """
    Looks for objects present in PSS* tiles of Zynq7 and masks out those
    that are purely PS related and not configued by the PL.
    """

    tile_type = db.get_tile_type(tile_type_name)
    sites = tile_type.get_sites()

    masked_wires = []
    masked_pips = []

    # Get all IOPADS for MIO and DDR signals
    iopad_sites = [s for s in sites if s.type == "IOPAD"]
    for site in iopad_sites:

        # Get pins/wires
        site_pins = [p for p in site.site_pins if p.name == "IO"]
        for site_pin in site_pins:

            # Mask the wire
            masked_wires.append(site_pin.wire)

            # Find a PIP(s) for this wire, mask them as well as wires on
            # their other sides.
            for p in tile_type.get_pips():
                if p.net_from == site_pin.wire:
                    masked_pips.append(p.name)
                    masked_wires.append(p.net_to)
                if p.net_to == site_pin.wire:
                    masked_pips.append(p.name)
                    masked_wires.append(p.net_from)

    # Masked sites names
    masked_sites = [(s.prefix, s.name) for s in iopad_sites]

    return masked_sites, masked_wires, masked_pips


def import_tile_type(db, write_cur, tile_types, site_types, tile_type_name):
    assert tile_type_name not in tile_types
    tile_type = db.get_tile_type(tile_type_name)

    # For Zynq7 PSS* tiles build a list of sites, wires and PIPs to ignore
    if tile_type_name.startswith("PSS"):
        masked_sites, masked_wires, masked_pips = build_pss_object_mask(
            db, tile_type_name)

    else:
        masked_sites = []
        masked_wires = []

    write_cur.execute("INSERT INTO tile_type(name) VALUES (?)",
                      (tile_type_name, ))
    tile_types[tile_type_name] = write_cur.lastrowid

    wires = {}
    for wire, wire_rc_element in tile_type.get_wires().items():
        if wire in masked_wires:
            continue

        write_cur.execute(
            """
INSERT INTO wire_in_tile(name, phy_tile_type_pkey, tile_type_pkey)
VALUES
  (?, ?, ?)""", (
                wire,
                tile_types[tile_type_name],
                tile_types[tile_type_name],
            ))
        wires[wire] = write_cur.lastrowid

    for site in tile_type.get_sites():
        if (site.prefix, site.name) in masked_sites:
            continue

        if site.type not in site_types:
            import_site_type(db, write_cur, site_types, site.type)


def add_wire_to_site_relation(db, write_cur, tile_types, site_types,
                              tile_type_name):
    tile_type = db.get_tile_type(tile_type_name)
    for site in tile_type.get_sites():

        if site.type not in site_types:
            continue

        write_cur.execute(
            """
INSERT INTO site(name, x_coord, y_coord, site_type_pkey, tile_type_pkey)
VALUES
  (?, ?, ?, ?, ?)""", (site.name, site.x, site.y, site_types[site.type],
                       tile_types[tile_type_name]))

        site_pkey = write_cur.lastrowid

        for site_pin in site.site_pins:
            write_cur.execute(
                """
SELECT
  pkey
FROM
  site_pin
WHERE
  name = ?
  AND site_type_pkey = ?""", (site_pin.name, site_types[site.type]))
            result = write_cur.fetchone()
            site_pin_pkey = result[0]

            write_cur.execute(
                """
UPDATE
  wire_in_tile
SET
  site_pkey = ?,
  site_pin_pkey = ?
WHERE
  name = ?
  and tile_type_pkey = ?;""", (site_pkey, site_pin_pkey, site_pin.wire,
                               tile_types[tile_type_name]))


def build_tile_type_indicies(write_cur):
    write_cur.execute(
        "CREATE INDEX site_pin_index ON site_pin(name, site_type_pkey);")
    write_cur.execute(
        "CREATE INDEX wire_name_index ON wire_in_tile(name, tile_type_pkey);")
    write_cur.execute(
        "CREATE INDEX wire_tile_site_index ON wire_in_tile(tile_type_pkey, site_pkey);"
    )
    write_cur.execute(
        "CREATE INDEX wire_site_pin_index ON wire_in_tile(site_pin_pkey);")
    write_cur.execute(
        "CREATE INDEX tile_type_index ON phy_tile(tile_type_pkey);")


def build_other_indicies(write_cur):
    write_cur.execute("CREATE INDEX phy_tile_name_index ON phy_tile(name);")
    write_cur.execute(
        "CREATE INDEX phy_tile_location_index ON phy_tile(grid_x, grid_y);")
    write_cur.execute(
        "CREATE INDEX site_instance_index on site_instance(name);")


def import_phy_grid(db, grid, conn):
    write_cur = conn.cursor()

    tile_types = {}
    site_types = {}

    for tile in grid.tiles():
        gridinfo = grid.gridinfo_at_tilename(tile)

        if gridinfo.tile_type not in tile_types:
            if gridinfo.tile_type in tile_types:
                continue

            import_tile_type(db, write_cur, tile_types, site_types,
                             gridinfo.tile_type)

    write_cur.connection.commit()

    build_tile_type_indicies(write_cur)
    write_cur.connection.commit()

    for tile_type in tile_types:
        add_wire_to_site_relation(db, write_cur, tile_types, site_types,
                                  tile_type)

    for tile in grid.tiles():
        gridinfo = grid.gridinfo_at_tilename(tile)

        loc = grid.loc_of_tilename(tile)
        # tile: pkey name tile_type_pkey grid_x grid_y
        write_cur.execute(
            """
INSERT INTO phy_tile(name, tile_type_pkey, grid_x, grid_y)
VALUES
  (?, ?, ?, ?)""", (
                tile,
                tile_types[gridinfo.tile_type],
                loc.grid_x,
                loc.grid_y,
            ))
        phy_tile_pkey = write_cur.lastrowid

        tile_type = db.get_tile_type(gridinfo.tile_type)
        for site, instance_site in zip(tile_type.sites,
                                       tile_type.get_instance_sites(gridinfo)):
            write_cur.execute(
                """
INSERT INTO site_instance(name, x_coord, y_coord, site_pkey, phy_tile_pkey, prohibited)
SELECT ?, ?, ?, site.pkey, ?, ?
FROM site
WHERE
    site.name = ?
AND
    site.x_coord = ?
AND
    site.y_coord = ?
AND
    site.site_type_pkey = (SELECT pkey FROM site_type WHERE name = ?)
AND
    tile_type_pkey = ?;
                """, (
                    instance_site.name,
                    instance_site.x,
                    instance_site.y,
                    phy_tile_pkey,
                    instance_site.name in gridinfo.prohibited_sites,
                    site.name,
                    site.x,
                    site.y,
                    site.type,
                    tile_types[gridinfo.tile_type],
                ))

    build_other_indicies(write_cur)
    write_cur.connection.commit()


def import_nodes(db, grid, conn):
    # Some nodes are just 1 wire, so start by enumerating all wires.

    cur = conn.cursor()
    write_cur = conn.cursor()
    write_cur.execute("""BEGIN EXCLUSIVE TRANSACTION;""")

    tile_wire_map = {}
    wires = {}
    for tile in progressbar_utils.progressbar(grid.tiles()):
        gridinfo = grid.gridinfo_at_tilename(tile)
        tile_type = db.get_tile_type(gridinfo.tile_type)

        cur.execute(
            """SELECT pkey, tile_type_pkey FROM phy_tile WHERE name = ?;""",
            (tile, ))
        phy_tile_pkey, tile_type_pkey = cur.fetchone()

        for wire in tile_type.get_wires():
            # pkey node_pkey tile_pkey wire_in_tile_pkey
            cur.execute(
                """
SELECT pkey FROM wire_in_tile WHERE name = ? and tile_type_pkey = ?;""",
                (wire, tile_type_pkey))

            wire_in_tile_pkey = cur.fetchone()
            if wire_in_tile_pkey is None:
                continue
            wire_in_tile_pkey = wire_in_tile_pkey[0]

            write_cur.execute(
                """
INSERT INTO wire(phy_tile_pkey, wire_in_tile_pkey)
VALUES
  (?, ?);""", (phy_tile_pkey, wire_in_tile_pkey))

            assert (tile, wire) not in tile_wire_map
            wire_pkey = write_cur.lastrowid
            tile_wire_map[(tile, wire)] = wire_pkey
            wires[wire_pkey] = None

    write_cur.execute("""COMMIT TRANSACTION;""")

    connections = db.connections()

    for connection in progressbar_utils.progressbar(
            connections.get_connections()):
        a_pkey = tile_wire_map[(connection.wire_a.tile,
                                connection.wire_a.wire)]
        b_pkey = tile_wire_map[(connection.wire_b.tile,
                                connection.wire_b.wire)]

        a_node = wires[a_pkey]
        b_node = wires[b_pkey]

        if a_node is None:
            a_node = set((a_pkey, ))

        if b_node is None:
            b_node = set((b_pkey, ))

        if a_node is not b_node:
            a_node |= b_node

            for wire in a_node:
                wires[wire] = a_node

    nodes = {}
    for wire_pkey, node in wires.items():
        if node is None:
            node = set((wire_pkey, ))

        assert wire_pkey in node

        nodes[id(node)] = node

    wires_assigned = set()
    for node in progressbar_utils.progressbar(nodes.values()):
        write_cur.execute("""INSERT INTO node(number_pips) VALUES (0);""")
        node_pkey = write_cur.lastrowid

        for wire_pkey in node:
            wires_assigned.add(wire_pkey)
            write_cur.execute(
                """
            UPDATE wire
                SET node_pkey = ?
                WHERE pkey = ?
            ;""", (node_pkey, wire_pkey))

    assert len(set(wires.keys()) ^ wires_assigned) == 0

    del tile_wire_map
    del nodes
    del wires

    write_cur.execute(
        "CREATE INDEX wire_in_tile_index ON wire(wire_in_tile_pkey);")
    write_cur.execute(
        "CREATE INDEX wire_index ON wire(phy_tile_pkey, wire_in_tile_pkey);")
    write_cur.execute("CREATE INDEX wire_node_index ON wire(node_pkey);")

    write_cur.connection.commit()


def count_sites_on_nodes(conn):
    cur = conn.cursor()

    print("{}: Counting sites on nodes".format(datetime.datetime.now()))
    cur.execute("""
WITH node_sites(node_pkey, number_site_pins) AS (
  SELECT
    wire.node_pkey,
    count(wire_in_tile.site_pin_pkey)
  FROM
    wire_in_tile
    INNER JOIN wire ON wire.wire_in_tile_pkey = wire_in_tile.pkey
  WHERE
    wire_in_tile.site_pin_pkey IS NOT NULL
  GROUP BY
    wire.node_pkey
)
SELECT
  max(node_sites.number_site_pins)
FROM
  node_sites;
""")

    # Nodes are only expected to have 1 site
    assert cur.fetchone()[0] == 1

    print("{}: Assigning site wires for nodes".format(datetime.datetime.now()))
    cur.execute("""
WITH site_wires(wire_pkey, node_pkey) AS (
  SELECT
    wire.pkey,
    wire.node_pkey
  FROM
    wire_in_tile
    INNER JOIN wire ON wire.wire_in_tile_pkey = wire_in_tile.pkey
  WHERE
    wire_in_tile.site_pin_pkey IS NOT NULL
)
UPDATE
  node
SET
  site_wire_pkey = (
    SELECT
      site_wires.wire_pkey
    FROM
      site_wires
    WHERE
      site_wires.node_pkey = node.pkey
  );
      """)

    cur.connection.commit()


def create_channels(db_root, part, connection_database):
    db = Database(db_root, part)
    grid = db.grid()

    if os.path.exists(connection_database):
        return

    with DatabaseCache(connection_database) as conn:
        create_tables(conn)

        print("{}: About to load database".format(datetime.datetime.now()))
        import_phy_grid(db, grid, conn)
        print("{}: Initial database formed".format(datetime.datetime.now()))
        import_nodes(db, grid, conn)
        print("{}: Connections made".format(datetime.datetime.now()))
        count_sites_on_nodes(conn)
        print("{}: Counted sites".format(datetime.datetime.now()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--db-root',
        required=True,
        help="Path to prjxray database for given FASM file part.")
    parser.add_argument(
        '--part', required=True, help="Name of part being targeted.")
    parser.add_argument(
        '--connection-database-output',
        required=True,
        help="Path to SQLite3 database for the given part.")

    args = parser.parse_args()

    create_channels(args.db_root, args.part, args.connection_database_output)


if __name__ == "__main__":
    main()

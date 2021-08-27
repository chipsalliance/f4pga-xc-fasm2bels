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

import functools


def create_maybe_get_wire(conn):
    c = conn.cursor()

    @functools.lru_cache(maxsize=None)
    def get_tile_type_pkey(tile):
        c.execute('SELECT pkey, tile_type_pkey FROM phy_tile WHERE name = ?',
                  (tile, ))
        return c.fetchone()

    @functools.lru_cache(maxsize=None)
    def maybe_get_wire(tile, wire):
        phy_tile_pkey, tile_type_pkey = get_tile_type_pkey(tile)

        c.execute(
            'SELECT pkey FROM wire_in_tile WHERE phy_tile_type_pkey = ? and name = ?',
            (tile_type_pkey, wire))

        result = c.fetchone()

        if result is None:
            return None

        wire_in_tile_pkey = result[0]

        c.execute(
            'SELECT pkey FROM wire WHERE phy_tile_pkey = ? AND wire_in_tile_pkey = ?',
            (phy_tile_pkey, wire_in_tile_pkey))

        return c.fetchone()[0]

    return maybe_get_wire


def get_node_pkey(conn, wire_pkey):
    c = conn.cursor()

    c.execute("SELECT node_pkey FROM wire WHERE pkey = ?", (wire_pkey, ))

    return c.fetchone()[0]


def get_wires_in_node(conn, node_pkey):
    c = conn.cursor()

    c.execute("SELECT pkey FROM wire WHERE node_pkey = ?", (node_pkey, ))

    for row in c.fetchall():
        yield row[0]


def get_wire(conn, phy_tile_pkey, wire_in_tile_pkey):
    c = conn.cursor()
    c.execute(
        "SELECT pkey FROM wire WHERE wire_in_tile_pkey = ? AND phy_tile_pkey = ?;",
        (
            wire_in_tile_pkey,
            phy_tile_pkey,
        ))
    return c.fetchone()[0]


def get_tile_type(conn, tile_name):
    c = conn.cursor()

    c.execute(
        """
SELECT name FROM tile_type WHERE pkey = (
    SELECT tile_type_pkey FROM phy_tile WHERE name = ?);""", (tile_name, ))

    return c.fetchone()[0]


def get_wire_pkey(conn, tile_name, wire):
    c = conn.cursor()
    c.execute(
        """
WITH selected_tile(phy_tile_pkey, tile_type_pkey) AS (
  SELECT
    pkey,
    tile_type_pkey
  FROM
    phy_tile
  WHERE
    name = ?
)
SELECT
  wire.pkey
FROM
  wire
WHERE
  wire.phy_tile_pkey = (
    SELECT
      selected_tile.phy_tile_pkey
    FROM
      selected_tile
  )
  AND wire.wire_in_tile_pkey = (
    SELECT
      wire_in_tile.pkey
    FROM
      wire_in_tile
    WHERE
      wire_in_tile.name = ?
      AND wire_in_tile.phy_tile_type_pkey = (
        SELECT
          tile_type_pkey
        FROM
          selected_tile
      )
  );
""", (tile_name, wire))

    results = c.fetchone()
    assert results is not None, (tile_name, wire)
    return results[0]

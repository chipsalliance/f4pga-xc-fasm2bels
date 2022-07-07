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

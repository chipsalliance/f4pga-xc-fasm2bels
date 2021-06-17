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

from .verilog_modeling import Bel, Site, make_site_pin_map, make_inverter_path
from fasm2bels.make_routes import make_routes, ZERO_NET, ONE_NET

BUFHCE_RE = re.compile('BUFHCE_X([0-9]+)Y([0-9]+)')


def get_bufg_site(db, grid, tile, generic_site):
    y = int(generic_site[generic_site.find('Y') + 1:])
    if '_TOP_' in tile:
        y += 16

    site_name = 'BUFGCTRL_X0Y{}'.format(y)

    gridinfo = grid.gridinfo_at_tilename(tile)

    tile = db.get_tile_type(gridinfo.tile_type)

    for site in tile.get_instance_sites(gridinfo):
        if site.name == site_name:
            return site

    assert False, (tile, generic_site)


def bufhce_xy(site):
    m = BUFHCE_RE.fullmatch(site)
    assert m is not None, site

    return int(m.group(1)), int(m.group(2))


def get_bufhce_site(db, grid, tile, generic_site):
    x, y = bufhce_xy(generic_site)

    gridinfo = grid.gridinfo_at_tilename(tile)

    tile = db.get_tile_type(gridinfo.tile_type)

    for site in tile.get_instance_sites(gridinfo):
        instance_x, instance_y = bufhce_xy(site.name)

        if instance_x == x and y == (instance_y % 12):
            return site

    assert False, (tile, generic_site)


def process_bufg(conn, top, tile, features):
    bufgs = {}
    for f in features:
        parts = f.feature.split('.')

        if parts[1] != 'BUFGCTRL':
            continue

        if parts[2] not in bufgs:
            bufgs[parts[2]] = []

        bufgs[parts[2]].append(f)

    for bufg, features in bufgs.items():
        set_features = set()

        for f in features:
            if f.value == 0:
                continue

            parts = f.feature.split('.')

            set_features.add('.'.join(parts[3:]))

        if 'IN_USE' not in set_features:
            continue

        bufg_site = get_bufg_site(top.db, top.grid, tile,
                                  features[0].feature.split('.')[2])
        site = Site(features, site=bufg_site)

        bel = Bel('BUFGCTRL')
        bel.set_bel('BUFGCTRL')
        bel.parameters['IS_IGNORE0_INVERTED'] = int(
            'IS_IGNORE0_INVERTED' not in set_features)
        bel.parameters['IS_IGNORE1_INVERTED'] = int(
            'IS_IGNORE1_INVERTED' not in set_features)
        bel.parameters['IS_CE0_INVERTED'] = int('ZINV_CE0' not in set_features)
        bel.parameters['IS_CE1_INVERTED'] = int('ZINV_CE1' not in set_features)
        bel.parameters['IS_S0_INVERTED'] = int('ZINV_S0' not in set_features)
        bel.parameters['IS_S1_INVERTED'] = int('ZINV_S1' not in set_features)
        bel.parameters['PRESELECT_I0'] = '"TRUE"' if (
            'ZPRESELECT_I0' not in set_features) else '"FALSE"'
        bel.parameters['PRESELECT_I1'] = '"TRUE"' if int(
            'PRESELECT_I1' in set_features) else '"FALSE"'
        bel.parameters['INIT_OUT'] = int('INIT_OUT' in set_features)

        for sink in ('S0', 'S1', 'CE0', 'CE1', 'IGNORE0', 'IGNORE1'):
            site_pips = make_inverter_path(
                sink, bel.parameters['IS_{}_INVERTED'.format(sink)])
            site.add_sink(bel, sink, sink, bel.bel, sink, site_pips=site_pips)

        for sink in ('I0', 'I1'):
            site.add_sink(bel, sink, sink, bel.bel, sink)

        site.add_source(bel, 'O', 'O', bel.bel, 'O')

        site.add_bel(bel)

        top.add_site(site)


def cleanup_hrow(top, site):
    """
    Cleans-up BUFHCE if one is configured as pass-throu
    """

    # Check if we have a BUFHCE
    bel = site.maybe_get_bel("BUFHCE")
    if bel is not None:

        # Get source for CE
        source = top.find_source_from_sink(site, 'CE')
        # Get CE inversion
        inv_ce = bel.parameters['IS_CE_INVERTED']

        # Determine if the BUFHCE is permanently enabled
        if source in [0, 1] and (source ^ inv_ce) == 1:

            # Prune site routing
            site.prune_site_routing(('site_pin', 'I'))
            site.prune_site_routing(('site_pin', 'CE'))
            site.prune_site_routing(('bel_pin', 'BUFHCE', 'O', 'output'))

            # Remove the BUFHCE source. This is needed as the bel cannot be
            # removed when connected to the source (clearing bel.connections
            # doesn't solve that).
            del site.sources['O']

            # Remove the BUFHCE bel connection and the bel itself
            bel.connections = {}
            top.remove_bel(site, bel)

            del site.sinks['I']

            # Link site input and output
            site.link_site_routing([
                ('site_pin', 'I'),
                ('site_pin', 'O'),
            ])

            # Get wire pkeys
            bufhce_i_wire_pkey = site.site_wire_to_wire_pkey['I']
            bufhce_o_wire_pkey = site.site_wire_to_wire_pkey['O']

            # Get full wire names
            bufhce_i_wire_name = top.wire_pkey_to_wire.get(
                bufhce_i_wire_pkey, None)
            bufhce_o_wire_name = top.wire_pkey_to_wire.get(
                bufhce_o_wire_pkey, None)

            # Identify all sinks driven by the BUFHCE, store their wire pkeys
            clk_sinks = []
            bufhce_o_net = top.nets[bufhce_o_wire_pkey]
            for wire_pkey in bufhce_o_net.route_wire_pkeys:
                if wire_pkey not in top.nets:

                    if wire_pkey not in top.wire_pkey_to_wire:
                        continue

                    wire = top.wire_pkey_to_wire[wire_pkey]
                    if wire in top.wires:
                        clk_sinks.append(wire_pkey)

            # Identify the clock source that drives the BUFHCE, store its pkey
            for net_src_pkey, net in top.nets.items():
                if bufhce_i_wire_pkey in net.route_wire_pkeys:
                    bufhce_i_net = net
                    break
            else:
                assert False, bufhce_i_wire_pkey
            clk_source = bufhce_i_net.source_wire_pkey

            # Get other sinks that are driven by the same source as the BUFHCE
            # and store them
            other_clk_sinks = []
            for wire_pkey in bufhce_i_net.route_wire_pkeys:
                if wire_pkey not in top.nets:

                    if wire_pkey == bufhce_i_wire_pkey:
                        continue

                    if wire_pkey not in top.wire_pkey_to_wire:
                        continue

                    wire = top.wire_pkey_to_wire[wire_pkey]
                    if wire in top.wires:
                        other_clk_sinks.append(wire_pkey)

            # Identify the pip that bypasses the BUFHCE
            site_pin_map = make_site_pin_map(frozenset(site.site.site_pins))
            pip = "{}.{}.{}".format(
                site.tile,
                site_pin_map['O'],
                site_pin_map['I'],
            )

            # Do not add the PIP to the active PIPs. Make a short between
            # BUFHCE input and output using the PIP instead.
            top.shorted_nets[bufhce_o_wire_pkey] = bufhce_i_wire_pkey, pip

            # Delete old nets
            del top.nets[bufhce_o_net.source_wire_pkey]
            del top.nets[bufhce_i_net.source_wire_pkey]

            # Re-route the clock signal having the BUFHCE shorted. This will
            # create new net(s)
            nets = {}
            net_map = {}

            for sink_wire, src_wire in make_routes(
                    db=top.db,
                    conn=top.conn,
                    wire_pkey_to_wire=top.wire_pkey_to_wire,
                    unrouted_sinks=clk_sinks + other_clk_sinks,
                    unrouted_sources=[clk_source],
                    active_pips=top.active_pips,
                    allow_orphan_sinks=False,
                    shorted_nets=top.shorted_nets,
                    nets=nets,
                    net_map=net_map,
            ):
                top.wire_assigns.remove_sink(sink_wire)
                top.wire_assigns.add_wire(
                    sink_wire=sink_wire, src_wire=src_wire)

            # Do not overwrite const nets. We don't expect any as a result of
            # the clock signal re-routing
            if ZERO_NET in nets:
                del nets[ZERO_NET]
            if ONE_NET in nets:
                del nets[ONE_NET]

            # Merge new nets and net_map
            top.nets.update(nets)
            top.net_map.update(net_map)

            # Remove BUFHCE wires as they are not used anymore
            if bufhce_i_wire_name in top.wires:
                top.wires.discard(bufhce_i_wire_name)
            if bufhce_o_wire_name in top.wires:
                top.wires.discard(bufhce_o_wire_name)


def process_hrow(conn, top, tile, features):
    bufhs = {}
    for f in features:
        parts = f.feature.split('.')

        if parts[1] != 'BUFHCE':
            continue

        if parts[2] not in bufhs:
            bufhs[parts[2]] = []

        bufhs[parts[2]].append(f)

    for bufh, features in bufhs.items():
        set_features = set()

        for f in features:
            if f.value == 0:
                continue

            parts = f.feature.split('.')

            set_features.add('.'.join(parts[3:]))

        if 'IN_USE' not in set_features:
            continue

        bufhce_site = get_bufhce_site(top.db, top.grid, tile,
                                      features[0].feature.split('.')[2])
        site = Site(features, site=bufhce_site)

        bel = Bel('BUFHCE')
        bel.set_bel('BUFHCE')
        if 'CE_TYPE.ASYNC' in set_features:
            bel.parameters['CE_TYPE'] = '"ASYNC"'
        else:
            bel.parameters['CE_TYPE'] = '"SYNC"'
        bel.parameters['IS_CE_INVERTED'] = int('ZINV_CE' not in set_features)
        bel.parameters['INIT_OUT'] = int('INIT_OUT' in set_features)

        for sink in ('I', 'CE'):
            site.add_sink(bel, sink, sink, bel.bel, sink)

        site.add_source(bel, 'O', 'O', bel.bel, 'O')

        site.add_bel(bel, name="BUFHCE")

        site.set_post_route_cleanup_function(cleanup_hrow)
        top.add_site(site)

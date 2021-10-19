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

from .verilog_modeling import Bel, Site
import math


def make_hex_verilog_value(width, value):
    return "{width}'h{{:0{format_width}X}}".format(
        width=width, format_width=int(math.ceil(width / 4))).format(value)


def get_clb_site(db, grid, tile, site):
    """ Return the prjxray.tile.Site object for the given CLB site. """
    gridinfo = grid.gridinfo_at_tilename(tile)
    tile_type = db.get_tile_type(gridinfo.tile_type)

    sites = sorted(tile_type.get_instance_sites(gridinfo), key=lambda x: x.x)

    return sites[int(site[-1])]


def get_lut_init(site, lut):
    """ Return the INIT value for the specified LUT. """
    init = site.decode_multi_bit_feature('{}LUT.INIT'.format(lut))
    return "64'b{:064b}".format(init)


def get_lut_hex_init(site, lut):
    """ Return the INIT value for the specified LUT. """
    init = site.decode_multi_bit_feature('{}LUT.INIT'.format(lut))
    return "64'h{:016x}".format(init)


def get_shifted_lut_init(site, lut, shift=0):
    """ Return the shifted INIT value as integer. The init input is a string."""
    int_init = site.decode_multi_bit_feature('{}LUT.INIT'.format(lut))
    return int_init << shift


def create_lut(site, lut):
    """ Create the BEL for the specified LUT. """
    bel = Bel('LUT6_2', lut + 'LUT', priority=3)
    bel_name = lut + '6LUT'
    bel.set_bel(bel_name)

    for idx in range(6):
        site.add_sink(
            bel=bel,
            cell_pin='I{}'.format(idx),
            sink_site_pin='{}{}'.format(lut, idx + 1),
            bel_name=bel_name,
            bel_pin='A{}'.format(idx + 1))

    site.add_internal_source(
        bel=bel,
        cell_pin='O6',
        wire_name=lut + 'O6',
        bel_name=bel_name,
        bel_pin='O6')
    site.add_internal_source(
        bel=bel,
        cell_pin='O5',
        wire_name=lut + 'O5',
        bel_name=lut + '5LUT',
        bel_pin='O5')

    bel.parameters['INIT'] = get_lut_hex_init(site, lut)
    site.add_bel(bel)

    bel_lut6 = Bel('LUT6', 'LUT6')
    bel_lut6.set_bel(bel_name)
    bel_lut6.parameters['INIT'] = get_lut_hex_init(site, lut)

    for idx in range(6):
        bel_lut6.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin='A{}'.format(idx + 1),
            cell_pin='I{}'.format(idx))

    bel_lut6.map_bel_pin_to_cell_pin(
        bel_name=bel_name, bel_pin='O6', cell_pin='O')

    bel.add_physical_bel(bel_lut6)
    bel.physical_net_names[bel_name, 'O6'] = 'O6'

    bel_lut5 = Bel('LUT5', 'LUT5')
    bel_name = lut + '5LUT'
    bel_lut5.set_bel(bel_name)

    init = site.decode_multi_bit_feature('{}LUT.INIT'.format(lut))
    bel_lut5.parameters['INIT'] = "32'h{:08x}".format(init & 0xFFFFFFFF)

    for idx in range(5):
        bel_lut5.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin='A{}'.format(idx + 1),
            cell_pin='I{}'.format(idx))

    bel_lut5.map_bel_pin_to_cell_pin(
        bel_name=bel_name, bel_pin='O5', cell_pin='O')

    bel.add_physical_bel(bel_lut5)
    bel.physical_net_names[bel_name, 'O5'] = 'O5'


def get_srl32_init(site, srl):

    lut_init = get_lut_init(site, srl)
    bits = lut_init.replace("64'b", "")

    assert bits[1::2] == bits[::2]

    return make_hex_verilog_value(32, int(bits[::2], 2))


def create_srl32(site, srl, up_chain):
    bel = Bel('SRLC32E', srl + 'SRL', priority=2)
    bel_name = srl + '6LUT'
    bel.set_bel(bel_name)

    site.add_sink(
        bel=bel,
        cell_pin='CLK',
        sink_site_pin='CLK',
        bel_name=bel_name,
        bel_pin='CLK')

    if up_chain:
        srl_plus_1 = chr(ord(srl) + 1)
        site.connect_internal(
            bel=bel,
            cell_pin='D',
            source='{}MC31'.format(srl_plus_1),
            bel_name=bel_name,
            bel_pin='DI1',
            site_pips=[('site_pip', '{}DI1MUX'.format(srl),
                        '{}MC31'.format(srl_plus_1))])
    else:
        if srl in 'ABC':
            assert site.has_feature('{srl}LUT.DI1MUX.{srl}I'.format(srl=srl))
            site_pips = [('site_pip', '{}DI1MUX'.format(srl),
                          '{}I'.format(srl))]
        else:
            site_pips = []

        site.add_sink(
            bel=bel,
            cell_pin='D',
            sink_site_pin='{}I'.format(srl),
            bel_name=bel_name,
            bel_pin='DI1',
            site_pips=site_pips,
        )

    for idx in range(5):
        site.add_sink(
            bel=bel,
            cell_pin='A[{}]'.format(idx),
            sink_site_pin='{}{}'.format(srl, idx + 2),
            bel_name=bel_name,
            bel_pin='A{}'.format(idx + 2))

    site.add_sink(
        bel=bel,
        cell_pin='A1',
        sink_site_pin='{}1'.format(srl),
        bel_name=bel_name,
        bel_pin='A1')

    site.add_internal_source(
        bel=bel,
        cell_pin='Q',
        wire_name=srl + 'O6',
        bel_name=bel_name,
        bel_pin='O6')

    return bel


def get_srl16_init(site, srl):
    """
    Decodes SRL16 INIT parameter. Returns two initialization strings, each one
    for one of two SRL16s.
    """

    lut_init = get_lut_init(site, srl)
    bits = lut_init.replace("64'b", "")

    assert bits[1::2] == bits[::2]

    srl_init = bits[::2]
    return make_hex_verilog_value(16, int(srl_init[:16],
                                          2)), make_hex_verilog_value(
                                              16, int(srl_init[16:], 2))


def create_srl16(site, srl, srl_type, part, up_chain):
    """
    Create an instance of SRL16 bel. Either for "x6LUT" or for "x5LUT"
    depending on the part parameter.
    """

    assert part == '5' or part == '6'

    bel = Bel(srl_type, srl + part + 'SRL', priority=2)
    bel_name = srl + part + 'LUT'
    bel.set_bel(bel_name)

    site.add_sink(bel, 'CLK', 'CLK', bel_name=bel_name, bel_pin='CLK')

    if part == '5':
        if up_chain:
            srl_plus_1 = chr(ord(srl) + 1)
            site.connect_internal(
                bel,
                'D',
                '{}MC31'.format(srl_plus_1),
                bel_name=bel_name,
                bel_pin='DI1',
                site_pips=[('site_pip', '{}DI1MUX'.format(srl),
                            '{}MC31'.format(srl_plus_1))])
        else:
            if srl in 'ABC':
                assert site.has_feature(
                    '{srl}LUT.DI1MUX.{srl}I'.format(srl=srl))
                site_pips = [('site_pip', '{}DI1MUX'.format(srl),
                              '{}I'.format(srl))]
            else:
                site_pips = []

            site.add_sink(
                bel,
                'D',
                '{}I'.format(srl),
                bel_name=bel_name,
                bel_pin='DI1',
                site_pips=site_pips)

        bel_pin = 'O5'
    else:
        assert part == '6'
        assert not up_chain
        site.add_sink(
            bel, 'D', '{}X'.format(srl), bel_name=bel_name, bel_pin='DI2')
        bel_pin = 'O6'

    for idx in range(4):
        site.add_sink(
            bel,
            'A{}'.format(idx),
            '{}{}'.format(srl, idx + 2),
            bel_name=bel_name,
            bel_pin='A{}'.format(idx + 2))

    site.add_sink(
        bel=bel,
        cell_pin='dummyA1',
        sink_site_pin='{}1'.format(srl),
        bel_name=bel_name,
        bel_pin='A1')
    site.add_sink(
        bel=bel,
        cell_pin='A6',
        sink_site_pin='{}6'.format(srl),
        bel_name=bel_name,
        bel_pin='A6')

    site.add_internal_source(
        bel, 'Q', srl + 'O' + part, bel_name=bel_name, bel_pin=bel_pin)

    return bel


def decode_dram(site):
    """ Decode the modes of each LUT in the slice based on set features.

    Returns dictionary of lut position (e.g. 'A') to lut mode.
    """
    lut_ram = {}
    lut_small = {}
    for lut in 'ABCD':
        lut_ram[lut] = site.has_feature('{}LUT.RAM'.format(lut))
        lut_small[lut] = site.has_feature('{}LUT.SMALL'.format(lut))

    di = {}
    for lut in 'ABC':
        di[lut] = site.has_feature('{}LUT.DI1MUX.{}I'.format(lut, lut))

    lut_modes = {}
    if site.has_feature('WA8USED'):
        assert site.has_feature('WA7USED')
        assert lut_ram['A']
        assert lut_ram['B']
        assert lut_ram['C']
        assert lut_ram['D']

        lut_modes['A'] = 'RAM256X1S'
        lut_modes['B'] = 'RAM256X1S'
        lut_modes['C'] = 'RAM256X1S'
        lut_modes['D'] = 'RAM256X1S'
        return lut_modes

    if site.has_feature('WA7USED'):
        if not lut_ram['A']:
            assert not lut_ram['B']
            assert lut_ram['C']
            assert lut_ram['D']
            lut_modes['A'] = 'LUT'
            lut_modes['B'] = 'LUT'
            lut_modes['C'] = 'RAM128X1S'
            lut_modes['D'] = 'RAM128X1S'

            return lut_modes

        assert lut_ram['B']

        if di['B']:
            lut_modes['A'] = 'RAM128X1S'
            lut_modes['B'] = 'RAM128X1S'
            lut_modes['C'] = 'RAM128X1S'
            lut_modes['D'] = 'RAM128X1S'
        else:
            assert lut_ram['B']
            assert lut_ram['C']
            assert lut_ram['D']

            lut_modes['A'] = 'RAM128X1D'
            lut_modes['B'] = 'RAM128X1D'
            lut_modes['C'] = 'RAM128X1D'
            lut_modes['D'] = 'RAM128X1D'

        return lut_modes

    all_ram = all(lut_ram[lut] for lut in 'ABCD')
    all_small = all(lut_small[lut] for lut in 'ABCD')

    if all_ram and not all_small:
        return {'D': 'RAM64M'}
    elif all_ram and all_small:
        return {'D': 'RAM32M'}
    else:
        # Remaining modes:
        # RAM32X1S, RAM32X1D, RAM64X1S, RAM64X1D
        remaining = set('ABCD')

        for lut in 'AC':
            if lut_ram[lut] and di[lut]:
                remaining.remove(lut)

                if lut_small[lut]:
                    lut_modes[lut] = 'RAM32X1S'
                else:
                    lut_modes[lut] = 'RAM64X1S'

        for lut in 'BD':
            if not lut_ram[lut]:
                continue

            minus_one = chr(ord(lut) - 1)
            if minus_one in remaining:
                if lut_ram[minus_one]:
                    remaining.remove(lut)
                    remaining.remove(minus_one)
                    if lut_small[lut]:
                        lut_modes[lut] = 'RAM32X1D'
                        lut_modes[minus_one] = 'RAM32X1D'
                    else:
                        lut_modes[lut] = 'RAM64X1D'
                        lut_modes[minus_one] = 'RAM64X1D'

            if lut in remaining:
                remaining.remove(lut)
                if lut_small[lut]:
                    lut_modes[lut] = 'RAM32X1S'
                else:
                    lut_modes[lut] = 'RAM64X1S'

        for lut in remaining:
            lut_modes[lut] = 'LUT'

        return lut_modes


def ff_bel(site, lut, ff5):
    """ Returns FF information for given FF.

    site (Site): Site object
    lut (str): FF in question (e.g. 'A')
    ff5 (bool): True if the 5FF versus the FF.

    Returns tuple of (module name, clock pin, clock enable pin, reset pin,
        init parameter).

    """
    ffsync = site.has_feature('FFSYNC')
    latch = site.has_feature('LATCH') and not ff5
    zrst = site.has_feature('{}{}FF.ZRST'.format(lut, '5' if ff5 else ''))
    zini = site.has_feature('{}{}FF.ZINI'.format(lut, '5' if ff5 else ''))
    init = int(not zini)

    if latch:
        assert not ffsync

    return {
        (False, False, False): ('FDPE', 'C', 'CE', 'PRE', init),
        (True, False, False): ('FDSE', 'C', 'CE', 'S', init),
        (True, False, True): ('FDRE', 'C', 'CE', 'R', init),
        (False, False, True): ('FDCE', 'C', 'CE', 'CLR', init),
        (False, True, True): ('LDCE', 'G', 'GE', 'CLR', init),
        (False, True, False): ('LDPE', 'G', 'GE', 'PRE', init),
    }[(ffsync, latch, zrst)]


def cleanup_carry4(top, site):
    """ Performs post-routing cleanups of CARRY4 bel required for SLICE.

    Cleanups:
     - Detect if CARRY4 is required.  If not, remove from site.
     - Remove connections to CARRY4 that are not in used (e.g. if C[3] and
       CO[3] are not used, disconnect S[3] and DI[2]).
    """

    carry4 = site.maybe_get_bel('CARRY4')
    if carry4 is not None:

        # Simplest check is if the CARRY4 has output in used by either the OUTMUX
        # or the FFMUX, if any of these muxes are enable, CARRY4 must remain.
        co_in_use = [False for _ in range(4)]
        o_in_use = [False for _ in range(4)]
        for idx, lut in enumerate('ABCD'):
            if site.has_feature('{}FFMUX.XOR'.format(lut)):
                o_in_use[idx] = True

            if site.has_feature('{}FFMUX.CY'.format(lut)):
                co_in_use[idx] = True

            if site.has_feature('{}OUTMUX.XOR'.format(lut)):
                o_in_use[idx] = True

            if site.has_feature('{}OUTMUX.CY'.format(lut)):
                co_in_use[idx] = True

        # No outputs in the SLICE use CARRY4, check if the COUT line is in use.
        for sink in top.find_sinks_from_source(site, 'COUT'):
            co_in_use[idx] = True
            break

        for idx in [3, 2, 1, 0]:
            if co_in_use[idx] or o_in_use[idx]:
                for odx in range(idx):
                    co_in_use[odx] = True
                    o_in_use[odx] = True

                break

        if not any(co_in_use) and not any(o_in_use):
            # No outputs in use, remove entire BEL
            top.remove_bel(site, carry4)
        else:
            pass
            """
            for idx in range(4):
                if not o_in_use[idx] and not co_in_use[idx]:
                    sink_wire_pkey = site.remove_internal_sink(
                        carry4, 'S[{}]'.format(idx)
                    )
                    if sink_wire_pkey is not None:
                        top.remove_sink(sink_wire_pkey)

                    sink_wire_pkey = site.remove_internal_sink(
                        carry4, 'DI[{}]'.format(idx)
                    )
                    if sink_wire_pkey is not None:
                        top.remove_sink(sink_wire_pkey)
            """


def cleanup_srl(top, site):
    """Performs post-routing cleanups of SRLs required for SLICE.

    Cleanups:
     - For each LUT if in 2xSRL16 mode detect whether both SRL16 are used.
       removes unused ones.
    """

    # Remove unused SRL16
    for i, row in enumerate("ABCD"):

        srl6 = site.maybe_get_bel("{}6SRL".format(row))
        srl5 = site.maybe_get_bel("{}5SRL".format(row))

        if srl6 is not None or srl5 is not None:
            # Mask A1 and A6 BEL pin and attached site pin.
            if srl6 is not None:
                site.mask_sink(srl6, 'dummyA1')
                site.mask_sink(srl6, 'A6')

                if srl5 is not None:
                    del srl5.connections['dummyA1']
                    del srl5.connections['A6']
            else:
                site.mask_sink(srl5, 'dummyA1')
                site.mask_sink(srl5, 'A6')

            # Remove BEL pin mappings.
            if srl6 is not None:
                srl6.unmap_bel_pin(srl6.bel, 'A1')
                srl6.unmap_bel_pin(srl6.bel, 'A6')

            if srl5 is not None:
                srl5.unmap_bel_pin(srl5.bel, 'A1')
                srl5.unmap_bel_pin(srl5.bel, 'A6')

        srl = site.maybe_get_bel("{}6SRL_32".format(row))
        if srl is not None:
            site.mask_sink(srl, 'A1')
            srl.unmap_bel_pin(srl.bel, 'A1')


def cleanup_dram(top, site):
    """Performs post-routing cleanup of DRAMs for SLICEMs.

    Depending on the DRAM mode, the fake sinks are masked so that they
    are not present in the verilog output.
    """
    lut_modes = decode_dram(site)

    if 'RAM32X1D' in lut_modes.values():
        for lut in 'BD':
            if lut_modes[lut] == 'RAM32X1D':
                minus_one = chr(ord(lut) - 1)

                ram32_0 = site.maybe_get_bel('RAM32X1D_{}_0'.format(lut))
                ram32_1 = site.maybe_get_bel('RAM32X1D_{}_1'.format(lut))

                if ram32_0 is not None or ram32_1 is not None:
                    if ram32_0 is not None:
                        site.mask_sink(ram32_0, 'A5')
                        site.mask_sink(ram32_0, 'DPRA5')

                        if ram32_1 is not None:
                            del ram32_1.connections['A5']
                            del ram32_1.connections['DPRA5']
                    else:
                        site.mask_sink(ram32_1, 'A5')
                        site.mask_sink(ram32_1, 'DPRA5')

                    for bel, sub_bel in zip((ram32_0, ram32_1), ('6', '5')):
                        if bel is None:
                            continue

                        bel.unmap_bel_pin('{}{}LUT'.format(lut, sub_bel), 'A6')
                        bel.unmap_bel_pin('{}{}LUT'.format(minus_one, sub_bel),
                                          'A6')

                for idx, sub_bel in zip(range(2), ['6', '5']):
                    name = 'RAM32X1D_{}_{}'.format(lut, idx)
                    ram32 = site.maybe_get_bel(name)
                    assert ram32 is not None, name
                    site.mask_sink(ram32, "D0")

                    bel_name = '{}{}LUT'.format(minus_one, sub_bel)

                    if sub_bel == '6':
                        bel_pin = 'DI2'
                    else:
                        bel_pin = 'DI1'

                    ram32.remap_bel_pin_to_cell_pin(bel_name, bel_pin, "D")

    if 'RAM128X1D' in lut_modes.values():
        ram128 = site.maybe_get_bel('RAM128X1D')
        for idx in range(6):
            site.mask_sink(ram128, 'ADDR_C[{}]'.format(idx))
            ram128.remap_bel_pin_to_cell_pin('C6LUT', 'A{}'.format(idx + 1),
                                             'A[{}]'.format(idx))

            site.mask_sink(ram128, 'DATA_A[{}]'.format(idx))
            ram128.remap_bel_pin_to_cell_pin('A6LUT', 'A{}'.format(idx + 1),
                                             'DPRA[{}]'.format(idx))

    if 'RAM128X1S' in lut_modes.values():
        if lut_modes['D'] == 'RAM128X1S' and lut_modes['C'] == 'RAM128X1S':
            ram128 = site.maybe_get_bel('RAM128X1S_CD')
            for idx in range(6):
                site.mask_sink(ram128, 'ADDR_C{}'.format(idx))
                ram128.remap_bel_pin_to_cell_pin(
                    'C6LUT', 'A{}'.format(idx + 1), 'A{}'.format(idx))

        if 'B' in lut_modes.keys():
            if lut_modes['B'] == 'RAM128X1S' and lut_modes['A'] == 'RAM128X1S':
                ram128 = site.maybe_get_bel('RAM128X1S_AB')
                for idx in range(6):
                    site.mask_sink(ram128, 'ADDR_A{}'.format(idx))
                    ram128.remap_bel_pin_to_cell_pin(
                        'A6LUT', 'A{}'.format(idx + 1), 'A{}'.format(idx))

    if 'RAM256X1S' in lut_modes.values():
        ram256 = site.maybe_get_bel('RAM256X1S')

        site.mask_sink(ram256, 'AX')
        ram256.remap_bel_pin_to_cell_pin('F7AMUX', 'S0', 'A[6]')

        for idx in range(6):
            site.mask_sink(ram256, 'ADDR_C[{}]'.format(idx))
            ram256.remap_bel_pin_to_cell_pin('C6LUT', 'A{}'.format(idx + 1),
                                             'A[{}]'.format(idx))

            site.mask_sink(ram256, 'ADDR_B[{}]'.format(idx))
            ram256.remap_bel_pin_to_cell_pin('B6LUT', 'A{}'.format(idx + 1),
                                             'A[{}]'.format(idx))

            site.mask_sink(ram256, 'ADDR_A[{}]'.format(idx))
            ram256.remap_bel_pin_to_cell_pin('A6LUT', 'A{}'.format(idx + 1),
                                             'A[{}]'.format(idx))

    if 'RAM32M' in lut_modes['D']:
        ram32m = site.maybe_get_bel('RAM32M')
        assert ram32m is not None

        for lut in 'ABCD':
            site.mask_sink(ram32m, 'ADDR{}[5]'.format(lut))
            ram32m.unmap_bel_pin('{}6LUT'.format(lut), 'A6')


def cleanup_o6(top, site):
    lut_modes = decode_dram(site)

    for lut in 'ABCD':
        if lut not in lut_modes or lut_modes[lut] != 'LUT':
            continue

        used = False
        for _ in top.find_sinks_from_source(site, lut):
            used = True

        if site.has_feature('{}OUTMUX.O6'.format(lut)):
            used = True

        if not used:
            key = ('site_pip', '{}USED'.format(lut), '0')
            site.prune_site_routing(key)


def cleanup_slice(top, site):
    """Performs post-routing cleanups required for SLICE."""

    # Cleanup CARRY4 stuff
    cleanup_carry4(top, site)

    # Cleanup SRL stuff
    cleanup_srl(top, site)

    # Cleanup DRAM stuff
    cleanup_dram(top, site)

    cleanup_o6(top, site)


def munge_ram32m_init(init):
    """ RAM32M INIT is interleaved, while the underlying data is not.

    INIT[::2] = INIT[:32]
    INIT[1::2] = INIT[32:]

    """

    bits = init.replace("64'b", "")[::-1]
    assert len(bits) == 64

    out_init = ['0' for _ in range(64)]
    out_init[::2] = bits[:32]
    out_init[1::2] = bits[32:]

    return make_hex_verilog_value(64, int(''.join(out_init[::-1]), 2))


def di_mux(site, bel, di_port, lut, bel_name):
    """ Implements DI1 mux. """

    if lut == 'A':
        if site.has_feature('ALUT.DI1MUX.AI'):
            site.add_sink(
                bel,
                di_port,
                "AI",
                bel_name,
                "DI1",
                site_pips=[('site_pip', 'ADI1MUX', 'AI')])
        else:
            if site.has_feature('BLUT.DI1MUX.BI'):
                site.add_sink(
                    bel,
                    di_port,
                    "BI",
                    bel_name,
                    "DI1",
                    site_pips=[
                        ('site_pip', 'BDI1MUX', 'BI'),
                        ('site_pip', 'ADI1MUX', 'BDI1'),
                    ])
            else:
                site.add_sink(
                    bel,
                    di_port,
                    "DI",
                    bel_name,
                    "DI1",
                    site_pips=[
                        ('site_pip', 'BDI1MUX', 'DI'),
                        ('site_pip', 'ADI1MUX', 'BDI1'),
                    ])
    elif lut == 'B':
        if site.has_feature('BLUT.DI1MUX.BI'):
            site.add_sink(
                bel,
                di_port,
                "BI",
                bel_name,
                "DI1",
                site_pips=[
                    ('site_pip', 'BDI1MUX', 'BI'),
                ])
        else:
            site.add_sink(
                bel,
                di_port,
                "DI",
                bel_name,
                "DI1",
                site_pips=[
                    ('site_pip', 'BDI1MUX', 'DI'),
                ])
    elif lut == 'C':
        if site.has_feature('CLUT.DI1MUX.CI'):
            site.add_sink(
                bel,
                di_port,
                "CI",
                bel_name,
                "DI1",
                site_pips=[
                    ('site_pip', 'CDI1MUX', 'CI'),
                ])
        else:
            site.add_sink(
                bel,
                di_port,
                "DI",
                bel_name,
                "DI1",
                site_pips=[
                    ('site_pip', 'CDI1MUX', 'DI'),
                ])
    elif lut == 'D':
        site.add_sink(bel, di_port, "DI", bel_name, "DI1")
    else:
        assert False, lut


def create_ramd32(bel_name, cell_name):
    bel = Bel('RAMD32', cell_name)
    bel.set_bel(bel_name)

    for idx in range(5):
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin="A{}".format(idx + 1),
            cell_pin="RADR{}".format(idx))
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin="WA{}".format(idx + 1),
            cell_pin="WADR{}".format(idx))

    if bel_name.endswith('6LUT'):
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name, bel_pin="O6", cell_pin="O")
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name, bel_pin="DI2", cell_pin="I")
    else:
        assert bel_name.endswith('5LUT')
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name, bel_pin="O5", cell_pin="O")
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name, bel_pin="DI1", cell_pin="I")

    bel.map_bel_pin_to_cell_pin(
        bel_name=bel_name, bel_pin="CLK", cell_pin="CLK")
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin="WE", cell_pin="WE")

    return bel


def create_rams32(bel_name, cell_name):
    bel = Bel('RAMS32', cell_name)
    bel.set_bel(bel_name)

    for idx in range(5):
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin="A{}".format(idx + 1),
            cell_pin="ADR{}".format(idx))
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin="WA{}".format(idx + 1),
            cell_pin="ADR{}".format(idx))

    if bel_name.endswith('6LUT'):
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name, bel_pin="O6", cell_pin="O")
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name, bel_pin="DI2", cell_pin="I")
    else:
        assert bel_name.endswith('5LUT')
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name, bel_pin="O5", cell_pin="O")
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name, bel_pin="DI1", cell_pin="I")

    bel.map_bel_pin_to_cell_pin(
        bel_name=bel_name, bel_pin="CLK", cell_pin="CLK")
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin="WE", cell_pin="WE")

    return bel


def create_ramd64e(bel_name, cell_name):
    bel = Bel('RAMD64E', cell_name)
    bel.set_bel(bel_name)

    for idx in range(6):
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin="A{}".format(idx + 1),
            cell_pin="RADR{}".format(idx))

    for idx in range(8):
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin="WA{}".format(idx + 1),
            cell_pin="WADR{}".format(idx))

    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin="O6", cell_pin="O")
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin="DI1", cell_pin="I")
    bel.map_bel_pin_to_cell_pin(
        bel_name=bel_name, bel_pin="CLK", cell_pin="CLK")
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin="WE", cell_pin="WE")

    return bel


def create_rams64e(bel_name, cell_name):
    bel = Bel('RAMS64E', cell_name)
    bel.set_bel(bel_name)

    for idx in range(6):
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin="A{}".format(idx + 1),
            cell_pin="ADR{}".format(idx))
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin="WA{}".format(idx + 1),
            cell_pin="ADR{}".format(idx))

    for idx in [6, 7]:
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel_name,
            bel_pin="WA{}".format(idx + 1),
            cell_pin="WADR{}".format(idx))

    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin="O6", cell_pin="O")
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin="DI1", cell_pin="I")
    bel.map_bel_pin_to_cell_pin(
        bel_name=bel_name, bel_pin="CLK", cell_pin="CLK")
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin="WE", cell_pin="WE")

    return bel


def create_f7mux(bel_name, cell_name):
    bel = Bel('MUXF7', cell_name)
    bel.set_bel(bel_name)

    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin='0', cell_pin='I0')
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin='1', cell_pin='I1')
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin='S0', cell_pin='S')
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin='OUT', cell_pin='O')

    return bel


def create_f8mux(bel_name, cell_name):
    bel = Bel('MUXF8', cell_name)
    bel.set_bel(bel_name)

    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin='0', cell_pin='I0')
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin='1', cell_pin='I1')
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin='S0', cell_pin='S')
    bel.map_bel_pin_to_cell_pin(bel_name=bel_name, bel_pin='OUT', cell_pin='O')

    return bel


def process_slice(top, s):
    """ Convert SLICE features in Bel and Site objects.

    """
    """
    Available options:

    LUT/DRAM/SRL:
    SLICE[LM]_X[01].[ABCD]LUT.INIT[63:0]
    SLICEM_X0.[ABCD]LUT.RAM
    SLICEM_X0.[ABCD]LUT.SMALL
    SLICEM_X0.[ABCD]LUT.SRL

    FF:
    SLICE[LM]_X[01].[ABCD]5?FF.ZINI
    SLICE[LM]_X[01].[ABCD]5?FF.ZRST
    SLICE[LM]_X[01].CLKINV
    SLICE[LM]_X[01].FFSYNC
    SLICE[LM]_X[01].LATCH
    SLICE[LM]_X[01].CEUSEDMUX
    SLICE[LM]_X[01].SRUSEDMUX

    CARRY4:
    SLICE[LM]_X[01].PRECYINIT = AX|CIN|C0|C1

    Muxes:
    SLICE[LM]_X[01].CARRY4.ACY0
    SLICE[LM]_X[01].CARRY4.BCY0
    SLICE[LM]_X[01].CARRY4.CCY0
    SLICE[LM]_X[01].CARRY4.DCY0
    SLICE[LM]_X[01].[ABCD]5FFMUX.IN_[AB]
    SLICE[LM]_X[01].[ABCD]AFFMUX = [ABCD]X|CY|XOR|F[78]|O5|O6
    SLICE[LM]_X[01].[ABCD]OUTMUX = CY|XOR|F[78]|O5|O6|[ABCD]5Q
    SLICEM_X0.WA7USED
    SLICEM_X0.WA8USED
    SLICEM_X0.WEMUX.CE
    """

    aparts = s[0].feature.split('.')

    mlut = aparts[1].startswith('SLICEM')

    site_obj = get_clb_site(top.db, top.grid, tile=aparts[0], site=aparts[1])
    site = Site(s, site_obj)

    def connect_ce_sr(bel, ce, sr):
        if site.has_feature('CEUSEDMUX'):
            site.add_sink(bel, ce, 'CE', bel.bel, 'CE',
                          [('site_pip', 'CEUSEDMUX', 'IN')])
        else:
            site.connect_constant(
                bel=bel,
                cell_pin=ce,
                bel_name=bel.bel,
                bel_pin='CE',
                value=1,
                source_bel='CEUSEDVCC',
                source_bel_pin='1',
                site_pips=[
                    ('site_pip', 'CEUSEDMUX', '1'),
                ])

        if site.has_feature('SRUSEDMUX'):
            site.add_sink(bel, sr, 'SR', bel.bel, 'SR',
                          [('site_pip', 'SRUSEDMUX', 'IN')])
        else:
            site.connect_constant(
                bel=bel,
                cell_pin=sr,
                bel_name=bel.bel,
                bel_pin='SR',
                value=0,
                source_bel='SRUSEDGND',
                source_bel_pin='0',
                site_pips=[
                    ('site_pip', 'SRUSEDMUX', '0'),
                ])

    IS_C_INVERTED = int(site.has_feature('CLKINV'))
    if IS_C_INVERTED:
        clk_site_pips = [('site_pip', 'CLKINV', 'CLK_B')]
    else:
        clk_site_pips = [('site_pip', 'CLKINV', 'CLK')]

    if mlut:
        if site.has_feature('WEMUX.CE'):
            WE = 'CE'
            we_site_pips = [('site_pip', 'WEMUX', 'CE')]
        else:
            WE = 'WE'
            we_site_pips = [('site_pip', 'WEMUX', 'WE')]

    if site.has_feature('DLUT.RAM'):
        # Must be a SLICEM to have RAM set.
        assert mlut
    else:
        for row in 'ABC':
            assert not site.has_feature('{}LUT.RAM'.format(row))

    muxes = set(('F7AMUX', 'F7BMUX', 'F8MUX'))

    luts = {}
    any_srls = False
    for row in 'ABCD':
        if site.has_feature('{}LUT.SRL'.format(row)):
            any_srls = True
            break

    # Add BELs for LUTs/RAMs
    if not site.has_feature('DLUT.RAM'):
        chain_features = (None, 'CLUT.DI1MUX.DI_DMC31', 'BLUT.DI1MUX.DI_CMC31',
                          'ALUT.DI1MUX.BDI1_BMC31', None)
        chain_feature_values = []
        for feat in chain_features:
            if feat is not None:
                chain_feature_values.append(site.has_feature(feat))
            else:
                chain_feature_values.append(None)

        for row, up_chain, down_chain in zip('DCBA', chain_feature_values[:4],
                                             chain_feature_values[1:]):
            # SRL
            if site.has_feature('{}LUT.SRL'.format(row)):
                # Cannot have both SRL and DRAM
                assert not site.has_feature('{}LUT.RAM'.format(row))

                # SRL32
                if not site.has_feature('{}LUT.SMALL'.format(row)):
                    srl = create_srl32(site, row, up_chain)
                    srl.parameters['INIT'] = get_srl32_init(site, row)

                    site.add_sink(
                        srl, 'CE', WE, srl.bel, 'WE', site_pips=we_site_pips)

                    if row == 'A' and site.has_feature('DOUTMUX.MC31'):
                        down_chain = True

                    if row == 'A' and site.has_feature('DFFMUX.MC31'):
                        down_chain = True

                    if down_chain:
                        site.add_internal_source(
                            srl, 'Q31', '{}MC31'.format(row), srl.bel, 'MC31')
                    else:
                        srl.add_unconnected_port(
                            'Q31', None, direction="output")

                    site.add_bel(srl, name='{}6SRL_32'.format(row))

                # 2x SRL16
                else:
                    init = get_srl16_init(site, row)

                    for i, part in enumerate(['5', '6']):
                        if part == '5' and up_chain:
                            # Check if SRL in previous row exists.  If it
                            # doesn't exist, this SRL is impossible and should
                            # not be emitted.
                            row_plus_1 = chr(ord(row) + 1)
                            up_srl = site.maybe_get_bel(
                                '{}6SRL'.format(row_plus_1))
                            if not up_srl:
                                continue

                        # Determine whether to use SRL16E or SRLC16E
                        srl_type = 'SRL16E'
                        use_mc31 = False

                        if part == '6':
                            if row == 'A' and site.has_feature('DOUTMUX.MC31'):
                                srl_type = 'SRLC16E'
                                use_mc31 = True
                            if row == 'A' and site.has_feature('DFFMUX.MC31'):
                                srl_type = 'SRLC16E'
                                use_mc31 = True

                            if down_chain:
                                srl_type = 'SRLC16E'
                                use_mc31 = True

                        # Create the SRL
                        srl = create_srl16(site, row, srl_type, part, up_chain
                                           and part == '5')
                        srl.parameters['INIT'] = init[i]

                        site.add_sink(
                            srl,
                            'CE',
                            WE,
                            srl.bel,
                            'WE',
                            site_pips=we_site_pips)

                        if use_mc31:
                            site.add_internal_source(srl, 'Q15',
                                                     '{}MC31'.format(row),
                                                     srl.bel, 'MC31')

                        site.add_bel(srl, name="{}{}SRL".format(row, part))

            # LUT
            else:
                luts[row] = create_lut(site, row)
    else:
        # DRAM is active.  Determine what BELs are in use.
        lut_modes = decode_dram(site)

        if lut_modes['D'] == 'RAM256X1S':
            ram256 = Bel('RAM256X1S', priority=3)
            site.add_sink(
                ram256, 'WE', WE, 'A6LUT', "WE", site_pips=we_site_pips)
            site.add_sink(
                ram256, 'WCLK', 'CLK', 'A6LUT', "CLK", site_pips=clk_site_pips)
            site.add_sink(
                ram256,
                'D',
                'DI',
                "A6LUT",
                "DI1",
                site_pips=[
                    ('site_pip', 'BDI1MUX', 'DI'),
                    ('site_pip', 'ADI1MUX', 'BDI1'),
                ])

            for idx in range(6):
                site.add_sink(ram256, 'A[{}]'.format(idx),
                              "D{}".format(idx + 1), "D6LUT",
                              "A{}".format(idx + 1))
                # Add fake sinks as they need to be routed to
                site.add_sink(ram256, 'ADDR_C[{}]'.format(idx),
                              "C{}".format(idx + 1), "C6LUT",
                              "A{}".format(idx + 1))
                site.add_sink(ram256, 'ADDR_B[{}]'.format(idx),
                              "B{}".format(idx + 1), "B6LUT",
                              "A{}".format(idx + 1))
                site.add_sink(ram256, 'ADDR_A[{}]'.format(idx),
                              "A{}".format(idx + 1), "A6LUT",
                              "A{}".format(idx + 1))

            site.add_sink(ram256, 'A[6]', "CX", "F7BMUX", "S0")
            site.add_sink(ram256, 'A[7]', "BX", "F8MUX", "S0")
            site.add_internal_source(ram256, 'O', 'F8MUX_O', "F8MUX", "OUT")

            for row in 'ABCD':
                ram256.add_physical_bel(
                    create_rams64e(row + '6LUT', 'RAMS64E_' + row))

            ram256.add_physical_bel(create_f7mux('F7AMUX', 'F7.A'))
            ram256.add_physical_bel(create_f7mux('F7BMUX', 'F7.B'))
            ram256.add_physical_bel(create_f7mux('F8MUX', 'F8'))
            ram256.physical_net_names['F8MUX', 'OUT'] = 'O'

            # Add fake sink to preserve routing thorugh AX pin.
            # The AX pin is used in the same net as for the CX pin.
            site.add_sink(ram256, 'AX', "AX", "F7AMUX", "S0")

            ram256.parameters['INIT'] = (make_hex_verilog_value(
                256,
                get_shifted_lut_init(site, 'D')
                | get_shifted_lut_init(site, 'C', 64)
                | get_shifted_lut_init(site, 'B', 128)
                | get_shifted_lut_init(site, 'A', 192)))

            site.add_bel(ram256, name="RAM256X1S")

            muxes = set()

            del lut_modes['A']
            del lut_modes['B']
            del lut_modes['C']
            del lut_modes['D']
        elif lut_modes['D'] == 'RAM128X1S':
            ram128 = Bel('RAM128X1S', name='RAM128X1S_CD', priority=3)
            bel_name = 'D6LUT'
            site.add_sink(
                ram128, 'WE', WE, bel_name, 'WE', site_pips=we_site_pips)
            site.add_sink(
                ram128,
                'WCLK',
                "CLK",
                bel_name,
                'CLK',
                site_pips=clk_site_pips)
            di_mux(site, ram128, 'D', 'C', 'C6LUT')

            for idx in range(6):
                site.add_sink(ram128, 'A{}'.format(idx), "D{}".format(idx + 1),
                              'D6LUT', 'A{}'.format(idx + 1))
                # Add fake sink to route through the C[N] pins
                site.add_sink(ram128, 'ADDR_C{}'.format(idx),
                              "C{}".format(idx + 1), 'C6LUT',
                              'A{}'.format(idx + 1))

            site.add_sink(ram128, 'A6', "CX", 'F7BMUX', 'S0')
            site.link_site_routing([('bel_pin', 'CX', 'CX', 'site_source'),
                                    ('site_pip', 'WA7USED', '0'),
                                    ('bel_pin', 'A6LUT', 'WA7', 'input')])
            site.add_internal_source(ram128, 'O', 'F7BMUX_O', 'F7BMUX', 'OUT')

            ram128.parameters['INIT'] = make_hex_verilog_value(
                128, (get_shifted_lut_init(site, 'D')
                      | get_shifted_lut_init(site, 'C', 64)))

            ram128.add_physical_bel(create_rams64e('D6LUT', 'LOW'))
            ram128.add_physical_bel(create_rams64e('C6LUT', 'HIGH'))
            ram128.add_physical_bel(create_f7mux('F7BMUX', 'F7'))
            ram128.physical_net_names['F7BMUX', 'OUT'] = 'O'

            site.add_bel(ram128, name='RAM128X1S_CD')
            muxes.remove('F7BMUX')

            del lut_modes['C']
            del lut_modes['D']

            if lut_modes['B'] == 'RAM128X1S':
                bel_name = 'B6LUT'
                ram128 = Bel('RAM128X1S', name='RAM128X1S_AB', priority=4)
                site.add_sink(
                    ram128, 'WE', WE, bel_name, 'WE', site_pips=we_site_pips)
                site.add_sink(
                    ram128,
                    'WCLK',
                    "CLK",
                    bel_name,
                    'CLK',
                    site_pips=clk_site_pips)

                di_mux(site, ram128, 'D', 'A', 'A6LUT')

                for idx in range(6):
                    site.add_sink(ram128, 'A{}'.format(idx),
                                  "B{}".format(idx + 1), 'B6LUT',
                                  'A{}'.format(idx + 1))
                    # Add fake sink to route through the A[N] pins
                    site.add_sink(ram128, 'ADDR_A{}'.format(idx),
                                  "A{}".format(idx + 1), 'A6LUT',
                                  'A{}'.format(idx + 1))

                site.add_sink(ram128, 'A6', "AX", 'F7AMUX', 'S0')

                site.add_internal_source(ram128, 'O', 'F7AMUX_O', 'F7AMUX',
                                         'OUT')

                ram128.parameters['INIT'] = make_hex_verilog_value(
                    128, (get_shifted_lut_init(site, 'B')
                          | get_shifted_lut_init(site, 'A', 64)))

                site.add_bel(ram128, name='RAM128X1S_AB')

                ram128.add_physical_bel(create_rams64e('B6LUT', 'LOW'))
                ram128.add_physical_bel(create_rams64e('A6LUT', 'HIGH'))
                ram128.add_physical_bel(create_f7mux('F7AMUX', 'F7'))
                ram128.physical_net_names['F7AMUX', 'OUT'] = 'O'

                muxes.remove('F7AMUX')

                del lut_modes['A']
                del lut_modes['B']

        elif lut_modes['D'] == 'RAM128X1D':
            ram128 = Bel('RAM128X1D', priority=3)

            site.add_sink(
                ram128, 'WE', WE, 'A6LUT', "WE", site_pips=we_site_pips)
            site.add_sink(
                ram128, 'WCLK', "CLK", 'A6LUT', "CLK", site_pips=clk_site_pips)
            site.add_sink(
                ram128,
                'D',
                "DI",
                "A6LUT",
                "DI1",
                site_pips=[
                    ('site_pip', 'BDI1MUX', 'DI'),
                    ('site_pip', 'ADI1MUX', 'BDI1'),
                ])

            site.link_site_routing([
                ('bel_pin', 'DI', 'DI', 'site_source'),
                ('site_pip', 'CDI1MUX', 'DI'),
                ('bel_pin', 'C6LUT', 'DI1', 'input'),
            ])

            for idx in range(6):
                site.add_sink(ram128, 'A[{}]'.format(idx),
                              "D{}".format(idx + 1), "D6LUT",
                              "A{}".format(idx + 1))
                # Add fake sink to route through the C[N] pins
                site.add_sink(
                    ram128,
                    'ADDR_C[{}]'.format(idx),
                    "C{}".format(idx + 1),
                    "C6LUT",
                    "A{}".format(idx + 1),
                    real_cell_pin='A[{}]'.format(idx))
                site.add_sink(ram128, 'DPRA[{}]'.format(idx),
                              "B{}".format(idx + 1), "B6LUT",
                              "A{}".format(idx + 1))
                # Add fake sink to route through the A[N] pins
                site.add_sink(
                    ram128,
                    'DATA_A[{}]'.format(idx),
                    "A{}".format(idx + 1),
                    "A6LUT",
                    "A{}".format(idx + 1),
                    real_cell_pin='DPRA[{}]'.format(idx))

            site.add_sink(ram128, 'A[6]', "CX", "F7BMUX", "S0")
            site.link_site_routing([('bel_pin', 'CX', 'CX', 'site_source'),
                                    ('site_pip', 'WA7USED', '0'),
                                    ('bel_pin', 'A6LUT', 'WA7', 'input')])
            site.add_sink(ram128, 'DPRA[6]', "AX", "F7AMUX", "S0")

            site.add_internal_source(ram128, 'SPO', 'F7BMUX_O', "F7BMUX",
                                     "OUT")
            site.add_internal_source(ram128, 'DPO', 'F7AMUX_O', "F7AMUX",
                                     "OUT")

            site.link_site_routing([('bel_pin', 'D6LUT', 'O6', 'output'),
                                    ('bel_pin', 'F7BMUX', '0', 'input')])
            site.link_site_routing([('bel_pin', 'C6LUT', 'O6', 'output'),
                                    ('bel_pin', 'F7BMUX', '1', 'input')])
            site.link_site_routing([('bel_pin', 'B6LUT', 'O6', 'output'),
                                    ('bel_pin', 'F7AMUX', '0', 'input')])
            site.link_site_routing([('bel_pin', 'A6LUT', 'O6', 'output'),
                                    ('bel_pin', 'F7AMUX', '1', 'input')])

            ram128.physical_net_names['D6LUT', 'O6'] = 'SPO0'
            ram128.physical_net_names['C6LUT', 'O6'] = 'SPO1'
            ram128.physical_net_names['B6LUT', 'O6'] = 'DPO0'
            ram128.physical_net_names['A6LUT', 'O6'] = 'DPO1'

            ram128.add_physical_bel(create_ramd64e('D6LUT', 'SP.LOW'))
            ram128.add_physical_bel(create_ramd64e('C6LUT', 'SP.HIGH'))
            ram128.add_physical_bel(create_ramd64e('B6LUT', 'DP.LOW'))
            ram128.add_physical_bel(create_ramd64e('A6LUT', 'DP.HIGH'))

            ram128.add_physical_bel(create_f7mux('F7BMUX', 'F7.SP'))
            ram128.add_physical_bel(create_f7mux('F7AMUX', 'F7.DP'))

            ram128.parameters['INIT'] = make_hex_verilog_value(
                128, (get_shifted_lut_init(site, 'D')
                      | get_shifted_lut_init(site, 'C', 64)))

            other_init = make_hex_verilog_value(
                128, (get_shifted_lut_init(site, 'B')
                      | get_shifted_lut_init(site, 'A', 64)))

            assert ram128.parameters['INIT'] == other_init

            site.add_bel(ram128, name="RAM128X1D")

            muxes.remove('F7AMUX')
            muxes.remove('F7BMUX')

            del lut_modes['A']
            del lut_modes['B']
            del lut_modes['C']
            del lut_modes['D']
        elif lut_modes['D'] == 'RAM64M':
            del lut_modes['D']

            ram64m = Bel('RAM64M', name='RAM64M', priority=3)

            site.add_sink(
                ram64m, 'WE', WE, 'A6LUT', "WE", site_pips=we_site_pips)
            site.add_sink(
                ram64m, 'WCLK', "CLK", 'A6LUT', "CLK", site_pips=clk_site_pips)

            di_mux(site, ram64m, 'DIA', 'A', 'A6LUT')
            di_mux(site, ram64m, 'DIB', 'B', 'B6LUT')
            di_mux(site, ram64m, 'DIC', 'C', 'C6LUT')
            di_mux(site, ram64m, 'DID', 'D', 'D6LUT')

            for lut in 'ABCD':
                bel_name = '{}6LUT'.format(lut)
                phys_bel = create_ramd64e(bel_name, 'RAM{}'.format(lut))

                site.add_internal_source(ram64m, 'DO' + lut, lut + "O6",
                                         bel_name, "O6")

                for idx in range(6):
                    site.add_sink(
                        ram64m, 'ADDR{}[{}]'.format(lut, idx), "{}{}".format(
                            lut, idx + 1), bel_name, "A{}".format(idx + 1))

                ram64m.add_physical_bel(phys_bel)
                ram64m.physical_net_names[bel_name, 'O6'] = 'DO' + lut

                ram64m.parameters['INIT_' + lut] = get_lut_hex_init(site, lut)

            site.add_bel(ram64m)
        elif lut_modes['D'] == 'RAM32M':
            del lut_modes['D']

            ram32m = Bel('RAM32M', name='RAM32M', priority=3)

            site.add_sink(
                ram32m, 'WE', WE, 'A6LUT', "WE", site_pips=we_site_pips)
            site.add_sink(
                ram32m, 'WCLK', "CLK", 'A6LUT', "CLK", site_pips=clk_site_pips)

            di_mux(site, ram32m, 'DIA[0]', 'A', 'A6LUT')
            di_mux(site, ram32m, 'DIB[0]', 'B', 'B6LUT')
            di_mux(site, ram32m, 'DIC[0]', 'C', 'C6LUT')
            di_mux(site, ram32m, 'DID[0]', 'D', 'D6LUT')

            for lut in 'ABCD':
                bel_name = '{}6LUT'.format(lut)
                site.add_sink(ram32m, 'DI{}[1]'.format(lut), lut + "X",
                              bel_name, 'DI2')
                site.add_internal_source(ram32m, 'DO{}[1]'.format(lut),
                                         lut + "O6", bel_name, "O6")

                site.add_internal_source(ram32m, 'DO{}[0]'.format(lut),
                                         lut + "O5", '{}5LUT'.format(lut),
                                         "O5")

                for idx in range(6):
                    site.add_sink(
                        ram32m, 'ADDR{}[{}]'.format(lut, idx), "{}{}".format(
                            lut, idx + 1), bel_name, "A{}".format(idx + 1))

                ram32m.parameters['INIT_' + lut] = munge_ram32m_init(
                    get_lut_init(site, lut))

                if lut == 'D':
                    ram32m.add_physical_bel(
                        create_rams32('{}6LUT'.format(lut),
                                      'RAM{}_D1'.format(lut)))
                    ram32m.add_physical_bel(
                        create_rams32('{}5LUT'.format(lut),
                                      'RAM{}'.format(lut)))
                else:
                    ram32m.add_physical_bel(
                        create_ramd32('{}6LUT'.format(lut),
                                      'RAM{}_D1'.format(lut)))
                    ram32m.add_physical_bel(
                        create_ramd32('{}5LUT'.format(lut),
                                      'RAM{}'.format(lut)))

                ram32m.physical_net_names[lut +
                                          '6LUT', 'O6'] = 'DO{}1'.format(lut)
                ram32m.physical_net_names[lut +
                                          '5LUT', 'O5'] = 'DO{}0'.format(lut)

            site.add_bel(ram32m, name='RAM32M')

        for priority, lut in zip([4, 3], 'BD'):
            if lut not in lut_modes:
                continue

            minus_one = chr(ord(lut) - 1)

            if lut_modes[lut] == 'RAM64X1D':
                assert lut_modes[minus_one] == lut_modes[lut]

                ram64 = Bel(
                    'RAM64X1D',
                    name='RAM64X1D_' + minus_one + lut,
                    priority=priority)
                ram64.set_bel(minus_one + '6LUT')

                upper_lut = lut + '6LUT'
                lower_lut = minus_one + '6LUT'

                site.add_sink(
                    ram64, 'WE', WE, lower_lut, "WE", site_pips=we_site_pips)
                site.add_sink(
                    ram64,
                    'WCLK',
                    "CLK",
                    lower_lut,
                    "CLK",
                    site_pips=clk_site_pips)
                di_mux(site, ram64, 'D', minus_one, lower_lut)

                upper_bel = create_ramd64e(upper_lut, 'SP')
                lower_bel = create_ramd64e(lower_lut, 'DP')

                ram64.add_physical_bel(upper_bel)
                ram64.add_physical_bel(lower_bel)

                ram64.physical_net_names[upper_lut, 'O6'] = 'SPO'
                ram64.physical_net_names[lower_lut, 'O6'] = 'DPO'

                for idx in range(6):
                    site.add_sink(ram64, 'A{}'.format(idx), "{}{}".format(
                        lut, idx + 1), upper_lut, "A{}".format(idx + 1))
                    site.add_sink(ram64, 'DPRA{}'.format(idx), "{}{}".format(
                        minus_one, idx + 1), lower_lut, "A{}".format(idx + 1))

                site.add_internal_source(ram64, 'SPO', lut + "O6", upper_lut,
                                         "O6")
                site.add_internal_source(ram64, 'DPO', minus_one + "O6",
                                         lower_lut, "O6")

                ram64.parameters['INIT'] = get_lut_hex_init(site, lut)
                other_init = get_lut_hex_init(site, minus_one)

                assert ram64.parameters['INIT'] == other_init

                site.add_bel(ram64)

                del lut_modes[lut]
                del lut_modes[minus_one]
            elif lut_modes[lut] == 'RAM32X1D':
                ram32 = [
                    Bel('RAM32X1D',
                        name='RAM32X1D_{}_{}'.format(lut, idx),
                        priority=priority + 1 - idx) for idx in range(2)
                ]

                ram32[0].set_bel('{}6LUT'.format(lut))
                ram32[1].set_bel('{}5LUT'.format(lut))

                for idx, sub_bel in zip(range(2), ['6', '5']):
                    bel_name = '{}{}LUT'.format(lut, sub_bel)
                    minus_bel_name = '{}{}LUT'.format(minus_one, sub_bel)

                    site.add_sink(
                        ram32[idx],
                        'WE',
                        WE,
                        bel_name,
                        'WE',
                        site_pips=we_site_pips)
                    site.add_sink(
                        ram32[idx],
                        'WCLK',
                        "CLK",
                        bel_name,
                        'CLK',
                        site_pips=clk_site_pips)
                    for aidx in range(6):
                        site.add_sink(ram32[idx], 'A{}'.format(aidx),
                                      "{}{}".format(lut, aidx + 1), bel_name,
                                      'A{}'.format(aidx + 1))
                        site.add_sink(ram32[idx], 'DPRA{}'.format(aidx),
                                      "{}{}".format(minus_one, aidx + 1),
                                      minus_bel_name, 'A{}'.format(aidx + 1))

                    ram32[idx].add_physical_bel(create_ramd32(bel_name, 'SP'))
                    ram32[idx].add_physical_bel(
                        create_ramd32(minus_bel_name, 'DP'))

                    if sub_bel == '5':
                        ram32[idx].physical_net_names[bel_name, 'O5'] = 'SPO'
                        ram32[idx].physical_net_names[minus_bel_name,
                                                      'O5'] = 'DPO'
                    else:
                        ram32[idx].physical_net_names[bel_name, 'O6'] = 'SPO'
                        ram32[idx].physical_net_names[minus_bel_name,
                                                      'O6'] = 'DPO'

                site.add_sink(ram32[0], 'D', lut + "X", '{}6LUT'.format(lut),
                              'DI2')
                site.add_sink(ram32[0], 'D0', minus_one + "X",
                              '{}6LUT'.format(minus_one), 'DI2')

                site.add_internal_source(ram32[0], 'SPO', lut + "O6",
                                         '{}6LUT'.format(lut), 'O6')
                site.add_internal_source(ram32[0], 'DPO', minus_one + "O6",
                                         '{}6LUT'.format(minus_one), 'O6')

                di_mux(site, ram32[1], 'D', lut, '{}5LUT'.format(lut))
                di_mux(site, ram32[1], 'D0', minus_one,
                       '{}5LUT'.format(minus_one))
                site.add_internal_source(ram32[1], 'SPO', lut + "O5",
                                         '{}5LUT'.format(lut), 'O5')
                site.add_internal_source(ram32[1], 'DPO', minus_one + "O5",
                                         '{}5LUT'.format(minus_one), 'O5')

                lut_init = get_lut_init(site, lut)
                other_init = get_lut_init(site, minus_one)
                assert lut_init == other_init

                bits = lut_init.replace("64'b", "")
                assert len(bits) == 64
                ram32[0].parameters['INIT'] = make_hex_verilog_value(
                    32, int(bits[:32], 2))
                ram32[1].parameters['INIT'] = make_hex_verilog_value(
                    32, int(bits[32:], 2))

                site.add_bel(ram32[0], name=ram32[0].name)
                site.add_bel(ram32[1], name=ram32[1].name)

                del lut_modes[lut]
                del lut_modes[minus_one]

        for priority, lut in zip([6, 5, 4, 3], 'ABCD'):
            if lut not in lut_modes:
                continue

            if lut_modes[lut] == 'LUT':
                luts[lut] = create_lut(site, lut)
            elif lut_modes[lut] == 'RAM64X1S':
                ram64 = Bel(
                    'RAM64X1S', name='RAM64X1S_' + lut, priority=priority)
                bel_name = '{}6LUT'.format(lut)
                ram64.set_bel(bel_name)

                site.add_sink(
                    ram64, 'WE', WE, ram64.bel, "WE", site_pips=we_site_pips)
                site.add_sink(
                    ram64,
                    'WCLK',
                    "CLK",
                    ram64.bel,
                    "CLK",
                    site_pips=clk_site_pips)
                di_mux(site, ram64, 'D', lut, ram64.bel)

                for idx in range(6):
                    site.add_sink(ram64, 'A{}'.format(idx), "{}{}".format(
                        lut, idx + 1), ram64.bel, "A{}".format(idx + 1))

                site.add_internal_source(ram64, 'O', lut + "O6", ram64.bel,
                                         "O6")

                ram64.add_physical_bel(create_rams64e(bel_name, 'SP'))
                ram64.physical_net_names[ram64.bel, 'O6'] = 'O'

                ram64.parameters['INIT'] = get_lut_hex_init(site, lut)

                site.add_bel(ram64)
            elif lut_modes[lut] == 'RAM32X1S':
                ram32 = [
                    Bel('RAM32X1S',
                        name='RAM32X1S_{}_{}'.format(lut, idx),
                        priority=priority) for idx in range(2)
                ]

                ram32[0].set_bel('{}6LUT'.format(lut))
                ram32[1].set_bel('{}5LUT'.format(lut))

                for idx in range(2):
                    site.add_sink(ram32[idx], 'WE', WE, ram32[idx].bel, 'WE')
                    site.add_sink(ram32[idx], 'WCLK', "CLK", ram32[idx].bel,
                                  'CLK')
                    for aidx in range(5):
                        site.add_sink(ram32[idx], 'A{}'.format(aidx),
                                      "{}{}".format(lut, aidx + 1),
                                      ram32[idx].bel, 'A{}'.format(aidx + 1))

                site.add_sink(ram32[0], 'D', lut + "X", ram32[0].bel, 'DI2')
                site.add_internal_source(ram32[0], 'O', lut + "O6",
                                         ram32[0].bel, 'O6')

                di_mux(site, ram32[1], 'D', lut, ram32[1].bel)
                site.add_internal_source(ram32[1], 'O', lut + "O5",
                                         ram32[1].bel, 'O5')

                lut_init = get_lut_init(site, lut)

                bits = lut_init.replace("64'b", "")
                assert len(bits) == 64
                ram32[0].parameters['INIT'] = make_hex_verilog_value(
                    32, int(bits[:32], 2))
                ram32[1].parameters['INIT'] = make_hex_verilog_value(
                    32, int(bits[32:], 2))

                site.add_bel(ram32[0])
                site.add_bel(ram32[1])
            else:
                assert False, lut_modes[lut]

    need_f8 = site.has_feature('BFFMUX.F8') or site.has_feature('BOUTMUX.F8')
    need_f7a = site.has_feature('AFFMUX.F7') or site.has_feature('AOUTMUX.F7')
    need_f7b = site.has_feature('CFFMUX.F7') or site.has_feature('COUTMUX.F7')

    if need_f8:
        need_f7a = True
        need_f7b = True

    for mux in sorted(muxes):
        if mux == 'F7AMUX':
            if not need_f8 and not need_f7a:
                continue
            else:
                bel_type = 'MUXF7'
                opin = 'O'

            f7amux = Bel(bel_type, 'MUXF7A', priority=7)
            f7amux.set_bel('F7AMUX')

            site.connect_internal(f7amux, 'I0', 'BO6', f7amux.bel, '0')
            site.connect_internal(f7amux, 'I1', 'AO6', f7amux.bel, '1')
            site.add_sink(f7amux, 'S', 'AX', f7amux.bel, 'S0')

            site.add_internal_source(f7amux, opin, 'F7AMUX_O', f7amux.bel,
                                     'OUT')

            site.add_bel(f7amux)
        elif mux == 'F7BMUX':
            if not need_f8 and not need_f7b:
                continue
            else:
                bel_type = 'MUXF7'
                opin = 'O'

            f7bmux = Bel(bel_type, 'MUXF7B', priority=7)
            f7bmux.set_bel('F7BMUX')

            site.connect_internal(f7bmux, 'I0', 'DO6', f7bmux.bel, '0')
            site.connect_internal(f7bmux, 'I1', 'CO6', f7bmux.bel, '1')
            site.add_sink(f7bmux, 'S', 'CX', f7bmux.bel, 'S0')

            site.add_internal_source(f7bmux, opin, 'F7BMUX_O', f7bmux.bel,
                                     'OUT')

            site.add_bel(f7bmux)
        elif mux == 'F8MUX':
            if not need_f8:
                continue
            else:
                bel_type = 'MUXF8'
                opin = 'O'

            f8mux = Bel(bel_type, priority=7)
            f8mux.set_bel('F8MUX')

            site.connect_internal(f8mux, 'I0', 'F7BMUX_O', f8mux.bel, '0')
            site.connect_internal(f8mux, 'I1', 'F7AMUX_O', f8mux.bel, '1')
            site.add_sink(f8mux, 'S', 'BX', f8mux.bel, 'S0')

            site.add_internal_source(f8mux, opin, 'F8MUX_O', f8mux.bel, 'OUT')

            site.add_bel(f8mux)
        else:
            assert False, mux

    can_have_carry4 = True
    for lut in 'ABCD':
        if site.has_feature(lut + 'O6') or site.has_feature(lut + 'LUT.RAM'):
            can_have_carry4 = False
            break

    if any_srls:
        can_have_carry4 = False

    if can_have_carry4:
        bel = Bel('CARRY4', priority=1)
        bel.set_bel('CARRY4')

        for idx in range(4):
            lut = chr(ord('A') + idx)
            if site.has_feature('CARRY4.{}CY0'.format(lut)):
                source = lut + 'O5'
                site.connect_internal(
                    bel=bel,
                    cell_pin='DI[{}]'.format(idx),
                    source=source,
                    bel_name=bel.bel,
                    bel_pin='DI{}'.format(idx),
                    site_pips=[('site_pip', '{}CY0'.format(lut), 'O5')])
            else:
                site.add_sink(
                    bel=bel,
                    cell_pin='DI[{}]'.format(idx),
                    sink_site_pin=lut + 'X',
                    bel_name=bel.bel,
                    bel_pin='DI{}'.format(idx),
                    site_pips=[('site_pip', '{}CY0'.format(lut),
                                '{}X'.format(lut))])

            source = lut + 'O6'

            site.connect_internal(bel, 'S[{}]'.format(idx), source, bel.bel,
                                  'S{}'.format(idx))

            site.add_internal_source(bel, 'O[{}]'.format(idx), lut + '_XOR',
                                     bel.bel, 'O{}'.format(idx))

            co_pin = 'CO[{}]'.format(idx)

            site.add_internal_source(bel, co_pin, lut + '_CY', bel.bel,
                                     'CO{}'.format(idx))
            if idx == 3:
                # Connects internal pin CO[3] to site pin COUT
                site.add_output_from_internal('COUT', lut + '_CY',
                                              [('site_pip', 'COUTUSED', '0')])

        bel.map_bel_pin_to_cell_pin(
            bel_name=bel.bel, bel_pin='CIN', cell_pin='CI')
        bel.map_bel_pin_to_cell_pin(
            bel_name=bel.bel, bel_pin='CYINIT', cell_pin='CYINIT')

        if site.has_feature('PRECYINIT.AX'):
            site.add_sink(bel, 'CYINIT', 'AX', bel.bel, 'CYINIT',
                          [('site_pip', 'PRECYINIT', 'AX')])
            bel.connections['CI'] = 0

        elif site.has_feature('PRECYINIT.C0'):
            site.connect_constant(
                bel=bel,
                cell_pin='CYINIT',
                bel_name=bel.bel,
                bel_pin='CYINIT',
                value=0,
                source_bel='CYINITGND',
                source_bel_pin='0',
                site_pips=[
                    ('site_pip', 'PRECYINIT', '0'),
                ])
            bel.connections['CI'] = 0

        elif site.has_feature('PRECYINIT.C1'):
            site.connect_constant(
                bel=bel,
                cell_pin='CYINIT',
                bel_name=bel.bel,
                bel_pin='CYINIT',
                value=1,
                source_bel='CYINITVCC',
                source_bel_pin='1',
                site_pips=[
                    ('site_pip', 'PRECYINIT', '1'),
                ])
            bel.connections['CI'] = 0

        elif site.has_feature('PRECYINIT.CIN'):
            bel.connections['CYINIT'] = 0
            site.add_sink(bel, 'CI', 'CIN', bel.bel, 'CIN')

        else:
            assert False, site.features

        site.add_bel(bel, name='CARRY4')

    ff5_bels = {}
    for lut in 'ABCD':
        if site.has_feature('{}OUTMUX.{}5Q'.format(lut, lut)) or \
                site.has_feature('{}5FFMUX.IN_A'.format(lut)) or \
                site.has_feature('{}5FFMUX.IN_B'.format(lut)):
            # 5FF in use, emit
            name, clk, ce, sr, init = ff_bel(site, lut, ff5=True)
            ff5 = Bel(name, "{}5_{}".format(lut, name))
            ff5_bels[lut] = ff5
            ff5.set_bel(lut + '5FF')

            if site.has_feature('{}5FFMUX.IN_A'.format(lut)):
                site.connect_internal(
                    ff5,
                    'D',
                    lut + 'O5',
                    ff5.bel,
                    'D',
                    site_pips=[('site_pip', '{}5FFMUX'.format(lut), 'IN_A')],
                )
            elif site.has_feature('{}5FFMUX.IN_B'.format(lut)):
                site.add_sink(
                    ff5,
                    'D',
                    lut + 'X',
                    ff5.bel,
                    'D',
                    site_pips=[('site_pip', '{}5FFMUX'.format(lut), 'IN_B')],
                )

            site.add_sink(
                ff5, clk, "CLK", ff5.bel, 'CK', site_pips=clk_site_pips)

            connect_ce_sr(ff5, ce, sr)

            site.add_internal_source(ff5, 'Q', lut + '5Q', ff5.bel, 'Q')
            ff5.parameters['INIT'] = init

            if name in ['LDCE', 'LDPE']:
                ff5.parameters['IS_G_INVERTED'] = int(not IS_C_INVERTED)
            else:
                ff5.parameters['IS_C_INVERTED'] = IS_C_INVERTED

            site.add_bel(ff5)

    for lut in 'ABCD':
        name, clk, ce, sr, init = ff_bel(site, lut, ff5=False)
        ff = Bel(name, "{}_{}".format(lut, name))
        ff.set_bel(lut + 'FF')

        if site.has_feature('{}FFMUX.{}X'.format(lut, lut)):
            site.add_sink(
                ff,
                'D',
                lut + 'X',
                ff.bel,
                'D',
                site_pips=[('site_pip', '{}FFMUX'.format(lut),
                            '{}X'.format(lut))])

        elif lut == 'A' and site.has_feature('AFFMUX.F7'):
            site.connect_internal(
                ff,
                'D',
                'F7AMUX_O',
                ff.bel,
                'D',
                site_pips=[('site_pip', 'AFFMUX', 'F7')])

        elif lut == 'C' and site.has_feature('CFFMUX.F7'):
            site.connect_internal(
                ff,
                'D',
                'F7BMUX_O',
                ff.bel,
                'D',
                site_pips=[('site_pip', 'CFFMUX', 'F7')])

        elif lut == 'B' and site.has_feature('BFFMUX.F8'):
            site.connect_internal(
                ff,
                'D',
                'F8MUX_O',
                ff.bel,
                'D',
                site_pips=[('site_pip', 'BFFMUX', 'F8')])

        elif lut == 'D' and site.has_feature('DFFMUX.MC31'):
            site.connect_internal(
                ff,
                'D',
                'AMC31',
                ff.bel,
                'D',
                site_pips=[('site_pip', 'DFFMUX', 'MC31')])

        elif site.has_feature('{}FFMUX.O5'.format(lut)):
            site.connect_internal(
                ff,
                'D',
                lut + 'O5',
                ff.bel,
                'D',
                site_pips=[('site_pip', '{}FFMUX'.format(lut), 'O5')])

        elif site.has_feature('{}FFMUX.O6'.format(lut)):
            site.connect_internal(
                ff,
                'D',
                lut + 'O6',
                ff.bel,
                'D',
                site_pips=[('site_pip', '{}FFMUX'.format(lut), 'O6')])

        elif site.has_feature('{}FFMUX.CY'.format(lut)):
            assert can_have_carry4
            site.connect_internal(
                ff,
                'D',
                lut + '_CY',
                ff.bel,
                'D',
                site_pips=[('site_pip', '{}FFMUX'.format(lut), 'CY')])

        elif site.has_feature('{}FFMUX.XOR'.format(lut)):
            assert can_have_carry4
            site.connect_internal(
                ff,
                'D',
                lut + '_XOR',
                ff.bel,
                'D',
                site_pips=[('site_pip', '{}FFMUX'.format(lut), 'XOR')])
        else:
            continue

        site.add_source(ff, 'Q', lut + 'Q', ff.bel, 'Q')
        site.add_sink(ff, clk, "CLK", ff.bel, 'CK', site_pips=clk_site_pips)

        connect_ce_sr(ff, ce, sr)

        ff.parameters['INIT'] = init

        if name in ['LDCE', 'LDPE']:
            ff.parameters['IS_G_INVERTED'] = int(not IS_C_INVERTED)
        else:
            ff.parameters['IS_C_INVERTED'] = IS_C_INVERTED

        site.add_bel(ff)

    for lut in 'ABCD':
        if lut + 'O6' in site.internal_sources:
            site.add_output_from_internal(
                lut,
                lut + 'O6',
                site_pips=[('site_pip', '{}USED'.format(lut), '0')])

    for lut in 'ABCD':
        output_wire = lut + 'MUX'
        if site.has_feature('{}OUTMUX.{}5Q'.format(lut, lut)):
            site.add_output_from_internal(
                output_wire,
                lut + '5Q',
                site_pips=[('site_pip', '{}OUTMUX'.format(lut),
                            '{}5Q'.format(lut))])

        elif lut == 'A' and site.has_feature('AOUTMUX.F7'):
            site.add_output_from_internal(
                output_wire,
                'F7AMUX_O',
                site_pips=[('site_pip', 'AOUTMUX', 'F7')])

        elif lut == 'C' and site.has_feature('COUTMUX.F7'):
            site.add_output_from_internal(
                output_wire,
                'F7BMUX_O',
                site_pips=[('site_pip', 'COUTMUX', 'F7')])

        elif lut == 'B' and site.has_feature('BOUTMUX.F8'):
            site.add_output_from_internal(
                output_wire,
                'F8MUX_O',
                site_pips=[('site_pip', 'BOUTMUX', 'F8')])

        elif site.has_feature('{}OUTMUX.O5'.format(lut)):
            site.add_output_from_internal(
                output_wire,
                lut + 'O5',
                site_pips=[('site_pip', '{}OUTMUX'.format(lut), 'O5')])

        elif site.has_feature('{}OUTMUX.O6'.format(lut)):
            # Note: There is a dedicated O6 output.  Fixed routing requires
            # treating xMUX.O6 as a routing connection.
            site.add_output_from_output(output_wire, lut)

        elif site.has_feature('{}OUTMUX.CY'.format(lut)):
            assert can_have_carry4
            site.add_output_from_internal(
                output_wire,
                lut + '_CY',
                site_pips=[('site_pip', '{}OUTMUX'.format(lut), 'CY')])

        elif site.has_feature('{}OUTMUX.XOR'.format(lut)):
            assert can_have_carry4
            site.add_output_from_internal(
                output_wire,
                lut + '_XOR',
                site_pips=[('site_pip', '{}OUTMUX'.format(lut), 'XOR')])
        else:
            continue

    if site.has_feature('DOUTMUX.MC31'):
        site.add_output_from_internal(
            'DMUX', 'AMC31', site_pips=[('site_pip', 'DOUTMUX', 'MC31')])

    site.set_post_route_cleanup_function(cleanup_slice)
    top.add_site(site)


def process_clb(conn, top, tile_name, features):
    slices = {
        '0': [],
        '1': [],
    }

    for f in features:
        parts = f.feature.split('.')

        if not parts[1].startswith('SLICE'):
            continue

        slices[parts[1][-1]].append(f)

    for s in slices:
        if len(slices[s]) > 0:
            process_slice(top, slices[s])

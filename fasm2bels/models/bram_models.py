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

import fasm
import re
from .verilog_modeling import Bel, Site, make_inverter_path
import math


def get_init(features, target_features, invert, width):
    """ Returns INIT argument for specified feature.

    features: List of fasm.SetFeature objects
    target_feature (list[str]): Target feature prefix (e.g. INIT_A or INITP_0).
        If multiple features are specified, first feature will be set at LSB.
    invert (bool): Controls whether output value should be bit inverted.
    width (int): Bit width of INIT value.

    Returns int

    """

    assert width % len(target_features) == 0, (width, len(target_features))

    final_init = 0
    for idx, target_feature in enumerate(target_features):
        init = 0
        for f in features:
            if f.feature.startswith(target_feature):
                for canon_f in fasm.canonical_features(f):
                    if canon_f.start is None:
                        init |= 1
                    else:
                        init |= (1 << canon_f.start)

        final_init |= init << idx * (width // len(target_features))

    if invert:
        final_init ^= (2**width) - 1

    return "{{width}}'h{{init:0{}X}}".format(int(math.ceil(width / 4))).format(
        width=width, init=final_init)


def get_bram_site(db, grid, tile, site):
    """ Return the prjxray.tile.Site object for the given BRAM site. """
    gridinfo = grid.gridinfo_at_tilename(tile)
    tile_type = db.get_tile_type(gridinfo.tile_type)

    if site == 'RAMB18_Y0':
        target_type = 'FIFO18E1'
    elif site == 'RAMB18_Y1':
        target_type = 'RAMB18E1'
    else:
        assert False, site

    sites = tile_type.get_instance_sites(gridinfo)
    for site in sites:
        if site.type == target_type:
            return site

    assert False, sites


def get_bram36_site(db, grid, tile):
    """ Return the BRAM36 prjxray.tile.Site object for the given BRAM tile. """
    gridinfo = grid.gridinfo_at_tilename(tile)
    tile_type = db.get_tile_type(gridinfo.tile_type)

    sites = tile_type.get_instance_sites(gridinfo)
    for site in sites:
        if site.type == 'RAMBFIFO36E1':
            return site

    assert False, sites


def eligible_for_merge(top, bram_sites, tile_features, verbose=False):
    """ Returns True if the two BRAM18's in this tile can be merged into a BRAM36.

    Parameters
    ----------
    verbose : bool
        If true, will print to stdout reason that this tile cannot merge the
        BRAM18's.

    """
    assert len(bram_sites) == 2

    bram_y0 = bram_sites[0].maybe_get_bel('RAMB18E1')
    assert bram_y0 is not None

    bram_y1 = bram_sites[1].maybe_get_bel('RAMB18E1')
    assert bram_y1 is not None

    def check_wire_match(wire_base, nwires):
        for idx in range(nwires):
            wire = '{}{}'.format(wire_base, idx)
            source_a = top.find_source_from_sink(bram_sites[0], wire)
            source_b = top.find_source_from_sink(bram_sites[1], wire)
            if source_a != source_b:
                if verbose:
                    print('Cannot merge because wire {}, {} != {}'.format(
                        wire, source_a, source_b))
                return False

        return True

    if not check_wire_match('WEA', 4):
        return False
    if not check_wire_match('WEBWE', 8):
        return False
    if not check_wire_match('ADDRARDADDR', 14):
        return False
    if not check_wire_match('ADDRATIEHIGH', 2):
        return False
    if not check_wire_match('ADDRBWRADDR', 14):
        return False
    if not check_wire_match('ADDRBTIEHIGH', 2):
        return False

    for param in [
            'IS_CLKARDCLK_INVERTED',
            'IS_CLKBWRCLK_INVERTED',
            'IS_ENARDEN_INVERTED',
            'IS_ENBWREN_INVERTED',
            'IS_RSTRAMARSTRAM_INVERTED',
            'IS_RSTRAMB_INVERTED',
            'IS_RSTREGARSTREG_INVERTED',
            'IS_RSTREGB_INVERTED',
            'DOA_REG',
            'DOB_REG',
            'READ_WIDTH_A',
            'READ_WIDTH_B',
            'WRITE_WIDTH_A',
            'WRITE_WIDTH_B',
            'WRITE_MODE_A',
            'WRITE_MODE_B',
            # 'RSTREG_PRIORITY',
            # 'RDADDR_COLLISION_HWCONFIG',
    ]:
        if bram_y0.parameters[param] != bram_y1.parameters[param]:
            if verbose:
                print('Cannot merge because parameter {}, {} != {}'.format(
                    param, bram_y0.parameters[param],
                    bram_y1.parameters[param]))
            return False

    for rw in ['READ', 'WRITE']:
        for ab in 'AB':
            feature = '{}_WIDTH_{}'.format(rw, ab)
            bram36_feature = 'RAMB36.BRAM36_{}_1'.format(feature)
            if bram_y0.parameters[feature] == 4 and bram_y1.parameters[
                    feature] == 4:
                if bram36_feature not in tile_features:
                    if verbose:
                        print('Cannot merge {} and {} because {} is not set'.
                              format(bram_sites[0].site.name,
                                     bram_sites[1].site.name, bram36_feature))

                    return False

    return True


def clean_up_to_bram18(top, site):
    """ Renames and masks sinks of BEL that are not visible to Verilog.

    Note: Masked paths are still emitted for FIXED_ROUTE.

    """
    bel = site.maybe_get_bel('RAMB18E1')
    assert bel is not None

    for idx in range(2):
        bel.unmap_bel_pin(bel.bel, 'ADDRATIEHIGH{}'.format(idx))
        bel.unmap_bel_pin(bel.bel, 'ADDRBTIEHIGH{}'.format(idx))

        site.mask_sink(bel, 'ADDRATIEHIGH[{}]'.format(idx))
        site.mask_sink(bel, 'ADDRBTIEHIGH[{}]'.format(idx))

    bel.unmap_bel_pin(bel.bel, 'REGCLKB')
    bel.unmap_bel_pin(bel.bel, 'REGCLKARDRCLK')

    site.mask_sink(bel, 'REGCLKB')
    site.mask_sink(bel, 'REGCLKARDRCLK')

    site.mask_sink(bel, 'WEA[1]')
    site.mask_sink(bel, 'WEA[3]')
    site.mask_sink(bel, 'WEBWE[1]')
    site.mask_sink(bel, 'WEBWE[3]')
    site.mask_sink(bel, 'WEBWE[5]')
    site.mask_sink(bel, 'WEBWE[7]')

    site.rename_sink(bel, 'WEA[2]', 'WEA[1]')
    site.rename_sink(bel, 'WEBWE[2]', 'WEBWE[1]')
    site.rename_sink(bel, 'WEBWE[4]', 'WEBWE[2]')
    site.rename_sink(bel, 'WEBWE[6]', 'WEBWE[3]')

    if bel.parameters['WRITE_WIDTH_A'] < 18:
        site.mask_sink(bel, "WEA[1]")

        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEA1", "WEA[0]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEA2", "WEA[0]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEA3", "WEA[0]")
    else:
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEA1", "WEA[0]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEA2", "WEA[1]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEA3", "WEA[1]")

    if bel.parameters['WRITE_WIDTH_B'] < 18:
        site.mask_sink(bel, "WEBWE[1]")
        site.mask_sink(bel, "WEBWE[2]")
        site.mask_sink(bel, "WEBWE[3]")

        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE1", "WEBWE[0]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE2", "WEBWE[0]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE3", "WEBWE[0]")

        bel.unmap_bel_pin(bel.bel, "WEBWE4")
        bel.unmap_bel_pin(bel.bel, "WEBWE5")
        bel.unmap_bel_pin(bel.bel, "WEBWE6")
        bel.unmap_bel_pin(bel.bel, "WEBWE7")
    elif bel.parameters['WRITE_WIDTH_B'] == 18:
        site.mask_sink(bel, "WEBWE[2]")
        site.mask_sink(bel, "WEBWE[3]")

        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE1", "WEBWE[0]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE2", "WEBWE[1]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE3", "WEBWE[1]")

        bel.unmap_bel_pin(bel.bel, "WEBWE4")
        bel.unmap_bel_pin(bel.bel, "WEBWE5")
        bel.unmap_bel_pin(bel.bel, "WEBWE6")
        bel.unmap_bel_pin(bel.bel, "WEBWE7")
    else:
        assert bel.parameters['WRITE_WIDTH_B'] == 36

        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE1", "WEBWE[0]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE2", "WEBWE[1]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE3", "WEBWE[1]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE4", "WEBWE[2]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE5", "WEBWE[2]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE6", "WEBWE[3]")
        bel.remap_bel_pin_to_cell_pin(bel.bel, "WEBWE7", "WEBWE[3]")


def clean_up_to_bram36(top, site):
    """ Cleans up BRAM36 BEL to match Verilog model.

    Also checks BRAM36 signal sources for sanity (e.g. can be merged) and
    then masks/renames signals to match Verilog model.

    """
    bel = site.maybe_get_bel('RAMB36E1')
    assert bel is not None

    for idx in range(15):
        assert top.find_source_from_sink(site, 'ADDRARDADDRL{}'.format(idx)) == \
            top.find_source_from_sink(site, 'ADDRARDADDRU{}'.format(idx))
        assert top.find_source_from_sink(site, 'ADDRBWRADDRL{}'.format(idx)) == \
            top.find_source_from_sink(site, 'ADDRBWRADDRU{}'.format(idx))

        site.mask_sink(bel, 'ADDRARDADDRU[{}]'.format(idx))
        site.mask_sink(bel, 'ADDRBWRADDRU[{}]'.format(idx))

        bel.remap_bel_pin_to_cell_pin(
            bel.bel,
            'ADDRARDADDRL{}'.format(idx),
            'ADDRARDADDR[{}]'.format(idx),
        )
        bel.remap_bel_pin_to_cell_pin(
            bel.bel,
            'ADDRBWRADDRL{}'.format(idx),
            'ADDRBWRADDR[{}]'.format(idx),
        )
        bel.remap_bel_pin_to_cell_pin(
            bel.bel,
            'ADDRARDADDRU{}'.format(idx),
            'ADDRARDADDR[{}]'.format(idx),
        )
        bel.remap_bel_pin_to_cell_pin(
            bel.bel,
            'ADDRBWRADDRU{}'.format(idx),
            'ADDRBWRADDR[{}]'.format(idx),
        )

        site.rename_sink(bel, 'ADDRARDADDRL[{}]'.format(idx),
                         'ADDRARDADDR[{}]'.format(idx))
        site.rename_sink(bel, 'ADDRBWRADDRL[{}]'.format(idx),
                         'ADDRBWRADDR[{}]'.format(idx))

    site.rename_sink(bel, 'ADDRARDADDRL[15]', 'ADDRARDADDR[15]')
    site.rename_sink(bel, 'ADDRBWRADDRL[15]', 'ADDRBWRADDR[15]')
    bel.remap_bel_pin_to_cell_pin(bel.bel, 'ADDRARDADDRL15', 'ADDRARDADDR[15]')
    bel.remap_bel_pin_to_cell_pin(bel.bel, 'ADDRBWRADDRL15', 'ADDRBWRADDR[15]')

    if bel.parameters['WRITE_WIDTH_A'] < 18:
        for idx in range(4):
            assert top.find_source_from_sink(site, 'WEAL{}'.format(idx)) == \
                top.find_source_from_sink(site, 'WEAU{}'.format(idx))
            site.mask_sink(bel, "WEAU[{}]".format(idx))
            bel.remap_bel_pin_to_cell_pin(
                bel.bel,
                'WEAL{}'.format(idx),
                'WEA[0]',
            )
            bel.remap_bel_pin_to_cell_pin(
                bel.bel,
                'WEAU{}'.format(idx),
                'WEA[0]',
            )

    else:
        for idx in range(4):
            assert top.find_source_from_sink(site, 'WEAL{}'.format(idx)) == \
                top.find_source_from_sink(site, 'WEAU{}'.format(idx))
            site.mask_sink(bel, "WEAU[{}]".format(idx))
            bel.remap_bel_pin_to_cell_pin(
                bel.bel,
                'WEAU{}'.format(idx),
                'WEA[{}]'.format(idx),
            )

    if bel.parameters['WRITE_WIDTH_B'] < 18:
        for idx in range(8):
            assert top.find_source_from_sink(site, 'WEBWEL{}'.format(idx)) == \
                top.find_source_from_sink(site, 'WEBWEU{}'.format(idx))
            site.mask_sink(bel, "WEBWEU[{}]".format(idx))

        for idx in range(4):
            bel.remap_bel_pin_to_cell_pin(
                bel.bel,
                'WEBWEL{}'.format(idx),
                'WEBWE[0]',
            )
            bel.remap_bel_pin_to_cell_pin(
                bel.bel,
                'WEBWEU{}'.format(idx),
                'WEBWE[0]',
            )

            bel.unmap_bel_pin(bel.bel, 'WEBWEU{}'.format(idx + 4))
            bel.unmap_bel_pin(bel.bel, 'WEBWEL{}'.format(idx + 4))

    else:
        for idx in range(8):
            assert top.find_source_from_sink(site, 'WEBWEL{}'.format(idx)) == \
                top.find_source_from_sink(site, 'WEBWEU{}'.format(idx))
            site.mask_sink(bel, "WEBWEU[{}]".format(idx))
            bel.remap_bel_pin_to_cell_pin(
                bel.bel,
                'WEBWEU{}'.format(idx),
                'WEBWE[{}]'.format(idx),
            )

    if bel.parameters['WRITE_WIDTH_A'] == 9:
        bel.remap_bel_pin_to_cell_pin(bel.bel, 'DIPADIP1', 'DIPADIP[0]')

    if bel.parameters['WRITE_WIDTH_B'] == 9:
        bel.remap_bel_pin_to_cell_pin(bel.bel, 'DIPBDIP1', 'DIPBDIP[0]')

    if bel.parameters['WRITE_WIDTH_A'] == 1:
        bel.unmap_bel_pin(bel.bel, 'DIPADIP1')
        bel.unmap_bel_pin(bel.bel, 'DIPADIP0')

        bel.remap_bel_pin_to_cell_pin(bel.bel, 'DIADI1', 'DIADI[0]')

    if bel.parameters['WRITE_WIDTH_B'] == 1:
        bel.unmap_bel_pin(bel.bel, 'DIPBDIP1')
        bel.unmap_bel_pin(bel.bel, 'DIPBDIP0')

        bel.remap_bel_pin_to_cell_pin(bel.bel, 'DIBDI1', 'DIBDI[0]')

    bel.unmap_bel_pin(bel.bel, 'REGCLKBU')
    bel.unmap_bel_pin(bel.bel, 'REGCLKBL')
    bel.unmap_bel_pin(bel.bel, 'REGCLKARDRCLKU')
    bel.unmap_bel_pin(bel.bel, 'REGCLKARDRCLKL')

    site.mask_sink(bel, 'REGCLKB')
    site.mask_sink(bel, 'REGCLKARDRCLK')

    for input_wire in [
            "CLKARDCLK",
            "CLKBWRCLK",
            "ENARDEN",
            "ENBWREN",
            "REGCEAREGCE",
            "REGCEB",
            "RSTREGARSTREG",
            "RSTRAMB",
            "RSTREGB",
    ]:
        assert top.find_source_from_sink(
            site, input_wire + 'L') == top.find_source_from_sink(
                site, input_wire + 'U')
        site.mask_sink(bel, input_wire + 'U')
        bel.remap_bel_pin_to_cell_pin(bel.bel, input_wire + 'U', input_wire)

    for input_wire in [
            "REGCLKB",
            "REGCLKARDRCLK",
    ]:
        assert top.find_source_from_sink(
            site, input_wire + 'L') == top.find_source_from_sink(
                site, input_wire + 'U')
        site.mask_sink(bel, input_wire + 'U')

    assert top.find_source_from_sink(
        site, 'RSTRAMARSTRAMLRST') == top.find_source_from_sink(
            site, 'RSTRAMARSTRAMU')

    site.mask_sink(bel, 'RSTRAMARSTRAMU')
    bel.remap_bel_pin_to_cell_pin(bel.bel, 'RSTRAMARSTRAMU', 'RSTRAMARSTRAM')


def clean_brams(top, bram_sites, bram36_site, tile_features, verbose=False):
    """ Cleanup BRAM tile when BRAM18's might be merged into BRAM36. """
    if not eligible_for_merge(top, bram_sites, tile_features, verbose=verbose):
        if verbose:
            print("Don't merge")
        for bram in bram_sites:
            clean_up_to_bram18(top, bram)
        top.remove_site(bram36_site)
    else:
        if verbose:
            print("Merge sites!")
        clean_up_to_bram36(top, bram36_site)
        for bram in bram_sites:
            top.remove_site(bram)


def process_bram_site(top, features, set_features):
    if 'IN_USE' not in set_features:
        return

    aparts = features[0].feature.split('.')
    bram_site = get_bram_site(top.db, top.grid, aparts[0], aparts[1])
    site = Site(features, bram_site)

    bel = Bel('RAMB18E1')
    bel.set_bel('RAMB18E1')
    site.add_bel(bel, name='RAMB18E1')
    site.override_site_type('RAMB18E1')

    bel.set_port_width('WEA', 2)
    bel.set_port_width('WEBWE', 4)

    fifo_site = bram_site.type == 'FIFO18E1'

    fifo_site_wire_map = {
        'REGCEAREGCE': 'REGCE',
        'REGCLKARDRCLK': 'RDRCLK',
        'RSTRAMARSTRAM': 'RST',
        'RSTREGARSTREG': 'RSTREG',
        'ENBWREN': 'WREN',
        'CLKBWRCLK': 'WRCLK',
        'ENARDEN': 'RDEN',
        'CLKARDCLK': 'RDCLK',
    }

    for idx in range(16):
        fifo_site_wire_map['DOADO{}'.format(idx)] = 'DO{}'.format(idx)
        fifo_site_wire_map['DOBDO{}'.format(idx)] = 'DO{}'.format(idx + 16)

    for idx in range(2):
        fifo_site_wire_map['DOPADOP{}'.format(idx)] = 'DOP{}'.format(idx)
        fifo_site_wire_map['DOPBDOP{}'.format(idx)] = 'DOP{}'.format(idx + 2)

    def make_wire(wire_name):
        if fifo_site and wire_name in fifo_site_wire_map:
            return fifo_site_wire_map[wire_name]
        else:
            return wire_name

    # Parameters

    def make_target_feature(feature):
        return '{}.{}.{}'.format(aparts[0], aparts[1], feature)

    parameter_binds = [
        ('INIT_A', ['ZINIT_A'], True, 18),
        ('INIT_B', ['ZINIT_B'], True, 18),
        ('SRVAL_A', ['ZSRVAL_A'], True, 18),
        ('SRVAL_B', ['ZSRVAL_B'], True, 18),
    ]

    for pidx in range(8):
        parameter_binds.append(('INITP_0{}'.format(pidx),
                                ['INITP_0{}'.format(pidx)], False, 256))

    for idx in range(0x40):
        parameter_binds.append(('INIT_{:02X}'.format(idx),
                                ['INIT_{:02X}'.format(idx)], False, 256))

    for vparam, fparam, invert, width in parameter_binds:
        bel.parameters[vparam] = get_init(
            features, [make_target_feature(p) for p in fparam],
            invert=invert,
            width=width)

    bel.parameters['DOA_REG'] = int('DOA_REG' in set_features)
    bel.parameters['DOB_REG'] = int('DOB_REG' in set_features)
    """
     SDP_READ_WIDTH_36 = SDP_READ_WIDTH_36
     READ_WIDTH_A_18 = READ_WIDTH_A_18
     READ_WIDTH_A_9 = READ_WIDTH_A_9
     READ_WIDTH_A_4 = READ_WIDTH_A_4
     READ_WIDTH_A_2 = READ_WIDTH_A_2
     READ_WIDTH_A_1 = READ_WIDTH_A_1
     READ_WIDTH_B_18 = READ_WIDTH_B_18
     READ_WIDTH_B_9 = READ_WIDTH_B_9
     READ_WIDTH_B_4 = READ_WIDTH_B_4
     READ_WIDTH_B_2 = READ_WIDTH_B_2
     READ_WIDTH_B_1 = READ_WIDTH_B_1
    """

    RAM_MODE = '"TDP"'
    if 'SDP_READ_WIDTH_36' in set_features:
        assert 'READ_WIDTH_A_1' in set_features or 'READ_WIDTH_A_18' in set_features
        assert 'READ_WIDTH_B_18' in set_features
        READ_WIDTH_A = 36
        READ_WIDTH_B = 0
        RAM_MODE = '"SDP"'
    else:
        if 'READ_WIDTH_A_1' in set_features:
            READ_WIDTH_A = 1
        elif 'READ_WIDTH_A_2' in set_features:
            READ_WIDTH_A = 2
        elif 'READ_WIDTH_A_4' in set_features:
            READ_WIDTH_A = 4
        elif 'READ_WIDTH_A_9' in set_features:
            READ_WIDTH_A = 9
        elif 'READ_WIDTH_A_18' in set_features:
            READ_WIDTH_A = 18
        else:
            assert False

        if 'READ_WIDTH_B_1' in set_features:
            READ_WIDTH_B = 1
        elif 'READ_WIDTH_B_2' in set_features:
            READ_WIDTH_B = 2
        elif 'READ_WIDTH_B_4' in set_features:
            READ_WIDTH_B = 4
        elif 'READ_WIDTH_B_9' in set_features:
            READ_WIDTH_B = 9
        elif 'READ_WIDTH_B_18' in set_features:
            READ_WIDTH_B = 18
        else:
            assert False
    """
     SDP_WRITE_WIDTH_36 = SDP_WRITE_WIDTH_36
     WRITE_WIDTH_A_18 = WRITE_WIDTH_A_18
     WRITE_WIDTH_A_9 = WRITE_WIDTH_A_9
     WRITE_WIDTH_A_4 = WRITE_WIDTH_A_4
     WRITE_WIDTH_A_2 = WRITE_WIDTH_A_2
     WRITE_WIDTH_A_1 = WRITE_WIDTH_A_1
     WRITE_WIDTH_B_18 = WRITE_WIDTH_B_18
     WRITE_WIDTH_B_9 = WRITE_WIDTH_B_9
     WRITE_WIDTH_B_4 = WRITE_WIDTH_B_4
     WRITE_WIDTH_B_2 = WRITE_WIDTH_B_2
     WRITE_WIDTH_B_1 = WRITE_WIDTH_B_1
    """

    if 'SDP_WRITE_WIDTH_36' in set_features:
        assert 'WRITE_WIDTH_A_18' in set_features
        assert 'WRITE_WIDTH_B_18' in set_features
        WRITE_WIDTH_A = 0
        WRITE_WIDTH_B = 36
        RAM_MODE = '"SDP"'
    else:
        if 'WRITE_WIDTH_A_1' in set_features:
            WRITE_WIDTH_A = 1
        elif 'WRITE_WIDTH_A_2' in set_features:
            WRITE_WIDTH_A = 2
        elif 'WRITE_WIDTH_A_4' in set_features:
            WRITE_WIDTH_A = 4
        elif 'WRITE_WIDTH_A_9' in set_features:
            WRITE_WIDTH_A = 9
        elif 'WRITE_WIDTH_A_18' in set_features:
            WRITE_WIDTH_A = 18
        else:
            assert False

        if 'WRITE_WIDTH_B_1' in set_features:
            WRITE_WIDTH_B = 1
        elif 'WRITE_WIDTH_B_2' in set_features:
            WRITE_WIDTH_B = 2
        elif 'WRITE_WIDTH_B_4' in set_features:
            WRITE_WIDTH_B = 4
        elif 'WRITE_WIDTH_B_9' in set_features:
            WRITE_WIDTH_B = 9
        elif 'WRITE_WIDTH_B_18' in set_features:
            WRITE_WIDTH_B = 18
        else:
            assert False

    bel.parameters['RAM_MODE'] = RAM_MODE
    bel.parameters['READ_WIDTH_A'] = READ_WIDTH_A
    bel.parameters['READ_WIDTH_B'] = READ_WIDTH_B
    bel.parameters['WRITE_WIDTH_A'] = WRITE_WIDTH_A
    bel.parameters['WRITE_WIDTH_B'] = WRITE_WIDTH_B
    """
     ZINV_CLKARDCLK = ZINV_CLKARDCLK
     ZINV_CLKBWRCLK = ZINV_CLKBWRCLK
     ZINV_ENARDEN = ZINV_ENARDEN
     ZINV_ENBWREN = ZINV_ENBWREN
     ZINV_RSTRAMARSTRAM = ZINV_RSTRAMARSTRAM
     ZINV_RSTRAMB = ZINV_RSTRAMB
     ZINV_RSTREGARSTREG = ZINV_RSTREGARSTREG
     ZINV_RSTREGB = ZINV_RSTREGB
     ZINV_REGCLKARDRCLK = ZINV_REGCLKARDRCLK
     ZINV_REGCLKB = ZINV_REGCLKB
    """
    for wire in (
            'CLKARDCLK',
            'CLKBWRCLK',
            'ENARDEN',
            'ENBWREN',
            'RSTRAMARSTRAM',
            'RSTRAMB',
            'RSTREGARSTREG',
            'RSTREGB',
    ):
        bel.parameters['IS_{}_INVERTED'.format(wire)] = int(
            not 'ZINV_{}'.format(wire) in set_features)

        site_pips = make_inverter_path(
            wire, bel.parameters['IS_{}_INVERTED'.format(wire)])

        wire_name = make_wire(wire)
        site.add_sink(
            bel=bel,
            cell_pin=wire,
            sink_site_pin=wire_name,
            bel_name=bel.bel,
            bel_pin=wire,
            site_pips=site_pips,
            sink_site_type_pin=wire,
        )

    for wire in (
            "REGCLKARDRCLK",
            "REGCLKB",
    ):

        wire_inverted = (not 'ZINV_{}'.format(wire) in set_features)
        site_pips = make_inverter_path(wire, wire_inverted)

        wire_name = make_wire(wire)
        site.add_sink(
            bel=bel,
            cell_pin=wire,
            sink_site_pin=wire_name,
            bel_name=bel.bel,
            bel_pin=wire,
            site_pips=site_pips,
            sink_site_type_pin=wire,
        )
    """
     WRITE_MODE_A_NO_CHANGE = WRITE_MODE_A_NO_CHANGE
     WRITE_MODE_A_READ_FIRST = WRITE_MODE_A_READ_FIRST
     WRITE_MODE_B_NO_CHANGE = WRITE_MODE_B_NO_CHANGE
     WRITE_MODE_B_READ_FIRST = WRITE_MODE_B_READ_FIRST
    """
    if 'WRITE_MODE_A_NO_CHANGE' in set_features:
        bel.parameters['WRITE_MODE_A'] = '"NO_CHANGE"'
    elif 'WRITE_MODE_A_READ_FIRST' in set_features:
        bel.parameters['WRITE_MODE_A'] = '"READ_FIRST"'
    else:
        bel.parameters['WRITE_MODE_A'] = '"WRITE_FIRST"'

    if 'WRITE_MODE_B_NO_CHANGE' in set_features:
        bel.parameters['WRITE_MODE_B'] = '"NO_CHANGE"'
    elif 'WRITE_MODE_B_READ_FIRST' in set_features:
        bel.parameters['WRITE_MODE_B'] = '"READ_FIRST"'
    else:
        bel.parameters['WRITE_MODE_B'] = '"WRITE_FIRST"'

    for input_wire in [
            "REGCEAREGCE",
            "REGCEB",
    ]:
        wire_name = make_wire(input_wire)
        site.add_sink(
            bel=bel,
            cell_pin=input_wire,
            sink_site_pin=wire_name,
            bel_name=bel.bel,
            bel_pin=input_wire,
            sink_site_type_pin=input_wire,
        )

    input_wires = [
        ("ADDRARDADDR", 14),
        ("ADDRBWRADDR", 14),
        ("DIADI", 16),
        ("DIBDI", 16),
        ("DIPADIP", 2),
        ("DIPBDIP", 2),
        ("ADDRATIEHIGH", 2),
        ("ADDRBTIEHIGH", 2),
    ]

    for input_wire, width in input_wires:
        for idx in range(width):
            site_wire = '{}{}'.format(input_wire, idx)
            wire_name = make_wire(site_wire)
            site.add_sink(
                bel=bel,
                cell_pin='{}[{}]'.format(input_wire, idx),
                sink_site_pin=wire_name,
                bel_name=bel.bel,
                bel_pin=site_wire,
                sink_site_type_pin=site_wire)

    # If both BRAM's are in play, emit all wires and handle it in cleanup.
    for idx in range(4):
        site.add_sink(
            bel=bel,
            cell_pin="WEA[{}]".format(idx),
            sink_site_pin="WEA{}".format(idx),
            bel_name=bel.bel,
            bel_pin="WEA{}".format(idx))
    for idx in range(8):
        site.add_sink(
            bel=bel,
            cell_pin="WEBWE[{}]".format(idx),
            sink_site_pin="WEBWE{}".format(idx),
            bel_name=bel.bel,
            bel_pin="WEBWE{}".format(idx))

    for output_wire, width in [
        ('DOADO', 16),
        ('DOPADOP', 2),
        ('DOBDO', 16),
        ('DOPBDOP', 2),
    ]:
        for idx in range(width):
            input_wire = '{}{}'.format(output_wire, idx)
            wire_name = make_wire(input_wire)
            pin_name = '{}[{}]'.format(output_wire, idx)
            site.add_source(
                bel=bel,
                cell_pin=pin_name,
                source_site_pin=wire_name,
                bel_name=bel.bel,
                bel_pin=input_wire,
                source_site_type_pin=input_wire)

    top.add_site(site)

    return site


def fasm2bitarray(fasm_value):
    """ Convert FASM value into array of bits ('0', '1')

    Note: index 0 is the LSB.

    """
    m = re.match("([0-9]+)'([bh])([0-9a-fA-F]+)", fasm_value)
    assert m is not None, fasm_value

    bits = int(m.group(1))
    if m.group(2) == 'b':
        bitarray = m.group(2)
        int(bitarray, 2)
    else:
        bitarray = '{{:0{}b}}'.format(bits).format(int(m.group(3), 16))

    assert len(bitarray) == bits, (fasm_value, len(bitarray), bits)

    return [b for b in bitarray][::-1]


def bitarray2fasm(bitarray):
    """ Convert array of bits ('0', '1') into FASM value.

    Note: index 0 is the LSB.

    """
    bitstr = ''.join(bitarray[::-1])

    return "{{}}'h{{:0{}X}}".format(int(math.ceil(len(bitstr) / 4))).format(
        len(bitstr), int(bitstr, 2))


def remap_init(parameters):
    """ Remap INIT and INITP parameters from BRAM18 oriented FASM to BRAM36 BEL parameters.

    Algorithm documentation, modelling parameters as array of bits.  ARR[0] is
    LSB, ARR[-1] is MSB.

    Forward:

    INITP_00 = INITP_00[::2] + INITP_01[::2]
    INITP_08 = INITP_00[1::2] + INITP_01[1::2]

    INITP_01 = INITP_02[::2] + INITP_03[::2]
    INITP_09 = INITP_02[1::2] + INITP_03[1::2]

    ...

    INITP_07 = INITP_0E[::2] + INITP_0F[::2]
    INITP_0F = INITP_0E[1::2] + INITP_0F[1::2]

    INIT_00 = INIT_00[::2] + INIT_01[::2]
    INIT_08 = INIT_10[::2] + INIT_11[::2]

    ...

    INIT_37 = INIT_6E[::2] + INIT_6F[::2]
    INIT_3F = INIT_7E[::2] + INIT_7F[::2]

    INIT_40 = INIT_00[1::2] + INIT_01[1::2]
    INIT_48 = INIT_10[1::2] + INIT_11[1::2]

    ...

    INIT_77 = INIT_6E[1::2] + INIT_6F[1::2]
    INIT_7F = INIT_7E[1::2] + INIT_7F[1::2]

    Backward:

    INITP_00[::2] = INITP_00[:128]
    INITP_00[1::2] = INITP_08[:128]
    INITP_01[::2] = INITP_00[128:]
    INITP_01[1::2] = INITP_08[128:]

    INITP_02[::2] = INITP_01[:128]
    INITP_02[1::2] = INITP_09[:128]
    INITP_03[::2] = INITP_01[128:]
    INITP_03[1::2] = INITP_09[128:]

    ...

    INITP_0E[::2] = INITP_07[:128]
    INITP_0E[1::2] = INITP_0F[:128]
    INITP_0F[::2] = INITP_07[128:]
    INITP_0F[1::2] = INITP_0F[128:]

    INIT_00[::2] = INIT_00[:128]
    INIT_00[1::2] = INIT_40[:128]
    INIT_01[::2] = INIT_00[128:]
    INIT_01[1::2] = INIT_40[:128]

    ...

    INIT_7E[::2] = INIT_3F[:128]
    INIT_7E[1::2] = INIT_7F[:128]
    INIT_7F[::2] = INIT_3F[128:]
    INIT_7F[1::2] = INIT_7F[128:]

    """

    init = {}

    # First convert FASM parameters into bitarray's.
    for idx in range(0x10):
        init[('P',
              idx)] = fasm2bitarray(parameters['INITP_{:02X}'.format(idx)])

    for idx in range(0x80):
        init[('', idx)] = fasm2bitarray(parameters['INIT_{:02X}'.format(idx)])

    out_init = {}

    # Initial output arrays.
    for k in init:
        assert len(init[k]) == 256
        out_init[k] = ['0' for _ in range(256)]
    """
    INITP_00[::2] = INITP_00[:128]
    INITP_00[1::2] = INITP_08[:128]
    INITP_01[::2] = INITP_00[128:]
    INITP_01[1::2] = INITP_08[128:]

    INITP_02[::2] = INITP_01[:128]
    INITP_02[1::2] = INITP_09[:128]
    INITP_03[::2] = INITP_01[128:]
    INITP_03[1::2] = INITP_09[128:]

    ...

    INITP_0E[::2] = INITP_07[:128]
    INITP_0E[1::2] = INITP_0F[:128]
    INITP_0F[::2] = INITP_07[128:]
    INITP_0F[1::2] = INITP_0F[128:]

    """
    for idx in range(0x8):
        out_init[('P', idx * 2)][::2] = init[('P', idx)][:128]
        out_init[('P', idx * 2)][1::2] = init[('P', idx + 0x8)][:128]
        out_init[('P', idx * 2 + 1)][::2] = init[('P', idx)][128:]
        out_init[('P', idx * 2 + 1)][1::2] = init[('P', idx + 0x8)][128:]
    """

    INIT_00[::2] = INIT_00[:128]
    INIT_00[1::2] = INIT_40[:128]
    INIT_01[::2] = INIT_00[128:]
    INIT_01[1::2] = INIT_40[:128]

    ...

    INIT_7E[::2] = INIT_3F[:128]
    INIT_7E[1::2] = INIT_7F[:128]
    INIT_7F[::2] = INIT_3F[128:]
    INIT_7F[1::2] = INIT_7F[128:]

    """
    for idx in range(0x40):
        out_init[('', idx * 2)][::2] = init[('', idx)][:128]
        out_init[('', idx * 2)][1::2] = init[('', idx + 0x40)][:128]
        out_init[('', idx * 2 + 1)][::2] = init[('', idx)][128:]
        out_init[('', idx * 2 + 1)][1::2] = init[('', idx + 0x40)][128:]

    # Convert bitarrays back into FASM values and update parameters dict.
    for (postfix, idx), bitarray in out_init.items():
        param = 'INIT{}_{:02X}'.format(postfix, idx)
        parameters[param] = bitarray2fasm(bitarray)


def process_bram36_site(top, features, set_features):
    aparts = features[0].feature.split('.')
    bram_site = get_bram36_site(top.db, top.grid, aparts[0])
    site = Site(features, bram_site, merged_site=True)

    bel = Bel('RAMB36E1')
    bel.set_bel('RAMB36E1')
    site.add_bel(bel, name='RAMB36E1')
    site.override_site_type('RAMB36E1')

    # Parameters

    def make_target_feature(feature):
        return '{}.{}'.format(aparts[0], feature)

    parameter_binds = [
        ('INIT_A', ['RAMB18_Y0.ZINIT_A', 'RAMB18_Y1.ZINIT_A'], True, 36),
        ('INIT_B', ['RAMB18_Y0.ZINIT_B', 'RAMB18_Y1.ZINIT_A'], True, 36),
        ('SRVAL_A', ['RAMB18_Y0.ZSRVAL_A', 'RAMB18_Y1.ZSRVAL_A'], True, 36),
        ('SRVAL_B', ['RAMB18_Y0.ZSRVAL_B', 'RAMB18_Y1.ZSRVAL_B'], True, 36),
    ]

    for pidx in range(8):
        parameter_binds.append(
            ('INITP_{:02X}'.format(pidx),
             ['RAMB18_Y0.INITP_{:02}'.format(pidx)], False, 256))
        parameter_binds.append(
            ('INITP_{:02X}'.format(pidx + 8),
             ['RAMB18_Y1.INITP_{:02X}'.format(pidx)], False, 256))

    for idx in range(0x40):
        parameter_binds.append(
            ('INIT_{:02X}'.format(idx), ['RAMB18_Y0.INIT_{:02X}'.format(idx)],
             False, 256))
        parameter_binds.append(
            ('INIT_{:02X}'.format(idx + 0x40),
             ['RAMB18_Y1.INIT_{:02X}'.format(idx)], False, 256))

    for vparam, fparam, invert, width in parameter_binds:
        bel.parameters[vparam] = get_init(
            features, [make_target_feature(p) for p in fparam],
            invert=invert,
            width=width)

    remap_init(bel.parameters)

    bel.parameters['DOA_REG'] = int('RAMB18_Y0.DOA_REG' in set_features)
    bel.parameters['DOB_REG'] = int('RAMB18_Y0.DOB_REG' in set_features)
    """
     SDP_READ_WIDTH_36 = SDP_READ_WIDTH_36
     READ_WIDTH_A_18 = READ_WIDTH_A_18
     READ_WIDTH_A_9 = READ_WIDTH_A_9
     READ_WIDTH_A_4 = READ_WIDTH_A_4
     READ_WIDTH_A_2 = READ_WIDTH_A_2
     READ_WIDTH_A_1 = READ_WIDTH_A_1
     READ_WIDTH_B_18 = READ_WIDTH_B_18
     READ_WIDTH_B_9 = READ_WIDTH_B_9
     READ_WIDTH_B_4 = READ_WIDTH_B_4
     READ_WIDTH_B_2 = READ_WIDTH_B_2
     READ_WIDTH_B_1 = READ_WIDTH_B_1
    """

    RAM_MODE = '"TDP"'
    if 'RAMB18_Y0.SDP_READ_WIDTH_36' in set_features:
        assert 'RAMB18_Y0.READ_WIDTH_A_18' in set_features
        assert 'RAMB18_Y0.READ_WIDTH_B_18' in set_features
        READ_WIDTH_A = 72
        READ_WIDTH_B = 0
        RAM_MODE = '"SDP"'
    else:
        if 'RAMB18_Y0.READ_WIDTH_A_1' in set_features:
            if 'RAMB36.BRAM36_READ_WIDTH_A_1' in set_features:
                READ_WIDTH_A = 1
            else:
                READ_WIDTH_A = 2
        elif 'RAMB18_Y0.READ_WIDTH_A_2' in set_features:
            READ_WIDTH_A = 4
        elif 'RAMB18_Y0.READ_WIDTH_A_4' in set_features:
            READ_WIDTH_A = 9
        elif 'RAMB18_Y0.READ_WIDTH_A_9' in set_features:
            READ_WIDTH_A = 18
        elif 'RAMB18_Y0.READ_WIDTH_A_18' in set_features:
            READ_WIDTH_A = 36
        else:
            assert False

        if 'RAMB18_Y0.READ_WIDTH_B_1' in set_features:
            if 'RAMB36.BRAM36_READ_WIDTH_B_1' in set_features:
                READ_WIDTH_B = 1
            else:
                READ_WIDTH_B = 2
        elif 'RAMB18_Y0.READ_WIDTH_B_2' in set_features:
            READ_WIDTH_B = 4
        elif 'RAMB18_Y0.READ_WIDTH_B_4' in set_features:
            READ_WIDTH_B = 9
        elif 'RAMB18_Y0.READ_WIDTH_B_9' in set_features:
            READ_WIDTH_B = 18
        elif 'RAMB18_Y0.READ_WIDTH_B_18' in set_features:
            READ_WIDTH_B = 36
        else:
            assert False
    """
     SDP_WRITE_WIDTH_36 = SDP_WRITE_WIDTH_36
     WRITE_WIDTH_A_18 = WRITE_WIDTH_A_18
     WRITE_WIDTH_A_9 = WRITE_WIDTH_A_9
     WRITE_WIDTH_A_4 = WRITE_WIDTH_A_4
     WRITE_WIDTH_A_2 = WRITE_WIDTH_A_2
     WRITE_WIDTH_A_1 = WRITE_WIDTH_A_1
     WRITE_WIDTH_B_18 = WRITE_WIDTH_B_18
     WRITE_WIDTH_B_9 = WRITE_WIDTH_B_9
     WRITE_WIDTH_B_4 = WRITE_WIDTH_B_4
     WRITE_WIDTH_B_2 = WRITE_WIDTH_B_2
     WRITE_WIDTH_B_1 = WRITE_WIDTH_B_1
    """

    if 'RAMB18_Y0.SDP_WRITE_WIDTH_36' in set_features:
        assert 'RAMB18_Y0.WRITE_WIDTH_A_18' in set_features
        assert 'RAMB18_Y0.WRITE_WIDTH_B_18' in set_features
        WRITE_WIDTH_A = 0
        WRITE_WIDTH_B = 72
        RAM_MODE = '"SDP"'
    else:
        if 'RAMB18_Y0.WRITE_WIDTH_A_1' in set_features:
            if 'RAMB36.BRAM36_WRITE_WIDTH_A_1' in set_features:
                WRITE_WIDTH_A = 1
            else:
                WRITE_WIDTH_A = 2
        elif 'RAMB18_Y0.WRITE_WIDTH_A_2' in set_features:
            WRITE_WIDTH_A = 4
        elif 'RAMB18_Y0.WRITE_WIDTH_A_4' in set_features:
            WRITE_WIDTH_A = 9
        elif 'RAMB18_Y0.WRITE_WIDTH_A_9' in set_features:
            WRITE_WIDTH_A = 18
        elif 'RAMB18_Y0.WRITE_WIDTH_A_18' in set_features:
            WRITE_WIDTH_A = 36
        else:
            assert False

        if 'RAMB18_Y0.WRITE_WIDTH_B_1' in set_features:
            if 'RAMB36.BRAM36_WRITE_WIDTH_B_1' in set_features:
                WRITE_WIDTH_B = 1
            else:
                WRITE_WIDTH_B = 2
        elif 'RAMB18_Y0.WRITE_WIDTH_B_2' in set_features:
            WRITE_WIDTH_B = 4
        elif 'RAMB18_Y0.WRITE_WIDTH_B_4' in set_features:
            WRITE_WIDTH_B = 9
        elif 'RAMB18_Y0.WRITE_WIDTH_B_9' in set_features:
            WRITE_WIDTH_B = 18
        elif 'RAMB18_Y0.WRITE_WIDTH_B_18' in set_features:
            WRITE_WIDTH_B = 36
        else:
            assert False

    bel.parameters['RAM_MODE'] = RAM_MODE
    bel.parameters['READ_WIDTH_A'] = READ_WIDTH_A
    bel.parameters['READ_WIDTH_B'] = READ_WIDTH_B
    bel.parameters['WRITE_WIDTH_A'] = WRITE_WIDTH_A
    bel.parameters['WRITE_WIDTH_B'] = WRITE_WIDTH_B
    """
     ZINV_CLKARDCLK = ZINV_CLKARDCLK
     ZINV_CLKBWRCLK = ZINV_CLKBWRCLK
     ZINV_ENARDEN = ZINV_ENARDEN
     ZINV_ENBWREN = ZINV_ENBWREN
     ZINV_RSTRAMARSTRAM = ZINV_RSTRAMARSTRAM
     ZINV_RSTRAMB = ZINV_RSTRAMB
     ZINV_RSTREGARSTREG = ZINV_RSTREGARSTREG
     ZINV_RSTREGB = ZINV_RSTREGB
     ZINV_REGCLKARDRCLK = ZINV_REGCLKARDRCLK
     ZINV_REGCLKB = ZINV_REGCLKB
    """
    for wire in (
            'CLKARDCLK',
            'CLKBWRCLK',
            'ENARDEN',
            'ENBWREN',
            'RSTRAMARSTRAM',
            'RSTRAMB',
            'RSTREGARSTREG',
            'RSTREGB',
    ):
        bel.parameters['IS_{}_INVERTED'.format(wire)] = int(
            not 'RAMB18_Y0.ZINV_{}'.format(wire) in set_features)

        for ul in 'UL':
            site_pips = make_inverter_path(
                wire + ul, bel.parameters['IS_{}_INVERTED'.format(wire)])

            extra = ''
            if ul == 'U':
                cell_pin = wire + 'U'
            else:
                assert ul == 'L'
                cell_pin = wire

                if wire == 'RSTRAMARSTRAM':
                    extra = 'RST'

            site.add_sink(
                bel=bel,
                cell_pin=cell_pin,
                sink_site_pin=wire + ul + extra,
                bel_name=bel.bel,
                bel_pin=wire + ul,
                site_pips=site_pips,
                sink_site_type_pin=wire + ul,
            )

    for wire in (
            "REGCLKARDRCLK",
            "REGCLKB",
    ):

        for ul in 'UL':
            wire_inverted = (not 'ZINV_{}'.format(wire) in set_features)
            site_pips = make_inverter_path(wire + ul, wire_inverted)

            if ul == 'U':
                cell_pin = wire + 'U'
            else:
                cell_pin = wire

            site.add_sink(
                bel=bel,
                cell_pin=cell_pin,
                sink_site_pin=wire + ul,
                bel_name=bel.bel,
                bel_pin=wire + ul,
                site_pips=site_pips,
            )

    for input_wire in [
            "REGCEAREGCE",
            "REGCEB",
    ]:
        site.add_sink(bel, input_wire, input_wire + 'L', bel.bel,
                      input_wire + 'L')
        site.add_sink(bel, input_wire + 'U', input_wire + 'U', bel.bel,
                      input_wire + 'U')
    """
     WRITE_MODE_A_NO_CHANGE = WRITE_MODE_A_NO_CHANGE
     WRITE_MODE_A_READ_FIRST = WRITE_MODE_A_READ_FIRST
     WRITE_MODE_B_NO_CHANGE = WRITE_MODE_B_NO_CHANGE
     WRITE_MODE_B_READ_FIRST = WRITE_MODE_B_READ_FIRST
    """
    if 'RAMB18_Y0.WRITE_MODE_A_NO_CHANGE' in set_features:
        bel.parameters['WRITE_MODE_A'] = '"NO_CHANGE"'
    elif 'RAMB18_Y0.WRITE_MODE_A_READ_FIRST' in set_features:
        bel.parameters['WRITE_MODE_A'] = '"READ_FIRST"'
    else:
        bel.parameters['WRITE_MODE_A'] = '"WRITE_FIRST"'

    if 'RAMB18_Y0.WRITE_MODE_B_NO_CHANGE' in set_features:
        bel.parameters['WRITE_MODE_B'] = '"NO_CHANGE"'
    elif 'RAMB18_Y0.WRITE_MODE_B_READ_FIRST' in set_features:
        bel.parameters['WRITE_MODE_B'] = '"READ_FIRST"'
    else:
        bel.parameters['WRITE_MODE_B'] = '"WRITE_FIRST"'

    input_wires = [
        ("ADDRARDADDRL", 16),
        ("ADDRARDADDRU", 15),
        ("ADDRBWRADDRL", 16),
        ("ADDRBWRADDRU", 15),
        ("DIADI", 32),
        ("DIBDI", 32),
        ("DIPADIP", 4),
        ("DIPBDIP", 4),
    ]

    for input_wire, width in input_wires:
        for idx in range(width):
            wire_name = '{}{}'.format(input_wire, idx)
            site.add_sink(bel, '{}[{}]'.format(input_wire, idx), wire_name,
                          bel.bel, wire_name)

    bel.set_port_width('WEA', 4)
    bel.set_port_width('WEBWE', 8)

    for idx in range(4):
        site_pin = "WEAL{}".format(idx)
        site.add_sink(bel, "WEA[{}]".format(idx), site_pin, bel.bel, site_pin)
        site_pin = "WEAU{}".format(idx)
        site.add_sink(bel, "WEAU[{}]".format(idx), site_pin, bel.bel, site_pin)

    for idx in range(8):
        site_pin = "WEBWEL{}".format(idx)
        site.add_sink(bel, "WEBWE[{}]".format(idx), site_pin, bel.bel,
                      site_pin)
        site_pin = "WEBWEU{}".format(idx)
        site.add_sink(bel, "WEBWEU[{}]".format(idx), site_pin, bel.bel,
                      site_pin)

    for output_wire, width in [
        ('DOADO', 32),
        ('DOPADOP', 4),
        ('DOBDO', 32),
        ('DOPBDOP', 4),
    ]:
        for idx in range(width):
            wire_name = '{}{}'.format(output_wire, idx)
            pin_name = '{}[{}]'.format(output_wire, idx)
            site.add_source(bel, pin_name, wire_name, bel.bel, wire_name)

    bel.add_unconnected_port('INJECTSBITERR', None, direction="input")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'INJECTSBITERR', 'INJECTSBITERR')
    bel.add_unconnected_port('INJECTDBITERR', None, direction="input")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'INJECTDBITERR', 'INJECTDBITERR')

    bel.add_unconnected_port('SBITERR', None, direction="output")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'SBITERR', 'SBITERR')
    bel.add_unconnected_port('DBITERR', None, direction="output")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'DBITERR', 'DBITERR')

    bel.add_unconnected_port('CASCADEINA', None, direction="input")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'CASCADEINA', 'CASCADEINA')
    bel.add_unconnected_port('CASCADEINB', None, direction="input")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'CASCADEINB', 'CASCADEINB')

    bel.add_unconnected_port('CASCADEOUTA', None, direction="output")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'CASCADEOUTA', 'CASCADEOUTA')
    bel.add_unconnected_port('CASCADEOUTB', None, direction="output")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'CASCADEOUTB', 'CASCADEOUTB')

    bel.add_unconnected_port('ECCPARITY', 8, direction="output")
    for idx in range(8):
        bel.map_bel_pin_to_cell_pin(bel.bel, 'ECCPARITY{}'.format(idx),
                                    'ECCPARITY[{}]'.format(idx))

    bel.add_unconnected_port('RDADDRECC', 9, direction="output")
    for idx in range(9):
        bel.map_bel_pin_to_cell_pin(bel.bel, 'RDADDRECC{}'.format(idx),
                                    'RDADDRECC[{}]'.format(idx))

    top.add_site(site)

    return site


def process_bram(conn, top, tile, features):
    tile_features = set()

    brams = {'RAMB18_Y0': [], 'RAMB18_Y1': []}

    bram_features = {'RAMB18_Y0': set(), 'RAMB18_Y1': set()}

    for f in features:
        if f.value == 0:
            continue

        parts = f.feature.split('.')

        tile_features.add('.'.join(parts[1:]))

        if parts[1] in brams:
            bram_features[parts[1]].add('.'.join(parts[2:]))
            brams[parts[1]].append(f)
    """
    FIFO config:

    EN_SYN 27_171
    FIRST_WORD_FALL_THROUGH 27_170
    ZALMOST_EMPTY_OFFSET[12:0] 27_288
    ZALMOST_FULL_OFFSET[12:0] 27_32

    RAMB18 config:

    RAMB18_Y[01].FIFO_MODE 27_169
    RAMB18_Y[01].IN_USE 27_220 27_221

    RAMB18_Y[01].DOA_REG 27_251
    RAMB18_Y[01].DOB_REG 27_248
    RAMB18_Y[01].RDADDR_COLLISION_HWCONFIG_DELAYED_WRITE !27_224
    RAMB18_Y[01].RDADDR_COLLISION_HWCONFIG_PERFORMANCE 27_224
    RAMB18_Y[01].READ_WIDTH_A_1 !27_283 !27_284 !27_285
    RAMB18_Y[01].READ_WIDTH_A_2 !27_283 !27_284 27_285
    RAMB18_Y[01].READ_WIDTH_A_4 !27_283 27_284 !27_285
    RAMB18_Y[01].READ_WIDTH_A_9 !27_283 27_284 27_285
    RAMB18_Y[01].READ_WIDTH_A_18 27_283 !27_284 !27_285
    RAMB18_Y[01].READ_WIDTH_B_1 !27_275 !27_276 !27_277
    RAMB18_Y[01].READ_WIDTH_B_2 !27_275 !27_276 27_277
    RAMB18_Y[01].READ_WIDTH_B_4 !27_275 27_276 !27_277
    RAMB18_Y[01].READ_WIDTH_B_9 !27_275 27_276 27_277
    RAMB18_Y[01].READ_WIDTH_B_18 27_275 !27_276 !27_277
    RAMB18_Y[01].RSTREG_PRIORITY_A_REGCE 27_196
    RAMB18_Y[01].RSTREG_PRIORITY_A_RSTREG !27_196
    RAMB18_Y[01].RSTREG_PRIORITY_B_REGCE 27_195
    RAMB18_Y[01].RSTREG_PRIORITY_B_RSTREG !27_195

    RAMB18_Y[01].ZINV_CLKARDCLK 27_213
    RAMB18_Y[01].ZINV_CLKBWRCLK 27_211
    RAMB18_Y[01].ZINV_ENARDEN 27_208
    RAMB18_Y[01].ZINV_ENBWREN 27_205
    RAMB18_Y[01].ZINV_REGCLKARDRCLK 27_216
    RAMB18_Y[01].ZINV_REGCLKB 27_212
    RAMB18_Y[01].ZINV_RSTRAMARSTRAM 27_204
    RAMB18_Y[01].ZINV_RSTRAMB 27_203
    RAMB18_Y[01].ZINV_RSTREGARSTREG 27_200
    RAMB18_Y[01].ZINV_RSTREGB 27_197
    RAMB18_Y[01].ZINIT_A[17:0] 27_249
    RAMB18_Y[01].ZINIT_B[17:0] 27_255
    RAMB18_Y[01].ZSRVAL_A[17:0]
    RAMB18_Y[01].ZSRVAL_B[17:0]
    RAMB18_Y[01].SDP_READ_WIDTH_36 27_272
    RAMB18_Y[01].SDP_WRITE_WIDTH_36 27_280
    RAMB18_Y[01].WRITE_MODE_A_NO_CHANGE 27_256
    RAMB18_Y[01].WRITE_MODE_A_READ_FIRST 27_264
    RAMB18_Y[01].WRITE_MODE_B_NO_CHANGE 27_252
    RAMB18_Y[01].WRITE_MODE_B_READ_FIRST 27_253
    RAMB18_Y[01].WRITE_WIDTH_A_1 !27_267 !27_268 !27_269
    RAMB18_Y[01].WRITE_WIDTH_A_2 !27_267 !27_268 27_269
    RAMB18_Y[01].WRITE_WIDTH_A_4 !27_267 27_268 !27_269
    RAMB18_Y[01].WRITE_WIDTH_A_9 !27_267 27_268 27_269
    RAMB18_Y[01].WRITE_WIDTH_A_18 27_267 !27_268 !27_269
    RAMB18_Y[01].WRITE_WIDTH_B_1 !27_259 !27_260 !27_261
    RAMB18_Y[01].WRITE_WIDTH_B_2 !27_259 !27_260 27_261
    RAMB18_Y[01].WRITE_WIDTH_B_4 !27_259 27_260 !27_261
    RAMB18_Y[01].WRITE_WIDTH_B_9 !27_259 27_260 27_261
    RAMB18_Y[01].WRITE_WIDTH_B_18 27_259 !27_260 !27_261

    RAMB36 config:

    RAMB36.EN_ECC_READ
    RAMB36.EN_ECC_WRITE
    RAMB36.RAM_EXTENSION_A_LOWER
    RAMB36.RAM_EXTENSION_A_NONE_OR_UPPER
    RAMB36.RAM_EXTENSION_B_LOWER
    RAMB36.RAM_EXTENSION_B_NONE_OR_UPPER
    """

    for f in bram_features.values():
        # TODO: Add support for FIFO mode
        assert 'FIFO_MODE' not in f

    # TODO: Add support for data cascade.
    assert 'RAMB36.RAM_EXTENSION_A_NONE_OR_UPPER' in tile_features
    assert 'RAMB36.RAM_EXTENSION_B_NONE_OR_UPPER' in tile_features

    # TODO: Add support for ECC mode.
    assert 'RAMB36.EN_ECC_READ' not in tile_features
    assert 'RAMB36.EN_ECC_WRITE' not in tile_features

    num_brams = 0
    num_sdp_brams = 0
    num_read_width_18 = 0
    for bram in brams:
        if 'IN_USE' in bram_features[bram]:
            num_brams += 1
        # The following are counters to check whether the bram
        # occupies both RAMB18 and is in SDP mode.
        if 'SDP_READ_WIDTH_36' in bram_features[bram]:
            num_sdp_brams += 1
        if 'READ_WIDTH_A_18' in bram_features[bram]:
            num_read_width_18 += 1

    assert num_brams >= 0 and num_brams <= 2, num_brams

    is_bram_36 = num_sdp_brams == 2 and num_read_width_18 == 2

    sites = []
    for bram in sorted(brams):
        sites.append(process_bram_site(top, brams[bram], bram_features[bram]))

    # RAMB36E1 can be instantiated only if there are two RAMB18E1 and, if they
    # are both in SDP mode, they must corresposnd to the implementation of a
    # RAMB36E1.
    #
    # This is to solve the issue of the READ_WIDTH_A parameter.
    #   - one RAMB36 in SDP mode has the READ_WIDTH_A parameter of both Y0 and Y1 BRAMs set to 18
    #   - two RAMB18 in SDP mode have the READ_WIDTH_A parameter set to 1 for Y0 and to 18 for Y1
    if num_brams == 2 and (num_sdp_brams == 0 or is_bram_36):
        assert len(sites) == 2
        assert sites[0] is not None
        assert sites[1] is not None

        # RAMB36 is actually a merger of both of the RAMB18's, but the only
        # difference is in the routing.
        #
        # When both Y0 and Y1 RAM's are present, always generate the BRAM36
        # site (for routing purposes).  During cleanup, then determine if the
        # two BRAM18's are two independent BRAM's or one BRAM.
        bram36_site = process_bram36_site(top, features, tile_features)

        sites[0].set_post_route_cleanup_function(
            lambda top, site: clean_brams(top, sites, bram36_site, tile_features)
        )
    else:
        for site in sites:
            if site is None:
                continue
            bram_bel = site.maybe_get_bel('RAMB18E1')
            if bram_bel is not None:
                site.set_post_route_cleanup_function(clean_up_to_bram18)

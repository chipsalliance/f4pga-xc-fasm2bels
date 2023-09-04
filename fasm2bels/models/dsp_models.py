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
import math
from .verilog_modeling import Bel, Site, make_inverter_path

# =============================================================================

def cleanup_dsp(top, site):
    """ Performs post-routing cleanup of DSP48E1.
    
    - Check if any of the output pins (including the cascaded outputs) are in use. If not, remove the DSP48E1 site.
    """
    
    dsp48e1= site.maybe_get_bel('DSP48E1')
    if dsp48e1 is not None:
        
        dsp_in_use=False
        
        for output in ("OVERFLOW", "PATTERNBDETECT", "PATTERNDETECT",
                        "UNDERFLOW"):
            if top.wire_assigns.find_sinks_from_source(output) is not None:
                dsp_in_use=True
                break
        
        outputs = [
            ("P", 48),
            ("CARRYOUT", 4),
        ]
        
        for output, width in outputs:
            for idx in range(width):
                if top.wire_assigns.find_sinks_from_source('{}[{}]'.format(output, idx)) is not None:
                    dsp_in_use=True
                    break
            
            if dsp_in_use:
                break
        
        if dsp48e1.parameters['A_INPUT'] == '"CASCADE"':
            dsp_in_use=True
        
        if dsp48e1.parameters['B_INPUT'] == '"CASCADE"':
            dsp_in_use=True
        
        if top.wire_assigns.find_sources_from_sink('CARRYIN') is not None:
            dsp_in_use=True
        
        inputs = [
            ("A", 30),
            ("B", 18),
            ("C", 48),
            ("CARRYINSEL", 3),
            ("OPMODE", 7),
            ("ALUMODE", 4),
            ("INMODE", 5)
        ]
        
        for input, width in inputs:
            for idx in range(width):
                if top.wire_assigns.find_sources_from_sink('{}[{}]'.format(input, idx)) is not None:
                    dsp_in_use=True
                    break
            
            if dsp_in_use:
                break
        
        if dsp48e1.parameters['USE_DPORT'] == '"TRUE"':
            for idx in range(25):
                if top.wire_assigns.find_sources_from_sink('{}[{}]'.format("D", idx)) is not None:
                    dsp_in_use=True
                    break
        
        if not dsp_in_use:
            top.remove_site(site)

def binary_value_from_multi_bit_feature(features, target_feature, width, invert=False):
    value = 0
    for f in features:
        if f.feature.startswith(target_feature):
            for canon_f in fasm.canonical_features(f):
                if canon_f.start is None:
                    value |= 1
                else:
                    value |= (1 << canon_f.start)

    if invert:
        value ^= (2**width) - 1

    value = format(value, f'0{width}b')

    return "{width}'b{value}".format(width=width, value=value[-width:])

def get_dsp_site(db, grid, tile, site):
    """ Return the prjxray.tile.Site object for the given dsp site. """
    gridinfo = grid.gridinfo_at_tilename(tile)
    tile_type = db.get_tile_type(gridinfo.tile_type)

    sites = list(tile_type.get_instance_sites(gridinfo))
    
    if site == 'DSP_0':
        return sites[0]
    elif site == 'DSP_1':
        return sites[2]


def process_dsp48e1_site(top, features, set_features):

    if len(features) == 0:
        return

    aparts = features[0].feature.split('.')
    dsp_site = get_dsp_site(top.db, top.grid, aparts[0], aparts[2])

    site = Site(features, dsp_site)

    assert 'DSP48E1', site.site.type

    bel = Bel('DSP48E1')
    bel.set_bel('DSP48E1')

    def make_target_feature(feature):
        return '{}.{}.{}.{}'.format(aparts[0], aparts[1], aparts[2], feature)

    for input_wire in [
            "CEA1", "CEA2", "CEAD", "CEALUMODE", "CEB1", "CEB2", "CEC",
            "CECARRYIN", "CECTRL", "CED", "CEINMODE", "CEM", "CEP", "RSTA",
            "RSTALLCARRYIN", "RSTALUMODE", "RSTB", "RSTC", "RSTCTRL", "RSTD",
            "RSTINMODE", "RSTM", "RSTP"
    ]:
        site.add_sink(
            bel=bel,
            cell_pin=input_wire,
            sink_site_pin=input_wire,
            bel_name=bel.bel,
            bel_pin=input_wire,
            sink_site_type_pin=input_wire,
        )

    for output_wire in ('OVERFLOW', 'PATTERNBDETECT', 'PATTERNDETECT',
                        'UNDERFLOW'):
        site.add_source(
            bel=bel,
            cell_pin=output_wire,
            source_site_pin=output_wire,
            bel_name=bel.bel,
            bel_pin=output_wire,
            source_site_type_pin=output_wire)

    input_wires = [
        ("A", 30),
        ("B", 18),
        ("C", 48),
        ("CARRYINSEL", 3),
        ("D", 25),
        ("OPMODE", 7),
        ("ALUMODE", 4),
        ("INMODE", 5)
    ]

    for input_wire, width in input_wires:
        for idx in range(width):
            site_wire = '{}{}'.format(input_wire, idx)
            site.add_sink(
                bel=bel,
                cell_pin='{}[{}]'.format(input_wire, idx),
                sink_site_pin=site_wire,
                bel_name=bel.bel,
                bel_pin=site_wire,
                sink_site_type_pin=site_wire)

    output_wires = [
        ("P", 48),
        ("CARRYOUT", 4),
    ]

    for output_wire, width in output_wires:
        for idx in range(width):
            site_wire = '{}{}'.format(output_wire, idx)
            site.add_source(
                bel=bel,
                cell_pin='{}[{}]'.format(output_wire, idx),
                source_site_pin=site_wire,
                bel_name=bel.bel,
                bel_pin=site_wire,
                source_site_type_pin=site_wire)

    for wire in ["CARRYIN", "CLK"]:
        bel.parameters['IS_{}_INVERTED'.format(wire)] = "1'b{}".format(int(
            not 'ZIS_{}_INVERTED'.format(wire) in set_features))

        site_pips = make_inverter_path(
            wire, bel.parameters['IS_{}_INVERTED'.format(wire)])

        site.add_sink(
            bel=bel,
            cell_pin=wire,
            sink_site_pin=wire,
            bel_name=bel.bel,
            bel_pin=wire,
            site_pips=site_pips,
            sink_site_type_pin=wire,
        )

    if 'A_INPUT' in set_features:
        bel.parameters['A_INPUT'] = '"CASCADE"'
    else:
        bel.parameters['A_INPUT'] = '"DIRECT"'

    if 'B_INPUT' in set_features:
        bel.parameters['B_INPUT'] = '"CASCADE"'
    else:
        bel.parameters['B_INPUT'] = '"DIRECT"'

    if 'AREG_0' in set_features:
        bel.parameters['AREG'] = "1'b0"
        bel.parameters['ACASCREG'] = "1'b0"
    elif 'AREG_2' in set_features:
        bel.parameters['AREG'] = "2'b10"
        if 'ZAREG_2_ACASCREG_1' in set_features:
            bel.parameters['ACASCREG'] = "2'b10"
        else:
            bel.parameters['ACASCREG'] = "1'b1"
    else:
        bel.parameters['AREG'] = "1'b1"
        bel.parameters['ACASCREG'] = "1'b1"

    if 'BREG_0' in set_features:
        bel.parameters['BREG'] = "1'b0"
        bel.parameters['BCASCREG'] = "1'b0"
    elif 'BREG_2' in set_features:
        bel.parameters['BREG'] = "2'b10"
        if 'ZBREG_2_BCASCREG_1' in set_features:
            bel.parameters['BCASCREG'] = "2'b10"
        else:
            bel.parameters['BCASCREG'] = "1'b1"
    else:
        bel.parameters['BREG'] = "1'b1"
        bel.parameters['BCASCREG'] = "1'b1"

    if 'ZALUMODEREG' in set_features:
        bel.parameters['ALUMODEREG'] = "1'b0"
    else:
        bel.parameters['ALUMODEREG'] = "1'b1"

    if 'ZCARRYINREG' in set_features:
        bel.parameters['CARRYINREG'] = "1'b0"
    else:
        bel.parameters['CARRYINREG'] = "1'b1"

    if 'ZCARRYINSELREG' in set_features:
        bel.parameters['CARRYINSELREG'] = "1'b0"
    else:
        bel.parameters['CARRYINSELREG'] = "1'b1"

    if 'ZCREG' in set_features:
        bel.parameters['CREG'] = "1'b0"
    else:
        bel.parameters['CREG'] = "1'b1"

    if 'ZOPMODEREG' in set_features:
        bel.parameters['OPMODEREG'] = "1'b0"
    else:
        bel.parameters['OPMODEREG'] = "1'b1"

    #TO DO: USE_MULT, SEL_PATTERN, USE_PATTERNDETECT are not found in the segbits database. They are always set as their default value.
    bel.parameters['USE_MULT'] = '"MULTIPLY"'
    bel.parameters['SEL_PATTERN'] = '"PATTERN"'
    bel.parameters['USE_PATTERN_DETECT'] = '"NO_PATDET"'

    if 'AUTORESET_PATDET_RESET' in set_features:
        bel.parameters['AUTORESET_PATDET'] = '"RESET_MATCH"'
    elif 'AUTORESET_PATDET_RESET_NOT_MATCH' in set_features:
        bel.parameters['AUTORESET_PATDET'] = '"RESET_NOT_MATCH"'
    else:
        bel.parameters['AUTORESET_PATDET'] = '"NO_RESET"'

    if 'SEL_MASK_C' in set_features:
        bel.parameters['SEL_MASK'] = '"C"'
    elif 'SEL_MASK_ROUNDING_MODE1' in set_features:
        bel.parameters['SEL_MASK'] = '"ROUNDING_MODE1"'
    elif 'SEL_MASK_ROUNDING_MODE2' in set_features:
        bel.parameters['SEL_MASK'] = '"ROUNDING_MODE2"'
    else:
        bel.parameters['SEL_MASK'] = '"MASK"'

    if 'ZMREG' in set_features:
        bel.parameters['MREG'] = "1'b0"
    else:
        bel.parameters['MREG'] = "1'b1"

    if 'ZPREG' in set_features:
        bel.parameters['PREG'] = "1'b0"
    else:
        bel.parameters['PREG'] = "1'b1"

    if 'ZADREG' in set_features:
        bel.parameters['ADREG'] = "1'b0"
    else:
        bel.parameters['ADREG'] = "1'b1"

    if 'ZDREG' in set_features:
        bel.parameters['DREG'] = "1'b0"
    else:
        bel.parameters['DREG'] = "1'b1"

    if 'ZINMODEREG' in set_features:
        bel.parameters['INMODEREG'] = "1'b0"
    else:
        bel.parameters['INMODEREG'] = "1'b1"

    if 'USE_DPORT' in set_features:
        bel.parameters['USE_DPORT'] = '"TRUE"'
    else:
        bel.parameters['USE_DPORT'] = '"FALSE"'

    if 'USE_SIMD_FOUR12' in set_features:
        bel.parameters['USE_SIMD'] = '"FOUR12"'
    elif 'USE_SIMD_FOUR12_TWO24' in set_features:
        bel.parameters['USE_SIMD'] = '"TWO24"'
    else:
        bel.parameters['USE_SIMD'] = '"ONE48"'

    bel.parameters['MASK'] = binary_value_from_multi_bit_feature(features, make_target_feature('MASK'), 48)
    bel.parameters['PATTERN'] = binary_value_from_multi_bit_feature(features, make_target_feature('PATTERN'), 48)
    
    bel.parameters['IS_ALUMODE_INVERTED'] = binary_value_from_multi_bit_feature(features, make_target_feature('ZIS_ALUMODE_INVERTED'), 4, invert=True)
    bel.parameters['IS_OPMODE_INVERTED'] = binary_value_from_multi_bit_feature(features, make_target_feature('ZIS_OPMODE_INVERTED'), 7, invert=True)
    bel.parameters['IS_INMODE_INVERTED'] = binary_value_from_multi_bit_feature(features, make_target_feature('ZIS_INMODE_INVERTED'), 5, invert=True)

    bel.add_unconnected_port('ACIN', 30, direction="input")
    for idx in range(30):
        bel.map_bel_pin_to_cell_pin(bel.bel, 'ACIN{}'.format(idx),
                                    'ACIN[{}]'.format(idx))

    bel.add_unconnected_port('ACOUT', 30, direction="output")
    for idx in range(30):
        bel.map_bel_pin_to_cell_pin(bel.bel, 'ACOUT{}'.format(idx),
                                    'ACOUT[{}]'.format(idx))

    bel.add_unconnected_port('BCIN', 18, direction="input")
    for idx in range(18):
        bel.map_bel_pin_to_cell_pin(bel.bel, 'BCIN{}'.format(idx),
                                    'BCIN[{}]'.format(idx))

    bel.add_unconnected_port('BCOUT', 18, direction="output")
    for idx in range(18):
        bel.map_bel_pin_to_cell_pin(bel.bel, 'BCOUT{}'.format(idx),
                                    'BCOUT[{}]'.format(idx))

    bel.add_unconnected_port('CARRYCASCIN', None, direction="input")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'CARRYCASCIN', 'CARRYCASCIN')
    bel.add_unconnected_port('CARRYCASCOUT', None, direction="output")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'CARRYCASCOUT', 'CARRYCASCOUT')

    bel.add_unconnected_port('MULTSIGNIN', None, direction="input")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'MULTSIGNIN', 'MULTSIGNIN')
    bel.add_unconnected_port('MULTSIGNOUT', None, direction="output")
    bel.map_bel_pin_to_cell_pin(bel.bel, 'MULTSIGNOUT', 'MULTSIGNOUT')

    bel.add_unconnected_port('PCIN', 48, direction="input")
    for idx in range(48):
        bel.map_bel_pin_to_cell_pin(bel.bel, 'PCIN{}'.format(idx),
                                    'PCIN[{}]'.format(idx))

    bel.add_unconnected_port('PCOUT', 48, direction="output")
    for idx in range(48):
        bel.map_bel_pin_to_cell_pin(bel.bel, 'PCOUT{}'.format(idx),
                                    'PCOUT[{}]'.format(idx))

    site.add_bel(bel, name='DSP48E1')
    site.set_post_route_cleanup_function(cleanup_dsp(top, site))
    top.add_site(site)

def process_dsp(conn, top, tile, features):
    """
    Processes a DSP_[LR] tile with DSP48E1 sites.
    
    
    DSP48 config:
    
    DSP48.DSP_[01].A_INPUT[0] 27_244
    DSP48.DSP_[01].AREG_0 26_273 26_297 27_271
    DSP48.DSP_[01].AREG_2 27_296
    DSP48.DSP_[01].AUTORESET_PATDET_RESET 26_239
    DSP48.DSP_[01].AUTORESET_PATDET_RESET_NOT_MATCH 26_238
    DSP48.DSP_[01].B_INPUT[0] 26_171
    DSP48.DSP_[01].BREG_0 26_200 26_208 27_198
    DSP48.DSP_[01].BREG_2 27_207
    DSP48.DSP_[01].MASK[47:0]
    DSP48.DSP_[01].PATTERN[47:0]
    DSP48.DSP_[01].SEL_MASK_C 26_243
    DSP48.DSP_[01].SEL_MASK_ROUNDING_MODE1 27_242
    DSP48.DSP_[01].SEL_MASK_ROUNDING_MODE2 27_241 27_242
    DSP48.DSP_[01].USE_DPORT[0] 26_255
    DSP48.DSP_[01].USE_SIMD_FOUR12 26_303 27_212
    DSP48.DSP_[01].USE_SIMD_FOUR12_TWO24 26_244
    DSP48.DSP_[01].ZADREG[0] 27_255
    DSP48.DSP_[01].ZALUMODEREG[0] 26_214
    DSP48.DSP_[01].ZAREG_2_ACASCREG_1 26_299
    DSP48.DSP_[01].ZBREG_2_BCASCREG_1 27_209
    DSP48.DSP_[01].ZCARRYINREG[0] 26_162
    DSP48.DSP_[01].ZCARRYINSELREG[0] 27_170
    DSP48.DSP_[01].ZCREG[0] 26_236
    DSP48.DSP_[01].ZDREG[0] 27_253
    DSP48.DSP_[01].ZINMODEREG[0] 26_247
    DSP48.DSP_[01].ZIS_ALUMODE_INVERTED[3:0]
    DSP48.DSP_[01].ZIS_CARRYIN_INVERTED 27_169
    DSP48.DSP_[01].ZIS_CLK_INVERTED 27_237
    DSP48.DSP_[01].ZIS_INMODE_INVERTED[4:0]
    DSP48.DSP_[01].ZIS_OPMODE_INVERTED[6:0]
    DSP48.DSP_[01].ZMREG[0] 26_198
    DSP48.DSP_[01].ZOPMODEREG[0] 26_185
    DSP48.DSP_[01].ZPREG[0] 27_235
    """

    dsps = {'DSP_0': [], 'DSP_1': []}

    dsp_features = {'DSP_0': set(), 'DSP_1': set()}

    for f in features:
        if f.value == 0:
            continue

        parts = f.feature.split('.')

        if parts[2] in dsps:
            dsp_features[parts[2]].add('.'.join(parts[3:]))
            dsps[parts[2]].append(f)

    for dsp in dsps:
        process_dsp48e1_site(top, dsps[dsp], dsp_features[dsp])

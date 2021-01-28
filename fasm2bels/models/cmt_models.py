from .verilog_modeling import Bel, Site, make_inverter_path

# =============================================================================

# A lookup table for content of the TABLE register to get the BANDWIDTH
# setting. Values taken from XAPP888 reference design.
BANDWIDTH_LOOKUP = {
    "PLLE2_ADV": {

        # LOW
        0b0010111100: "LOW",
        0b0010011100: "LOW",
        0b0010110100: "LOW",
        0b0010010100: "LOW",
        0b0010100100: "LOW",
        0b0010111000: "LOW",
        0b0010000100: "LOW",
        0b0010011000: "LOW",
        0b0010101000: "LOW",
        0b0010110000: "LOW",
        0b0010001000: "LOW",
        0b0011110000: "LOW",
        # 0b0010010000: "LOW",  # Overlaps with one of "OPTIMIZED"

        # OPTIMIZED and HIGH are the same
        0b0011011100: "OPTIMIZED",
        0b0101111100: "OPTIMIZED",
        0b0111111100: "OPTIMIZED",
        0b0111101100: "OPTIMIZED",
        0b1101011100: "OPTIMIZED",
        0b1110101100: "OPTIMIZED",
        0b1110110100: "OPTIMIZED",
        0b1111110100: "OPTIMIZED",
        0b1111011100: "OPTIMIZED",
        0b1111101100: "OPTIMIZED",
        0b1111110100: "OPTIMIZED",
        0b1111001100: "OPTIMIZED",
        0b1110010100: "OPTIMIZED",
        0b1111010100: "OPTIMIZED",
        0b0111011000: "OPTIMIZED",
        0b0101110000: "OPTIMIZED",
        0b1100000100: "OPTIMIZED",
        0b0100001000: "OPTIMIZED",
        0b0010100000: "OPTIMIZED",
        0b0011010000: "OPTIMIZED",
        0b0010100000: "OPTIMIZED",
        0b0100110000: "OPTIMIZED",
        0b0010010000: "OPTIMIZED",
    },
    "MMCME2_ADV": {

        # LOW
        0b0010000100: "LOW",
        0b0010001000: "LOW",
        0b0010001000: "LOW",
        0b0010001100: "LOW",
        0b0010010100: "LOW",
        0b0010011000: "LOW",
        0b0010011100: "LOW",
        0b0010100100: "LOW",
        0b0010101000: "LOW",
        0b0010101100: "LOW",
        0b0010110000: "LOW",
        0b0010110100: "LOW",
        0b0010111000: "LOW",
        #0b0010111100: "LOW",  # Overlaps with one of "OPTIMIZED"

        # OPTIMIZED and HIGH are the same
        0b0010010000: "OPTIMIZED",
        0b0010100000: "OPTIMIZED",
        0b0010111100: "OPTIMIZED",
        0b0011010000: "OPTIMIZED",
        0b0011110000: "OPTIMIZED",
        0b0011110000: "OPTIMIZED",
        0b0100101000: "OPTIMIZED",
        0b0100110000: "OPTIMIZED",
        0b0100111100: "OPTIMIZED",
        0b0101011000: "OPTIMIZED",
        0b0101101100: "OPTIMIZED",
        0b0101110000: "OPTIMIZED",
        0b0110000100: "OPTIMIZED",
        0b0111000100: "OPTIMIZED",
        0b0111011100: "OPTIMIZED",
        0b1100000100: "OPTIMIZED",
        0b1101000100: "OPTIMIZED",
        0b1101011100: "OPTIMIZED",
        0b1110010100: "OPTIMIZED",
        0b1110101100: "OPTIMIZED",
        0b1110110100: "OPTIMIZED",
        0b1111001100: "OPTIMIZED",
        0b1111010100: "OPTIMIZED",
        0b1111100100: "OPTIMIZED",
    }
}


def decode_mmcm_fractional_divider(frac, low_time, high_time, frac_wf_fall,
                                   frac_wf_rise):
    """
    Decodes the value of a MMCM fractional divider given relevant register
    fields.
    """

    # A special case of 1:2.125 division
    if (frac, low_time, high_time, frac_wf_fall, frac_wf_rise) == \
       (1, 0, 0, 1, 1):
        return 2.125

    # Base divider
    divider = high_time + frac_wf_rise * 0.5 + \
              low_time + frac_wf_fall * 0.5 + \
              frac / 8.0

    # Correct
    if frac == 0:
        divider += 2.0
    elif frac == 1:
        divider += 1.5
    else:
        divider += 1.0

    return divider


# =============================================================================


def get_site(db, grid, tile, site):
    """ Return the prjxray.tile.Site object for the given PLL/MMCM site. """
    gridinfo = grid.gridinfo_at_tilename(tile)
    tile_type = db.get_tile_type(gridinfo.tile_type)

    sites = list(tile_type.get_instance_sites(gridinfo))
    assert len(sites) == 1, sites

    return sites[0]


def process_pll_or_mmcm(top, site):
    """
    Processes the PLL or MMCM site
    """

    assert site.site.type in ["PLLE2_ADV", "MMCME2_ADV"], site.site.type
    is_mmcm = site.site.type == "MMCME2_ADV"

    # VCO operating ranges [MHz] (for speed grade -1)
    # Max. CLKIN period [ns]
    if is_mmcm:
        vco_range = (600.0, 1200.0)
        max_clkin_period = 52.631
    else:
        vco_range = (800.0, 1600.0)
        max_clkin_period = 52.631

    # Create the bel and add its ports
    bel_type = site.site.type

    bel = Bel(bel_type)
    bel.set_bel(bel_type)

    for i in range(7):
        site.add_sink(bel, 'DADDR[{}]'.format(i), 'DADDR{}'.format(i), bel.bel,
                      'DADDR{}'.format(i))

    for i in range(16):
        site.add_sink(bel, 'DI[{}]'.format(i), 'DI{}'.format(i), bel.bel,
                      'DI{}'.format(i))

    # Built-in inverters
    bel.parameters['IS_CLKINSEL_INVERTED'] =\
        "1'b1" if site.has_feature('INV_CLKINSEL') else "1'b0"
    bel.parameters['IS_PWRDWN_INVERTED'] =\
        "1'b1" if site.has_feature('ZINV_PWRDWN') else "1'b0"
    bel.parameters['IS_RST_INVERTED'] =\
        "1'b1" if site.has_feature('ZINV_RST') else "1'b0"

    if is_mmcm:
        bel.parameters['IS_PSEN_INVERTED'] =\
            "1'b1" if site.has_feature('ZINV_PSEN') else "1'b0"
        bel.parameters['IS_PSINCDEC_INVERTED'] =\
            "1'b1" if site.has_feature('ZINV_PSINCDEC') else "1'b0"

    for wire in (
            'CLKINSEL',
            'PWRDWN',
            'RST',
    ):
        site_pips = make_inverter_path(
            wire, bel.parameters['IS_{}_INVERTED'.format(wire)] == "1'b1")
        site.add_sink(bel, wire, wire, bel.bel, wire, site_pips)

    if is_mmcm:
        for wire in ('PSEN', 'PSINCDEC'):
            site_pips = make_inverter_path(
                wire, bel.parameters['IS_{}_INVERTED'.format(wire)] == "1'b1")
            site.add_sink(bel, wire, wire, bel.bel, wire, site_pips)

    for wire in (
            'DCLK',
            'DEN',
            'DWE',
            'CLKIN1',
            'CLKIN2',
            'CLKFBIN',
    ):
        site.add_sink(bel, wire, wire, bel.bel, wire)

    for wire in (
            'DRDY',
            'LOCKED',
    ):
        site.add_source(bel, wire, wire, bel.bel, wire)

    for i in range(16):
        site.add_source(bel, 'DO[{}]'.format(i), 'DO{}'.format(i), bel.bel,
                        'DO{}'.format(i))

    if is_mmcm:
        site.add_sink(bel, 'PSCLK', 'PSCLK', bel.bel, 'PSCLK')

        for wire in (
                'PSDONE',
                'CLKINSTOPPED',
                'CLKFBSTOPPED',
        ):
            site.add_source(bel, wire, wire, bel.bel, wire)

    # Process clock outputs
    clkouts = ['FBOUT'] + ['OUT{}'.format(i) for i in range(6 + int(is_mmcm))]

    for clkout in clkouts:

        suffix = "_F" if is_mmcm and clkout in ["FBOUT", "OUT0"] else ""
        prefix = "_FRACTIONAL" if is_mmcm and clkout in ["OUT5", "OUT6"
                                                         ] else ""

        if site.has_feature('CLK{}_CLKOUT1_OUTPUT_ENABLE'.format(clkout)):

            # Get common parameters
            high_time = site.decode_multi_bit_feature(
                'CLK{}_CLKOUT1_HIGH_TIME'.format(clkout))
            low_time = site.decode_multi_bit_feature(
                'CLK{}_CLKOUT1_LOW_TIME'.format(clkout))

            phase = site.decode_multi_bit_feature(
                'CLK{}_CLKOUT1_PHASE_MUX'.format(clkout))
            delay = site.decode_multi_bit_feature(
                'CLK{}_CLKOUT2{}_DELAY_TIME'.format(clkout, prefix))
            edge = site.decode_multi_bit_feature('CLK{}_CLKOUT2{}_EDGE'.format(
                clkout, prefix))
            no_count = site.has_feature('CLK{}_CLKOUT2{}_NO_COUNT'.format(
                clkout, prefix))

            # Add output source
            wire = 'CLK' + clkout
            site.add_source(bel, wire, wire, bel.bel, wire)

            # Add complementary output
            if is_mmcm and clkout in ["FBOUT", "OUT0", "OUT1", "OUT2", "OUT3"]:
                wire = 'CLK' + clkout + 'B'
                site.add_source(bel, wire, wire, bel.bel, wire)

            # Check for fractional divider for MMCM
            is_frac = is_mmcm and clkout in ['FBOUT', 'OUT0'] and \
                site.has_feature('CLK{}_CLKOUT2_FRAC_EN'.format(clkout))

            # Calculate the divider and duty cycle for fractional divider
            if is_frac:

                # Associated register with fractional divider data
                alt_clkout = {
                    "OUT0": "OUT5",
                    "FBOUT": "OUT6",
                }[clkout]

                # Get additional fractional parameters
                frac = site.decode_multi_bit_feature(
                    'CLK{}_CLKOUT2_FRAC'.format(clkout))
                frac_wf_rise = site.decode_multi_bit_feature(
                    'CLK{}_CLKOUT2_FRAC_WF_R'.format(clkout))
                frac_wf_fall = site.decode_multi_bit_feature(
                    'CLK{}_CLKOUT2_FRACTIONAL_FRAC_WF_F'.format(alt_clkout))
                pm_fall = site.decode_multi_bit_feature(
                    'CLK{}_CLKOUT2_FRACTIONAL_PHASE_MUX_F'.format(alt_clkout))

                # Decode the divider
                divider = decode_mmcm_fractional_divider(
                    frac,
                    low_time,
                    high_time,
                    frac_wf_fall,
                    frac_wf_rise,
                )

                if clkout == 'FBOUT':
                    vco_m = divider
                    bel.parameters['CLKFBOUT_MULT_F'] = "{:.3f}".format(
                        divider)
                else:
                    bel.parameters['CLK{}_DIVIDE_F'.format(
                        clkout)] = "{:.3f}".format(divider)
                    # Fractional divider enforces 50% duty cycle
                    bel.parameters['CLK{}_DUTY_CYCLE'.format(clkout)] = "0.500"

            # Calculate the divider and duty cycle for regular (integer)
            # divider
            else:

                # Divider & duty
                if edge:
                    high_time += 0.5
                    low_time = max(0, low_time - 0.5)

                if no_count:
                    divider = 1
                    duty = 0.5
                else:
                    divider = int(high_time + low_time)
                    duty = high_time / (low_time + high_time)

                if clkout == 'FBOUT':
                    vco_m = float(divider)
                    bel.parameters['CLKFBOUT_MULT' + suffix] = str(divider)
                else:
                    bel.parameters['CLK{}_DIVIDE{}'.format(
                        clkout, suffix)] = str(divider)
                    bel.parameters['CLK{}_DUTY_CYCLE'.format(
                        clkout)] = "{0:.4f}".format(duty)

            # Phase shift
            phase = float(delay) + phase / 8.0  # Delay in VCO cycles
            phase = 360.0 * phase / divider  # Phase of CLK in degrees

            bel.parameters['CLK{}_PHASE'.format(clkout)] = \
                "{0:.3f}".format(phase)

        else:

            # Add the clock output as unconnected
            wire = 'CLK' + clkout
            bel.add_unconnected_port(wire, None, direction="output")
            bel.map_bel_pin_to_cell_pin(
                bel_name=bel.bel,
                bel_pin=wire,
                cell_pin=wire,
            )

            # Add complementary clock output as unconnected for MMCM
            if is_mmcm and clkout in ["FBOUT", "OUT0", "OUT1", "OUT2", "OUT3"]:
                wire = 'CLK' + clkout + 'B'
                bel.add_unconnected_port(wire, None, direction="output")
                bel.map_bel_pin_to_cell_pin(
                    bel_name=bel.bel,
                    bel_pin=wire,
                    cell_pin=wire,
                )

            # Set default parameters for feedback clock
            if clkout != 'FBOUT':
                bel.parameters['CLK{}_DIVIDE{}'.format(clkout, suffix)] = "1"
                bel.parameters['CLK{}_DUTY_CYCLE'.format(clkout)] = "0.500"
                bel.parameters['CLK{}_PHASE'.format(clkout)] = "0.000"

    # Input clock divider
    high_time = site.decode_multi_bit_feature('DIVCLK_DIVCLK_HIGH_TIME')
    low_time = site.decode_multi_bit_feature('DIVCLK_DIVCLK_LOW_TIME')

    divider = high_time + low_time

    if site.has_feature('DIVCLK_DIVCLK_NO_COUNT'):
        divider = 1

    vco_d = float(divider)
    bel.parameters['DIVCLK_DIVIDE'] = divider

    # Compute CLKIN1 and CLKIN2 periods so the VCO frequency derived from
    # it falls within its operation range. This is needed to pass Vivado
    # DRC checks. Those calculations are NOT based on any design constraints!
    clkin_period = (vco_m / vco_d) * (2.0 /
                                      (vco_range[0] + vco_range[1])) * 1e3
    clkin_period = min(clkin_period, max_clkin_period)

    bel.parameters['CLKIN1_PERIOD'] = "{:.3f}".format(clkin_period)
    bel.parameters['CLKIN2_PERIOD'] = "{:.3f}".format(clkin_period)

    # Startup wait
    bel.parameters['STARTUP_WAIT'] = '"TRUE"' if site.has_feature(
        'STARTUP_WAIT') else '"FALSE"'

    # Bandwidth
    table = site.decode_multi_bit_feature('TABLE')
    if table in BANDWIDTH_LOOKUP[bel_type]:
        bel.parameters['BANDWIDTH'] =\
            '"{}"'.format(BANDWIDTH_LOOKUP[bel_type][table])

    # MMCM compensation
    if is_mmcm:

        # ZHOLD
        if site.has_feature('COMP.ZHOLD'):
            bel.parameters['COMPENSATION'] = '"ZHOLD"'

        # Not ZHOLD
        elif site.has_feature('COMP.Z_ZHOLD'):

            # FIXME: Cannot determine which one is it. Possibly could analyze
            # routing and distinguish betweein INTERNAL and EXTERNAL.
            bel.parameters['COMPENSATION'] = '"INTERNAL"'

        # Either of the two above features needs to be set
        else:
            assert False, \
                "Either COMP.ZHOLD or COMP.Z_ZHOLD feature must be set!"

    # PLL compensation  TODO: Probably need to rework database tags for those.
    else:
        if site.has_feature('COMPENSATION.INTERNAL'):
            bel.parameters['COMPENSATION'] = '"INTERNAL"'
        elif site.has_feature(
                'COMPENSATION.BUF_IN_OR_EXTERNAL_OR_ZHOLD_CLKIN_BUF'):
            bel.parameters['COMPENSATION'] = '"BUF_IN"'
        elif site.has_feature('COMPENSATION.Z_ZHOLD_OR_CLKIN_BUF'):
            bel.parameters['COMPENSATION'] = '"ZHOLD"'
        else:
            # FIXME: This is probably wrong?
            # No path is COMPENSATION = "EXTERNAL" ???
            bel.parameters['COMPENSATION'] = '"INTERNAL"'

    # MMCM required parameters
    if is_mmcm:

        # Spread-spectrum clock generation.
        # Decoding of these parameters is not possible untill all relevant
        # bits / FASM features are known. For now default values are assigned
        # for Vivado not to complain.
        bel.parameters['SS_EN'] = '"FALSE"'
        bel.parameters['SS_MODE'] = '"CENTER_HIGH"'
        bel.parameters['SS_MOD_PERIOD'] = "10000"

    # Add the bel and site
    site.add_bel(bel)
    top.add_site(site)


# =============================================================================


def process_cmt_upper_t(conn, top, tile_name, features):
    """
    Processes a CMT_TOP_[LR]_UPPER_T tile with PLLE2 site.
    """

    # Filter only PLL related features
    pll_features = [f for f in features if 'PLLE2_ADV.' in f.feature]
    if len(pll_features) == 0:
        return

    # Create the site
    site = Site(pll_features,
                get_site(top.db, top.grid, tile=tile_name, site='PLLE2_ADV'))

    # If the PLL is not used then skip the rest
    if not site.has_feature("IN_USE"):
        return

    # Decode site features
    process_pll_or_mmcm(top, site)


def process_cmt_lower_b(conn, top, tile_name, features):
    """
    Processes a CMT_TOP_[LR]_LOWER_B tile with MMCME2 site.
    """

    # Filter only MMCM related features
    mmcm_features = [f for f in features if 'MMCME2_ADV.' in f.feature]
    if len(mmcm_features) == 0:
        return

    # Create the site
    site = Site(mmcm_features,
                get_site(top.db, top.grid, tile=tile_name, site='MMCME2_ADV'))

    # If the MMCM is not used then skip the rest
    if not site.has_feature("IN_USE"):
        return

    # Decode site features
    process_pll_or_mmcm(top, site)

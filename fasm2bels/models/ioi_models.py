from .verilog_modeling import Site, Bel

# =============================================================================


def get_ioi_site(db, grid, tile, site):
    """
    Returns a prxjray.tile.Site object for given ILOGIC/OLOGIC/IDELAY site.
    """

    gridinfo = grid.gridinfo_at_tilename(tile)
    tile_type = db.get_tile_type(gridinfo.tile_type)

    site_type, site_y = site.split("_")

    sites = tile_type.get_instance_sites(gridinfo)
    sites = [s for s in sites if site_type in s.name]
    sites.sort(key=lambda s: s.y)

    if len(sites) == 1:
        iob_site = sites[0]
    else:
        iob_site = sites[1 - int(site[-1])]

    return iob_site


def cleanup_ilogic(top, site):
    """
    Cleans-up an ILOGIC site after its routing is known.

    - IDDR/ODDR bels have both S and R inputs but physically it is only one.
      When connecting one of them to a const the other one has to be tied to
      the same const too.

    - IDDR as two physical clock inputs CLK and CLKB. Whenever a single clock
      is used the CLKB input has to be connected to the inverted CLK clock.
    """

    # Check if we have an IDDR
    bel = site.maybe_get_bel("IDDR")
    if bel is not None:

        # Check if the SR is const
        source = top.find_source_from_sink(site, 'SR')

        # If so then connect both 'S' and 'R' of the BEL to the same const.
        if source in [0, 1]:
            bel.connections['S'] = source
            bel.connections['R'] = source

        # We are using IDDR_2CLK which has separate inputs for CK and CKB.
        # If both are connected to the same source toggle the IS_CB_INVERTED
        # parameter
        ck_source = top.find_source_from_sink(site, 'CLK')
        ckb_source = top.find_source_from_sink(site, 'CLKB')

        if ck_source is not None and ckb_source is not None and ck_source == ckb_source:
            is_cb_inverted = bool(
                int(bel.parameters.get("IS_CB_INVERTED", "0")))
            bel.parameters["IS_CB_INVERTED"] = str(int(not is_cb_inverted))

    # Check if we have an ODDR for OQ/TQ
    for oddr in ["ODDR_OQ", "ODDR_TQ"]:
        bel = site.maybe_get_bel(oddr)
        if bel is not None:

            # Check if the SR is const
            source = top.find_source_from_sink(site, 'SR')

            # If so then connect both 'S' and 'R' of the BEL to the same const.
            if source in [0, 1]:
                bel.connections['S'] = source
                bel.connections['R'] = source


# =============================================================================


def process_idelay(top, features):
    """
    Decodes the IDELAYE2 primitive
    """

    aparts = features[0].feature.split('.')
    # tile_name = aparts[0]
    ioi_site = get_ioi_site(top.db, top.grid, aparts[0], aparts[1])

    site = Site(features, ioi_site)

    if site.has_feature("IN_USE") and (site.has_feature("IDELAY_VALUE")
                                       or site.has_feature("ZIDELAY_VALUE")):
        bel = Bel('IDELAYE2')

        if site.has_feature("CINVCTRL_SEL"):
            bel.parameters["CINVCTRL_SEL"] = '"TRUE"'

        if site.has_feature("PIPE_SEL"):
            bel.parameters['PIPE_SEL'] = '"TRUE"'

        if site.has_feature("HIGH_PERFORMANCE_MODE"):
            bel.parameters['HIGH_PERFORMANCE_MODE'] = '"TRUE"'

        if site.has_feature("DELAY_SRC_DATAIN"):
            bel.parameters['DELAY_SRC'] = '"DATAIN"'
            site.add_sink(bel, 'DATAIN', 'DATAIN')
        elif site.has_feature("DELAY_SRC_IDATAIN"):
            bel.parameters['DELAY_SRC'] = '"IDATAIN"'
            site.add_sink(bel, 'IDATAIN', 'IDATAIN')

        if site.has_feature("IDELAY_VALUE"):
            idelay_value = site.decode_multi_bit_feature('IDELAY_VALUE')
            bel.parameters['IDELAY_VALUE'] = idelay_value

        if site.has_feature("IS_DATAIN_INVERTED"):
            bel.parameters['IS_DATAIN_INVERTED'] = 1

        if site.has_feature("IS_IDATAIN_INVERTED"):
            bel.parameters['IS_IDATAIN_INVERTED'] = 1

        if site.has_feature("IDELAY_TYPE_VARIABLE"):
            bel.parameters['IDELAY_TYPE'] = '"VARIABLE"'
        elif site.has_feature("IDELAY_TYPE_VAR_LOAD"):
            bel.parameters['IDELAY_TYPE'] = '"VAR_LOAD"'
        else:
            bel.parameters['IDELAY_TYPE'] = '"FIXED"'

        # Adding sinks
        site.add_sink(bel, 'C', 'C')
        site.add_sink(bel, 'CE', 'CE')
        site.add_sink(bel, 'CINVCTRL', 'CINVCTRL')
        site.add_sink(bel, 'INC', 'INC')
        site.add_sink(bel, 'LD', 'LD')
        site.add_sink(bel, 'LDPIPEEN', 'LDPIPEEN')
        site.add_sink(bel, 'REGRST', 'REGRST')

        # Adding sources
        site.add_source(bel, 'DATAOUT', 'DATAOUT')

        site.add_bel(bel)

        # TODO: handle CNTVALUEIN and CNTVALUEOUT

    top.add_site(site)


def process_iserdes(top, site, idelay_site=None):
    """
    Decodes the ISERDES primitive
    """

    # ISERDES
    bel = Bel('ISERDESE2')

    data_rate = None
    if site.has_feature("ISERDES.DATA_RATE.SDR"):
        data_rate = '"SDR"'
    else:
        data_rate = '"DDR"'
    bel.parameters['DATA_RATE'] = data_rate

    # TODO: There shouldn't be mixed width in FASM features.
    #       Probably it is worth revisiting the fuzzer, as it
    #       is not possible to determine the width in case there
    #       is a multiple choice in the fasm features.
    data_width = None
    if site.has_feature("ISERDES.DATA_WIDTH.W3"):
        data_width = 3
    elif site.has_feature("ISERDES.DATA_WIDTH.W4_6"):
        data_width = 6
    elif site.has_feature("ISERDES.DATA_WIDTH.W5_7"):
        data_width = 7
    elif site.has_feature("ISERDES.DATA_WIDTH.W8"):
        data_width = 8
    else:
        data_width = 2

    bel.parameters['DATA_WIDTH'] = data_width

    interface = None
    if site.has_feature("ISERDES.INTERFACE_TYPE.MEMORY_DDR3"):
        interface = '"MEMORY_DDR3"'
    elif site.has_feature(
            "ISERDES.INTERFACE_TYPE.NOT_MEMORY") and site.has_feature(
                "ISERDES.INTERFACE_TYPE.Z_MEMORY"):
        interface = '"NETWORKING"'
    elif site.has_feature("ISERDES.INTERFACE_TYPE.OVERSAMPLE"):
        interface = '"OVERSAMPLE"'
    else:
        assert False

    bel.parameters['INTERFACE_TYPE'] = interface

    site.add_source(bel, 'O', 'O')

    site.add_sink(bel, 'CLK', 'CLK')
    site.add_sink(bel, 'CLKB', 'CLKB')
    site.add_sink(bel, 'CLKDIV', 'CLKDIV')

    site.add_sink(bel, 'RST', 'SR')

    if site.has_feature('ZINV_D'):
        bel.parameters['IS_D_INVERTED'] = 0
    else:
        bel.parameters['IS_D_INVERTED'] = 1

    if site.has_feature('IFF.ZINV_C'):
        bel.parameters['IS_CLK_INVERTED'] = 0
        bel.parameters['IS_CLKB_INVERTED'] = 1
    else:
        bel.parameters['IS_CLK_INVERTED'] = 1
        bel.parameters['IS_CLKB_INVERTED'] = 0

    num_ce = None
    if site.has_feature('ISERDES.NUM_CE.N2'):
        num_ce = 2
    else:
        num_ce = 1

    bel.parameters['NUM_CE'] = num_ce

    if site.has_feature('IDELMUXE3.P0') and site.has_feature('IFFDELMUXE3.P0'):
        bel.parameters['IOBDELAY'] = '"BOTH"'
    elif site.has_feature('IFFDELMUXE3.P0'):
        bel.parameters['IOBDELAY'] = '"IFD"'
    elif site.has_feature('IDELMUXE3.P0'):
        bel.parameters['IOBDELAY'] = '"IBUF"'

    site.add_sink(bel, 'CE1', 'CE1')
    site.add_sink(bel, 'CE2', 'CE2')
    site.add_sink(bel, 'BITSLIP', 'BITSLIP')

    if idelay_site and idelay_site.has_feature("IN_USE") and (
            idelay_site.has_feature("IDELAY_VALUE")
            or idelay_site.has_feature("ZIDELAY_VALUE")):
        site.add_sink(bel, 'DDLY', 'DDLY')
    else:
        site.add_sink(bel, 'D', 'D')

    for i in range(1, 9):
        port_q = 'Q{}'.format(i)
        site.add_source(bel, port_q, port_q)

    site.add_bel(bel)


def process_iddr(top, site, idelay_site=None):
    """
    Decodes the IDDR primitive
    """

    # IDDR. At this point we can't tell if it is IDDR or IDDR_2CLK so the
    # more generic one is instanced.
    bel = Bel('IDDR_2CLK')

    site.add_sink(bel, 'C', 'CLK')
    site.add_sink(bel, 'CB', 'CLKB')
    site.add_sink(bel, 'CE', 'CE1')
    site.add_source(bel, 'Q1', 'Q1')
    site.add_source(bel, 'Q2', 'Q2')

    if idelay_site and idelay_site.has_feature("IN_USE") and (
            idelay_site.has_feature("IDELAY_VALUE")
            or idelay_site.has_feature("ZIDELAY_VALUE")):
        site.add_sink(bel, 'D', 'DDLY')
    else:
        site.add_sink(bel, 'D', 'D')

    # Determine whether we have SET or RESET
    assert site.has_feature('IFF.ZSRVAL_Q1') == site.has_feature(
        'IFF.ZSRVAL_Q2'), (site.tile, site.site)

    if site.has_feature('IFF.ZSRVAL_Q1'):
        site.add_sink(bel, 'R', 'SR')
    else:
        site.add_sink(bel, 'S', 'SR')

    # DDR_CLK_EDGE
    assert site.has_feature('IFF.DDR_CLK_EDGE.SAME_EDGE') != site.has_feature(
        'IFF.DDR_CLK_EDGE.OPPOSITE_EDGE'), (site.tile, site.site)

    if site.has_feature('IFF.DDR_CLK_EDGE.SAME_EDGE'):
        bel.parameters['DDR_CLK_EDGE'] = '"SAME_EDGE"'
    if site.has_feature('IFF.DDR_CLK_EDGE.OPPOSITE_EDGE'):
        bel.parameters['DDR_CLK_EDGE'] = '"OPPOSITE_EDGE"'

    # INIT
    for q in ['Q1', 'Q2']:
        if site.has_feature('IFF.ZINIT_' + q):
            bel.parameters['INIT_' + q] = "1'b0"
        else:
            bel.parameters['INIT_' + q] = "1'b1"

    # SRTYPE
    if site.has_feature('IFF.SRTYPE.SYNC'):
        bel.parameters['SRTYPE'] = '"SYNC"'
    else:
        bel.parameters['SRTYPE'] = '"ASYNC"'

    # IS_C_INVERTED
    if site.has_feature('IFF.ZINV_C'):
        bel.parameters['IS_C_INVERTED'] = "1'b0"
    else:
        bel.parameters['IS_C_INVERTED'] = "1'b1"

    # IS_CB_INVERTED
    # There seem not to be any bits for this one...

    # IS_D_INVERTED
    if site.has_feature('ZINV_D'):
        bel.parameters['IS_D_INVERTED'] = "1'b0"
    else:
        bel.parameters['IS_D_INVERTED'] = "1'b1"

    site.add_bel(bel, name="IDDR")


def process_ilogic_idelay(top, features):
    """
    Processes the ILOGIC and IDELAY sites.
    """

    ilogic_features = features['ILOGIC']
    idelay_features = features['IDELAY']

    ilogic_aparts = ilogic_features[0].feature.split('.')
    idelay_aparts = idelay_features[0].feature.split('.')

    # tile_name = aparts[0]
    ioi_ilogic_site = get_ioi_site(top.db, top.grid, ilogic_aparts[0],
                                   ilogic_aparts[1])
    ioi_idelay_site = get_ioi_site(top.db, top.grid, idelay_aparts[0],
                                   idelay_aparts[1])

    site = Site(ilogic_features, ioi_ilogic_site)

    # Get idelay site corresponding to this tile and check if it is used
    idelay_site = None
    if len(idelay_features):
        idelay_site = Site(idelay_features, ioi_idelay_site)

    # ILOGICE3 in ISERDES mode
    if site.has_feature("ISERDES.IN_USE") and site.has_feature(
            "IDDR_OR_ISERDES.IN_USE"):
        process_iserdes(top, site, idelay_site)

    # ILOGICE3 in IDDR mode
    elif site.has_feature("IDDR_OR_ISERDES.IN_USE"):
        process_iddr(top, site, idelay_site)

    # Passthrough
    else:
        site.sources['O'] = None
        site.sinks['D'] = []
        site.outputs['O'] = 'D'

    site.set_post_route_cleanup_function(cleanup_ilogic)
    top.add_site(site)


# =============================================================================


def process_oddr_oq(top, site):
    """
    Decodes the ODDR primitive driving OQ (data) signal
    """

    # ODDR
    bel = Bel('ODDR', name='ODDR_OQ')

    site.add_sink(bel, 'C', 'CLK')
    site.add_sink(bel, 'CE', 'OCE')
    site.add_sink(bel, 'D1', 'D1')
    site.add_sink(bel, 'D2', 'D2')

    site.add_source(bel, 'Q', 'OQ')

    # Determine whether we have SET or RESET
    if site.has_feature('ZSRVAL_OQ'):
        site.add_sink(bel, 'R', 'SR')
    else:
        site.add_sink(bel, 'S', 'SR')

    # DDR_CLK_EDGE
    if site.has_feature('ODDR.DDR_CLK_EDGE.SAME_EDGE'):
        bel.parameters['DDR_CLK_EDGE'] = '"SAME_EDGE"'
    else:
        bel.parameters['DDR_CLK_EDGE'] = '"OPPOSITE_EDGE"'

    # INIT
    if site.has_feature('ZINIT_OQ'):
        bel.parameters['INIT'] = "1'b0"
    else:
        bel.parameters['INIT'] = "1'b1"

    # SRTYPE
    if site.has_feature('OSERDES.SRTYPE.SYNC'):
        bel.parameters['SRTYPE'] = '"SYNC"'
    else:
        bel.parameters['SRTYPE'] = '"ASYNC"'

    # IS_C_INVERTED
    if site.has_feature('ZINV_CLK'):
        bel.parameters['IS_C_INVERTED'] = "1'b0"
    else:
        bel.parameters['IS_C_INVERTED'] = "1'b1"

    # IS_D1_INVERTED
    if site.has_feature('IS_D1_INVERTED'):
        bel.parameters['IS_D1_INVERTED'] = "1'b1"
    else:
        bel.parameters['IS_D1_INVERTED'] = "1'b0"

    # IS_D2_INVERTED
    if site.has_feature('IS_D2_INVERTED'):
        bel.parameters['IS_D2_INVERTED'] = "1'b1"
    else:
        bel.parameters['IS_D2_INVERTED'] = "1'b0"

    site.add_bel(bel, name="ODDR_OQ")


def process_oddr_tq(top, site):
    """
    Decodes the ODDR primitive driving TQ (tri-state) signal
    """

    # ODDR
    bel = Bel('ODDR', name='ODDR_TQ')

    site.add_sink(bel, 'C', 'CLK')
    site.add_sink(bel, 'CE', 'TCE')
    site.add_sink(bel, 'D1', 'T1')
    site.add_sink(bel, 'D2', 'T2')

    site.add_source(bel, 'Q', 'TQ')

    # Determine whether we have SET or RESET
    if site.has_feature('ZSRVAL_TQ'):
        site.add_sink(bel, 'R', 'SR')
    else:
        site.add_sink(bel, 'S', 'SR')

    # DDR_CLK_EDGE
    if site.has_feature('ODDR.DDR_CLK_EDGE.SAME_EDGE'):
        bel.parameters['DDR_CLK_EDGE'] = '"SAME_EDGE"'
    else:
        bel.parameters['DDR_CLK_EDGE'] = '"OPPOSITE_EDGE"'

    # INIT
    if site.has_feature('ZINIT_TQ'):
        bel.parameters['INIT'] = "1'b0"
    else:
        bel.parameters['INIT'] = "1'b1"

    # SRTYPE
    if site.has_feature('OSERDES.TSRTYPE.SYNC'):
        bel.parameters['SRTYPE'] = '"SYNC"'
    else:
        bel.parameters['SRTYPE'] = '"ASYNC"'

    # IS_C_INVERTED
    if site.has_feature('ZINV_CLK'):
        bel.parameters['IS_C_INVERTED'] = "1'b0"
    else:
        bel.parameters['IS_C_INVERTED'] = "1'b1"

    # IS_D1_INVERTED
    if site.has_feature('ZINV_T1'):
        bel.parameters['IS_D1_INVERTED'] = "1'b0"
    else:
        bel.parameters['IS_D1_INVERTED'] = "1'b1"

    # IS_D2_INVERTED
    if site.has_feature('ZINV_T2'):
        bel.parameters['IS_D2_INVERTED'] = "1'b0"
    else:
        bel.parameters['IS_D2_INVERTED'] = "1'b1"

    site.add_bel(bel, name="ODDR_TQ")


def process_oserdes(top, site):
    """
    Decodes the OSERDESE2 primitive
    """

    # OSERDES
    bel = Bel('OSERDESE2')

    data_rate_oq = None
    if site.has_feature("OSERDES.DATA_RATE_OQ.DDR"):
        data_rate_oq = '"DDR"'
    elif site.has_feature("OSERDES.DATA_RATE_OQ.SDR"):
        data_rate_oq = '"SDR"'
    else:
        assert False
    bel.parameters['DATA_RATE_OQ'] = data_rate_oq

    data_rate_tq = None
    if site.has_feature("OSERDES.DATA_RATE_TQ.DDR"):
        data_rate_tq = '"DDR"'
    elif site.has_feature("OSERDES.DATA_RATE_TQ.SDR"):
        data_rate_tq = '"SDR"'
    elif site.has_feature("OSERDES.DATA_RATE_TQ.BUF"):
        data_rate_tq = '"BUF"'
    else:
        assert False
    bel.parameters['DATA_RATE_TQ'] = data_rate_tq

    data_width = None
    if site.has_feature("OSERDES.DATA_WIDTH.W2"):
        data_width = 2
    elif site.has_feature("OSERDES.DATA_WIDTH.W3"):
        data_width = 3
    elif site.has_feature("OSERDES.DATA_WIDTH.W4"):
        data_width = 4
    elif site.has_feature("OSERDES.DATA_WIDTH.W5"):
        data_width = 5
    elif site.has_feature("OSERDES.DATA_WIDTH.W6"):
        data_width = 6
    elif site.has_feature("OSERDES.DATA_WIDTH.W7"):
        data_width = 7
    elif site.has_feature("OSERDES.DATA_WIDTH.W8"):
        data_width = 8
    else:
        assert False

    bel.parameters['DATA_WIDTH'] = data_width

    bel.parameters['TRISTATE_WIDTH'] = "4" if site.has_feature(
        "OSERDES.TRISTATE_WIDTH.W4") else "1"
    bel.parameters['SERDES_MODE'] = '"SLAVE"' if site.has_feature(
        "OSERES.SERDES_MODE.SLAVE") else '"MASTER"'

    site.add_source(bel, 'OQ', 'OQ')
    site.add_source(bel, 'TQ', 'TQ')

    site.add_sink(bel, 'CLK', 'CLK')
    site.add_sink(bel, 'CLKDIV', 'CLKDIV')

    for i in range(1, 9):
        site.add_sink(bel, 'D{}'.format(i), 'D{}'.format(i))

        inverted = ("IS_D{}_INVERTED".format(i))
        if site.has_feature(inverted):
            bel.parameters[inverted] = 1

    for i in range(1, 5):
        site.add_sink(bel, 'T{}'.format(i), 'T{}'.format(i))

        if not site.has_feature("ZINV_T{}".format(i)):
            bel.parameters["IS_T{}_INVERTED".format(i)] = 1

    site.add_sink(bel, 'OCE', 'OCE')
    site.add_sink(bel, 'TCE', 'TCE')

    site.add_sink(bel, 'RST', 'SR')

    site.add_bel(bel)


def process_ologic(top, features):
    """
    Processes the OLOGICE2 site
    """

    aparts = features[0].feature.split('.')
    # tile_name = aparts[0]
    ioi_site = get_ioi_site(top.db, top.grid, aparts[0], aparts[1])

    site = Site(features, ioi_site)

    # OLOGICE2 in OSERDES mode
    if site.has_feature("OSERDES.IN_USE"):
        process_oserdes(top, site)

    # OLOGICE2 with ODDRs or passtrhough
    else:

        # ODDR for OQ used
        if not site.has_feature("OMUX.D1"):
            process_oddr_oq(top, site)

        # Passthrough
        else:
            site.sources['OQ'] = None
            site.sinks['D1'] = []
            site.outputs['OQ'] = 'D1'

        # ODDR for TQ used
        if not site.has_feature("OSERDES.DATA_RATE_TQ.BUF"):
            process_oddr_tq(top, site)

        # Passthrough
        else:
            site.sources['TQ'] = None
            site.sinks['T1'] = []
            site.outputs['TQ'] = 'T1'

    top.add_site(site)


# =============================================================================


def process_ioi(conn, top, tile, features):

    ilogic_idelay = {
        "0": {
            'ILOGIC': [],
            'IDELAY': []
        },
        "1": {
            'ILOGIC': [],
            'IDELAY': []
        },
    }
    idelay = {
        "0": [],
        "1": [],
    }
    ologic = {
        "0": [],
        "1": [],
    }

    for f in features:
        site = f.feature.split('.')[1]

        if site.startswith('IDELAY_Y'):
            ilogic_idelay[site[-1]]['IDELAY'].append(f)
            idelay[site[-1]].append(f)
        if site.startswith('ILOGIC_Y'):
            ilogic_idelay[site[-1]]['ILOGIC'].append(f)
        if site.startswith('OLOGIC_Y'):
            ologic[site[-1]].append(f)

    for features in idelay.values():
        if len(features):
            process_idelay(top, features)

    for features in ilogic_idelay.values():
        if len(features['ILOGIC']):
            process_ilogic_idelay(top, features)

    for features in ologic.values():
        if len(features):
            process_ologic(top, features)

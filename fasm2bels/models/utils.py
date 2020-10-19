def make_bus(wires):
    """ Combine bus wires into a consecutive bus.

    Args:
        wires ([str]): Takes list of wire names.

    Returns list of (wire/bus name, max bus wire count).

    If the wire is NOT a bus, then max bus wire count will be None.
    If the wire was part of a bus, then max bus wire count will be the maximum
    observed bus index.  It is assumed that all buses will be sized as
    [max:0].

    >>> list(make_bus(['A', 'B']))
    [('A', None), ('B', None)]
    >>> list(make_bus(['A[0]', 'A[1]', 'B']))
    [('A', 1), ('B', None)]
    >>> list(make_bus(['A[0]', 'A[1]', 'B[0]']))
    [('A', 1), ('B', 0)]

    """
    output = {}
    buses = {}

    for w in wires:
        widx = w.rfind('[')
        if widx != -1 and w[-1] == ']':

            bus = w[0:widx]
            idx = int(w[widx + 1:-1])

            if bus not in buses:
                buses[bus] = []

            buses[bus].append(idx)
        else:
            output[w] = None

    for bus, values in buses.items():
        output[bus] = max(values)

    for name in sorted(output):
        yield name, output[name]


def escape_verilog_name(name):
    """ Transform net names into escaped id and bus selection (if any)

    Args:
        name (str): Net name

    Returns:
        Escape verilog name

    >>> escape_verilog_name(
    ...     '$abc$6513$auto$alumacc.cc:474:replace_alu$1259.B_buf[4]')
    '\\\\$abc$6513$auto$alumacc.cc:474:replace_alu$1259.B_buf [4]'
    >>> escape_verilog_name(
    ...     '$abc$6513$auto$alumacc.cc:474:replace_alu$1259.B_buf[4:0]')
    '\\\\$abc$6513$auto$alumacc.cc:474:replace_alu$1259.B_buf[4:0] '
    >>> escape_verilog_name(
    ...     '$abc$6513$auto$alumacc.cc:474:replace_alu$1259.B_buf[4:0][0]')
    '\\\\$abc$6513$auto$alumacc.cc:474:replace_alu$1259.B_buf[4:0] [0]'
    >>> escape_verilog_name(
    ...     'test')
    '\\\\test '
    """

    idx = name.rfind('[')
    bus_idx = None
    if idx != -1 and name[-1] == ']':
        try:
            bus_idx = int(name[idx + 1:-1])
        except ValueError:
            pass

    if bus_idx is None:
        # Escape whole name
        return '\\' + name + ' '

    return '\\' + name[:idx] + ' ' + name[idx:]


def unescape_verilog_name(name):
    """ Unescapes verilog names.

    >>> s0 = '$abc$6513$auto$alumacc.cc:474:replace_alu$1259.B_buf[4]'
    >>> s1 = escape_verilog_name(s0)
    >>> s1
    '\\\\$abc$6513$auto$alumacc.cc:474:replace_alu$1259.B_buf [4]'
    >>> s2 = unescape_verilog_name(s1)
    >>> assert s0 == s2
    >>> s2
    '$abc$6513$auto$alumacc.cc:474:replace_alu$1259.B_buf[4]'

    >>> s0 = 'test'

    >>> s1 = escape_verilog_name(
    ...     'test')
    >>> s1
    '\\\\test '
    >>> s2 = unescape_verilog_name(s1)
    >>> assert s0 == s2
    >>> s2
    'test'

    """
    # TODO: This is pretty terrible. Maybe defer usage of verilog_modeling.escape_verilog_name?
    if not name.startswith('\\'):
        return name
    else:
        return name[1:].replace(' ', '')


def flatten_wires(wire, wire_assigns, wire_name_net_map):
    """ Given a wire, return the source net name (or constant string).

    Arguments
    ---------
    wire : str
        Wire to translate to source
    wire_assigns : WireAssignsBimap object
        Map of wires to their parents.  Equivilant to assign statements in
        verilog.  Example:

        assign A = B;

        would be represented as:

        {
            'A': 'B'
        }
    wire_name_net_map : dict of str to str
        Some wires have net names that originate from the post-synth eblif.
        This maps programatic net names (e.g. CLBLL_L_X12Y110_SLICE_X16Y110_BO5)
        to these post-synth eblif names.

    """

    wire = wire_assigns.get_source_for_sink(wire)

    if wire in wire_name_net_map:
        return wire_name_net_map[wire]
    else:
        if wire in [0, 1]:
            return "1'b{}".format(wire)
        else:
            return wire

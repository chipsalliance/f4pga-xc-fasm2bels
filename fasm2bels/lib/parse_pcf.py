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

from collections import namedtuple
import re

PcfIoConstraint = namedtuple('PcfIoConstraint', 'net pad line_str line_num')


def parse_simple_pcf(f):
    """ Parse a simple PCF file object and yield PcfIoConstraint objects. """
    for line_number, line in enumerate(f):
        line_number += 1

        # Remove comments.
        args = re.sub(r"#.*", "", line.strip()).split()

        if not args or args[0] != 'set_io':
            continue

        # Ignore arguments to set_io.
        args = [arg for arg in args if arg[0] != '-']

        assert len(args) == 3, args

        yield PcfIoConstraint(
            net=args[1],
            pad=args[2],
            line_str=line.strip(),
            line_num=line_number,
        )

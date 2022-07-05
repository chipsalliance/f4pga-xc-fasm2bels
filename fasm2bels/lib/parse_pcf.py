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

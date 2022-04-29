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

import progressbar as bar
import sys


def disable_widgets_if_not_interactive(kwargs):
    if not (sys.stdout.isatty() and sys.stderr.isatty()):
        # Disable all widgets if non-interactive
        print('No progressbar disabled because non-interactive terminal.')
        kwargs['widgets'] = []


def progressbar(*args, **kwargs):
    disable_widgets_if_not_interactive(kwargs)
    b = bar.progressbar(*args, **kwargs)

    return b


class ProgressBar(bar.ProgressBar):
    def __init__(self, *args, **kwargs):
        disable_widgets_if_not_interactive(kwargs)
        super().__init__(*args, **kwargs)

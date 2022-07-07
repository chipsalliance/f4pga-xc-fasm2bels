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

#!/bin/bash
# Copyright (C) 2020-2021  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

yapf -i $(find fasm2bels -name "*py") setup.py
test $(git status --porcelain | wc -l) -eq 0 || { git diff; false;  }

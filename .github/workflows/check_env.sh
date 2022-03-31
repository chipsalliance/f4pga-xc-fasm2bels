#!/bin/bash
# Copyright (C) 2020-2021  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

YOSYS_DIR=$(which yosys)

if [ "$(pwd)/env/conda/envs/symbiflow_xc_fasm2bels/bin/yosys" != $YOSYS_DIR ]
then
    echo "ERROR: make env failed"
    return 1
fi

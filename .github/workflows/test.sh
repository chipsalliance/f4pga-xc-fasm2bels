#!/bin/bash
# Copyright (C) 2020-2021  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

export CAPNP_PATH="$(pwd)/third_party/capnproto-java/compiler/src/main/schema/"
export INTERCHANGE_SCHEMA_PATH="$(pwd)/third_party/fpga-interchange-schema/interchange"

make test-py

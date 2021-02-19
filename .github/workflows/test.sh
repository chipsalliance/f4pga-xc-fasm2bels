#!/bin/bash

export CAPNP_PATH="$GITHUB_WORKSPACE/capnproto-java/compiler/src/main/schema/"
export INTERCHANGE_SCHEMA_PATH="$GITHUB_WORKSPACE/fpga-interchange-schema/interchange"

make test-py

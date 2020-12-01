#!/bin/bash

export CAPNP_PATH="$GITHUB_WORKSPACE/capnproto-java/compiler/src/main/schema/"
export INTERCHANGE_SCHEMA_PATH="$GITHUB_WORKSPACE/RapidWright/interchange"

make test-py

# Copyright (C) 2021  The Symbiflow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

SHELL=bash

PYTHON:=python3

FASM2BELS_PYTHON_SRCS=$(shell find fasm2bels -name "*py")

TOP_DIR := $(realpath $(dir $(lastword $(MAKEFILE_LIST))))
REQUIREMENTS_FILE := requirements.txt
ENVIRONMENT_FILE := environment.yml

include third_party/make-env/conda.mk

IN_ENV = if [ -e env/bin/activate ]; then . env/bin/activate; fi;
env::
	git submodule update --init --recursive
	virtualenv --python=$(PYTHON) env
	$(IN_ENV) pip install --no-cache-dir --upgrade -r requirements.txt

format: ${PYTHON_SRCS}
	$(IN_ENV) yapf -i ${FASM2BELS_PYTHON_SRCS} setup.py

build:
	cd third_party/prjxray; make build -j`nproc`

test-py:
	$(IN_ENV) cd tests; PYTHONPATH=../ python -m unittest
	$(IN_ENV) python -m doctest ./fasm2bels/lib/parse_xdc.py

clean::
	rm -rf env

.PHONY: clean env build test-py

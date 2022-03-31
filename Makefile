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

$(TOP_DIR)/third_party/make-env/conda.mk: $(TOP_DIR)/.gitmodules
	cd $(TOP_DIR); git submodule update --init
	touch $(TOP_DIR)/third_party/make-env/conda.mk

-include $(TOP_DIR)/third_party/make-env/conda.mk

format: ${PYTHON_SRCS}
	$(IN_CONDA_ENV) yapf -i ${FASM2BELS_PYTHON_SRCS} setup.py

build:
	cd third_party/prjxray; make build -j`nproc`

test-py:
	$(IN_CONDA_ENV) cd tests; PYTHONPATH=../ python -m unittest
	$(IN_CONDA_ENV) python -m doctest ./fasm2bels/lib/parse_xdc.py

.PHONY: clean env build test-py

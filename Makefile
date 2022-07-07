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
	cd third_party/prjxray; make ALLOW_ROOT=1 build -j$(nproc)

test-py:
	$(IN_CONDA_ENV) cd tests; PYTHONPATH=../ python -m unittest
	$(IN_CONDA_ENV) python -m doctest ./fasm2bels/lib/parse_xdc.py

.PHONY: clean env build test-py

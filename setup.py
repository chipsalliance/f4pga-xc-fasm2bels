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

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fasm2bels",
    version="0.0.1",
    author="F4PGA Authors",
    author_email="f4pga-wg@lists.chipsalliance.org",
    description="fasm2bels libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chipsalliance/f4pga-xc-fasm2bels",
    python_requires=">=3.7",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "simplejson",
        "pycapnp",
        "intervaltree",
        "parameterized",
        "progressbar2",
        "lxml",
        "prjxray",
        "fasm",
        "rr-graph",
        "python-fpga-interchange",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)

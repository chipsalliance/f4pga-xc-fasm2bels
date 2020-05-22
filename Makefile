SHELL=bash

build:
	git submodule update --init --recursive
	cd third_party/prjxray; make build -j`nproc`

test-py:
	cd tests; python -m unittest

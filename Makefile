SHELL=bash

PYTHON_SRCS=$(shell find . -name "*py" -not -path "./third_party/*")

format: ${PYTHON_SRCS}
	yapf -i $?

build:
	git submodule update --init --recursive
	cd third_party/prjxray; make build -j`nproc`

test-py:
	cd tests; python -m unittest

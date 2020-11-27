SHELL=bash

FASM2BELS_PYTHON_SRCS=$(shell find fasm2bels -name "*py")

IN_ENV = if [ -e env/bin/activate ]; then . env/bin/activate; fi;
env:
	git submodule update --init --recursive
	virtualenv --python=python3 env
	$(IN_ENV) pip install --upgrade -r requirements.txt

format: ${PYTHON_SRCS}
	$(IN_ENV) yapf -i ${FASM2BELS_PYTHON_SRCS} setup.py

build:
	cd third_party/prjxray; make build -j`nproc`

test-py:
	$(IN_ENV) cd tests; PYTHONPATH=../ python -m unittest
	$(IN_ENV) python -m doctest ./fasm2bels/lib/parse_xdc.py

clean:
	rm -rf env

.PHONY: clean env build test-py

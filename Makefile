SHELL=bash

ALL_EXCLUDE = third_party .git env build
FORMAT_EXCLUDE = $(foreach x,$(ALL_EXCLUDE),-and -not -path './$(x)/*')

PYTHON_SRCS=$(shell find . -name "*py" $(FORMAT_EXCLUDE))

IN_ENV = if [ -e env/bin/activate ]; then . env/bin/activate; fi;
env:
	virtualenv --python=python3 env
	$(IN_ENV) pip install --upgrade -r requirements.txt

.PHONY: env


format: ${PYTHON_SRCS}
	$(IN_ENV) yapf -i $?

build:
	git submodule update --init --recursive
	cd third_party/prjxray; make build -j`nproc`

test-py:
	$(IN_ENV) cd tests; python -m unittest

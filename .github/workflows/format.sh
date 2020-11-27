#!/bin/bash

yapf -i $(find fasm2bels -name "*py") setup.py
test $(git status --porcelain | wc -l) -eq 0 || { git diff; false;  }

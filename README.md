FASM 2 BELs
-----------

fasm2bels is a tool designed to take a FASM file into Vivado.

It does this by generating a file describing the BEL connections (techmapped
Verilog) and TCL commands for Vivado which lock the BEL placements.

This makes it possible to perform simulation and analysis of a FASM file inside
Vivado.

In the absence of bugs, it is expected that after consuming the BEL
connections and TCL constraints Vivado will produce a bitstream identical to
the bitstream the FASM file would generate.

Installing
----------

Before cloning this repo, the RapidWright and capnproto-java repos must be installed first.

Follow the instructions to install RapidWright [here](https://github.com/Xilinx/RapidWright) and clone capnproto-java [here](https://github.com/capnproto/capnproto-java).

After RapidWright and capnproto-java are installed, clone this repo and run the following commands:
  - `make env` - python >=3.7 is required - you may have to upgrade and then change Makefile to use the new version (same for Invoking below)
    - To get python3.7 on Ubuntu 16.04 (or above) do the following:
      - sudo apt update
      - sudo apt install software-properties-common
      - sudo add-apt-repository ppa:deadsnakes/ppa
      - sudo apt update
      - sudo apt install python3.7
    - Then, modify the Makefile to use python3.7 instead of python3.
 - `make build`
 - `make test-py` - Before running, go into `.github/workflows/test.sh` and change the directory path from $GITHUB_WORKSPACE to your directory path for CAPN_PATH and INTERCHANGE_SCHEMA_PATH (fpga-interchange-schema is inside `RapidWright/interchange`). Source the `test.sh` from the main fasm2bels directory (`source .github/workflows/test.sh`) and `make test-py` will run automatically. It takes a few minutes to run all the tests (22).

 An `OK` should appear at the bottom of the terminal run if successful.

Invoking
--------

`python3.7 -mfasm2bels <options> <verilog> <tcl>`

Required arguments are:
 - `--connection_database` - Path to connection database for part
 - `--db_root` - Path to prjxray database for part
 - `--part` - FPGA part
 - `--fasm_file` - Path to FASM file to process
 - verilog - Path to verilog file to write
 - tcl - Path to TCL file to write

Once the verilog and TCL is generated, it should be importable to Vivado with
a script roughly like:

```
create_project -force -part {part} design design

read_verilog {bit_v}
synth_design -top {top}
source {bit_tcl}
set_property IS_ENABLED 0 [get_drc_checks {{LUTLP-1}}]
place_design
route_design
```

Timing constraints should be provided as needed, along with other property
modifications as needed for the design.  These properties are not embedded in
the bitstream, so must be supplied external.

Examples:
 - `set_property CFGBVS VCCO [current_design]`
 - `set_property CONFIG_VOLTAGE 3.3 [current_design]`

BELs / Sites supported
----------------------

- SLICEL (all)
- SLICEM (all)
- RAMB18/RAMB36 (BRAM only, no FIFO support)
- IOB (limited IOSTANDARDs)
- IOI
    - IDELAY
    - IDDR/ISERDES
    - ODDR/OSERDES
- CLK\_HROW\_\*
- CLK\_BUFG\_\*
- PLLs
- PSS

Future work
-----------
 - MMCMs
 - BUFR/BUFMR and other clock buffers
 - DSP

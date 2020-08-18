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
After cloning this repo:
  - `make env` - required python >=3.7 - may have to upgrade and then change Makefile to use new version (same for Invoking below)
    - To get python3.7 on Ubuntu 16.04 I had to do:
      - sudo apt update
      - sudo apt install software-properties-common
      - sudo add-apt-repository ppa:deadsnakes/ppa
      - sudo apt update
      - sudo apt install python3.7
    - Then, had to modify the Makefile to use python3.7 instead of python3
 - `make build`
 - `make test-py` - will run a few tests (6), takes a few minutes

Invoking
--------

`python3 -mfasm2bels <options> <verilog> <tcl>`

Required arguments are:
 - `--connection_database` - Path to connection database for part
 - `--db_root` - Path to prjxray database for part
 - `--part` - FPGA part
 - `--fasm_file` - Path to FASM file to process
 - verilog - Path to verilog file to write
 - tcl - Path to TCL file to write

The first time you run it you will not have a connection database for the part.  Provide a name for this parameter such as `./basys3.db` and the program will generate the database the first time you run.  On subsequent runs you can then specify that filename and avoid re-building the database each time.

Here is an example run:
```
python3.7 -mfasm2bels --connection_database mydb \
                      --db_root ~/prjxray/database/artix7 \
                      --part xc7a35tcpg236-1 \
                      --fasm_file cnt.fasm \
                      cnt.v cnt.tcl
```

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

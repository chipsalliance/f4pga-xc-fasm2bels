set_part xc7a35tcpg236-1
read_verilog equivalence_checking_data/FILENAME/FILENAME.v
synth_design -top FILENAME -max_dsp 0
place_ports
write_edif -force {FILENAME.edf}
write_checkpoint -force -file temp.dcp
report_io -force -file report_io.txt
read_edif FILENAME.edf
set_property design_mode GateLvl [current_fileset]
link_design -part xc7a35tcpg236-1
opt_design
place_design
route_design
write_checkpoint -force -file temp.dcp
write_verilog -force -file result_impl.v

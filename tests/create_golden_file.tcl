set module [lindex $argv 0] 
set temp_dir [lindex $argv 1]
set_part [lindex $argv 2]

# Reads the source design.
read_verilog equivalence_checking_data/$module/$module.v

# Synthesis & Implementation
synth_design -top $module -max_dsp 0
place_ports
write_edif -force $temp_dir/$module.edf
read_edif $temp_dir/$module.edf
set_property design_mode GateLvl [current_fileset]
link_design -part [lindex $argv 2]
opt_design
place_design
route_design

# Write out Implementation netlist to design folder.
write_verilog -force -file $temp_dir/top_bit.golden.v

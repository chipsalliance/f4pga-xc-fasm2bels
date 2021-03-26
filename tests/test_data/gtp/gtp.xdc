# clk
set_property LOC W5 [get_ports {clk}] 

# GTP Channel
set_property LOC D2 [get_ports {tx_p}]
set_property LOC D1 [get_ports {tx_n}]
set_property LOC B4 [get_ports {rx_p}]
set_property LOC A4 [get_ports {rx_n}]

# GTP Common / IBUFDS
set_property LOC A8  [get_ports clk_n_0]
set_property LOC B8  [get_ports clk_p_0]
set_property LOC A10 [get_ports clk_n_1]
set_property LOC B10 [get_ports clk_p_1]
set_property LOC V17 [get_ports test_in]
set_property LOC U16 [get_ports test_out]

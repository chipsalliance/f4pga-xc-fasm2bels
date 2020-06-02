set cell [get_cells *CLBLL_R_X19Y8_SLICE_X28Y8_D5_FDCE]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property BEL "[get_property SITE_TYPE [get_sites SLICE_X28Y8]].D5FF" $cell
set_property LOC [get_sites SLICE_X28Y8] $cell
set cell [get_cells *CLK_BUFG_BOT_R_X60Y48_BUFGCTRL_X0Y0_BUFGCTRL]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites BUFGCTRL_X0Y0] $cell
set cell [get_cells *CLK_HROW_BOT_R_X60Y26_BUFHCE_X0Y9_BUFHCE]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites BUFHCE_X0Y9] $cell
set cell [get_cells *LIOB33_X0Y1_IOB_X0Y1_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y1] $cell
set cell [get_cells *LIOB33_X0Y1_IOB_X0Y2_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y2] $cell
set cell [get_cells *LIOB33_X0Y3_IOB_X0Y3_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y3] $cell
set cell [get_cells *LIOB33_X0Y3_IOB_X0Y4_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y4] $cell
set cell [get_cells *LIOB33_X0Y9_IOB_X0Y10_IBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y10] $cell
set cell [get_cells *LIOB33_X0Y11_IOB_X0Y11_IBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y11] $cell
set cell [get_cells *LIOB33_X0Y11_IOB_X0Y12_IBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y12] $cell
set cell [get_cells *LIOB33_X0Y17_IOB_X0Y18_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y18] $cell
set cell [get_cells *LIOB33_X0Y19_IOB_X0Y19_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y19] $cell
set cell [get_cells *LIOB33_X0Y19_IOB_X0Y20_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y20] $cell
set cell [get_cells *LIOB33_X0Y43_IOB_X0Y43_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y43] $cell
set cell [get_cells *LIOB33_X0Y111_IOB_X0Y111_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y111] $cell
set cell [get_cells *LIOB33_SING_X0Y0_IOB_X0Y0_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X0Y0] $cell
set cell [get_cells *RIOB33_X43Y25_IOB_X1Y26_IBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X1Y26] $cell
set cell [get_cells *RIOB33_X43Y31_IOB_X1Y32_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X1Y32] $cell
set cell [get_cells *RIOB33_X43Y37_IOB_X1Y37_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X1Y37] $cell
set cell [get_cells *RIOB33_X43Y37_IOB_X1Y38_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X1Y38] $cell
set cell [get_cells *RIOB33_X43Y61_IOB_X1Y61_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X1Y61] $cell
set cell [get_cells *RIOB33_X43Y75_IOB_X1Y75_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X1Y75] $cell
set cell [get_cells *RIOB33_X43Y75_IOB_X1Y76_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X1Y76] $cell
set cell [get_cells *RIOB33_X43Y87_IOB_X1Y87_OBUF]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property LOC [get_sites IOB_X1Y87] $cell
set cell [get_cells *CLBLL_R_X19Y8_SLICE_X28Y8_ALUT]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property BEL "[get_property SITE_TYPE [get_sites SLICE_X28Y8]].A6LUT" $cell
set_property LOC [get_sites SLICE_X28Y8] $cell
set cell [get_cells *CLBLL_R_X19Y8_SLICE_X28Y8_BLUT]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property BEL "[get_property SITE_TYPE [get_sites SLICE_X28Y8]].B6LUT" $cell
set_property LOC [get_sites SLICE_X28Y8] $cell
set cell [get_cells *CLBLL_R_X19Y8_SLICE_X28Y8_CLUT]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property BEL "[get_property SITE_TYPE [get_sites SLICE_X28Y8]].C6LUT" $cell
set_property LOC [get_sites SLICE_X28Y8] $cell
set cell [get_cells *CLBLL_R_X19Y8_SLICE_X28Y8_DLUT]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property BEL "[get_property SITE_TYPE [get_sites SLICE_X28Y8]].D6LUT" $cell
set_property LOC [get_sites SLICE_X28Y8] $cell
set cell [get_cells *CLBLL_R_X19Y8_SLICE_X29Y8_ALUT]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property BEL "[get_property SITE_TYPE [get_sites SLICE_X29Y8]].A6LUT" $cell
set_property LOC [get_sites SLICE_X29Y8] $cell
set cell [get_cells *CLBLL_R_X19Y8_SLICE_X29Y8_BLUT]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property BEL "[get_property SITE_TYPE [get_sites SLICE_X29Y8]].B6LUT" $cell
set_property LOC [get_sites SLICE_X29Y8] $cell
set cell [get_cells *CLBLL_R_X19Y8_SLICE_X29Y8_CLUT]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property BEL "[get_property SITE_TYPE [get_sites SLICE_X29Y8]].C6LUT" $cell
set_property LOC [get_sites SLICE_X29Y8] $cell
set cell [get_cells *CLBLL_R_X19Y8_SLICE_X29Y8_DLUT]
if { $cell == {} } {
    error "Failed to find cell!"
}
set_property BEL "[get_property SITE_TYPE [get_sites SLICE_X29Y8]].D6LUT" $cell
set_property LOC [get_sites SLICE_X29Y8] $cell

set pin [get_pins *CLK_HROW_BOT_R_X60Y26_BUFHCE_X0Y9_BUFHCE/O]
if { $pin == {} } {
    error "Failed to find pin!"
}
set net [get_nets -of_object $pin]
if { $net == {} } {
    error "Failed to find net!"
}


set route_with_dummy [list [get_nodes -of_object [get_wires CLK_HROW_BOT_R_X60Y26/CLK_HROW_CK_HCLK_OUT_L9]] [get_nodes -of_object [get_wires CFG_CENTER_MID_X46Y32/CFG_CENTER_CK_BUFHCLK9]] HCLK_L_X49Y26/HCLK_LEAF_CLK_B_BOTL4 INT_L_X18Y8/GCLK_L_B10_EAST INT_R_X19Y8/CLK1 CLBLL_R_X19Y8/CLBLL_LL_CLK  {} ]

regsub -all {{}} $route_with_dummy "" route
set_property FIXED_ROUTE $route $net

set pin [get_pins *RIOB33_X43Y25_IOB_X1Y26_IBUF/O]
if { $pin == {} } {
    error "Failed to find pin!"
}
set net [get_nets -of_object $pin]
if { $net == {} } {
    error "Failed to find net!"
}


set route_with_dummy [list [get_nodes -of_object [get_wires RIOB33_X43Y25/IOB_IBUF0]] [get_nodes -of_object [get_wires RIOI3_X43Y25/RIOI_I0]] RIOI3_X43Y25/RIOI_ILOGIC0_D RIOI3_X43Y25/IOI_ILOGIC0_O RIOI3_X43Y25/IOI_LOGIC_OUTS18_1 IO_INT_INTERFACE_R_X43Y26/INT_INTERFACE_LOGIC_OUTS18 INT_R_X43Y26/WW4BEG0 INT_R_X39Y26/LV0 INT_R_X39Y44/WW4BEG3 INT_R_X35Y44/WW4BEG3 INT_R_X31Y44/WW2BEG2 INT_R_X29Y44/WW2BEG2 INT_R_X27Y44/NN2BEG3 INT_R_X27Y46/WW2BEG2 INT_R_X25Y46/WL1BEG1 INT_L_X24Y46/WL1BEG0 INT_R_X23Y46/IMUX24 CLK_BUFG_BOT_R_X60Y48/CLK_BUFG_BUFGCTRL0_I0  {} ]

regsub -all {{}} $route_with_dummy "" route
set_property FIXED_ROUTE $route $net

set pin [get_pins *CLBLL_R_X19Y8_SLICE_X28Y8_D5_FDCE/Q]
if { $pin == {} } {
    error "Failed to find pin!"
}
set net [get_nets -of_object $pin]
if { $net == {} } {
    error "Failed to find net!"
}


set route_with_dummy [list [get_nodes -of_object [get_wires CLBLL_R_X19Y8/CLBLL_LL_DMUX]] [get_nodes -of_object [get_wires CLBLL_R_X19Y8/CLBLL_LOGIC_OUTS23]] INT_R_X19Y8/SW6BEG1 INT_R_X11Y4/WW4BEG2 INT_R_X7Y4/WW4BEG2 INT_R_X3Y4/WW2BEG1 INT_R_X1Y4/SW2BEG1 INT_L_X0Y3/IMUX_L34 LIOI3_X0Y3/IOI_OLOGIC1_D1 LIOI3_X0Y3/LIOI_OLOGIC1_OQ LIOI3_X0Y3/LIOI_O1  {} ]

regsub -all {{}} $route_with_dummy "" route
set_property FIXED_ROUTE $route $net

set pin [get_pins *LIOB33_X0Y11_IOB_X0Y11_IBUF/O]
if { $pin == {} } {
    error "Failed to find pin!"
}
set net [get_nets -of_object $pin]
if { $net == {} } {
    error "Failed to find net!"
}


set route_with_dummy [list [get_nodes -of_object [get_wires LIOB33_X0Y11/IOB_IBUF1]] [get_nodes -of_object [get_wires LIOI3_X0Y11/LIOI_I1]] LIOI3_X0Y11/LIOI_ILOGIC1_D LIOI3_X0Y11/IOI_ILOGIC1_O LIOI3_X0Y11/IOI_LOGIC_OUTS18_0 IO_INT_INTERFACE_L_X0Y11/INT_INTERFACE_LOGIC_OUTS_L18 INT_L_X0Y11/EE4BEG0 INT_L_X4Y11/EE4BEG0 INT_L_X8Y11/EE2BEG0 INT_L_X10Y11/SE2BEG0 INT_R_X11Y10/EE2BEG0 INT_R_X19Y10/SL1BEG0 INT_R_X19Y9/SR1BEG1 INT_R_X19Y8/FAN_ALT7 INT_R_X19Y8/FAN7 CLBLL_R_X19Y8/CLBLL_LL_CE  {} ]

regsub -all {{}} $route_with_dummy "" route
set_property FIXED_ROUTE $route $net

set pin [get_pins *LIOB33_X0Y11_IOB_X0Y12_IBUF/O]
if { $pin == {} } {
    error "Failed to find pin!"
}
set net [get_nets -of_object $pin]
if { $net == {} } {
    error "Failed to find net!"
}


set route_with_dummy [list [get_nodes -of_object [get_wires LIOB33_X0Y11/IOB_IBUF0]] [get_nodes -of_object [get_wires LIOI3_X0Y11/LIOI_I0]] LIOI3_X0Y11/LIOI_ILOGIC0_D LIOI3_X0Y11/IOI_ILOGIC0_O LIOI3_X0Y11/IOI_LOGIC_OUTS18_1 IO_INT_INTERFACE_L_X0Y12/INT_INTERFACE_LOGIC_OUTS_L18 INT_L_X0Y12/EE4BEG0 INT_L_X4Y12/EE4BEG0 INT_L_X8Y12/EE4BEG0 INT_L_X18Y12/EL1BEG_N3 INT_R_X19Y11/SS2BEG3 INT_R_X19Y9/SL1BEG3 INT_R_X19Y8/BYP_ALT6 INT_R_X19Y8/BYP6 CLBLL_R_X19Y8/CLBLL_LL_DX  {} ]

regsub -all {{}} $route_with_dummy "" route
set_property FIXED_ROUTE $route $net

set pin [get_pins *CLK_BUFG_BOT_R_X60Y48_BUFGCTRL_X0Y0_BUFGCTRL/O]
if { $pin == {} } {
    error "Failed to find pin!"
}
set net [get_nets -of_object $pin]
if { $net == {} } {
    error "Failed to find net!"
}


set route_with_dummy [list [get_nodes -of_object [get_wires CLK_BUFG_BOT_R_X60Y48/CLK_BUFG_BUFGCTRL0_O]] CLK_BUFG_BOT_R_X60Y48/CLK_BUFG_CK_GCLK0 CLK_BUFG_REBUF_X60Y38/CLK_BUFG_REBUF_R_CK_GCLK0_BOT CLK_HROW_BOT_R_X60Y26/CLK_HROW_CK_MUX_OUT_L9  {} ]

regsub -all {{}} $route_with_dummy "" route
set_property FIXED_ROUTE $route $net

set pin [get_pins *LIOB33_X0Y9_IOB_X0Y10_IBUF/O]
if { $pin == {} } {
    error "Failed to find pin!"
}
set net [get_nets -of_object $pin]
if { $net == {} } {
    error "Failed to find net!"
}


set route_with_dummy [list [get_nodes -of_object [get_wires LIOB33_X0Y9/IOB_IBUF0]] [get_nodes -of_object [get_wires LIOI3_X0Y9/LIOI_I0]] LIOI3_X0Y9/LIOI_ILOGIC0_D LIOI3_X0Y9/IOI_ILOGIC0_O LIOI3_X0Y9/IOI_LOGIC_OUTS18_1 IO_INT_INTERFACE_L_X0Y10/INT_INTERFACE_LOGIC_OUTS_L18 INT_L_X0Y10/SE2BEG0 INT_R_X1Y9/EE4BEG0 INT_R_X5Y9/EL1BEG_N3 INT_L_X6Y8/EL1BEG2 INT_R_X7Y8/EE2BEG2 INT_R_X9Y8/EE4BEG2 INT_R_X19Y8/CTRL1 CLBLL_R_X19Y8/CLBLL_LL_SR  {} ]

regsub -all {{}} $route_with_dummy "" route
set_property FIXED_ROUTE $route $net
set net [get_nets {<const0>}]

set route_with_dummy [list  ( [list [get_nodes -of_object [get_wires INT_L_X0Y19/GND_WIRE]] INT_L_X0Y19/GFAN0 INT_L_X0Y19/IMUX_L34 LIOI3_TBYTESRC_X0Y19/IOI_OLOGIC1_D1 LIOI3_TBYTESRC_X0Y19/LIOI_OLOGIC1_OQ LIOI3_TBYTESRC_X0Y19/LIOI_O1  {} ] ) ( [list [get_nodes -of_object [get_wires INT_L_X0Y20/GND_WIRE]] INT_L_X0Y20/GFAN0 INT_L_X0Y20/IMUX_L34 LIOI3_TBYTESRC_X0Y19/IOI_OLOGIC0_D1 LIOI3_TBYTESRC_X0Y19/LIOI_OLOGIC0_OQ LIOI3_TBYTESRC_X0Y19/LIOI_O0  {} ] ) ( [list [get_nodes -of_object [get_wires INT_L_X0Y2/GND_WIRE]] INT_L_X0Y2/GFAN0 INT_L_X0Y2/IMUX_L34 LIOI3_X0Y1/IOI_OLOGIC0_D1 LIOI3_X0Y1/LIOI_OLOGIC0_OQ LIOI3_X0Y1/LIOI_O0  {} ] ) ( [list [get_nodes -of_object [get_wires INT_L_X0Y1/GND_WIRE]] INT_L_X0Y1/GFAN0 INT_L_X0Y1/IMUX_L34 LIOI3_X0Y1/IOI_OLOGIC1_D1 LIOI3_X0Y1/LIOI_OLOGIC1_OQ LIOI3_X0Y1/LIOI_O1  {} ] ) ( [list [get_nodes -of_object [get_wires INT_L_X0Y4/GND_WIRE]] INT_L_X0Y4/GFAN0 INT_L_X0Y4/IMUX_L34 LIOI3_X0Y3/IOI_OLOGIC0_D1 LIOI3_X0Y3/LIOI_OLOGIC0_OQ LIOI3_X0Y3/LIOI_O0  {} ] ) ( [list [get_nodes -of_object [get_wires INT_R_X43Y87/GND_WIRE]] INT_R_X43Y87/GFAN0 INT_R_X43Y87/IMUX34 RIOI3_TBYTETERM_X43Y87/IOI_OLOGIC1_D1 RIOI3_TBYTETERM_X43Y87/RIOI_OLOGIC1_OQ RIOI3_TBYTETERM_X43Y87/RIOI_O1  {} ] ) ( [list [get_nodes -of_object [get_wires INT_R_X43Y32/GND_WIRE]] INT_R_X43Y32/GFAN0 INT_R_X43Y32/IMUX34 RIOI3_TBYTESRC_X43Y31/IOI_OLOGIC0_D1 RIOI3_TBYTESRC_X43Y31/RIOI_OLOGIC0_OQ RIOI3_TBYTESRC_X43Y31/RIOI_O0  {} ] ) ( [list [get_nodes -of_object [get_wires INT_L_X0Y43/GND_WIRE]] INT_L_X0Y43/GFAN0 INT_L_X0Y43/IMUX_L34 LIOI3_TBYTESRC_X0Y43/IOI_OLOGIC1_D1 LIOI3_TBYTESRC_X0Y43/LIOI_OLOGIC1_OQ LIOI3_TBYTESRC_X0Y43/LIOI_O1  {} ] ) ( [list [get_nodes -of_object [get_wires INT_R_X43Y76/GND_WIRE]] INT_R_X43Y76/GFAN0 INT_R_X43Y76/IMUX34 RIOI3_X43Y75/IOI_OLOGIC0_D1 RIOI3_X43Y75/RIOI_OLOGIC0_OQ RIOI3_X43Y75/RIOI_O0  {} ] ) ( [list [get_nodes -of_object [get_wires INT_R_X43Y75/GND_WIRE]] INT_R_X43Y75/GFAN0 INT_R_X43Y75/IMUX34 RIOI3_X43Y75/IOI_OLOGIC1_D1 RIOI3_X43Y75/RIOI_OLOGIC1_OQ RIOI3_X43Y75/RIOI_O1  {} ] ) ( [list [get_nodes -of_object [get_wires INT_R_X43Y38/GND_WIRE]] INT_R_X43Y38/GFAN0 INT_R_X43Y38/IMUX34 RIOI3_TBYTETERM_X43Y37/IOI_OLOGIC0_D1 RIOI3_TBYTETERM_X43Y37/RIOI_OLOGIC0_OQ RIOI3_TBYTETERM_X43Y37/RIOI_O0  {} ] ) ( [list [get_nodes -of_object [get_wires INT_R_X43Y37/GND_WIRE]] INT_R_X43Y37/GFAN0 INT_R_X43Y37/IMUX34 RIOI3_TBYTETERM_X43Y37/IOI_OLOGIC1_D1 RIOI3_TBYTETERM_X43Y37/RIOI_OLOGIC1_OQ RIOI3_TBYTETERM_X43Y37/RIOI_O1  {} ] ) ( [list [get_nodes -of_object [get_wires INT_L_X0Y0/GND_WIRE]] INT_L_X0Y0/GFAN0 INT_L_X0Y0/IMUX_L34 LIOI3_SING_X0Y0/IOI_OLOGIC0_D1 LIOI3_SING_X0Y0/LIOI_OLOGIC0_OQ LIOI3_SING_X0Y0/LIOI_O0  {} ] ) ( [list [get_nodes -of_object [get_wires INT_R_X43Y61/GND_WIRE]] INT_R_X43Y61/GFAN0 INT_R_X43Y61/IMUX34 RIOI3_X43Y61/IOI_OLOGIC1_D1 RIOI3_X43Y61/RIOI_OLOGIC1_OQ RIOI3_X43Y61/RIOI_O1  {} ] ) ( [list [get_nodes -of_object [get_wires INT_L_X0Y111/GND_WIRE]] INT_L_X0Y111/GFAN0 INT_L_X0Y111/IMUX_L34 LIOI3_X0Y111/IOI_OLOGIC1_D1 LIOI3_X0Y111/LIOI_OLOGIC1_OQ LIOI3_X0Y111/LIOI_O1  {} ] ) ( [list [get_nodes -of_object [get_wires INT_L_X0Y18/GND_WIRE]] INT_L_X0Y18/GFAN0 INT_L_X0Y18/IMUX_L34 LIOI3_X0Y17/IOI_OLOGIC0_D1 LIOI3_X0Y17/LIOI_OLOGIC0_OQ LIOI3_X0Y17/LIOI_O0  {} ] ) {} ]

regsub -all {{}} $route_with_dummy "" route
set_property FIXED_ROUTE $route $net
set net [get_nets {<const1>}]

set route_with_dummy [list  ( [list [get_nodes -of_object [get_wires INT_R_X19Y8/VCC_WIRE]] [list INT_R_X19Y8/IMUX33 CLBLL_R_X19Y8/CLBLL_L_C1  {} ] [list INT_R_X19Y8/IMUX20 CLBLL_R_X19Y8/CLBLL_L_C2  {} ] [list INT_R_X19Y8/IMUX23 CLBLL_R_X19Y8/CLBLL_L_C3  {} ] [list INT_R_X19Y8/IMUX21 CLBLL_R_X19Y8/CLBLL_L_C4  {} ] [list INT_R_X19Y8/IMUX30 CLBLL_R_X19Y8/CLBLL_L_C5  {} ] [list INT_R_X19Y8/IMUX34 CLBLL_R_X19Y8/CLBLL_L_C6  {} ] [list INT_R_X19Y8/IMUX41 CLBLL_R_X19Y8/CLBLL_L_D1  {} ] [list INT_R_X19Y8/IMUX36 CLBLL_R_X19Y8/CLBLL_L_D2  {} ] [list INT_R_X19Y8/IMUX39 CLBLL_R_X19Y8/CLBLL_L_D3  {} ] [list INT_R_X19Y8/IMUX37 CLBLL_R_X19Y8/CLBLL_L_D4  {} ] [list INT_R_X19Y8/IMUX46 CLBLL_R_X19Y8/CLBLL_L_D5  {} ] [list INT_R_X19Y8/IMUX42 CLBLL_R_X19Y8/CLBLL_L_D6  {} ] [list INT_R_X19Y8/IMUX7 CLBLL_R_X19Y8/CLBLL_LL_A1  {} ] [list INT_R_X19Y8/IMUX2 CLBLL_R_X19Y8/CLBLL_LL_A2  {} ] [list INT_R_X19Y8/IMUX1 CLBLL_R_X19Y8/CLBLL_LL_A3  {} ] [list INT_R_X19Y8/IMUX11 CLBLL_R_X19Y8/CLBLL_LL_A4  {} ] [list INT_R_X19Y8/IMUX8 CLBLL_R_X19Y8/CLBLL_LL_A5  {} ] [list INT_R_X19Y8/IMUX4 CLBLL_R_X19Y8/CLBLL_LL_A6  {} ] [list INT_R_X19Y8/IMUX15 CLBLL_R_X19Y8/CLBLL_LL_B1  {} ] [list INT_R_X19Y8/IMUX18 CLBLL_R_X19Y8/CLBLL_LL_B2  {} ] [list INT_R_X19Y8/IMUX17 CLBLL_R_X19Y8/CLBLL_LL_B3  {} ] [list INT_R_X19Y8/IMUX27 CLBLL_R_X19Y8/CLBLL_LL_B4  {} ] [list INT_R_X19Y8/IMUX24 CLBLL_R_X19Y8/CLBLL_LL_B5  {} ] [list INT_R_X19Y8/IMUX12 CLBLL_R_X19Y8/CLBLL_LL_B6  {} ] [list INT_R_X19Y8/IMUX32 CLBLL_R_X19Y8/CLBLL_LL_C1  {} ] [list INT_R_X19Y8/IMUX29 CLBLL_R_X19Y8/CLBLL_LL_C2  {} ] [list INT_R_X19Y8/IMUX22 CLBLL_R_X19Y8/CLBLL_LL_C3  {} ] [list INT_R_X19Y8/IMUX28 CLBLL_R_X19Y8/CLBLL_LL_C4  {} ] [list INT_R_X19Y8/IMUX31 CLBLL_R_X19Y8/CLBLL_LL_C5  {} ] [list INT_R_X19Y8/IMUX35 CLBLL_R_X19Y8/CLBLL_LL_C6  {} ] [list INT_R_X19Y8/IMUX40 CLBLL_R_X19Y8/CLBLL_LL_D1  {} ] [list INT_R_X19Y8/IMUX45 CLBLL_R_X19Y8/CLBLL_LL_D2  {} ] [list INT_R_X19Y8/IMUX38 CLBLL_R_X19Y8/CLBLL_LL_D3  {} ] [list INT_R_X19Y8/IMUX44 CLBLL_R_X19Y8/CLBLL_LL_D4  {} ] [list INT_R_X19Y8/IMUX47 CLBLL_R_X19Y8/CLBLL_LL_D5  {} ] [list INT_R_X19Y8/IMUX43 CLBLL_R_X19Y8/CLBLL_LL_D6  {} ] [list INT_R_X19Y8/IMUX6 CLBLL_R_X19Y8/CLBLL_L_A1  {} ] [list INT_R_X19Y8/IMUX3 CLBLL_R_X19Y8/CLBLL_L_A2  {} ] [list INT_R_X19Y8/IMUX0 CLBLL_R_X19Y8/CLBLL_L_A3  {} ] [list INT_R_X19Y8/IMUX10 CLBLL_R_X19Y8/CLBLL_L_A4  {} ] [list INT_R_X19Y8/IMUX9 CLBLL_R_X19Y8/CLBLL_L_A5  {} ] [list INT_R_X19Y8/IMUX5 CLBLL_R_X19Y8/CLBLL_L_A6  {} ] [list INT_R_X19Y8/IMUX14 CLBLL_R_X19Y8/CLBLL_L_B1  {} ] [list INT_R_X19Y8/IMUX19 CLBLL_R_X19Y8/CLBLL_L_B2  {} ] [list INT_R_X19Y8/IMUX16 CLBLL_R_X19Y8/CLBLL_L_B3  {} ] [list INT_R_X19Y8/IMUX26 CLBLL_R_X19Y8/CLBLL_L_B4  {} ] [list INT_R_X19Y8/IMUX25 CLBLL_R_X19Y8/CLBLL_L_B5  {} ] INT_R_X19Y8/IMUX13 CLBLL_R_X19Y8/CLBLL_L_B6  {} ] ) ( [list [get_nodes -of_object [get_wires INT_R_X23Y25/VCC_WIRE]] INT_R_X23Y25/IMUX3 CLK_HROW_BOT_R_X60Y26/CLK_HROW_CE_INT_TOP3 CLK_HROW_BOT_R_X60Y26/CLK_HROW_BUFHCE_CE_L9  {} ] ) ( [list [get_nodes -of_object [get_wires INT_R_X23Y46/VCC_WIRE]] [list INT_R_X23Y46/IMUX20 CLK_BUFG_BOT_R_X60Y48/CLK_BUFG_R_BUFGCTRL0_CE0  {} ] [list INT_R_X23Y46/IMUX16 CLK_BUFG_BOT_R_X60Y48/CLK_BUFG_R_BUFGCTRL0_CE1  {} ] [list INT_R_X23Y46/IMUX12 CLK_BUFG_BOT_R_X60Y48/CLK_BUFG_R_BUFGCTRL0_IGNORE0  {} ] [list INT_R_X23Y46/IMUX8 CLK_BUFG_BOT_R_X60Y48/CLK_BUFG_R_BUFGCTRL0_IGNORE1  {} ] [list INT_R_X23Y46/IMUX4 CLK_BUFG_BOT_R_X60Y48/CLK_BUFG_R_BUFGCTRL0_S0  {} ] [list INT_R_X23Y46/IMUX0 CLK_BUFG_BOT_R_X60Y48/CLK_BUFG_R_BUFGCTRL0_S1  {} ] INT_R_X23Y46/IMUX28 CLK_BUFG_BOT_R_X60Y48/CLK_BUFG_BUFGCTRL0_I1  {} ] ) {} ]

regsub -all {{}} $route_with_dummy "" route
set_property FIXED_ROUTE $route $net

// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2019.2 (lin64) Build 2708876 Wed Nov  6 21:39:14 MST 2019
// Date        : Fri Jul 16 06:51:34 2021
// Host        : goeders-ssh8 running 64-bit Ubuntu 20.04.2 LTS
// Command     : write_verilog -force -file /home/jaromharris/bfasst/build/xilinx_yosys_impl/basic/add32_r_rst/add32_impl.v
// Design      : add32
// Purpose     : This is a Verilog netlist of the current design or from a specific cell of the design. The output is an
//               IEEE 1364-2001 compliant Verilog HDL file that contains netlist information obtained from the input
//               design files.
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* ECO_CHECKSUM = "be08f03c" *) 
(* STRUCTURAL_NETLIST = "yes" *)
module add32
   (clk,
    rst,
    a,
    b,
    o);
  input clk;
  input rst;
  input [31:0]a;
  input [31:0]b;
  output [31:0]o;

  wire \<const0> ;
  wire \<const1> ;
  wire [31:0]a;
  wire [31:0]a_IBUF;
  wire [31:0]b;
  wire [31:0]b_IBUF;
  wire clk;
  wire clk_IBUF;
  wire clk_IBUF_BUFG;
  wire [31:0]o;
  wire \o[11]_i_2_n_0 ;
  wire \o[11]_i_3_n_0 ;
  wire \o[11]_i_4_n_0 ;
  wire \o[11]_i_5_n_0 ;
  wire \o[15]_i_2_n_0 ;
  wire \o[15]_i_3_n_0 ;
  wire \o[15]_i_4_n_0 ;
  wire \o[15]_i_5_n_0 ;
  wire \o[19]_i_2_n_0 ;
  wire \o[19]_i_3_n_0 ;
  wire \o[19]_i_4_n_0 ;
  wire \o[19]_i_5_n_0 ;
  wire \o[23]_i_2_n_0 ;
  wire \o[23]_i_3_n_0 ;
  wire \o[23]_i_4_n_0 ;
  wire \o[23]_i_5_n_0 ;
  wire \o[27]_i_2_n_0 ;
  wire \o[27]_i_3_n_0 ;
  wire \o[27]_i_4_n_0 ;
  wire \o[27]_i_5_n_0 ;
  wire \o[31]_i_2_n_0 ;
  wire \o[31]_i_3_n_0 ;
  wire \o[31]_i_4_n_0 ;
  wire \o[31]_i_5_n_0 ;
  wire \o[3]_i_2_n_0 ;
  wire \o[3]_i_3_n_0 ;
  wire \o[3]_i_4_n_0 ;
  wire \o[3]_i_5_n_0 ;
  wire \o[7]_i_2_n_0 ;
  wire \o[7]_i_3_n_0 ;
  wire \o[7]_i_4_n_0 ;
  wire \o[7]_i_5_n_0 ;
  wire [31:0]o_OBUF;
  wire \o_reg[11]_i_1_n_0 ;
  wire \o_reg[15]_i_1_n_0 ;
  wire \o_reg[19]_i_1_n_0 ;
  wire \o_reg[23]_i_1_n_0 ;
  wire \o_reg[27]_i_1_n_0 ;
  wire \o_reg[3]_i_1_n_0 ;
  wire \o_reg[7]_i_1_n_0 ;
  wire [31:0]p_0_in;
  wire rst;
  wire rst_IBUF;
  wire [3:0]\NLW_o_reg[11]_i_1_CO_UNCONNECTED ;
  wire [3:0]\NLW_o_reg[15]_i_1_CO_UNCONNECTED ;
  wire [3:0]\NLW_o_reg[19]_i_1_CO_UNCONNECTED ;
  wire [3:0]\NLW_o_reg[23]_i_1_CO_UNCONNECTED ;
  wire [3:0]\NLW_o_reg[27]_i_1_CO_UNCONNECTED ;
  wire [3:0]\NLW_o_reg[3]_i_1_CO_UNCONNECTED ;
  wire [3:0]\NLW_o_reg[7]_i_1_CO_UNCONNECTED ;

  GND GND
       (.G(\<const0> ));
  VCC VCC
       (.P(\<const1> ));
  IBUF \a_IBUF[0]_inst 
       (.I(a[0]),
        .O(a_IBUF[0]));
  IBUF \a_IBUF[10]_inst 
       (.I(a[10]),
        .O(a_IBUF[10]));
  IBUF \a_IBUF[11]_inst 
       (.I(a[11]),
        .O(a_IBUF[11]));
  IBUF \a_IBUF[12]_inst 
       (.I(a[12]),
        .O(a_IBUF[12]));
  IBUF \a_IBUF[13]_inst 
       (.I(a[13]),
        .O(a_IBUF[13]));
  IBUF \a_IBUF[14]_inst 
       (.I(a[14]),
        .O(a_IBUF[14]));
  IBUF \a_IBUF[15]_inst 
       (.I(a[15]),
        .O(a_IBUF[15]));
  IBUF \a_IBUF[16]_inst 
       (.I(a[16]),
        .O(a_IBUF[16]));
  IBUF \a_IBUF[17]_inst 
       (.I(a[17]),
        .O(a_IBUF[17]));
  IBUF \a_IBUF[18]_inst 
       (.I(a[18]),
        .O(a_IBUF[18]));
  IBUF \a_IBUF[19]_inst 
       (.I(a[19]),
        .O(a_IBUF[19]));
  IBUF \a_IBUF[1]_inst 
       (.I(a[1]),
        .O(a_IBUF[1]));
  IBUF \a_IBUF[20]_inst 
       (.I(a[20]),
        .O(a_IBUF[20]));
  IBUF \a_IBUF[21]_inst 
       (.I(a[21]),
        .O(a_IBUF[21]));
  IBUF \a_IBUF[22]_inst 
       (.I(a[22]),
        .O(a_IBUF[22]));
  IBUF \a_IBUF[23]_inst 
       (.I(a[23]),
        .O(a_IBUF[23]));
  IBUF \a_IBUF[24]_inst 
       (.I(a[24]),
        .O(a_IBUF[24]));
  IBUF \a_IBUF[25]_inst 
       (.I(a[25]),
        .O(a_IBUF[25]));
  IBUF \a_IBUF[26]_inst 
       (.I(a[26]),
        .O(a_IBUF[26]));
  IBUF \a_IBUF[27]_inst 
       (.I(a[27]),
        .O(a_IBUF[27]));
  IBUF \a_IBUF[28]_inst 
       (.I(a[28]),
        .O(a_IBUF[28]));
  IBUF \a_IBUF[29]_inst 
       (.I(a[29]),
        .O(a_IBUF[29]));
  IBUF \a_IBUF[2]_inst 
       (.I(a[2]),
        .O(a_IBUF[2]));
  IBUF \a_IBUF[30]_inst 
       (.I(a[30]),
        .O(a_IBUF[30]));
  IBUF \a_IBUF[31]_inst 
       (.I(a[31]),
        .O(a_IBUF[31]));
  IBUF \a_IBUF[3]_inst 
       (.I(a[3]),
        .O(a_IBUF[3]));
  IBUF \a_IBUF[4]_inst 
       (.I(a[4]),
        .O(a_IBUF[4]));
  IBUF \a_IBUF[5]_inst 
       (.I(a[5]),
        .O(a_IBUF[5]));
  IBUF \a_IBUF[6]_inst 
       (.I(a[6]),
        .O(a_IBUF[6]));
  IBUF \a_IBUF[7]_inst 
       (.I(a[7]),
        .O(a_IBUF[7]));
  IBUF \a_IBUF[8]_inst 
       (.I(a[8]),
        .O(a_IBUF[8]));
  IBUF \a_IBUF[9]_inst 
       (.I(a[9]),
        .O(a_IBUF[9]));
  IBUF \b_IBUF[0]_inst 
       (.I(b[0]),
        .O(b_IBUF[0]));
  IBUF \b_IBUF[10]_inst 
       (.I(b[10]),
        .O(b_IBUF[10]));
  IBUF \b_IBUF[11]_inst 
       (.I(b[11]),
        .O(b_IBUF[11]));
  IBUF \b_IBUF[12]_inst 
       (.I(b[12]),
        .O(b_IBUF[12]));
  IBUF \b_IBUF[13]_inst 
       (.I(b[13]),
        .O(b_IBUF[13]));
  IBUF \b_IBUF[14]_inst 
       (.I(b[14]),
        .O(b_IBUF[14]));
  IBUF \b_IBUF[15]_inst 
       (.I(b[15]),
        .O(b_IBUF[15]));
  IBUF \b_IBUF[16]_inst 
       (.I(b[16]),
        .O(b_IBUF[16]));
  IBUF \b_IBUF[17]_inst 
       (.I(b[17]),
        .O(b_IBUF[17]));
  IBUF \b_IBUF[18]_inst 
       (.I(b[18]),
        .O(b_IBUF[18]));
  IBUF \b_IBUF[19]_inst 
       (.I(b[19]),
        .O(b_IBUF[19]));
  IBUF \b_IBUF[1]_inst 
       (.I(b[1]),
        .O(b_IBUF[1]));
  IBUF \b_IBUF[20]_inst 
       (.I(b[20]),
        .O(b_IBUF[20]));
  IBUF \b_IBUF[21]_inst 
       (.I(b[21]),
        .O(b_IBUF[21]));
  IBUF \b_IBUF[22]_inst 
       (.I(b[22]),
        .O(b_IBUF[22]));
  IBUF \b_IBUF[23]_inst 
       (.I(b[23]),
        .O(b_IBUF[23]));
  IBUF \b_IBUF[24]_inst 
       (.I(b[24]),
        .O(b_IBUF[24]));
  IBUF \b_IBUF[25]_inst 
       (.I(b[25]),
        .O(b_IBUF[25]));
  IBUF \b_IBUF[26]_inst 
       (.I(b[26]),
        .O(b_IBUF[26]));
  IBUF \b_IBUF[27]_inst 
       (.I(b[27]),
        .O(b_IBUF[27]));
  IBUF \b_IBUF[28]_inst 
       (.I(b[28]),
        .O(b_IBUF[28]));
  IBUF \b_IBUF[29]_inst 
       (.I(b[29]),
        .O(b_IBUF[29]));
  IBUF \b_IBUF[2]_inst 
       (.I(b[2]),
        .O(b_IBUF[2]));
  IBUF \b_IBUF[30]_inst 
       (.I(b[30]),
        .O(b_IBUF[30]));
  IBUF \b_IBUF[31]_inst 
       (.I(b[31]),
        .O(b_IBUF[31]));
  IBUF \b_IBUF[3]_inst 
       (.I(b[3]),
        .O(b_IBUF[3]));
  IBUF \b_IBUF[4]_inst 
       (.I(b[4]),
        .O(b_IBUF[4]));
  IBUF \b_IBUF[5]_inst 
       (.I(b[5]),
        .O(b_IBUF[5]));
  IBUF \b_IBUF[6]_inst 
       (.I(b[6]),
        .O(b_IBUF[6]));
  IBUF \b_IBUF[7]_inst 
       (.I(b[7]),
        .O(b_IBUF[7]));
  IBUF \b_IBUF[8]_inst 
       (.I(b[8]),
        .O(b_IBUF[8]));
  IBUF \b_IBUF[9]_inst 
       (.I(b[9]),
        .O(b_IBUF[9]));
  BUFG clk_IBUF_BUFG_inst
       (.I(clk_IBUF),
        .O(clk_IBUF_BUFG));
  IBUF clk_IBUF_inst
       (.I(clk),
        .O(clk_IBUF));
  LUT2 #(
    .INIT(4'h6)) 
    \o[11]_i_2 
       (.I0(a_IBUF[11]),
        .I1(b_IBUF[11]),
        .O(\o[11]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[11]_i_3 
       (.I0(a_IBUF[10]),
        .I1(b_IBUF[10]),
        .O(\o[11]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[11]_i_4 
       (.I0(a_IBUF[9]),
        .I1(b_IBUF[9]),
        .O(\o[11]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[11]_i_5 
       (.I0(a_IBUF[8]),
        .I1(b_IBUF[8]),
        .O(\o[11]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[15]_i_2 
       (.I0(a_IBUF[15]),
        .I1(b_IBUF[15]),
        .O(\o[15]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[15]_i_3 
       (.I0(a_IBUF[14]),
        .I1(b_IBUF[14]),
        .O(\o[15]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[15]_i_4 
       (.I0(a_IBUF[13]),
        .I1(b_IBUF[13]),
        .O(\o[15]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[15]_i_5 
       (.I0(a_IBUF[12]),
        .I1(b_IBUF[12]),
        .O(\o[15]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[19]_i_2 
       (.I0(a_IBUF[19]),
        .I1(b_IBUF[19]),
        .O(\o[19]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[19]_i_3 
       (.I0(a_IBUF[18]),
        .I1(b_IBUF[18]),
        .O(\o[19]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[19]_i_4 
       (.I0(a_IBUF[17]),
        .I1(b_IBUF[17]),
        .O(\o[19]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[19]_i_5 
       (.I0(a_IBUF[16]),
        .I1(b_IBUF[16]),
        .O(\o[19]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[23]_i_2 
       (.I0(a_IBUF[23]),
        .I1(b_IBUF[23]),
        .O(\o[23]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[23]_i_3 
       (.I0(a_IBUF[22]),
        .I1(b_IBUF[22]),
        .O(\o[23]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[23]_i_4 
       (.I0(a_IBUF[21]),
        .I1(b_IBUF[21]),
        .O(\o[23]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[23]_i_5 
       (.I0(a_IBUF[20]),
        .I1(b_IBUF[20]),
        .O(\o[23]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[27]_i_2 
       (.I0(a_IBUF[27]),
        .I1(b_IBUF[27]),
        .O(\o[27]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[27]_i_3 
       (.I0(a_IBUF[26]),
        .I1(b_IBUF[26]),
        .O(\o[27]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[27]_i_4 
       (.I0(a_IBUF[25]),
        .I1(b_IBUF[25]),
        .O(\o[27]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[27]_i_5 
       (.I0(a_IBUF[24]),
        .I1(b_IBUF[24]),
        .O(\o[27]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[31]_i_2 
       (.I0(a_IBUF[31]),
        .I1(b_IBUF[31]),
        .O(\o[31]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[31]_i_3 
       (.I0(a_IBUF[30]),
        .I1(b_IBUF[30]),
        .O(\o[31]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[31]_i_4 
       (.I0(a_IBUF[29]),
        .I1(b_IBUF[29]),
        .O(\o[31]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[31]_i_5 
       (.I0(a_IBUF[28]),
        .I1(b_IBUF[28]),
        .O(\o[31]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[3]_i_2 
       (.I0(a_IBUF[3]),
        .I1(b_IBUF[3]),
        .O(\o[3]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[3]_i_3 
       (.I0(a_IBUF[2]),
        .I1(b_IBUF[2]),
        .O(\o[3]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[3]_i_4 
       (.I0(a_IBUF[1]),
        .I1(b_IBUF[1]),
        .O(\o[3]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[3]_i_5 
       (.I0(a_IBUF[0]),
        .I1(b_IBUF[0]),
        .O(\o[3]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[7]_i_2 
       (.I0(a_IBUF[7]),
        .I1(b_IBUF[7]),
        .O(\o[7]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[7]_i_3 
       (.I0(a_IBUF[6]),
        .I1(b_IBUF[6]),
        .O(\o[7]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[7]_i_4 
       (.I0(a_IBUF[5]),
        .I1(b_IBUF[5]),
        .O(\o[7]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \o[7]_i_5 
       (.I0(a_IBUF[4]),
        .I1(b_IBUF[4]),
        .O(\o[7]_i_5_n_0 ));
  OBUF \o_OBUF[0]_inst 
       (.I(o_OBUF[0]),
        .O(o[0]));
  OBUF \o_OBUF[10]_inst 
       (.I(o_OBUF[10]),
        .O(o[10]));
  OBUF \o_OBUF[11]_inst 
       (.I(o_OBUF[11]),
        .O(o[11]));
  OBUF \o_OBUF[12]_inst 
       (.I(o_OBUF[12]),
        .O(o[12]));
  OBUF \o_OBUF[13]_inst 
       (.I(o_OBUF[13]),
        .O(o[13]));
  OBUF \o_OBUF[14]_inst 
       (.I(o_OBUF[14]),
        .O(o[14]));
  OBUF \o_OBUF[15]_inst 
       (.I(o_OBUF[15]),
        .O(o[15]));
  OBUF \o_OBUF[16]_inst 
       (.I(o_OBUF[16]),
        .O(o[16]));
  OBUF \o_OBUF[17]_inst 
       (.I(o_OBUF[17]),
        .O(o[17]));
  OBUF \o_OBUF[18]_inst 
       (.I(o_OBUF[18]),
        .O(o[18]));
  OBUF \o_OBUF[19]_inst 
       (.I(o_OBUF[19]),
        .O(o[19]));
  OBUF \o_OBUF[1]_inst 
       (.I(o_OBUF[1]),
        .O(o[1]));
  OBUF \o_OBUF[20]_inst 
       (.I(o_OBUF[20]),
        .O(o[20]));
  OBUF \o_OBUF[21]_inst 
       (.I(o_OBUF[21]),
        .O(o[21]));
  OBUF \o_OBUF[22]_inst 
       (.I(o_OBUF[22]),
        .O(o[22]));
  OBUF \o_OBUF[23]_inst 
       (.I(o_OBUF[23]),
        .O(o[23]));
  OBUF \o_OBUF[24]_inst 
       (.I(o_OBUF[24]),
        .O(o[24]));
  OBUF \o_OBUF[25]_inst 
       (.I(o_OBUF[25]),
        .O(o[25]));
  OBUF \o_OBUF[26]_inst 
       (.I(o_OBUF[26]),
        .O(o[26]));
  OBUF \o_OBUF[27]_inst 
       (.I(o_OBUF[27]),
        .O(o[27]));
  OBUF \o_OBUF[28]_inst 
       (.I(o_OBUF[28]),
        .O(o[28]));
  OBUF \o_OBUF[29]_inst 
       (.I(o_OBUF[29]),
        .O(o[29]));
  OBUF \o_OBUF[2]_inst 
       (.I(o_OBUF[2]),
        .O(o[2]));
  OBUF \o_OBUF[30]_inst 
       (.I(o_OBUF[30]),
        .O(o[30]));
  OBUF \o_OBUF[31]_inst 
       (.I(o_OBUF[31]),
        .O(o[31]));
  OBUF \o_OBUF[3]_inst 
       (.I(o_OBUF[3]),
        .O(o[3]));
  OBUF \o_OBUF[4]_inst 
       (.I(o_OBUF[4]),
        .O(o[4]));
  OBUF \o_OBUF[5]_inst 
       (.I(o_OBUF[5]),
        .O(o[5]));
  OBUF \o_OBUF[6]_inst 
       (.I(o_OBUF[6]),
        .O(o[6]));
  OBUF \o_OBUF[7]_inst 
       (.I(o_OBUF[7]),
        .O(o[7]));
  OBUF \o_OBUF[8]_inst 
       (.I(o_OBUF[8]),
        .O(o[8]));
  OBUF \o_OBUF[9]_inst 
       (.I(o_OBUF[9]),
        .O(o[9]));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[0] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[0]),
        .Q(o_OBUF[0]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[10] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[10]),
        .Q(o_OBUF[10]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[11] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[11]),
        .Q(o_OBUF[11]),
        .R(rst_IBUF));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \o_reg[11]_i_1 
       (.CI(\o_reg[7]_i_1_n_0 ),
        .CO({\o_reg[11]_i_1_n_0 ,\NLW_o_reg[11]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(a_IBUF[11:8]),
        .O(p_0_in[11:8]),
        .S({\o[11]_i_2_n_0 ,\o[11]_i_3_n_0 ,\o[11]_i_4_n_0 ,\o[11]_i_5_n_0 }));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[12] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[12]),
        .Q(o_OBUF[12]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[13] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[13]),
        .Q(o_OBUF[13]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[14] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[14]),
        .Q(o_OBUF[14]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[15] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[15]),
        .Q(o_OBUF[15]),
        .R(rst_IBUF));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \o_reg[15]_i_1 
       (.CI(\o_reg[11]_i_1_n_0 ),
        .CO({\o_reg[15]_i_1_n_0 ,\NLW_o_reg[15]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(a_IBUF[15:12]),
        .O(p_0_in[15:12]),
        .S({\o[15]_i_2_n_0 ,\o[15]_i_3_n_0 ,\o[15]_i_4_n_0 ,\o[15]_i_5_n_0 }));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[16] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[16]),
        .Q(o_OBUF[16]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[17] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[17]),
        .Q(o_OBUF[17]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[18] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[18]),
        .Q(o_OBUF[18]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[19] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[19]),
        .Q(o_OBUF[19]),
        .R(rst_IBUF));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \o_reg[19]_i_1 
       (.CI(\o_reg[15]_i_1_n_0 ),
        .CO({\o_reg[19]_i_1_n_0 ,\NLW_o_reg[19]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(a_IBUF[19:16]),
        .O(p_0_in[19:16]),
        .S({\o[19]_i_2_n_0 ,\o[19]_i_3_n_0 ,\o[19]_i_4_n_0 ,\o[19]_i_5_n_0 }));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[1] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[1]),
        .Q(o_OBUF[1]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[20] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[20]),
        .Q(o_OBUF[20]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[21] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[21]),
        .Q(o_OBUF[21]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[22] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[22]),
        .Q(o_OBUF[22]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[23] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[23]),
        .Q(o_OBUF[23]),
        .R(rst_IBUF));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \o_reg[23]_i_1 
       (.CI(\o_reg[19]_i_1_n_0 ),
        .CO({\o_reg[23]_i_1_n_0 ,\NLW_o_reg[23]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(a_IBUF[23:20]),
        .O(p_0_in[23:20]),
        .S({\o[23]_i_2_n_0 ,\o[23]_i_3_n_0 ,\o[23]_i_4_n_0 ,\o[23]_i_5_n_0 }));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[24] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[24]),
        .Q(o_OBUF[24]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[25] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[25]),
        .Q(o_OBUF[25]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[26] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[26]),
        .Q(o_OBUF[26]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[27] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[27]),
        .Q(o_OBUF[27]),
        .R(rst_IBUF));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \o_reg[27]_i_1 
       (.CI(\o_reg[23]_i_1_n_0 ),
        .CO({\o_reg[27]_i_1_n_0 ,\NLW_o_reg[27]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(a_IBUF[27:24]),
        .O(p_0_in[27:24]),
        .S({\o[27]_i_2_n_0 ,\o[27]_i_3_n_0 ,\o[27]_i_4_n_0 ,\o[27]_i_5_n_0 }));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[28] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[28]),
        .Q(o_OBUF[28]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[29] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[29]),
        .Q(o_OBUF[29]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[2] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[2]),
        .Q(o_OBUF[2]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[30] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[30]),
        .Q(o_OBUF[30]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[31] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[31]),
        .Q(o_OBUF[31]),
        .R(rst_IBUF));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \o_reg[31]_i_1 
       (.CI(\o_reg[27]_i_1_n_0 ),
        .CYINIT(\<const0> ),
        .DI({\<const0> ,a_IBUF[30:28]}),
        .O(p_0_in[31:28]),
        .S({\o[31]_i_2_n_0 ,\o[31]_i_3_n_0 ,\o[31]_i_4_n_0 ,\o[31]_i_5_n_0 }));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[3] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[3]),
        .Q(o_OBUF[3]),
        .R(rst_IBUF));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \o_reg[3]_i_1 
       (.CI(\<const0> ),
        .CO({\o_reg[3]_i_1_n_0 ,\NLW_o_reg[3]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(a_IBUF[3:0]),
        .O(p_0_in[3:0]),
        .S({\o[3]_i_2_n_0 ,\o[3]_i_3_n_0 ,\o[3]_i_4_n_0 ,\o[3]_i_5_n_0 }));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[4] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[4]),
        .Q(o_OBUF[4]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[5] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[5]),
        .Q(o_OBUF[5]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[6] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[6]),
        .Q(o_OBUF[6]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[7] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[7]),
        .Q(o_OBUF[7]),
        .R(rst_IBUF));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \o_reg[7]_i_1 
       (.CI(\o_reg[3]_i_1_n_0 ),
        .CO({\o_reg[7]_i_1_n_0 ,\NLW_o_reg[7]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(a_IBUF[7:4]),
        .O(p_0_in[7:4]),
        .S({\o[7]_i_2_n_0 ,\o[7]_i_3_n_0 ,\o[7]_i_4_n_0 ,\o[7]_i_5_n_0 }));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[8] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[8]),
        .Q(o_OBUF[8]),
        .R(rst_IBUF));
  FDRE #(
    .INIT(1'b0)) 
    \o_reg[9] 
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .D(p_0_in[9]),
        .Q(o_OBUF[9]),
        .R(rst_IBUF));
  IBUF rst_IBUF_inst
       (.I(rst),
        .O(rst_IBUF));
endmodule

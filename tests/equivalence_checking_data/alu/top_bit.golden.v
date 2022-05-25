// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2019.2 (lin64) Build 2708876 Wed Nov  6 21:39:14 MST 2019
// Date        : Thu May 19 11:28:25 2022
// Host        : CCL15 running 64-bit Ubuntu 20.04.4 LTS
// Command     : write_verilog -force -file /home/edvenson/bfasst/build/xilinx_yosys_impl/byu/alu/alu_impl.v
// Design      : alu
// Purpose     : This is a Verilog netlist of the current design or from a specific cell of the design. The output is an
//               IEEE 1364-2001 compliant Verilog HDL file that contains netlist information obtained from the input
//               design files.
// Device      : xc7a35tcpg236-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* ADD = "4'b0010" *) (* AND = "4'b0000" *) (* ECO_CHECKSUM = "8f4f26c" *) 
(* FALSE = "1'b0" *) (* OR = "4'b0001" *) (* SLL = "4'b1001" *) 
(* SLT = "4'b0111" *) (* SRA = "4'b1010" *) (* SRL = "4'b1000" *) 
(* SUB = "4'b0110" *) (* TRUE = "1'b1" *) (* XOR = "4'b1101" *) 
(* STRUCTURAL_NETLIST = "yes" *)
module alu
   (zero,
    alu_op,
    op1,
    op2,
    result);
  output zero;
  input [3:0]alu_op;
  input [31:0]op1;
  input [31:0]op2;
  output [31:0]result;

  wire \<const0> ;
  wire \<const1> ;
  wire [3:0]alu_op;
  wire [3:0]alu_op_IBUF;
  wire [31:0]data2;
  wire [31:0]data3;
  wire data4;
  wire [31:0]op1;
  wire [31:0]op1_IBUF;
  wire [31:0]op2;
  wire [31:0]op2_IBUF;
  wire [31:0]result;
  wire [31:0]result_OBUF;
  wire \result_OBUF[0]_inst_i_11_n_0 ;
  wire \result_OBUF[0]_inst_i_12_n_0 ;
  wire \result_OBUF[0]_inst_i_13_n_0 ;
  wire \result_OBUF[0]_inst_i_14_n_0 ;
  wire \result_OBUF[0]_inst_i_15_n_0 ;
  wire \result_OBUF[0]_inst_i_16_n_0 ;
  wire \result_OBUF[0]_inst_i_17_n_0 ;
  wire \result_OBUF[0]_inst_i_18_n_0 ;
  wire \result_OBUF[0]_inst_i_19_n_0 ;
  wire \result_OBUF[0]_inst_i_20_n_0 ;
  wire \result_OBUF[0]_inst_i_21_n_0 ;
  wire \result_OBUF[0]_inst_i_22_n_0 ;
  wire \result_OBUF[0]_inst_i_23_n_0 ;
  wire \result_OBUF[0]_inst_i_24_n_0 ;
  wire \result_OBUF[0]_inst_i_25_n_0 ;
  wire \result_OBUF[0]_inst_i_26_n_0 ;
  wire \result_OBUF[0]_inst_i_27_n_0 ;
  wire \result_OBUF[0]_inst_i_28_n_0 ;
  wire \result_OBUF[0]_inst_i_29_n_0 ;
  wire \result_OBUF[0]_inst_i_2_n_0 ;
  wire \result_OBUF[0]_inst_i_30_n_0 ;
  wire \result_OBUF[0]_inst_i_31_n_0 ;
  wire \result_OBUF[0]_inst_i_32_n_0 ;
  wire \result_OBUF[0]_inst_i_33_n_0 ;
  wire \result_OBUF[0]_inst_i_34_n_0 ;
  wire \result_OBUF[0]_inst_i_35_n_0 ;
  wire \result_OBUF[0]_inst_i_36_n_0 ;
  wire \result_OBUF[0]_inst_i_37_n_0 ;
  wire \result_OBUF[0]_inst_i_38_n_0 ;
  wire \result_OBUF[0]_inst_i_39_n_0 ;
  wire \result_OBUF[0]_inst_i_3_n_0 ;
  wire \result_OBUF[0]_inst_i_40_n_0 ;
  wire \result_OBUF[0]_inst_i_41_n_0 ;
  wire \result_OBUF[0]_inst_i_42_n_0 ;
  wire \result_OBUF[0]_inst_i_43_n_0 ;
  wire \result_OBUF[0]_inst_i_44_n_0 ;
  wire \result_OBUF[0]_inst_i_45_n_0 ;
  wire \result_OBUF[0]_inst_i_46_n_0 ;
  wire \result_OBUF[0]_inst_i_47_n_0 ;
  wire \result_OBUF[0]_inst_i_48_n_0 ;
  wire \result_OBUF[0]_inst_i_49_n_0 ;
  wire \result_OBUF[0]_inst_i_4_n_0 ;
  wire \result_OBUF[0]_inst_i_50_n_0 ;
  wire \result_OBUF[0]_inst_i_51_n_0 ;
  wire \result_OBUF[0]_inst_i_52_n_0 ;
  wire \result_OBUF[0]_inst_i_53_n_0 ;
  wire \result_OBUF[0]_inst_i_5_n_0 ;
  wire \result_OBUF[0]_inst_i_6_n_0 ;
  wire \result_OBUF[0]_inst_i_7_n_0 ;
  wire \result_OBUF[0]_inst_i_8_n_0 ;
  wire \result_OBUF[0]_inst_i_9_n_0 ;
  wire \result_OBUF[10]_inst_i_10_n_0 ;
  wire \result_OBUF[10]_inst_i_11_n_0 ;
  wire \result_OBUF[10]_inst_i_2_n_0 ;
  wire \result_OBUF[10]_inst_i_3_n_0 ;
  wire \result_OBUF[10]_inst_i_4_n_0 ;
  wire \result_OBUF[10]_inst_i_5_n_0 ;
  wire \result_OBUF[10]_inst_i_6_n_0 ;
  wire \result_OBUF[10]_inst_i_7_n_0 ;
  wire \result_OBUF[10]_inst_i_8_n_0 ;
  wire \result_OBUF[10]_inst_i_9_n_0 ;
  wire \result_OBUF[11]_inst_i_10_n_0 ;
  wire \result_OBUF[11]_inst_i_11_n_0 ;
  wire \result_OBUF[11]_inst_i_12_n_0 ;
  wire \result_OBUF[11]_inst_i_13_n_0 ;
  wire \result_OBUF[11]_inst_i_14_n_0 ;
  wire \result_OBUF[11]_inst_i_15_n_0 ;
  wire \result_OBUF[11]_inst_i_16_n_0 ;
  wire \result_OBUF[11]_inst_i_17_n_0 ;
  wire \result_OBUF[11]_inst_i_18_n_0 ;
  wire \result_OBUF[11]_inst_i_19_n_0 ;
  wire \result_OBUF[11]_inst_i_20_n_0 ;
  wire \result_OBUF[11]_inst_i_21_n_0 ;
  wire \result_OBUF[11]_inst_i_22_n_0 ;
  wire \result_OBUF[11]_inst_i_2_n_0 ;
  wire \result_OBUF[11]_inst_i_3_n_0 ;
  wire \result_OBUF[11]_inst_i_4_n_0 ;
  wire \result_OBUF[11]_inst_i_5_n_0 ;
  wire \result_OBUF[11]_inst_i_6_n_0 ;
  wire \result_OBUF[11]_inst_i_7_n_0 ;
  wire \result_OBUF[11]_inst_i_8_n_0 ;
  wire \result_OBUF[11]_inst_i_9_n_0 ;
  wire \result_OBUF[12]_inst_i_10_n_0 ;
  wire \result_OBUF[12]_inst_i_11_n_0 ;
  wire \result_OBUF[12]_inst_i_12_n_0 ;
  wire \result_OBUF[12]_inst_i_2_n_0 ;
  wire \result_OBUF[12]_inst_i_3_n_0 ;
  wire \result_OBUF[12]_inst_i_4_n_0 ;
  wire \result_OBUF[12]_inst_i_5_n_0 ;
  wire \result_OBUF[12]_inst_i_6_n_0 ;
  wire \result_OBUF[12]_inst_i_7_n_0 ;
  wire \result_OBUF[12]_inst_i_8_n_0 ;
  wire \result_OBUF[12]_inst_i_9_n_0 ;
  wire \result_OBUF[13]_inst_i_10_n_0 ;
  wire \result_OBUF[13]_inst_i_11_n_0 ;
  wire \result_OBUF[13]_inst_i_12_n_0 ;
  wire \result_OBUF[13]_inst_i_2_n_0 ;
  wire \result_OBUF[13]_inst_i_3_n_0 ;
  wire \result_OBUF[13]_inst_i_4_n_0 ;
  wire \result_OBUF[13]_inst_i_5_n_0 ;
  wire \result_OBUF[13]_inst_i_6_n_0 ;
  wire \result_OBUF[13]_inst_i_7_n_0 ;
  wire \result_OBUF[13]_inst_i_8_n_0 ;
  wire \result_OBUF[13]_inst_i_9_n_0 ;
  wire \result_OBUF[14]_inst_i_10_n_0 ;
  wire \result_OBUF[14]_inst_i_11_n_0 ;
  wire \result_OBUF[14]_inst_i_12_n_0 ;
  wire \result_OBUF[14]_inst_i_2_n_0 ;
  wire \result_OBUF[14]_inst_i_3_n_0 ;
  wire \result_OBUF[14]_inst_i_4_n_0 ;
  wire \result_OBUF[14]_inst_i_5_n_0 ;
  wire \result_OBUF[14]_inst_i_6_n_0 ;
  wire \result_OBUF[14]_inst_i_7_n_0 ;
  wire \result_OBUF[14]_inst_i_8_n_0 ;
  wire \result_OBUF[14]_inst_i_9_n_0 ;
  wire \result_OBUF[15]_inst_i_10_n_0 ;
  wire \result_OBUF[15]_inst_i_11_n_0 ;
  wire \result_OBUF[15]_inst_i_12_n_0 ;
  wire \result_OBUF[15]_inst_i_13_n_0 ;
  wire \result_OBUF[15]_inst_i_14_n_0 ;
  wire \result_OBUF[15]_inst_i_15_n_0 ;
  wire \result_OBUF[15]_inst_i_16_n_0 ;
  wire \result_OBUF[15]_inst_i_17_n_0 ;
  wire \result_OBUF[15]_inst_i_18_n_0 ;
  wire \result_OBUF[15]_inst_i_19_n_0 ;
  wire \result_OBUF[15]_inst_i_20_n_0 ;
  wire \result_OBUF[15]_inst_i_21_n_0 ;
  wire \result_OBUF[15]_inst_i_22_n_0 ;
  wire \result_OBUF[15]_inst_i_2_n_0 ;
  wire \result_OBUF[15]_inst_i_3_n_0 ;
  wire \result_OBUF[15]_inst_i_4_n_0 ;
  wire \result_OBUF[15]_inst_i_5_n_0 ;
  wire \result_OBUF[15]_inst_i_6_n_0 ;
  wire \result_OBUF[15]_inst_i_7_n_0 ;
  wire \result_OBUF[15]_inst_i_8_n_0 ;
  wire \result_OBUF[15]_inst_i_9_n_0 ;
  wire \result_OBUF[16]_inst_i_10_n_0 ;
  wire \result_OBUF[16]_inst_i_11_n_0 ;
  wire \result_OBUF[16]_inst_i_12_n_0 ;
  wire \result_OBUF[16]_inst_i_13_n_0 ;
  wire \result_OBUF[16]_inst_i_2_n_0 ;
  wire \result_OBUF[16]_inst_i_3_n_0 ;
  wire \result_OBUF[16]_inst_i_4_n_0 ;
  wire \result_OBUF[16]_inst_i_5_n_0 ;
  wire \result_OBUF[16]_inst_i_6_n_0 ;
  wire \result_OBUF[16]_inst_i_7_n_0 ;
  wire \result_OBUF[16]_inst_i_8_n_0 ;
  wire \result_OBUF[16]_inst_i_9_n_0 ;
  wire \result_OBUF[17]_inst_i_10_n_0 ;
  wire \result_OBUF[17]_inst_i_11_n_0 ;
  wire \result_OBUF[17]_inst_i_12_n_0 ;
  wire \result_OBUF[17]_inst_i_13_n_0 ;
  wire \result_OBUF[17]_inst_i_2_n_0 ;
  wire \result_OBUF[17]_inst_i_3_n_0 ;
  wire \result_OBUF[17]_inst_i_4_n_0 ;
  wire \result_OBUF[17]_inst_i_5_n_0 ;
  wire \result_OBUF[17]_inst_i_6_n_0 ;
  wire \result_OBUF[17]_inst_i_7_n_0 ;
  wire \result_OBUF[17]_inst_i_8_n_0 ;
  wire \result_OBUF[17]_inst_i_9_n_0 ;
  wire \result_OBUF[18]_inst_i_10_n_0 ;
  wire \result_OBUF[18]_inst_i_11_n_0 ;
  wire \result_OBUF[18]_inst_i_12_n_0 ;
  wire \result_OBUF[18]_inst_i_13_n_0 ;
  wire \result_OBUF[18]_inst_i_2_n_0 ;
  wire \result_OBUF[18]_inst_i_3_n_0 ;
  wire \result_OBUF[18]_inst_i_4_n_0 ;
  wire \result_OBUF[18]_inst_i_5_n_0 ;
  wire \result_OBUF[18]_inst_i_6_n_0 ;
  wire \result_OBUF[18]_inst_i_7_n_0 ;
  wire \result_OBUF[18]_inst_i_8_n_0 ;
  wire \result_OBUF[18]_inst_i_9_n_0 ;
  wire \result_OBUF[19]_inst_i_10_n_0 ;
  wire \result_OBUF[19]_inst_i_11_n_0 ;
  wire \result_OBUF[19]_inst_i_12_n_0 ;
  wire \result_OBUF[19]_inst_i_13_n_0 ;
  wire \result_OBUF[19]_inst_i_14_n_0 ;
  wire \result_OBUF[19]_inst_i_15_n_0 ;
  wire \result_OBUF[19]_inst_i_16_n_0 ;
  wire \result_OBUF[19]_inst_i_17_n_0 ;
  wire \result_OBUF[19]_inst_i_18_n_0 ;
  wire \result_OBUF[19]_inst_i_19_n_0 ;
  wire \result_OBUF[19]_inst_i_20_n_0 ;
  wire \result_OBUF[19]_inst_i_21_n_0 ;
  wire \result_OBUF[19]_inst_i_22_n_0 ;
  wire \result_OBUF[19]_inst_i_23_n_0 ;
  wire \result_OBUF[19]_inst_i_24_n_0 ;
  wire \result_OBUF[19]_inst_i_2_n_0 ;
  wire \result_OBUF[19]_inst_i_3_n_0 ;
  wire \result_OBUF[19]_inst_i_4_n_0 ;
  wire \result_OBUF[19]_inst_i_5_n_0 ;
  wire \result_OBUF[19]_inst_i_6_n_0 ;
  wire \result_OBUF[19]_inst_i_7_n_0 ;
  wire \result_OBUF[19]_inst_i_8_n_0 ;
  wire \result_OBUF[19]_inst_i_9_n_0 ;
  wire \result_OBUF[1]_inst_i_10_n_0 ;
  wire \result_OBUF[1]_inst_i_11_n_0 ;
  wire \result_OBUF[1]_inst_i_12_n_0 ;
  wire \result_OBUF[1]_inst_i_13_n_0 ;
  wire \result_OBUF[1]_inst_i_14_n_0 ;
  wire \result_OBUF[1]_inst_i_15_n_0 ;
  wire \result_OBUF[1]_inst_i_16_n_0 ;
  wire \result_OBUF[1]_inst_i_17_n_0 ;
  wire \result_OBUF[1]_inst_i_18_n_0 ;
  wire \result_OBUF[1]_inst_i_19_n_0 ;
  wire \result_OBUF[1]_inst_i_20_n_0 ;
  wire \result_OBUF[1]_inst_i_21_n_0 ;
  wire \result_OBUF[1]_inst_i_2_n_0 ;
  wire \result_OBUF[1]_inst_i_3_n_0 ;
  wire \result_OBUF[1]_inst_i_4_n_0 ;
  wire \result_OBUF[1]_inst_i_5_n_0 ;
  wire \result_OBUF[1]_inst_i_6_n_0 ;
  wire \result_OBUF[1]_inst_i_7_n_0 ;
  wire \result_OBUF[1]_inst_i_8_n_0 ;
  wire \result_OBUF[1]_inst_i_9_n_0 ;
  wire \result_OBUF[20]_inst_i_10_n_0 ;
  wire \result_OBUF[20]_inst_i_11_n_0 ;
  wire \result_OBUF[20]_inst_i_12_n_0 ;
  wire \result_OBUF[20]_inst_i_13_n_0 ;
  wire \result_OBUF[20]_inst_i_2_n_0 ;
  wire \result_OBUF[20]_inst_i_3_n_0 ;
  wire \result_OBUF[20]_inst_i_4_n_0 ;
  wire \result_OBUF[20]_inst_i_5_n_0 ;
  wire \result_OBUF[20]_inst_i_6_n_0 ;
  wire \result_OBUF[20]_inst_i_7_n_0 ;
  wire \result_OBUF[20]_inst_i_8_n_0 ;
  wire \result_OBUF[20]_inst_i_9_n_0 ;
  wire \result_OBUF[21]_inst_i_10_n_0 ;
  wire \result_OBUF[21]_inst_i_11_n_0 ;
  wire \result_OBUF[21]_inst_i_12_n_0 ;
  wire \result_OBUF[21]_inst_i_13_n_0 ;
  wire \result_OBUF[21]_inst_i_2_n_0 ;
  wire \result_OBUF[21]_inst_i_3_n_0 ;
  wire \result_OBUF[21]_inst_i_4_n_0 ;
  wire \result_OBUF[21]_inst_i_5_n_0 ;
  wire \result_OBUF[21]_inst_i_6_n_0 ;
  wire \result_OBUF[21]_inst_i_7_n_0 ;
  wire \result_OBUF[21]_inst_i_8_n_0 ;
  wire \result_OBUF[21]_inst_i_9_n_0 ;
  wire \result_OBUF[22]_inst_i_10_n_0 ;
  wire \result_OBUF[22]_inst_i_11_n_0 ;
  wire \result_OBUF[22]_inst_i_12_n_0 ;
  wire \result_OBUF[22]_inst_i_13_n_0 ;
  wire \result_OBUF[22]_inst_i_2_n_0 ;
  wire \result_OBUF[22]_inst_i_3_n_0 ;
  wire \result_OBUF[22]_inst_i_4_n_0 ;
  wire \result_OBUF[22]_inst_i_5_n_0 ;
  wire \result_OBUF[22]_inst_i_6_n_0 ;
  wire \result_OBUF[22]_inst_i_7_n_0 ;
  wire \result_OBUF[22]_inst_i_8_n_0 ;
  wire \result_OBUF[22]_inst_i_9_n_0 ;
  wire \result_OBUF[23]_inst_i_10_n_0 ;
  wire \result_OBUF[23]_inst_i_11_n_0 ;
  wire \result_OBUF[23]_inst_i_12_n_0 ;
  wire \result_OBUF[23]_inst_i_13_n_0 ;
  wire \result_OBUF[23]_inst_i_14_n_0 ;
  wire \result_OBUF[23]_inst_i_15_n_0 ;
  wire \result_OBUF[23]_inst_i_16_n_0 ;
  wire \result_OBUF[23]_inst_i_17_n_0 ;
  wire \result_OBUF[23]_inst_i_18_n_0 ;
  wire \result_OBUF[23]_inst_i_19_n_0 ;
  wire \result_OBUF[23]_inst_i_20_n_0 ;
  wire \result_OBUF[23]_inst_i_21_n_0 ;
  wire \result_OBUF[23]_inst_i_22_n_0 ;
  wire \result_OBUF[23]_inst_i_2_n_0 ;
  wire \result_OBUF[23]_inst_i_3_n_0 ;
  wire \result_OBUF[23]_inst_i_4_n_0 ;
  wire \result_OBUF[23]_inst_i_5_n_0 ;
  wire \result_OBUF[23]_inst_i_6_n_0 ;
  wire \result_OBUF[23]_inst_i_7_n_0 ;
  wire \result_OBUF[23]_inst_i_8_n_0 ;
  wire \result_OBUF[23]_inst_i_9_n_0 ;
  wire \result_OBUF[24]_inst_i_10_n_0 ;
  wire \result_OBUF[24]_inst_i_11_n_0 ;
  wire \result_OBUF[24]_inst_i_12_n_0 ;
  wire \result_OBUF[24]_inst_i_2_n_0 ;
  wire \result_OBUF[24]_inst_i_3_n_0 ;
  wire \result_OBUF[24]_inst_i_4_n_0 ;
  wire \result_OBUF[24]_inst_i_5_n_0 ;
  wire \result_OBUF[24]_inst_i_6_n_0 ;
  wire \result_OBUF[24]_inst_i_7_n_0 ;
  wire \result_OBUF[24]_inst_i_8_n_0 ;
  wire \result_OBUF[24]_inst_i_9_n_0 ;
  wire \result_OBUF[25]_inst_i_10_n_0 ;
  wire \result_OBUF[25]_inst_i_11_n_0 ;
  wire \result_OBUF[25]_inst_i_12_n_0 ;
  wire \result_OBUF[25]_inst_i_2_n_0 ;
  wire \result_OBUF[25]_inst_i_3_n_0 ;
  wire \result_OBUF[25]_inst_i_4_n_0 ;
  wire \result_OBUF[25]_inst_i_5_n_0 ;
  wire \result_OBUF[25]_inst_i_6_n_0 ;
  wire \result_OBUF[25]_inst_i_7_n_0 ;
  wire \result_OBUF[25]_inst_i_8_n_0 ;
  wire \result_OBUF[25]_inst_i_9_n_0 ;
  wire \result_OBUF[26]_inst_i_10_n_0 ;
  wire \result_OBUF[26]_inst_i_11_n_0 ;
  wire \result_OBUF[26]_inst_i_2_n_0 ;
  wire \result_OBUF[26]_inst_i_3_n_0 ;
  wire \result_OBUF[26]_inst_i_4_n_0 ;
  wire \result_OBUF[26]_inst_i_5_n_0 ;
  wire \result_OBUF[26]_inst_i_6_n_0 ;
  wire \result_OBUF[26]_inst_i_7_n_0 ;
  wire \result_OBUF[26]_inst_i_8_n_0 ;
  wire \result_OBUF[26]_inst_i_9_n_0 ;
  wire \result_OBUF[27]_inst_i_10_n_0 ;
  wire \result_OBUF[27]_inst_i_11_n_0 ;
  wire \result_OBUF[27]_inst_i_12_n_0 ;
  wire \result_OBUF[27]_inst_i_13_n_0 ;
  wire \result_OBUF[27]_inst_i_14_n_0 ;
  wire \result_OBUF[27]_inst_i_15_n_0 ;
  wire \result_OBUF[27]_inst_i_16_n_0 ;
  wire \result_OBUF[27]_inst_i_17_n_0 ;
  wire \result_OBUF[27]_inst_i_2_n_0 ;
  wire \result_OBUF[27]_inst_i_3_n_0 ;
  wire \result_OBUF[27]_inst_i_4_n_0 ;
  wire \result_OBUF[27]_inst_i_5_n_0 ;
  wire \result_OBUF[27]_inst_i_6_n_0 ;
  wire \result_OBUF[27]_inst_i_7_n_0 ;
  wire \result_OBUF[27]_inst_i_8_n_0 ;
  wire \result_OBUF[27]_inst_i_9_n_0 ;
  wire \result_OBUF[28]_inst_i_10_n_0 ;
  wire \result_OBUF[28]_inst_i_11_n_0 ;
  wire \result_OBUF[28]_inst_i_12_n_0 ;
  wire \result_OBUF[28]_inst_i_13_n_0 ;
  wire \result_OBUF[28]_inst_i_14_n_0 ;
  wire \result_OBUF[28]_inst_i_2_n_0 ;
  wire \result_OBUF[28]_inst_i_3_n_0 ;
  wire \result_OBUF[28]_inst_i_4_n_0 ;
  wire \result_OBUF[28]_inst_i_5_n_0 ;
  wire \result_OBUF[28]_inst_i_6_n_0 ;
  wire \result_OBUF[28]_inst_i_7_n_0 ;
  wire \result_OBUF[28]_inst_i_8_n_0 ;
  wire \result_OBUF[28]_inst_i_9_n_0 ;
  wire \result_OBUF[29]_inst_i_10_n_0 ;
  wire \result_OBUF[29]_inst_i_11_n_0 ;
  wire \result_OBUF[29]_inst_i_2_n_0 ;
  wire \result_OBUF[29]_inst_i_3_n_0 ;
  wire \result_OBUF[29]_inst_i_4_n_0 ;
  wire \result_OBUF[29]_inst_i_5_n_0 ;
  wire \result_OBUF[29]_inst_i_6_n_0 ;
  wire \result_OBUF[29]_inst_i_7_n_0 ;
  wire \result_OBUF[29]_inst_i_8_n_0 ;
  wire \result_OBUF[29]_inst_i_9_n_0 ;
  wire \result_OBUF[2]_inst_i_2_n_0 ;
  wire \result_OBUF[2]_inst_i_3_n_0 ;
  wire \result_OBUF[2]_inst_i_4_n_0 ;
  wire \result_OBUF[2]_inst_i_5_n_0 ;
  wire \result_OBUF[2]_inst_i_6_n_0 ;
  wire \result_OBUF[2]_inst_i_7_n_0 ;
  wire \result_OBUF[2]_inst_i_8_n_0 ;
  wire \result_OBUF[30]_inst_i_10_n_0 ;
  wire \result_OBUF[30]_inst_i_11_n_0 ;
  wire \result_OBUF[30]_inst_i_12_n_0 ;
  wire \result_OBUF[30]_inst_i_13_n_0 ;
  wire \result_OBUF[30]_inst_i_14_n_0 ;
  wire \result_OBUF[30]_inst_i_15_n_0 ;
  wire \result_OBUF[30]_inst_i_16_n_0 ;
  wire \result_OBUF[30]_inst_i_17_n_0 ;
  wire \result_OBUF[30]_inst_i_18_n_0 ;
  wire \result_OBUF[30]_inst_i_19_n_0 ;
  wire \result_OBUF[30]_inst_i_20_n_0 ;
  wire \result_OBUF[30]_inst_i_21_n_0 ;
  wire \result_OBUF[30]_inst_i_22_n_0 ;
  wire \result_OBUF[30]_inst_i_23_n_0 ;
  wire \result_OBUF[30]_inst_i_24_n_0 ;
  wire \result_OBUF[30]_inst_i_25_n_0 ;
  wire \result_OBUF[30]_inst_i_26_n_0 ;
  wire \result_OBUF[30]_inst_i_27_n_0 ;
  wire \result_OBUF[30]_inst_i_28_n_0 ;
  wire \result_OBUF[30]_inst_i_29_n_0 ;
  wire \result_OBUF[30]_inst_i_2_n_0 ;
  wire \result_OBUF[30]_inst_i_30_n_0 ;
  wire \result_OBUF[30]_inst_i_31_n_0 ;
  wire \result_OBUF[30]_inst_i_32_n_0 ;
  wire \result_OBUF[30]_inst_i_33_n_0 ;
  wire \result_OBUF[30]_inst_i_34_n_0 ;
  wire \result_OBUF[30]_inst_i_4_n_0 ;
  wire \result_OBUF[30]_inst_i_5_n_0 ;
  wire \result_OBUF[30]_inst_i_6_n_0 ;
  wire \result_OBUF[30]_inst_i_7_n_0 ;
  wire \result_OBUF[30]_inst_i_8_n_0 ;
  wire \result_OBUF[30]_inst_i_9_n_0 ;
  wire \result_OBUF[31]_inst_i_10_n_0 ;
  wire \result_OBUF[31]_inst_i_11_n_0 ;
  wire \result_OBUF[31]_inst_i_12_n_0 ;
  wire \result_OBUF[31]_inst_i_13_n_0 ;
  wire \result_OBUF[31]_inst_i_14_n_0 ;
  wire \result_OBUF[31]_inst_i_2_n_0 ;
  wire \result_OBUF[31]_inst_i_3_n_0 ;
  wire \result_OBUF[31]_inst_i_4_n_0 ;
  wire \result_OBUF[31]_inst_i_6_n_0 ;
  wire \result_OBUF[31]_inst_i_7_n_0 ;
  wire \result_OBUF[31]_inst_i_8_n_0 ;
  wire \result_OBUF[31]_inst_i_9_n_0 ;
  wire \result_OBUF[3]_inst_i_10_n_0 ;
  wire \result_OBUF[3]_inst_i_11_n_0 ;
  wire \result_OBUF[3]_inst_i_12_n_0 ;
  wire \result_OBUF[3]_inst_i_13_n_0 ;
  wire \result_OBUF[3]_inst_i_14_n_0 ;
  wire \result_OBUF[3]_inst_i_2_n_0 ;
  wire \result_OBUF[3]_inst_i_3_n_0 ;
  wire \result_OBUF[3]_inst_i_4_n_0 ;
  wire \result_OBUF[3]_inst_i_5_n_0 ;
  wire \result_OBUF[3]_inst_i_6_n_0 ;
  wire \result_OBUF[3]_inst_i_7_n_0 ;
  wire \result_OBUF[3]_inst_i_8_n_0 ;
  wire \result_OBUF[3]_inst_i_9_n_0 ;
  wire \result_OBUF[4]_inst_i_2_n_0 ;
  wire \result_OBUF[4]_inst_i_3_n_0 ;
  wire \result_OBUF[4]_inst_i_4_n_0 ;
  wire \result_OBUF[4]_inst_i_5_n_0 ;
  wire \result_OBUF[4]_inst_i_6_n_0 ;
  wire \result_OBUF[4]_inst_i_7_n_0 ;
  wire \result_OBUF[4]_inst_i_8_n_0 ;
  wire \result_OBUF[4]_inst_i_9_n_0 ;
  wire \result_OBUF[5]_inst_i_2_n_0 ;
  wire \result_OBUF[5]_inst_i_3_n_0 ;
  wire \result_OBUF[5]_inst_i_4_n_0 ;
  wire \result_OBUF[5]_inst_i_5_n_0 ;
  wire \result_OBUF[5]_inst_i_6_n_0 ;
  wire \result_OBUF[5]_inst_i_7_n_0 ;
  wire \result_OBUF[5]_inst_i_8_n_0 ;
  wire \result_OBUF[5]_inst_i_9_n_0 ;
  wire \result_OBUF[6]_inst_i_2_n_0 ;
  wire \result_OBUF[6]_inst_i_3_n_0 ;
  wire \result_OBUF[6]_inst_i_4_n_0 ;
  wire \result_OBUF[6]_inst_i_5_n_0 ;
  wire \result_OBUF[6]_inst_i_6_n_0 ;
  wire \result_OBUF[6]_inst_i_7_n_0 ;
  wire \result_OBUF[6]_inst_i_8_n_0 ;
  wire \result_OBUF[6]_inst_i_9_n_0 ;
  wire \result_OBUF[7]_inst_i_10_n_0 ;
  wire \result_OBUF[7]_inst_i_11_n_0 ;
  wire \result_OBUF[7]_inst_i_12_n_0 ;
  wire \result_OBUF[7]_inst_i_13_n_0 ;
  wire \result_OBUF[7]_inst_i_14_n_0 ;
  wire \result_OBUF[7]_inst_i_15_n_0 ;
  wire \result_OBUF[7]_inst_i_16_n_0 ;
  wire \result_OBUF[7]_inst_i_17_n_0 ;
  wire \result_OBUF[7]_inst_i_18_n_0 ;
  wire \result_OBUF[7]_inst_i_19_n_0 ;
  wire \result_OBUF[7]_inst_i_20_n_0 ;
  wire \result_OBUF[7]_inst_i_2_n_0 ;
  wire \result_OBUF[7]_inst_i_3_n_0 ;
  wire \result_OBUF[7]_inst_i_4_n_0 ;
  wire \result_OBUF[7]_inst_i_5_n_0 ;
  wire \result_OBUF[7]_inst_i_6_n_0 ;
  wire \result_OBUF[7]_inst_i_7_n_0 ;
  wire \result_OBUF[7]_inst_i_8_n_0 ;
  wire \result_OBUF[7]_inst_i_9_n_0 ;
  wire \result_OBUF[8]_inst_i_10_n_0 ;
  wire \result_OBUF[8]_inst_i_11_n_0 ;
  wire \result_OBUF[8]_inst_i_2_n_0 ;
  wire \result_OBUF[8]_inst_i_3_n_0 ;
  wire \result_OBUF[8]_inst_i_4_n_0 ;
  wire \result_OBUF[8]_inst_i_5_n_0 ;
  wire \result_OBUF[8]_inst_i_6_n_0 ;
  wire \result_OBUF[8]_inst_i_7_n_0 ;
  wire \result_OBUF[8]_inst_i_8_n_0 ;
  wire \result_OBUF[8]_inst_i_9_n_0 ;
  wire \result_OBUF[9]_inst_i_10_n_0 ;
  wire \result_OBUF[9]_inst_i_11_n_0 ;
  wire \result_OBUF[9]_inst_i_2_n_0 ;
  wire \result_OBUF[9]_inst_i_3_n_0 ;
  wire \result_OBUF[9]_inst_i_4_n_0 ;
  wire \result_OBUF[9]_inst_i_5_n_0 ;
  wire \result_OBUF[9]_inst_i_6_n_0 ;
  wire \result_OBUF[9]_inst_i_7_n_0 ;
  wire \result_OBUF[9]_inst_i_8_n_0 ;
  wire \result_OBUF[9]_inst_i_9_n_0 ;
  wire zero;
  wire zero_OBUF;
  wire zero_OBUF_inst_i_10_n_0;
  wire zero_OBUF_inst_i_11_n_0;
  wire zero_OBUF_inst_i_12_n_0;
  wire zero_OBUF_inst_i_13_n_0;
  wire zero_OBUF_inst_i_14_n_0;
  wire zero_OBUF_inst_i_15_n_0;
  wire zero_OBUF_inst_i_16_n_0;
  wire zero_OBUF_inst_i_17_n_0;
  wire zero_OBUF_inst_i_18_n_0;
  wire zero_OBUF_inst_i_19_n_0;
  wire zero_OBUF_inst_i_20_n_0;
  wire zero_OBUF_inst_i_21_n_0;
  wire zero_OBUF_inst_i_22_n_0;
  wire zero_OBUF_inst_i_23_n_0;
  wire zero_OBUF_inst_i_24_n_0;
  wire zero_OBUF_inst_i_25_n_0;
  wire zero_OBUF_inst_i_26_n_0;
  wire zero_OBUF_inst_i_27_n_0;
  wire zero_OBUF_inst_i_28_n_0;
  wire zero_OBUF_inst_i_29_n_0;
  wire zero_OBUF_inst_i_2_n_0;
  wire zero_OBUF_inst_i_30_n_0;
  wire zero_OBUF_inst_i_31_n_0;
  wire zero_OBUF_inst_i_32_n_0;
  wire zero_OBUF_inst_i_33_n_0;
  wire zero_OBUF_inst_i_34_n_0;
  wire zero_OBUF_inst_i_35_n_0;
  wire zero_OBUF_inst_i_36_n_0;
  wire zero_OBUF_inst_i_37_n_0;
  wire zero_OBUF_inst_i_38_n_0;
  wire zero_OBUF_inst_i_39_n_0;
  wire zero_OBUF_inst_i_3_n_0;
  wire zero_OBUF_inst_i_40_n_0;
  wire zero_OBUF_inst_i_41_n_0;
  wire zero_OBUF_inst_i_42_n_0;
  wire zero_OBUF_inst_i_43_n_0;
  wire zero_OBUF_inst_i_44_n_0;
  wire zero_OBUF_inst_i_45_n_0;
  wire zero_OBUF_inst_i_46_n_0;
  wire zero_OBUF_inst_i_47_n_0;
  wire zero_OBUF_inst_i_48_n_0;
  wire zero_OBUF_inst_i_49_n_0;
  wire zero_OBUF_inst_i_4_n_0;
  wire zero_OBUF_inst_i_50_n_0;
  wire zero_OBUF_inst_i_51_n_0;
  wire zero_OBUF_inst_i_52_n_0;
  wire zero_OBUF_inst_i_53_n_0;
  wire zero_OBUF_inst_i_54_n_0;
  wire zero_OBUF_inst_i_55_n_0;
  wire zero_OBUF_inst_i_56_n_0;
  wire zero_OBUF_inst_i_57_n_0;
  wire zero_OBUF_inst_i_58_n_0;
  wire zero_OBUF_inst_i_59_n_0;
  wire zero_OBUF_inst_i_5_n_0;
  wire zero_OBUF_inst_i_60_n_0;
  wire zero_OBUF_inst_i_61_n_0;
  wire zero_OBUF_inst_i_6_n_0;
  wire zero_OBUF_inst_i_7_n_0;
  wire zero_OBUF_inst_i_8_n_0;
  wire zero_OBUF_inst_i_9_n_0;
  wire [3:0]\NLW_result_OBUF[0]_inst_i_10_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[0]_inst_i_19_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[0]_inst_i_28_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[0]_inst_i_37_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[11]_inst_i_5_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[11]_inst_i_6_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[15]_inst_i_5_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[15]_inst_i_6_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[19]_inst_i_5_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[19]_inst_i_6_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[1]_inst_i_3_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[23]_inst_i_5_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[23]_inst_i_6_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[27]_inst_i_5_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[30]_inst_i_10_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[3]_inst_i_5_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[7]_inst_i_5_CO_UNCONNECTED ;
  wire [3:0]\NLW_result_OBUF[7]_inst_i_6_CO_UNCONNECTED ;

  GND GND
       (.G(\<const0> ));
  VCC VCC
       (.P(\<const1> ));
  IBUF \alu_op_IBUF[0]_inst 
       (.I(alu_op[0]),
        .O(alu_op_IBUF[0]));
  IBUF \alu_op_IBUF[1]_inst 
       (.I(alu_op[1]),
        .O(alu_op_IBUF[1]));
  IBUF \alu_op_IBUF[2]_inst 
       (.I(alu_op[2]),
        .O(alu_op_IBUF[2]));
  IBUF \alu_op_IBUF[3]_inst 
       (.I(alu_op[3]),
        .O(alu_op_IBUF[3]));
  IBUF \op1_IBUF[0]_inst 
       (.I(op1[0]),
        .O(op1_IBUF[0]));
  IBUF \op1_IBUF[10]_inst 
       (.I(op1[10]),
        .O(op1_IBUF[10]));
  IBUF \op1_IBUF[11]_inst 
       (.I(op1[11]),
        .O(op1_IBUF[11]));
  IBUF \op1_IBUF[12]_inst 
       (.I(op1[12]),
        .O(op1_IBUF[12]));
  IBUF \op1_IBUF[13]_inst 
       (.I(op1[13]),
        .O(op1_IBUF[13]));
  IBUF \op1_IBUF[14]_inst 
       (.I(op1[14]),
        .O(op1_IBUF[14]));
  IBUF \op1_IBUF[15]_inst 
       (.I(op1[15]),
        .O(op1_IBUF[15]));
  IBUF \op1_IBUF[16]_inst 
       (.I(op1[16]),
        .O(op1_IBUF[16]));
  IBUF \op1_IBUF[17]_inst 
       (.I(op1[17]),
        .O(op1_IBUF[17]));
  IBUF \op1_IBUF[18]_inst 
       (.I(op1[18]),
        .O(op1_IBUF[18]));
  IBUF \op1_IBUF[19]_inst 
       (.I(op1[19]),
        .O(op1_IBUF[19]));
  IBUF \op1_IBUF[1]_inst 
       (.I(op1[1]),
        .O(op1_IBUF[1]));
  IBUF \op1_IBUF[20]_inst 
       (.I(op1[20]),
        .O(op1_IBUF[20]));
  IBUF \op1_IBUF[21]_inst 
       (.I(op1[21]),
        .O(op1_IBUF[21]));
  IBUF \op1_IBUF[22]_inst 
       (.I(op1[22]),
        .O(op1_IBUF[22]));
  IBUF \op1_IBUF[23]_inst 
       (.I(op1[23]),
        .O(op1_IBUF[23]));
  IBUF \op1_IBUF[24]_inst 
       (.I(op1[24]),
        .O(op1_IBUF[24]));
  IBUF \op1_IBUF[25]_inst 
       (.I(op1[25]),
        .O(op1_IBUF[25]));
  IBUF \op1_IBUF[26]_inst 
       (.I(op1[26]),
        .O(op1_IBUF[26]));
  IBUF \op1_IBUF[27]_inst 
       (.I(op1[27]),
        .O(op1_IBUF[27]));
  IBUF \op1_IBUF[28]_inst 
       (.I(op1[28]),
        .O(op1_IBUF[28]));
  IBUF \op1_IBUF[29]_inst 
       (.I(op1[29]),
        .O(op1_IBUF[29]));
  IBUF \op1_IBUF[2]_inst 
       (.I(op1[2]),
        .O(op1_IBUF[2]));
  IBUF \op1_IBUF[30]_inst 
       (.I(op1[30]),
        .O(op1_IBUF[30]));
  IBUF \op1_IBUF[31]_inst 
       (.I(op1[31]),
        .O(op1_IBUF[31]));
  IBUF \op1_IBUF[3]_inst 
       (.I(op1[3]),
        .O(op1_IBUF[3]));
  IBUF \op1_IBUF[4]_inst 
       (.I(op1[4]),
        .O(op1_IBUF[4]));
  IBUF \op1_IBUF[5]_inst 
       (.I(op1[5]),
        .O(op1_IBUF[5]));
  IBUF \op1_IBUF[6]_inst 
       (.I(op1[6]),
        .O(op1_IBUF[6]));
  IBUF \op1_IBUF[7]_inst 
       (.I(op1[7]),
        .O(op1_IBUF[7]));
  IBUF \op1_IBUF[8]_inst 
       (.I(op1[8]),
        .O(op1_IBUF[8]));
  IBUF \op1_IBUF[9]_inst 
       (.I(op1[9]),
        .O(op1_IBUF[9]));
  IBUF \op2_IBUF[0]_inst 
       (.I(op2[0]),
        .O(op2_IBUF[0]));
  IBUF \op2_IBUF[10]_inst 
       (.I(op2[10]),
        .O(op2_IBUF[10]));
  IBUF \op2_IBUF[11]_inst 
       (.I(op2[11]),
        .O(op2_IBUF[11]));
  IBUF \op2_IBUF[12]_inst 
       (.I(op2[12]),
        .O(op2_IBUF[12]));
  IBUF \op2_IBUF[13]_inst 
       (.I(op2[13]),
        .O(op2_IBUF[13]));
  IBUF \op2_IBUF[14]_inst 
       (.I(op2[14]),
        .O(op2_IBUF[14]));
  IBUF \op2_IBUF[15]_inst 
       (.I(op2[15]),
        .O(op2_IBUF[15]));
  IBUF \op2_IBUF[16]_inst 
       (.I(op2[16]),
        .O(op2_IBUF[16]));
  IBUF \op2_IBUF[17]_inst 
       (.I(op2[17]),
        .O(op2_IBUF[17]));
  IBUF \op2_IBUF[18]_inst 
       (.I(op2[18]),
        .O(op2_IBUF[18]));
  IBUF \op2_IBUF[19]_inst 
       (.I(op2[19]),
        .O(op2_IBUF[19]));
  IBUF \op2_IBUF[1]_inst 
       (.I(op2[1]),
        .O(op2_IBUF[1]));
  IBUF \op2_IBUF[20]_inst 
       (.I(op2[20]),
        .O(op2_IBUF[20]));
  IBUF \op2_IBUF[21]_inst 
       (.I(op2[21]),
        .O(op2_IBUF[21]));
  IBUF \op2_IBUF[22]_inst 
       (.I(op2[22]),
        .O(op2_IBUF[22]));
  IBUF \op2_IBUF[23]_inst 
       (.I(op2[23]),
        .O(op2_IBUF[23]));
  IBUF \op2_IBUF[24]_inst 
       (.I(op2[24]),
        .O(op2_IBUF[24]));
  IBUF \op2_IBUF[25]_inst 
       (.I(op2[25]),
        .O(op2_IBUF[25]));
  IBUF \op2_IBUF[26]_inst 
       (.I(op2[26]),
        .O(op2_IBUF[26]));
  IBUF \op2_IBUF[27]_inst 
       (.I(op2[27]),
        .O(op2_IBUF[27]));
  IBUF \op2_IBUF[28]_inst 
       (.I(op2[28]),
        .O(op2_IBUF[28]));
  IBUF \op2_IBUF[29]_inst 
       (.I(op2[29]),
        .O(op2_IBUF[29]));
  IBUF \op2_IBUF[2]_inst 
       (.I(op2[2]),
        .O(op2_IBUF[2]));
  IBUF \op2_IBUF[30]_inst 
       (.I(op2[30]),
        .O(op2_IBUF[30]));
  IBUF \op2_IBUF[31]_inst 
       (.I(op2[31]),
        .O(op2_IBUF[31]));
  IBUF \op2_IBUF[3]_inst 
       (.I(op2[3]),
        .O(op2_IBUF[3]));
  IBUF \op2_IBUF[4]_inst 
       (.I(op2[4]),
        .O(op2_IBUF[4]));
  IBUF \op2_IBUF[5]_inst 
       (.I(op2[5]),
        .O(op2_IBUF[5]));
  IBUF \op2_IBUF[6]_inst 
       (.I(op2[6]),
        .O(op2_IBUF[6]));
  IBUF \op2_IBUF[7]_inst 
       (.I(op2[7]),
        .O(op2_IBUF[7]));
  IBUF \op2_IBUF[8]_inst 
       (.I(op2[8]),
        .O(op2_IBUF[8]));
  IBUF \op2_IBUF[9]_inst 
       (.I(op2[9]),
        .O(op2_IBUF[9]));
  OBUF \result_OBUF[0]_inst 
       (.I(result_OBUF[0]),
        .O(result[0]));
  LUT6 #(
    .INIT(64'hFF00EEEEF0F0EEEE)) 
    \result_OBUF[0]_inst_i_1 
       (.I0(\result_OBUF[0]_inst_i_2_n_0 ),
        .I1(\result_OBUF[0]_inst_i_3_n_0 ),
        .I2(\result_OBUF[0]_inst_i_4_n_0 ),
        .I3(\result_OBUF[0]_inst_i_5_n_0 ),
        .I4(alu_op_IBUF[2]),
        .I5(alu_op_IBUF[3]),
        .O(result_OBUF[0]));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[0]_inst_i_10 
       (.CI(\result_OBUF[0]_inst_i_19_n_0 ),
        .CO({data4,\NLW_result_OBUF[0]_inst_i_10_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI({\result_OBUF[0]_inst_i_20_n_0 ,\result_OBUF[0]_inst_i_21_n_0 ,\result_OBUF[0]_inst_i_22_n_0 ,\result_OBUF[0]_inst_i_23_n_0 }),
        .S({\result_OBUF[0]_inst_i_24_n_0 ,\result_OBUF[0]_inst_i_25_n_0 ,\result_OBUF[0]_inst_i_26_n_0 ,\result_OBUF[0]_inst_i_27_n_0 }));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[0]_inst_i_11 
       (.I0(op1_IBUF[1]),
        .I1(op1_IBUF[17]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[25]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[9]),
        .O(\result_OBUF[0]_inst_i_11_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[0]_inst_i_12 
       (.I0(op1_IBUF[5]),
        .I1(op1_IBUF[21]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[29]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[13]),
        .O(\result_OBUF[0]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hFCFC0C0CFA0AFA0A)) 
    \result_OBUF[0]_inst_i_13 
       (.I0(op1_IBUF[7]),
        .I1(op1_IBUF[23]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[15]),
        .I4(op1_IBUF[31]),
        .I5(op2_IBUF[4]),
        .O(\result_OBUF[0]_inst_i_13_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[0]_inst_i_14 
       (.I0(op1_IBUF[3]),
        .I1(op1_IBUF[19]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[27]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[11]),
        .O(\result_OBUF[0]_inst_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \result_OBUF[0]_inst_i_15 
       (.I0(alu_op_IBUF[0]),
        .I1(op2_IBUF[0]),
        .O(\result_OBUF[0]_inst_i_15_n_0 ));
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[0]_inst_i_16 
       (.I0(\result_OBUF[1]_inst_i_20_n_0 ),
        .I1(op2_IBUF[2]),
        .I2(\result_OBUF[1]_inst_i_21_n_0 ),
        .O(\result_OBUF[0]_inst_i_16_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[0]_inst_i_17 
       (.I0(op1_IBUF[0]),
        .I1(op1_IBUF[16]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[24]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[8]),
        .O(\result_OBUF[0]_inst_i_17_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair27" *) 
  LUT3 #(
    .INIT(8'h10)) 
    \result_OBUF[0]_inst_i_18 
       (.I0(op2_IBUF[3]),
        .I1(op2_IBUF[4]),
        .I2(op1_IBUF[0]),
        .O(\result_OBUF[0]_inst_i_18_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[0]_inst_i_19 
       (.CI(\result_OBUF[0]_inst_i_28_n_0 ),
        .CO({\result_OBUF[0]_inst_i_19_n_0 ,\NLW_result_OBUF[0]_inst_i_19_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI({\result_OBUF[0]_inst_i_29_n_0 ,\result_OBUF[0]_inst_i_30_n_0 ,\result_OBUF[0]_inst_i_31_n_0 ,\result_OBUF[0]_inst_i_32_n_0 }),
        .S({\result_OBUF[0]_inst_i_33_n_0 ,\result_OBUF[0]_inst_i_34_n_0 ,\result_OBUF[0]_inst_i_35_n_0 ,\result_OBUF[0]_inst_i_36_n_0 }));
  LUT6 #(
    .INIT(64'h8888888888888000)) 
    \result_OBUF[0]_inst_i_2 
       (.I0(\result_OBUF[30]_inst_i_4_n_0 ),
        .I1(\result_OBUF[30]_inst_i_9_n_0 ),
        .I2(\result_OBUF[0]_inst_i_6_n_0 ),
        .I3(\result_OBUF[0]_inst_i_7_n_0 ),
        .I4(\result_OBUF[0]_inst_i_8_n_0 ),
        .I5(\result_OBUF[0]_inst_i_9_n_0 ),
        .O(\result_OBUF[0]_inst_i_2_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_20 
       (.I0(op2_IBUF[30]),
        .I1(op1_IBUF[30]),
        .I2(op2_IBUF[31]),
        .I3(op1_IBUF[31]),
        .O(\result_OBUF[0]_inst_i_20_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_21 
       (.I0(op2_IBUF[28]),
        .I1(op1_IBUF[28]),
        .I2(op1_IBUF[29]),
        .I3(op2_IBUF[29]),
        .O(\result_OBUF[0]_inst_i_21_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_22 
       (.I0(op2_IBUF[26]),
        .I1(op1_IBUF[26]),
        .I2(op1_IBUF[27]),
        .I3(op2_IBUF[27]),
        .O(\result_OBUF[0]_inst_i_22_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_23 
       (.I0(op2_IBUF[24]),
        .I1(op1_IBUF[24]),
        .I2(op1_IBUF[25]),
        .I3(op2_IBUF[25]),
        .O(\result_OBUF[0]_inst_i_23_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_24 
       (.I0(op2_IBUF[30]),
        .I1(op1_IBUF[30]),
        .I2(op1_IBUF[31]),
        .I3(op2_IBUF[31]),
        .O(\result_OBUF[0]_inst_i_24_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_25 
       (.I0(op2_IBUF[28]),
        .I1(op1_IBUF[28]),
        .I2(op1_IBUF[29]),
        .I3(op2_IBUF[29]),
        .O(\result_OBUF[0]_inst_i_25_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_26 
       (.I0(op2_IBUF[26]),
        .I1(op1_IBUF[26]),
        .I2(op1_IBUF[27]),
        .I3(op2_IBUF[27]),
        .O(\result_OBUF[0]_inst_i_26_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_27 
       (.I0(op2_IBUF[24]),
        .I1(op1_IBUF[24]),
        .I2(op1_IBUF[25]),
        .I3(op2_IBUF[25]),
        .O(\result_OBUF[0]_inst_i_27_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[0]_inst_i_28 
       (.CI(\result_OBUF[0]_inst_i_37_n_0 ),
        .CO({\result_OBUF[0]_inst_i_28_n_0 ,\NLW_result_OBUF[0]_inst_i_28_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI({\result_OBUF[0]_inst_i_38_n_0 ,\result_OBUF[0]_inst_i_39_n_0 ,\result_OBUF[0]_inst_i_40_n_0 ,\result_OBUF[0]_inst_i_41_n_0 }),
        .S({\result_OBUF[0]_inst_i_42_n_0 ,\result_OBUF[0]_inst_i_43_n_0 ,\result_OBUF[0]_inst_i_44_n_0 ,\result_OBUF[0]_inst_i_45_n_0 }));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_29 
       (.I0(op2_IBUF[22]),
        .I1(op1_IBUF[22]),
        .I2(op1_IBUF[23]),
        .I3(op2_IBUF[23]),
        .O(\result_OBUF[0]_inst_i_29_n_0 ));
  LUT6 #(
    .INIT(64'h2323232023202020)) 
    \result_OBUF[0]_inst_i_3 
       (.I0(data2[0]),
        .I1(alu_op_IBUF[3]),
        .I2(alu_op_IBUF[1]),
        .I3(alu_op_IBUF[0]),
        .I4(op1_IBUF[0]),
        .I5(op2_IBUF[0]),
        .O(\result_OBUF[0]_inst_i_3_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_30 
       (.I0(op2_IBUF[20]),
        .I1(op1_IBUF[20]),
        .I2(op1_IBUF[21]),
        .I3(op2_IBUF[21]),
        .O(\result_OBUF[0]_inst_i_30_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_31 
       (.I0(op2_IBUF[18]),
        .I1(op1_IBUF[18]),
        .I2(op1_IBUF[19]),
        .I3(op2_IBUF[19]),
        .O(\result_OBUF[0]_inst_i_31_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_32 
       (.I0(op2_IBUF[16]),
        .I1(op1_IBUF[16]),
        .I2(op1_IBUF[17]),
        .I3(op2_IBUF[17]),
        .O(\result_OBUF[0]_inst_i_32_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_33 
       (.I0(op2_IBUF[22]),
        .I1(op1_IBUF[22]),
        .I2(op1_IBUF[23]),
        .I3(op2_IBUF[23]),
        .O(\result_OBUF[0]_inst_i_33_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_34 
       (.I0(op2_IBUF[20]),
        .I1(op1_IBUF[20]),
        .I2(op1_IBUF[21]),
        .I3(op2_IBUF[21]),
        .O(\result_OBUF[0]_inst_i_34_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_35 
       (.I0(op2_IBUF[18]),
        .I1(op1_IBUF[18]),
        .I2(op1_IBUF[19]),
        .I3(op2_IBUF[19]),
        .O(\result_OBUF[0]_inst_i_35_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_36 
       (.I0(op2_IBUF[16]),
        .I1(op1_IBUF[16]),
        .I2(op1_IBUF[17]),
        .I3(op2_IBUF[17]),
        .O(\result_OBUF[0]_inst_i_36_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[0]_inst_i_37 
       (.CI(\<const0> ),
        .CO({\result_OBUF[0]_inst_i_37_n_0 ,\NLW_result_OBUF[0]_inst_i_37_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI({\result_OBUF[0]_inst_i_46_n_0 ,\result_OBUF[0]_inst_i_47_n_0 ,\result_OBUF[0]_inst_i_48_n_0 ,\result_OBUF[0]_inst_i_49_n_0 }),
        .S({\result_OBUF[0]_inst_i_50_n_0 ,\result_OBUF[0]_inst_i_51_n_0 ,\result_OBUF[0]_inst_i_52_n_0 ,\result_OBUF[0]_inst_i_53_n_0 }));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_38 
       (.I0(op2_IBUF[14]),
        .I1(op1_IBUF[14]),
        .I2(op1_IBUF[15]),
        .I3(op2_IBUF[15]),
        .O(\result_OBUF[0]_inst_i_38_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_39 
       (.I0(op2_IBUF[12]),
        .I1(op1_IBUF[12]),
        .I2(op1_IBUF[13]),
        .I3(op2_IBUF[13]),
        .O(\result_OBUF[0]_inst_i_39_n_0 ));
  LUT5 #(
    .INIT(32'hFA0ACACA)) 
    \result_OBUF[0]_inst_i_4 
       (.I0(data2[0]),
        .I1(data3[0]),
        .I2(alu_op_IBUF[1]),
        .I3(data4),
        .I4(alu_op_IBUF[0]),
        .O(\result_OBUF[0]_inst_i_4_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_40 
       (.I0(op2_IBUF[10]),
        .I1(op1_IBUF[10]),
        .I2(op1_IBUF[11]),
        .I3(op2_IBUF[11]),
        .O(\result_OBUF[0]_inst_i_40_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_41 
       (.I0(op2_IBUF[8]),
        .I1(op1_IBUF[8]),
        .I2(op1_IBUF[9]),
        .I3(op2_IBUF[9]),
        .O(\result_OBUF[0]_inst_i_41_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_42 
       (.I0(op2_IBUF[14]),
        .I1(op1_IBUF[14]),
        .I2(op1_IBUF[15]),
        .I3(op2_IBUF[15]),
        .O(\result_OBUF[0]_inst_i_42_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_43 
       (.I0(op2_IBUF[12]),
        .I1(op1_IBUF[12]),
        .I2(op1_IBUF[13]),
        .I3(op2_IBUF[13]),
        .O(\result_OBUF[0]_inst_i_43_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_44 
       (.I0(op2_IBUF[10]),
        .I1(op1_IBUF[10]),
        .I2(op1_IBUF[11]),
        .I3(op2_IBUF[11]),
        .O(\result_OBUF[0]_inst_i_44_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_45 
       (.I0(op2_IBUF[8]),
        .I1(op1_IBUF[8]),
        .I2(op1_IBUF[9]),
        .I3(op2_IBUF[9]),
        .O(\result_OBUF[0]_inst_i_45_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_46 
       (.I0(op2_IBUF[6]),
        .I1(op1_IBUF[6]),
        .I2(op1_IBUF[7]),
        .I3(op2_IBUF[7]),
        .O(\result_OBUF[0]_inst_i_46_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_47 
       (.I0(op2_IBUF[4]),
        .I1(op1_IBUF[4]),
        .I2(op1_IBUF[5]),
        .I3(op2_IBUF[5]),
        .O(\result_OBUF[0]_inst_i_47_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_48 
       (.I0(op2_IBUF[2]),
        .I1(op1_IBUF[2]),
        .I2(op1_IBUF[3]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[0]_inst_i_48_n_0 ));
  LUT4 #(
    .INIT(16'h2F02)) 
    \result_OBUF[0]_inst_i_49 
       (.I0(op2_IBUF[0]),
        .I1(op1_IBUF[0]),
        .I2(op1_IBUF[1]),
        .I3(op2_IBUF[1]),
        .O(\result_OBUF[0]_inst_i_49_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT5 #(
    .INIT(32'h8ABABA8A)) 
    \result_OBUF[0]_inst_i_5 
       (.I0(data2[0]),
        .I1(alu_op_IBUF[1]),
        .I2(alu_op_IBUF[0]),
        .I3(op2_IBUF[0]),
        .I4(op1_IBUF[0]),
        .O(\result_OBUF[0]_inst_i_5_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_50 
       (.I0(op2_IBUF[6]),
        .I1(op1_IBUF[6]),
        .I2(op1_IBUF[7]),
        .I3(op2_IBUF[7]),
        .O(\result_OBUF[0]_inst_i_50_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_51 
       (.I0(op2_IBUF[4]),
        .I1(op1_IBUF[4]),
        .I2(op1_IBUF[5]),
        .I3(op2_IBUF[5]),
        .O(\result_OBUF[0]_inst_i_51_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_52 
       (.I0(op2_IBUF[2]),
        .I1(op1_IBUF[2]),
        .I2(op1_IBUF[3]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[0]_inst_i_52_n_0 ));
  LUT4 #(
    .INIT(16'h9009)) 
    \result_OBUF[0]_inst_i_53 
       (.I0(op2_IBUF[0]),
        .I1(op1_IBUF[0]),
        .I2(op1_IBUF[1]),
        .I3(op2_IBUF[1]),
        .O(\result_OBUF[0]_inst_i_53_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[0]_inst_i_6 
       (.I0(\result_OBUF[0]_inst_i_11_n_0 ),
        .I1(\result_OBUF[0]_inst_i_12_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[0]_inst_i_13_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[0]_inst_i_14_n_0 ),
        .O(\result_OBUF[0]_inst_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair4" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \result_OBUF[0]_inst_i_7 
       (.I0(op2_IBUF[0]),
        .I1(alu_op_IBUF[0]),
        .O(\result_OBUF[0]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h8A808A808A8A8080)) 
    \result_OBUF[0]_inst_i_8 
       (.I0(\result_OBUF[0]_inst_i_15_n_0 ),
        .I1(\result_OBUF[0]_inst_i_16_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[1]_inst_i_19_n_0 ),
        .I4(\result_OBUF[0]_inst_i_17_n_0 ),
        .I5(op2_IBUF[2]),
        .O(\result_OBUF[0]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAA000000AA00C000)) 
    \result_OBUF[0]_inst_i_9 
       (.I0(data2[0]),
        .I1(\result_OBUF[1]_inst_i_11_n_0 ),
        .I2(\result_OBUF[0]_inst_i_18_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(alu_op_IBUF[1]),
        .I5(op2_IBUF[0]),
        .O(\result_OBUF[0]_inst_i_9_n_0 ));
  OBUF \result_OBUF[10]_inst 
       (.I(result_OBUF[10]),
        .O(result[10]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[10]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[10]),
        .I2(op1_IBUF[10]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[10]_inst_i_2_n_0 ),
        .I5(\result_OBUF[10]_inst_i_3_n_0 ),
        .O(result_OBUF[10]));
  LUT6 #(
    .INIT(64'hCFC0AFAFCFC0A0A0)) 
    \result_OBUF[10]_inst_i_10 
       (.I0(op1_IBUF[18]),
        .I1(op1_IBUF[31]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[26]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[10]),
        .O(\result_OBUF[10]_inst_i_10_n_0 ));
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[10]_inst_i_11 
       (.I0(op1_IBUF[18]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[26]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[10]),
        .O(\result_OBUF[10]_inst_i_11_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[10]_inst_i_2 
       (.I0(\result_OBUF[10]_inst_i_4_n_0 ),
        .I1(data3[10]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[10]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[10]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[10]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[10]_inst_i_5_n_0 ),
        .I4(\result_OBUF[10]_inst_i_6_n_0 ),
        .I5(data2[10]),
        .O(\result_OBUF[10]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[10]_inst_i_4 
       (.I0(op1_IBUF[10]),
        .I1(op2_IBUF[10]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[10]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[10]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[10]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[10]_inst_i_7_n_0 ),
        .I2(\result_OBUF[11]_inst_i_17_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[10]),
        .O(\result_OBUF[10]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[10]_inst_i_6 
       (.I0(\result_OBUF[11]_inst_i_19_n_0 ),
        .I1(\result_OBUF[10]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[10]_inst_i_9_n_0 ),
        .I5(\result_OBUF[11]_inst_i_18_n_0 ),
        .O(\result_OBUF[10]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[10]_inst_i_7 
       (.I0(\result_OBUF[16]_inst_i_10_n_0 ),
        .I1(\result_OBUF[12]_inst_i_10_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[14]_inst_i_10_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[10]_inst_i_10_n_0 ),
        .O(\result_OBUF[10]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hB080FFFFB0800000)) 
    \result_OBUF[10]_inst_i_8 
       (.I0(op1_IBUF[3]),
        .I1(op2_IBUF[2]),
        .I2(\result_OBUF[30]_inst_i_26_n_0 ),
        .I3(op1_IBUF[7]),
        .I4(op2_IBUF[1]),
        .I5(\result_OBUF[12]_inst_i_11_n_0 ),
        .O(\result_OBUF[10]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[10]_inst_i_9 
       (.I0(\result_OBUF[16]_inst_i_13_n_0 ),
        .I1(\result_OBUF[12]_inst_i_12_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[14]_inst_i_12_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[10]_inst_i_11_n_0 ),
        .O(\result_OBUF[10]_inst_i_9_n_0 ));
  OBUF \result_OBUF[11]_inst 
       (.I(result_OBUF[11]),
        .O(result[11]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[11]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[11]),
        .I2(op2_IBUF[11]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[11]_inst_i_2_n_0 ),
        .I5(\result_OBUF[11]_inst_i_3_n_0 ),
        .O(result_OBUF[11]));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[11]_inst_i_10 
       (.I0(op1_IBUF[10]),
        .I1(op2_IBUF[10]),
        .O(\result_OBUF[11]_inst_i_10_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[11]_inst_i_11 
       (.I0(op1_IBUF[9]),
        .I1(op2_IBUF[9]),
        .O(\result_OBUF[11]_inst_i_11_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[11]_inst_i_12 
       (.I0(op1_IBUF[8]),
        .I1(op2_IBUF[8]),
        .O(\result_OBUF[11]_inst_i_12_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[11]_inst_i_13 
       (.I0(op1_IBUF[11]),
        .I1(op2_IBUF[11]),
        .O(\result_OBUF[11]_inst_i_13_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[11]_inst_i_14 
       (.I0(op2_IBUF[10]),
        .I1(op1_IBUF[10]),
        .O(\result_OBUF[11]_inst_i_14_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[11]_inst_i_15 
       (.I0(op1_IBUF[9]),
        .I1(op2_IBUF[9]),
        .O(\result_OBUF[11]_inst_i_15_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[11]_inst_i_16 
       (.I0(op2_IBUF[8]),
        .I1(op1_IBUF[8]),
        .O(\result_OBUF[11]_inst_i_16_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[11]_inst_i_17 
       (.I0(\result_OBUF[17]_inst_i_10_n_0 ),
        .I1(\result_OBUF[13]_inst_i_10_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[15]_inst_i_20_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[11]_inst_i_20_n_0 ),
        .O(\result_OBUF[11]_inst_i_17_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair32" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[11]_inst_i_18 
       (.I0(\result_OBUF[11]_inst_i_21_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[13]_inst_i_11_n_0 ),
        .O(\result_OBUF[11]_inst_i_18_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[11]_inst_i_19 
       (.I0(\result_OBUF[17]_inst_i_13_n_0 ),
        .I1(\result_OBUF[13]_inst_i_12_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[15]_inst_i_22_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[11]_inst_i_22_n_0 ),
        .O(\result_OBUF[11]_inst_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[11]_inst_i_2 
       (.I0(\result_OBUF[11]_inst_i_4_n_0 ),
        .I1(data3[11]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[11]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[11]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hCFC0AFAFCFC0A0A0)) 
    \result_OBUF[11]_inst_i_20 
       (.I0(op1_IBUF[19]),
        .I1(op1_IBUF[31]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[27]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[11]),
        .O(\result_OBUF[11]_inst_i_20_n_0 ));
  LUT6 #(
    .INIT(64'h000030300000BB88)) 
    \result_OBUF[11]_inst_i_21 
       (.I0(op1_IBUF[4]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[0]),
        .I3(op1_IBUF[8]),
        .I4(op2_IBUF[4]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[11]_inst_i_21_n_0 ));
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[11]_inst_i_22 
       (.I0(op1_IBUF[19]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[27]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[11]),
        .O(\result_OBUF[11]_inst_i_22_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[11]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[11]_inst_i_7_n_0 ),
        .I4(\result_OBUF[11]_inst_i_8_n_0 ),
        .I5(data2[11]),
        .O(\result_OBUF[11]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[11]_inst_i_4 
       (.I0(op2_IBUF[11]),
        .I1(op1_IBUF[11]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[11]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[11]_inst_i_4_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[11]_inst_i_5 
       (.CI(\result_OBUF[7]_inst_i_5_n_0 ),
        .CO({\result_OBUF[11]_inst_i_5_n_0 ,\NLW_result_OBUF[11]_inst_i_5_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[11:8]),
        .O(data3[11:8]),
        .S({\result_OBUF[11]_inst_i_9_n_0 ,\result_OBUF[11]_inst_i_10_n_0 ,\result_OBUF[11]_inst_i_11_n_0 ,\result_OBUF[11]_inst_i_12_n_0 }));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[11]_inst_i_6 
       (.CI(\result_OBUF[7]_inst_i_6_n_0 ),
        .CO({\result_OBUF[11]_inst_i_6_n_0 ,\NLW_result_OBUF[11]_inst_i_6_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[11:8]),
        .O(data2[11:8]),
        .S({\result_OBUF[11]_inst_i_13_n_0 ,\result_OBUF[11]_inst_i_14_n_0 ,\result_OBUF[11]_inst_i_15_n_0 ,\result_OBUF[11]_inst_i_16_n_0 }));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[11]_inst_i_7 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[11]_inst_i_17_n_0 ),
        .I2(\result_OBUF[12]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[11]),
        .O(\result_OBUF[11]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[11]_inst_i_8 
       (.I0(\result_OBUF[12]_inst_i_9_n_0 ),
        .I1(\result_OBUF[11]_inst_i_18_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[11]_inst_i_19_n_0 ),
        .I5(\result_OBUF[12]_inst_i_8_n_0 ),
        .O(\result_OBUF[11]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[11]_inst_i_9 
       (.I0(op1_IBUF[11]),
        .I1(op2_IBUF[11]),
        .O(\result_OBUF[11]_inst_i_9_n_0 ));
  OBUF \result_OBUF[12]_inst 
       (.I(result_OBUF[12]),
        .O(result[12]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[12]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[12]),
        .I2(op1_IBUF[12]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[12]_inst_i_2_n_0 ),
        .I5(\result_OBUF[12]_inst_i_3_n_0 ),
        .O(result_OBUF[12]));
  LUT6 #(
    .INIT(64'hCFC0AFAFCFC0A0A0)) 
    \result_OBUF[12]_inst_i_10 
       (.I0(op1_IBUF[20]),
        .I1(op1_IBUF[31]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[28]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[12]),
        .O(\result_OBUF[12]_inst_i_10_n_0 ));
  LUT6 #(
    .INIT(64'h000030300000BB88)) 
    \result_OBUF[12]_inst_i_11 
       (.I0(op1_IBUF[5]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[1]),
        .I3(op1_IBUF[9]),
        .I4(op2_IBUF[4]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[12]_inst_i_11_n_0 ));
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[12]_inst_i_12 
       (.I0(op1_IBUF[20]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[28]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[12]),
        .O(\result_OBUF[12]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[12]_inst_i_2 
       (.I0(\result_OBUF[12]_inst_i_4_n_0 ),
        .I1(data3[12]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[12]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[12]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[12]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[12]_inst_i_5_n_0 ),
        .I4(\result_OBUF[12]_inst_i_6_n_0 ),
        .I5(data2[12]),
        .O(\result_OBUF[12]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[12]_inst_i_4 
       (.I0(op1_IBUF[12]),
        .I1(op2_IBUF[12]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[12]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[12]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[12]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[12]_inst_i_7_n_0 ),
        .I2(\result_OBUF[13]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[12]),
        .O(\result_OBUF[12]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[12]_inst_i_6 
       (.I0(\result_OBUF[13]_inst_i_9_n_0 ),
        .I1(\result_OBUF[12]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[12]_inst_i_9_n_0 ),
        .I5(\result_OBUF[13]_inst_i_8_n_0 ),
        .O(\result_OBUF[12]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[12]_inst_i_7 
       (.I0(\result_OBUF[18]_inst_i_10_n_0 ),
        .I1(\result_OBUF[14]_inst_i_10_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[16]_inst_i_10_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[12]_inst_i_10_n_0 ),
        .O(\result_OBUF[12]_inst_i_7_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair34" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[12]_inst_i_8 
       (.I0(\result_OBUF[12]_inst_i_11_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[14]_inst_i_11_n_0 ),
        .O(\result_OBUF[12]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[12]_inst_i_9 
       (.I0(\result_OBUF[18]_inst_i_13_n_0 ),
        .I1(\result_OBUF[14]_inst_i_12_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[16]_inst_i_13_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[12]_inst_i_12_n_0 ),
        .O(\result_OBUF[12]_inst_i_9_n_0 ));
  OBUF \result_OBUF[13]_inst 
       (.I(result_OBUF[13]),
        .O(result[13]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[13]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[13]),
        .I2(op2_IBUF[13]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[13]_inst_i_2_n_0 ),
        .I5(\result_OBUF[13]_inst_i_3_n_0 ),
        .O(result_OBUF[13]));
  LUT6 #(
    .INIT(64'hCFC0AFAFCFC0A0A0)) 
    \result_OBUF[13]_inst_i_10 
       (.I0(op1_IBUF[21]),
        .I1(op1_IBUF[31]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[29]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[13]),
        .O(\result_OBUF[13]_inst_i_10_n_0 ));
  LUT6 #(
    .INIT(64'h000030300000BB88)) 
    \result_OBUF[13]_inst_i_11 
       (.I0(op1_IBUF[6]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[2]),
        .I3(op1_IBUF[10]),
        .I4(op2_IBUF[4]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[13]_inst_i_11_n_0 ));
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[13]_inst_i_12 
       (.I0(op1_IBUF[21]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[29]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[13]),
        .O(\result_OBUF[13]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[13]_inst_i_2 
       (.I0(\result_OBUF[13]_inst_i_4_n_0 ),
        .I1(data3[13]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[13]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[13]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[13]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[13]_inst_i_5_n_0 ),
        .I4(\result_OBUF[13]_inst_i_6_n_0 ),
        .I5(data2[13]),
        .O(\result_OBUF[13]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[13]_inst_i_4 
       (.I0(op2_IBUF[13]),
        .I1(op1_IBUF[13]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[13]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[13]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[13]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[13]_inst_i_7_n_0 ),
        .I2(\result_OBUF[14]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[13]),
        .O(\result_OBUF[13]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[13]_inst_i_6 
       (.I0(\result_OBUF[14]_inst_i_9_n_0 ),
        .I1(\result_OBUF[13]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[13]_inst_i_9_n_0 ),
        .I5(\result_OBUF[14]_inst_i_8_n_0 ),
        .O(\result_OBUF[13]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[13]_inst_i_7 
       (.I0(\result_OBUF[19]_inst_i_21_n_0 ),
        .I1(\result_OBUF[15]_inst_i_20_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[17]_inst_i_10_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[13]_inst_i_10_n_0 ),
        .O(\result_OBUF[13]_inst_i_7_n_0 ));
  LUT5 #(
    .INIT(32'hB8BBB888)) 
    \result_OBUF[13]_inst_i_8 
       (.I0(\result_OBUF[13]_inst_i_11_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[15]_inst_i_21_n_0 ),
        .I3(op2_IBUF[2]),
        .I4(\result_OBUF[19]_inst_i_22_n_0 ),
        .O(\result_OBUF[13]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[13]_inst_i_9 
       (.I0(\result_OBUF[19]_inst_i_24_n_0 ),
        .I1(\result_OBUF[15]_inst_i_22_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[17]_inst_i_13_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[13]_inst_i_12_n_0 ),
        .O(\result_OBUF[13]_inst_i_9_n_0 ));
  OBUF \result_OBUF[14]_inst 
       (.I(result_OBUF[14]),
        .O(result[14]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[14]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[14]),
        .I2(op1_IBUF[14]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[14]_inst_i_2_n_0 ),
        .I5(\result_OBUF[14]_inst_i_3_n_0 ),
        .O(result_OBUF[14]));
  LUT6 #(
    .INIT(64'hCFC0AFAFCFC0A0A0)) 
    \result_OBUF[14]_inst_i_10 
       (.I0(op1_IBUF[22]),
        .I1(op1_IBUF[31]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[30]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[14]),
        .O(\result_OBUF[14]_inst_i_10_n_0 ));
  LUT6 #(
    .INIT(64'h000030300000BB88)) 
    \result_OBUF[14]_inst_i_11 
       (.I0(op1_IBUF[7]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[3]),
        .I3(op1_IBUF[11]),
        .I4(op2_IBUF[4]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[14]_inst_i_11_n_0 ));
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[14]_inst_i_12 
       (.I0(op1_IBUF[22]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[30]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[14]),
        .O(\result_OBUF[14]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[14]_inst_i_2 
       (.I0(\result_OBUF[14]_inst_i_4_n_0 ),
        .I1(data3[14]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[14]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[14]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[14]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[14]_inst_i_5_n_0 ),
        .I4(\result_OBUF[14]_inst_i_6_n_0 ),
        .I5(data2[14]),
        .O(\result_OBUF[14]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[14]_inst_i_4 
       (.I0(op1_IBUF[14]),
        .I1(op2_IBUF[14]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[14]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[14]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[14]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[14]_inst_i_7_n_0 ),
        .I2(\result_OBUF[15]_inst_i_17_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[14]),
        .O(\result_OBUF[14]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[14]_inst_i_6 
       (.I0(\result_OBUF[15]_inst_i_19_n_0 ),
        .I1(\result_OBUF[14]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[14]_inst_i_9_n_0 ),
        .I5(\result_OBUF[15]_inst_i_18_n_0 ),
        .O(\result_OBUF[14]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[14]_inst_i_7 
       (.I0(\result_OBUF[20]_inst_i_11_n_0 ),
        .I1(\result_OBUF[16]_inst_i_10_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[18]_inst_i_10_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[14]_inst_i_10_n_0 ),
        .O(\result_OBUF[14]_inst_i_7_n_0 ));
  LUT5 #(
    .INIT(32'hB8BBB888)) 
    \result_OBUF[14]_inst_i_8 
       (.I0(\result_OBUF[14]_inst_i_11_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[16]_inst_i_11_n_0 ),
        .I3(op2_IBUF[2]),
        .I4(\result_OBUF[20]_inst_i_12_n_0 ),
        .O(\result_OBUF[14]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[14]_inst_i_9 
       (.I0(\result_OBUF[16]_inst_i_12_n_0 ),
        .I1(\result_OBUF[16]_inst_i_13_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[18]_inst_i_13_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[14]_inst_i_12_n_0 ),
        .O(\result_OBUF[14]_inst_i_9_n_0 ));
  OBUF \result_OBUF[15]_inst 
       (.I(result_OBUF[15]),
        .O(result[15]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[15]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[15]),
        .I2(op2_IBUF[15]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[15]_inst_i_2_n_0 ),
        .I5(\result_OBUF[15]_inst_i_3_n_0 ),
        .O(result_OBUF[15]));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[15]_inst_i_10 
       (.I0(op1_IBUF[14]),
        .I1(op2_IBUF[14]),
        .O(\result_OBUF[15]_inst_i_10_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[15]_inst_i_11 
       (.I0(op1_IBUF[13]),
        .I1(op2_IBUF[13]),
        .O(\result_OBUF[15]_inst_i_11_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[15]_inst_i_12 
       (.I0(op1_IBUF[12]),
        .I1(op2_IBUF[12]),
        .O(\result_OBUF[15]_inst_i_12_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[15]_inst_i_13 
       (.I0(op1_IBUF[15]),
        .I1(op2_IBUF[15]),
        .O(\result_OBUF[15]_inst_i_13_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[15]_inst_i_14 
       (.I0(op2_IBUF[14]),
        .I1(op1_IBUF[14]),
        .O(\result_OBUF[15]_inst_i_14_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[15]_inst_i_15 
       (.I0(op1_IBUF[13]),
        .I1(op2_IBUF[13]),
        .O(\result_OBUF[15]_inst_i_15_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[15]_inst_i_16 
       (.I0(op2_IBUF[12]),
        .I1(op1_IBUF[12]),
        .O(\result_OBUF[15]_inst_i_16_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[15]_inst_i_17 
       (.I0(\result_OBUF[21]_inst_i_11_n_0 ),
        .I1(\result_OBUF[17]_inst_i_10_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[19]_inst_i_21_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[15]_inst_i_20_n_0 ),
        .O(\result_OBUF[15]_inst_i_17_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[15]_inst_i_18 
       (.I0(\result_OBUF[15]_inst_i_21_n_0 ),
        .I1(\result_OBUF[19]_inst_i_22_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[17]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[21]_inst_i_12_n_0 ),
        .O(\result_OBUF[15]_inst_i_18_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[15]_inst_i_19 
       (.I0(\result_OBUF[17]_inst_i_12_n_0 ),
        .I1(\result_OBUF[17]_inst_i_13_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[19]_inst_i_24_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[15]_inst_i_22_n_0 ),
        .O(\result_OBUF[15]_inst_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[15]_inst_i_2 
       (.I0(\result_OBUF[15]_inst_i_4_n_0 ),
        .I1(data3[15]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[15]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[15]_inst_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair18" *) 
  LUT5 #(
    .INIT(32'hFF00B8B8)) 
    \result_OBUF[15]_inst_i_20 
       (.I0(op1_IBUF[23]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[15]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[4]),
        .O(\result_OBUF[15]_inst_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair13" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[15]_inst_i_21 
       (.I0(op1_IBUF[0]),
        .I1(op1_IBUF[8]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[15]_inst_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair18" *) 
  LUT5 #(
    .INIT(32'h3300B8B8)) 
    \result_OBUF[15]_inst_i_22 
       (.I0(op1_IBUF[23]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[15]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[4]),
        .O(\result_OBUF[15]_inst_i_22_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[15]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[15]_inst_i_7_n_0 ),
        .I4(\result_OBUF[15]_inst_i_8_n_0 ),
        .I5(data2[15]),
        .O(\result_OBUF[15]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[15]_inst_i_4 
       (.I0(op2_IBUF[15]),
        .I1(op1_IBUF[15]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[15]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[15]_inst_i_4_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[15]_inst_i_5 
       (.CI(\result_OBUF[11]_inst_i_5_n_0 ),
        .CO({\result_OBUF[15]_inst_i_5_n_0 ,\NLW_result_OBUF[15]_inst_i_5_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[15:12]),
        .O(data3[15:12]),
        .S({\result_OBUF[15]_inst_i_9_n_0 ,\result_OBUF[15]_inst_i_10_n_0 ,\result_OBUF[15]_inst_i_11_n_0 ,\result_OBUF[15]_inst_i_12_n_0 }));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[15]_inst_i_6 
       (.CI(\result_OBUF[11]_inst_i_6_n_0 ),
        .CO({\result_OBUF[15]_inst_i_6_n_0 ,\NLW_result_OBUF[15]_inst_i_6_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[15:12]),
        .O(data2[15:12]),
        .S({\result_OBUF[15]_inst_i_13_n_0 ,\result_OBUF[15]_inst_i_14_n_0 ,\result_OBUF[15]_inst_i_15_n_0 ,\result_OBUF[15]_inst_i_16_n_0 }));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[15]_inst_i_7 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[15]_inst_i_17_n_0 ),
        .I2(\result_OBUF[16]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[15]),
        .O(\result_OBUF[15]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[15]_inst_i_8 
       (.I0(\result_OBUF[16]_inst_i_9_n_0 ),
        .I1(\result_OBUF[15]_inst_i_18_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[15]_inst_i_19_n_0 ),
        .I5(\result_OBUF[16]_inst_i_8_n_0 ),
        .O(\result_OBUF[15]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[15]_inst_i_9 
       (.I0(op1_IBUF[15]),
        .I1(op2_IBUF[15]),
        .O(\result_OBUF[15]_inst_i_9_n_0 ));
  OBUF \result_OBUF[16]_inst 
       (.I(result_OBUF[16]),
        .O(result[16]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[16]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[16]),
        .I2(op1_IBUF[16]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[16]_inst_i_2_n_0 ),
        .I5(\result_OBUF[16]_inst_i_3_n_0 ),
        .O(result_OBUF[16]));
  (* SOFT_HLUTNM = "soft_lutpair11" *) 
  LUT5 #(
    .INIT(32'hFF00B8B8)) 
    \result_OBUF[16]_inst_i_10 
       (.I0(op1_IBUF[24]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[16]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[4]),
        .O(\result_OBUF[16]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair21" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[16]_inst_i_11 
       (.I0(op1_IBUF[1]),
        .I1(op1_IBUF[9]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[16]_inst_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair24" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[16]_inst_i_12 
       (.I0(op1_IBUF[28]),
        .I1(op1_IBUF[20]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[16]_inst_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair11" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[16]_inst_i_13 
       (.I0(op1_IBUF[24]),
        .I1(op1_IBUF[16]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[16]_inst_i_13_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[16]_inst_i_2 
       (.I0(\result_OBUF[16]_inst_i_4_n_0 ),
        .I1(data3[16]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[16]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[16]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[16]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[16]_inst_i_5_n_0 ),
        .I4(\result_OBUF[16]_inst_i_6_n_0 ),
        .I5(data2[16]),
        .O(\result_OBUF[16]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[16]_inst_i_4 
       (.I0(op1_IBUF[16]),
        .I1(op2_IBUF[16]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[16]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[16]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[16]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[16]_inst_i_7_n_0 ),
        .I2(\result_OBUF[17]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[16]),
        .O(\result_OBUF[16]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[16]_inst_i_6 
       (.I0(\result_OBUF[17]_inst_i_9_n_0 ),
        .I1(\result_OBUF[16]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[16]_inst_i_9_n_0 ),
        .I5(\result_OBUF[17]_inst_i_8_n_0 ),
        .O(\result_OBUF[16]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[16]_inst_i_7 
       (.I0(\result_OBUF[22]_inst_i_11_n_0 ),
        .I1(\result_OBUF[18]_inst_i_10_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[20]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[16]_inst_i_10_n_0 ),
        .O(\result_OBUF[16]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[16]_inst_i_8 
       (.I0(\result_OBUF[16]_inst_i_11_n_0 ),
        .I1(\result_OBUF[20]_inst_i_12_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[18]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[22]_inst_i_12_n_0 ),
        .O(\result_OBUF[16]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[16]_inst_i_9 
       (.I0(\result_OBUF[18]_inst_i_12_n_0 ),
        .I1(\result_OBUF[18]_inst_i_13_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[16]_inst_i_12_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[16]_inst_i_13_n_0 ),
        .O(\result_OBUF[16]_inst_i_9_n_0 ));
  OBUF \result_OBUF[17]_inst 
       (.I(result_OBUF[17]),
        .O(result[17]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[17]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[17]),
        .I2(op2_IBUF[17]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[17]_inst_i_2_n_0 ),
        .I5(\result_OBUF[17]_inst_i_3_n_0 ),
        .O(result_OBUF[17]));
  (* SOFT_HLUTNM = "soft_lutpair17" *) 
  LUT5 #(
    .INIT(32'hFF00B8B8)) 
    \result_OBUF[17]_inst_i_10 
       (.I0(op1_IBUF[25]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[17]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[4]),
        .O(\result_OBUF[17]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair16" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[17]_inst_i_11 
       (.I0(op1_IBUF[2]),
        .I1(op1_IBUF[10]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[17]_inst_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair19" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[17]_inst_i_12 
       (.I0(op1_IBUF[29]),
        .I1(op1_IBUF[21]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[17]_inst_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair17" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[17]_inst_i_13 
       (.I0(op1_IBUF[25]),
        .I1(op1_IBUF[17]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[17]_inst_i_13_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[17]_inst_i_2 
       (.I0(\result_OBUF[17]_inst_i_4_n_0 ),
        .I1(data3[17]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[17]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[17]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[17]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[17]_inst_i_5_n_0 ),
        .I4(\result_OBUF[17]_inst_i_6_n_0 ),
        .I5(data2[17]),
        .O(\result_OBUF[17]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[17]_inst_i_4 
       (.I0(op2_IBUF[17]),
        .I1(op1_IBUF[17]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[17]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[17]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[17]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[17]_inst_i_7_n_0 ),
        .I2(\result_OBUF[18]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[17]),
        .O(\result_OBUF[17]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[17]_inst_i_6 
       (.I0(\result_OBUF[18]_inst_i_9_n_0 ),
        .I1(\result_OBUF[17]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[17]_inst_i_9_n_0 ),
        .I5(\result_OBUF[18]_inst_i_8_n_0 ),
        .O(\result_OBUF[17]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[17]_inst_i_7 
       (.I0(\result_OBUF[19]_inst_i_20_n_0 ),
        .I1(\result_OBUF[19]_inst_i_21_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[21]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[17]_inst_i_10_n_0 ),
        .O(\result_OBUF[17]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[17]_inst_i_8 
       (.I0(\result_OBUF[17]_inst_i_11_n_0 ),
        .I1(\result_OBUF[21]_inst_i_12_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[19]_inst_i_22_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[23]_inst_i_21_n_0 ),
        .O(\result_OBUF[17]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[17]_inst_i_9 
       (.I0(\result_OBUF[19]_inst_i_23_n_0 ),
        .I1(\result_OBUF[19]_inst_i_24_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[17]_inst_i_12_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[17]_inst_i_13_n_0 ),
        .O(\result_OBUF[17]_inst_i_9_n_0 ));
  OBUF \result_OBUF[18]_inst 
       (.I(result_OBUF[18]),
        .O(result[18]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[18]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[18]),
        .I2(op1_IBUF[18]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[18]_inst_i_2_n_0 ),
        .I5(\result_OBUF[18]_inst_i_3_n_0 ),
        .O(result_OBUF[18]));
  (* SOFT_HLUTNM = "soft_lutpair10" *) 
  LUT5 #(
    .INIT(32'hFF00B8B8)) 
    \result_OBUF[18]_inst_i_10 
       (.I0(op1_IBUF[26]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[18]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[4]),
        .O(\result_OBUF[18]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair23" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[18]_inst_i_11 
       (.I0(op1_IBUF[3]),
        .I1(op1_IBUF[11]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[18]_inst_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair12" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[18]_inst_i_12 
       (.I0(op1_IBUF[30]),
        .I1(op1_IBUF[22]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[18]_inst_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair10" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[18]_inst_i_13 
       (.I0(op1_IBUF[26]),
        .I1(op1_IBUF[18]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[18]_inst_i_13_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[18]_inst_i_2 
       (.I0(\result_OBUF[18]_inst_i_4_n_0 ),
        .I1(data3[18]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[18]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[18]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[18]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[18]_inst_i_5_n_0 ),
        .I4(\result_OBUF[18]_inst_i_6_n_0 ),
        .I5(data2[18]),
        .O(\result_OBUF[18]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[18]_inst_i_4 
       (.I0(op1_IBUF[18]),
        .I1(op2_IBUF[18]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[18]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[18]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[18]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[18]_inst_i_7_n_0 ),
        .I2(\result_OBUF[19]_inst_i_17_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[18]),
        .O(\result_OBUF[18]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[18]_inst_i_6 
       (.I0(\result_OBUF[19]_inst_i_19_n_0 ),
        .I1(\result_OBUF[18]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[18]_inst_i_9_n_0 ),
        .I5(\result_OBUF[19]_inst_i_18_n_0 ),
        .O(\result_OBUF[18]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[18]_inst_i_7 
       (.I0(\result_OBUF[20]_inst_i_10_n_0 ),
        .I1(\result_OBUF[20]_inst_i_11_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[22]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[18]_inst_i_10_n_0 ),
        .O(\result_OBUF[18]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[18]_inst_i_8 
       (.I0(\result_OBUF[18]_inst_i_11_n_0 ),
        .I1(\result_OBUF[22]_inst_i_12_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[20]_inst_i_12_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[24]_inst_i_11_n_0 ),
        .O(\result_OBUF[18]_inst_i_8_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair6" *) 
  LUT5 #(
    .INIT(32'hB8BBB888)) 
    \result_OBUF[18]_inst_i_9 
       (.I0(\result_OBUF[20]_inst_i_13_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[18]_inst_i_12_n_0 ),
        .I3(op2_IBUF[2]),
        .I4(\result_OBUF[18]_inst_i_13_n_0 ),
        .O(\result_OBUF[18]_inst_i_9_n_0 ));
  OBUF \result_OBUF[19]_inst 
       (.I(result_OBUF[19]),
        .O(result[19]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[19]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[19]),
        .I2(op2_IBUF[19]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[19]_inst_i_2_n_0 ),
        .I5(\result_OBUF[19]_inst_i_3_n_0 ),
        .O(result_OBUF[19]));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[19]_inst_i_10 
       (.I0(op1_IBUF[18]),
        .I1(op2_IBUF[18]),
        .O(\result_OBUF[19]_inst_i_10_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[19]_inst_i_11 
       (.I0(op1_IBUF[17]),
        .I1(op2_IBUF[17]),
        .O(\result_OBUF[19]_inst_i_11_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[19]_inst_i_12 
       (.I0(op1_IBUF[16]),
        .I1(op2_IBUF[16]),
        .O(\result_OBUF[19]_inst_i_12_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[19]_inst_i_13 
       (.I0(op1_IBUF[19]),
        .I1(op2_IBUF[19]),
        .O(\result_OBUF[19]_inst_i_13_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[19]_inst_i_14 
       (.I0(op2_IBUF[18]),
        .I1(op1_IBUF[18]),
        .O(\result_OBUF[19]_inst_i_14_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[19]_inst_i_15 
       (.I0(op1_IBUF[17]),
        .I1(op2_IBUF[17]),
        .O(\result_OBUF[19]_inst_i_15_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[19]_inst_i_16 
       (.I0(op2_IBUF[16]),
        .I1(op1_IBUF[16]),
        .O(\result_OBUF[19]_inst_i_16_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[19]_inst_i_17 
       (.I0(\result_OBUF[21]_inst_i_10_n_0 ),
        .I1(\result_OBUF[21]_inst_i_11_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[19]_inst_i_20_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[19]_inst_i_21_n_0 ),
        .O(\result_OBUF[19]_inst_i_17_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[19]_inst_i_18 
       (.I0(\result_OBUF[19]_inst_i_22_n_0 ),
        .I1(\result_OBUF[23]_inst_i_21_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[21]_inst_i_12_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[25]_inst_i_11_n_0 ),
        .O(\result_OBUF[19]_inst_i_18_n_0 ));
  LUT5 #(
    .INIT(32'hB8BBB888)) 
    \result_OBUF[19]_inst_i_19 
       (.I0(\result_OBUF[21]_inst_i_13_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[19]_inst_i_23_n_0 ),
        .I3(op2_IBUF[2]),
        .I4(\result_OBUF[19]_inst_i_24_n_0 ),
        .O(\result_OBUF[19]_inst_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[19]_inst_i_2 
       (.I0(\result_OBUF[19]_inst_i_4_n_0 ),
        .I1(data3[19]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[19]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[19]_inst_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair25" *) 
  LUT4 #(
    .INIT(16'hF0E2)) 
    \result_OBUF[19]_inst_i_20 
       (.I0(op1_IBUF[23]),
        .I1(op2_IBUF[4]),
        .I2(op1_IBUF[31]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[19]_inst_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair9" *) 
  LUT5 #(
    .INIT(32'hFF00B8B8)) 
    \result_OBUF[19]_inst_i_21 
       (.I0(op1_IBUF[27]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[19]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[4]),
        .O(\result_OBUF[19]_inst_i_21_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[19]_inst_i_22 
       (.I0(op1_IBUF[4]),
        .I1(op1_IBUF[12]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[19]_inst_i_22_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair25" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[19]_inst_i_23 
       (.I0(op1_IBUF[31]),
        .I1(op1_IBUF[23]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[19]_inst_i_23_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair9" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[19]_inst_i_24 
       (.I0(op1_IBUF[27]),
        .I1(op1_IBUF[19]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[19]_inst_i_24_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[19]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[19]_inst_i_7_n_0 ),
        .I4(\result_OBUF[19]_inst_i_8_n_0 ),
        .I5(data2[19]),
        .O(\result_OBUF[19]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[19]_inst_i_4 
       (.I0(op2_IBUF[19]),
        .I1(op1_IBUF[19]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[19]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[19]_inst_i_4_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[19]_inst_i_5 
       (.CI(\result_OBUF[15]_inst_i_5_n_0 ),
        .CO({\result_OBUF[19]_inst_i_5_n_0 ,\NLW_result_OBUF[19]_inst_i_5_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[19:16]),
        .O(data3[19:16]),
        .S({\result_OBUF[19]_inst_i_9_n_0 ,\result_OBUF[19]_inst_i_10_n_0 ,\result_OBUF[19]_inst_i_11_n_0 ,\result_OBUF[19]_inst_i_12_n_0 }));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[19]_inst_i_6 
       (.CI(\result_OBUF[15]_inst_i_6_n_0 ),
        .CO({\result_OBUF[19]_inst_i_6_n_0 ,\NLW_result_OBUF[19]_inst_i_6_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[19:16]),
        .O(data2[19:16]),
        .S({\result_OBUF[19]_inst_i_13_n_0 ,\result_OBUF[19]_inst_i_14_n_0 ,\result_OBUF[19]_inst_i_15_n_0 ,\result_OBUF[19]_inst_i_16_n_0 }));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[19]_inst_i_7 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[19]_inst_i_17_n_0 ),
        .I2(\result_OBUF[20]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[19]),
        .O(\result_OBUF[19]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[19]_inst_i_8 
       (.I0(\result_OBUF[20]_inst_i_9_n_0 ),
        .I1(\result_OBUF[19]_inst_i_18_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[19]_inst_i_19_n_0 ),
        .I5(\result_OBUF[20]_inst_i_8_n_0 ),
        .O(\result_OBUF[19]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[19]_inst_i_9 
       (.I0(op1_IBUF[19]),
        .I1(op2_IBUF[19]),
        .O(\result_OBUF[19]_inst_i_9_n_0 ));
  OBUF \result_OBUF[1]_inst 
       (.I(result_OBUF[1]),
        .O(result[1]));
  LUT6 #(
    .INIT(64'hFFFFFFAEAAAAAAAA)) 
    \result_OBUF[1]_inst_i_1 
       (.I0(\result_OBUF[1]_inst_i_2_n_0 ),
        .I1(data2[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[1]_inst_i_4_n_0 ),
        .I4(\result_OBUF[1]_inst_i_5_n_0 ),
        .I5(\result_OBUF[30]_inst_i_7_n_0 ),
        .O(result_OBUF[1]));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[1]_inst_i_10 
       (.I0(op2_IBUF[0]),
        .I1(op1_IBUF[0]),
        .O(\result_OBUF[1]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair6" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \result_OBUF[1]_inst_i_11 
       (.I0(op2_IBUF[2]),
        .I1(op2_IBUF[1]),
        .O(\result_OBUF[1]_inst_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair7" *) 
  LUT3 #(
    .INIT(8'h10)) 
    \result_OBUF[1]_inst_i_12 
       (.I0(op2_IBUF[3]),
        .I1(op2_IBUF[4]),
        .I2(op1_IBUF[1]),
        .O(\result_OBUF[1]_inst_i_12_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair3" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \result_OBUF[1]_inst_i_13 
       (.I0(alu_op_IBUF[0]),
        .I1(op2_IBUF[0]),
        .O(\result_OBUF[1]_inst_i_13_n_0 ));
  LUT3 #(
    .INIT(8'h10)) 
    \result_OBUF[1]_inst_i_14 
       (.I0(op2_IBUF[0]),
        .I1(alu_op_IBUF[0]),
        .I2(\result_OBUF[0]_inst_i_6_n_0 ),
        .O(\result_OBUF[1]_inst_i_14_n_0 ));
  LUT6 #(
    .INIT(64'h80800000FF000000)) 
    \result_OBUF[1]_inst_i_15 
       (.I0(\result_OBUF[1]_inst_i_11_n_0 ),
        .I1(op1_IBUF[0]),
        .I2(\result_OBUF[30]_inst_i_26_n_0 ),
        .I3(\result_OBUF[2]_inst_i_8_n_0 ),
        .I4(op2_IBUF[0]),
        .I5(alu_op_IBUF[0]),
        .O(\result_OBUF[1]_inst_i_15_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[1]_inst_i_16 
       (.I0(\result_OBUF[1]_inst_i_18_n_0 ),
        .I1(\result_OBUF[1]_inst_i_19_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[1]_inst_i_20_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[1]_inst_i_21_n_0 ),
        .O(\result_OBUF[1]_inst_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair28" *) 
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[1]_inst_i_17 
       (.I0(op2_IBUF[1]),
        .I1(op1_IBUF[1]),
        .O(\result_OBUF[1]_inst_i_17_n_0 ));
  LUT6 #(
    .INIT(64'hCFC0AFAFCFC0A0A0)) 
    \result_OBUF[1]_inst_i_18 
       (.I0(op1_IBUF[16]),
        .I1(op1_IBUF[31]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[24]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[8]),
        .O(\result_OBUF[1]_inst_i_18_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[1]_inst_i_19 
       (.I0(op1_IBUF[4]),
        .I1(op1_IBUF[20]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[28]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[12]),
        .O(\result_OBUF[1]_inst_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    \result_OBUF[1]_inst_i_2 
       (.I0(\result_OBUF[1]_inst_i_6_n_0 ),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(op1_IBUF[1]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(\result_OBUF[1]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[1]_inst_i_20 
       (.I0(op1_IBUF[6]),
        .I1(op1_IBUF[22]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[30]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[14]),
        .O(\result_OBUF[1]_inst_i_20_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[1]_inst_i_21 
       (.I0(op1_IBUF[2]),
        .I1(op1_IBUF[18]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[26]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[10]),
        .O(\result_OBUF[1]_inst_i_21_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[1]_inst_i_3 
       (.CI(\<const0> ),
        .CO({\result_OBUF[1]_inst_i_3_n_0 ,\NLW_result_OBUF[1]_inst_i_3_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[3:0]),
        .O(data2[3:0]),
        .S({\result_OBUF[1]_inst_i_7_n_0 ,\result_OBUF[1]_inst_i_8_n_0 ,\result_OBUF[1]_inst_i_9_n_0 ,\result_OBUF[1]_inst_i_10_n_0 }));
  LUT6 #(
    .INIT(64'hAAAAAAAAAAAA8000)) 
    \result_OBUF[1]_inst_i_4 
       (.I0(\result_OBUF[30]_inst_i_17_n_0 ),
        .I1(\result_OBUF[1]_inst_i_11_n_0 ),
        .I2(\result_OBUF[1]_inst_i_12_n_0 ),
        .I3(\result_OBUF[1]_inst_i_13_n_0 ),
        .I4(\result_OBUF[1]_inst_i_14_n_0 ),
        .I5(\result_OBUF[1]_inst_i_15_n_0 ),
        .O(\result_OBUF[1]_inst_i_4_n_0 ));
  LUT6 #(
    .INIT(64'hAAAAAAAA8A808080)) 
    \result_OBUF[1]_inst_i_5 
       (.I0(\result_OBUF[30]_inst_i_15_n_0 ),
        .I1(data2[1]),
        .I2(alu_op_IBUF[0]),
        .I3(\result_OBUF[1]_inst_i_16_n_0 ),
        .I4(op2_IBUF[0]),
        .I5(\result_OBUF[1]_inst_i_14_n_0 ),
        .O(\result_OBUF[1]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    \result_OBUF[1]_inst_i_6 
       (.I0(data3[1]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[1]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(\result_OBUF[1]_inst_i_17_n_0 ),
        .O(\result_OBUF[1]_inst_i_6_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[1]_inst_i_7 
       (.I0(op1_IBUF[3]),
        .I1(op2_IBUF[3]),
        .O(\result_OBUF[1]_inst_i_7_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[1]_inst_i_8 
       (.I0(op2_IBUF[2]),
        .I1(op1_IBUF[2]),
        .O(\result_OBUF[1]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[1]_inst_i_9 
       (.I0(op1_IBUF[1]),
        .I1(op2_IBUF[1]),
        .O(\result_OBUF[1]_inst_i_9_n_0 ));
  OBUF \result_OBUF[20]_inst 
       (.I(result_OBUF[20]),
        .O(result[20]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[20]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[20]),
        .I2(op1_IBUF[20]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[20]_inst_i_2_n_0 ),
        .I5(\result_OBUF[20]_inst_i_3_n_0 ),
        .O(result_OBUF[20]));
  (* SOFT_HLUTNM = "soft_lutpair26" *) 
  LUT4 #(
    .INIT(16'hF0E2)) 
    \result_OBUF[20]_inst_i_10 
       (.I0(op1_IBUF[24]),
        .I1(op2_IBUF[4]),
        .I2(op1_IBUF[31]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[20]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair24" *) 
  LUT5 #(
    .INIT(32'hFF00B8B8)) 
    \result_OBUF[20]_inst_i_11 
       (.I0(op1_IBUF[28]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[20]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[4]),
        .O(\result_OBUF[20]_inst_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair20" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[20]_inst_i_12 
       (.I0(op1_IBUF[5]),
        .I1(op1_IBUF[13]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[20]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'h000030300000BB88)) 
    \result_OBUF[20]_inst_i_13 
       (.I0(op1_IBUF[24]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[28]),
        .I3(op1_IBUF[20]),
        .I4(op2_IBUF[4]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[20]_inst_i_13_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[20]_inst_i_2 
       (.I0(\result_OBUF[20]_inst_i_4_n_0 ),
        .I1(data3[20]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[20]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[20]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[20]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[20]_inst_i_5_n_0 ),
        .I4(\result_OBUF[20]_inst_i_6_n_0 ),
        .I5(data2[20]),
        .O(\result_OBUF[20]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[20]_inst_i_4 
       (.I0(op1_IBUF[20]),
        .I1(op2_IBUF[20]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[20]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[20]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[20]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[20]_inst_i_7_n_0 ),
        .I2(\result_OBUF[21]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[20]),
        .O(\result_OBUF[20]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[20]_inst_i_6 
       (.I0(\result_OBUF[21]_inst_i_9_n_0 ),
        .I1(\result_OBUF[20]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[20]_inst_i_9_n_0 ),
        .I5(\result_OBUF[21]_inst_i_8_n_0 ),
        .O(\result_OBUF[20]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[20]_inst_i_7 
       (.I0(\result_OBUF[22]_inst_i_10_n_0 ),
        .I1(\result_OBUF[22]_inst_i_11_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[20]_inst_i_10_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[20]_inst_i_11_n_0 ),
        .O(\result_OBUF[20]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[20]_inst_i_8 
       (.I0(\result_OBUF[20]_inst_i_12_n_0 ),
        .I1(\result_OBUF[24]_inst_i_11_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[22]_inst_i_12_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[26]_inst_i_11_n_0 ),
        .O(\result_OBUF[20]_inst_i_8_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair28" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[20]_inst_i_9 
       (.I0(\result_OBUF[22]_inst_i_13_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[20]_inst_i_13_n_0 ),
        .O(\result_OBUF[20]_inst_i_9_n_0 ));
  OBUF \result_OBUF[21]_inst 
       (.I(result_OBUF[21]),
        .O(result[21]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[21]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[21]),
        .I2(op2_IBUF[21]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[21]_inst_i_2_n_0 ),
        .I5(\result_OBUF[21]_inst_i_3_n_0 ),
        .O(result_OBUF[21]));
  (* SOFT_HLUTNM = "soft_lutpair26" *) 
  LUT4 #(
    .INIT(16'hF0E2)) 
    \result_OBUF[21]_inst_i_10 
       (.I0(op1_IBUF[25]),
        .I1(op2_IBUF[4]),
        .I2(op1_IBUF[31]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[21]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair19" *) 
  LUT5 #(
    .INIT(32'hFF00B8B8)) 
    \result_OBUF[21]_inst_i_11 
       (.I0(op1_IBUF[29]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[21]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[4]),
        .O(\result_OBUF[21]_inst_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair14" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[21]_inst_i_12 
       (.I0(op1_IBUF[6]),
        .I1(op1_IBUF[14]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[21]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'h000030300000BB88)) 
    \result_OBUF[21]_inst_i_13 
       (.I0(op1_IBUF[25]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[29]),
        .I3(op1_IBUF[21]),
        .I4(op2_IBUF[4]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[21]_inst_i_13_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[21]_inst_i_2 
       (.I0(\result_OBUF[21]_inst_i_4_n_0 ),
        .I1(data3[21]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[21]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[21]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[21]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[21]_inst_i_5_n_0 ),
        .I4(\result_OBUF[21]_inst_i_6_n_0 ),
        .I5(data2[21]),
        .O(\result_OBUF[21]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[21]_inst_i_4 
       (.I0(op2_IBUF[21]),
        .I1(op1_IBUF[21]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[21]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[21]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[21]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[21]_inst_i_7_n_0 ),
        .I2(\result_OBUF[22]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[21]),
        .O(\result_OBUF[21]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[21]_inst_i_6 
       (.I0(\result_OBUF[22]_inst_i_9_n_0 ),
        .I1(\result_OBUF[21]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[21]_inst_i_9_n_0 ),
        .I5(\result_OBUF[22]_inst_i_8_n_0 ),
        .O(\result_OBUF[21]_inst_i_6_n_0 ));
  LUT5 #(
    .INIT(32'hB8BBB888)) 
    \result_OBUF[21]_inst_i_7 
       (.I0(\result_OBUF[23]_inst_i_20_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[21]_inst_i_10_n_0 ),
        .I3(op2_IBUF[2]),
        .I4(\result_OBUF[21]_inst_i_11_n_0 ),
        .O(\result_OBUF[21]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[21]_inst_i_8 
       (.I0(\result_OBUF[21]_inst_i_12_n_0 ),
        .I1(\result_OBUF[25]_inst_i_11_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[23]_inst_i_21_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[27]_inst_i_17_n_0 ),
        .O(\result_OBUF[21]_inst_i_8_n_0 ));
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[21]_inst_i_9 
       (.I0(\result_OBUF[23]_inst_i_22_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[21]_inst_i_13_n_0 ),
        .O(\result_OBUF[21]_inst_i_9_n_0 ));
  OBUF \result_OBUF[22]_inst 
       (.I(result_OBUF[22]),
        .O(result[22]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[22]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[22]),
        .I2(op1_IBUF[22]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[22]_inst_i_2_n_0 ),
        .I5(\result_OBUF[22]_inst_i_3_n_0 ),
        .O(result_OBUF[22]));
  (* SOFT_HLUTNM = "soft_lutpair27" *) 
  LUT4 #(
    .INIT(16'hF0E2)) 
    \result_OBUF[22]_inst_i_10 
       (.I0(op1_IBUF[26]),
        .I1(op2_IBUF[4]),
        .I2(op1_IBUF[31]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[22]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair12" *) 
  LUT5 #(
    .INIT(32'hFF00B8B8)) 
    \result_OBUF[22]_inst_i_11 
       (.I0(op1_IBUF[30]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[22]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[4]),
        .O(\result_OBUF[22]_inst_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair22" *) 
  LUT4 #(
    .INIT(16'h0A0C)) 
    \result_OBUF[22]_inst_i_12 
       (.I0(op1_IBUF[7]),
        .I1(op1_IBUF[15]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .O(\result_OBUF[22]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'h000030300000BB88)) 
    \result_OBUF[22]_inst_i_13 
       (.I0(op1_IBUF[26]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[30]),
        .I3(op1_IBUF[22]),
        .I4(op2_IBUF[4]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[22]_inst_i_13_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[22]_inst_i_2 
       (.I0(\result_OBUF[22]_inst_i_4_n_0 ),
        .I1(data3[22]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[22]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[22]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[22]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[22]_inst_i_5_n_0 ),
        .I4(\result_OBUF[22]_inst_i_6_n_0 ),
        .I5(data2[22]),
        .O(\result_OBUF[22]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[22]_inst_i_4 
       (.I0(op1_IBUF[22]),
        .I1(op2_IBUF[22]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[22]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[22]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[22]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[22]_inst_i_7_n_0 ),
        .I2(\result_OBUF[23]_inst_i_17_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[22]),
        .O(\result_OBUF[22]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[22]_inst_i_6 
       (.I0(\result_OBUF[23]_inst_i_19_n_0 ),
        .I1(\result_OBUF[22]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[22]_inst_i_9_n_0 ),
        .I5(\result_OBUF[23]_inst_i_18_n_0 ),
        .O(\result_OBUF[22]_inst_i_6_n_0 ));
  LUT5 #(
    .INIT(32'hB8BBB888)) 
    \result_OBUF[22]_inst_i_7 
       (.I0(\result_OBUF[24]_inst_i_10_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[22]_inst_i_10_n_0 ),
        .I3(op2_IBUF[2]),
        .I4(\result_OBUF[22]_inst_i_11_n_0 ),
        .O(\result_OBUF[22]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[22]_inst_i_8 
       (.I0(\result_OBUF[22]_inst_i_12_n_0 ),
        .I1(\result_OBUF[26]_inst_i_11_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[24]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[28]_inst_i_14_n_0 ),
        .O(\result_OBUF[22]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hB080FFFFB0800000)) 
    \result_OBUF[22]_inst_i_9 
       (.I0(op1_IBUF[28]),
        .I1(op2_IBUF[2]),
        .I2(\result_OBUF[30]_inst_i_26_n_0 ),
        .I3(op1_IBUF[24]),
        .I4(op2_IBUF[1]),
        .I5(\result_OBUF[22]_inst_i_13_n_0 ),
        .O(\result_OBUF[22]_inst_i_9_n_0 ));
  OBUF \result_OBUF[23]_inst 
       (.I(result_OBUF[23]),
        .O(result[23]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[23]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[23]),
        .I2(op2_IBUF[23]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[23]_inst_i_2_n_0 ),
        .I5(\result_OBUF[23]_inst_i_3_n_0 ),
        .O(result_OBUF[23]));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[23]_inst_i_10 
       (.I0(op1_IBUF[22]),
        .I1(op2_IBUF[22]),
        .O(\result_OBUF[23]_inst_i_10_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[23]_inst_i_11 
       (.I0(op1_IBUF[21]),
        .I1(op2_IBUF[21]),
        .O(\result_OBUF[23]_inst_i_11_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[23]_inst_i_12 
       (.I0(op1_IBUF[20]),
        .I1(op2_IBUF[20]),
        .O(\result_OBUF[23]_inst_i_12_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[23]_inst_i_13 
       (.I0(op1_IBUF[23]),
        .I1(op2_IBUF[23]),
        .O(\result_OBUF[23]_inst_i_13_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[23]_inst_i_14 
       (.I0(op2_IBUF[22]),
        .I1(op1_IBUF[22]),
        .O(\result_OBUF[23]_inst_i_14_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[23]_inst_i_15 
       (.I0(op1_IBUF[21]),
        .I1(op2_IBUF[21]),
        .O(\result_OBUF[23]_inst_i_15_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[23]_inst_i_16 
       (.I0(op2_IBUF[20]),
        .I1(op1_IBUF[20]),
        .O(\result_OBUF[23]_inst_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair32" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[23]_inst_i_17 
       (.I0(\result_OBUF[25]_inst_i_10_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[23]_inst_i_20_n_0 ),
        .O(\result_OBUF[23]_inst_i_17_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[23]_inst_i_18 
       (.I0(\result_OBUF[23]_inst_i_21_n_0 ),
        .I1(\result_OBUF[27]_inst_i_17_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[25]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[29]_inst_i_11_n_0 ),
        .O(\result_OBUF[23]_inst_i_18_n_0 ));
  LUT6 #(
    .INIT(64'hB080FFFFB0800000)) 
    \result_OBUF[23]_inst_i_19 
       (.I0(op1_IBUF[29]),
        .I1(op2_IBUF[2]),
        .I2(\result_OBUF[30]_inst_i_26_n_0 ),
        .I3(op1_IBUF[25]),
        .I4(op2_IBUF[1]),
        .I5(\result_OBUF[23]_inst_i_22_n_0 ),
        .O(\result_OBUF[23]_inst_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[23]_inst_i_2 
       (.I0(\result_OBUF[23]_inst_i_4_n_0 ),
        .I1(data3[23]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[23]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[23]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hFFFF0000FFB800B8)) 
    \result_OBUF[23]_inst_i_20 
       (.I0(op1_IBUF[27]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[23]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[31]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[23]_inst_i_20_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair13" *) 
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[23]_inst_i_21 
       (.I0(op1_IBUF[8]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[0]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[16]),
        .O(\result_OBUF[23]_inst_i_21_n_0 ));
  LUT6 #(
    .INIT(64'h000030300000BB88)) 
    \result_OBUF[23]_inst_i_22 
       (.I0(op1_IBUF[27]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[31]),
        .I3(op1_IBUF[23]),
        .I4(op2_IBUF[4]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[23]_inst_i_22_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[23]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[23]_inst_i_7_n_0 ),
        .I4(\result_OBUF[23]_inst_i_8_n_0 ),
        .I5(data2[23]),
        .O(\result_OBUF[23]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[23]_inst_i_4 
       (.I0(op2_IBUF[23]),
        .I1(op1_IBUF[23]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[23]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[23]_inst_i_4_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[23]_inst_i_5 
       (.CI(\result_OBUF[19]_inst_i_5_n_0 ),
        .CO({\result_OBUF[23]_inst_i_5_n_0 ,\NLW_result_OBUF[23]_inst_i_5_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[23:20]),
        .O(data3[23:20]),
        .S({\result_OBUF[23]_inst_i_9_n_0 ,\result_OBUF[23]_inst_i_10_n_0 ,\result_OBUF[23]_inst_i_11_n_0 ,\result_OBUF[23]_inst_i_12_n_0 }));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[23]_inst_i_6 
       (.CI(\result_OBUF[19]_inst_i_6_n_0 ),
        .CO({\result_OBUF[23]_inst_i_6_n_0 ,\NLW_result_OBUF[23]_inst_i_6_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[23:20]),
        .O(data2[23:20]),
        .S({\result_OBUF[23]_inst_i_13_n_0 ,\result_OBUF[23]_inst_i_14_n_0 ,\result_OBUF[23]_inst_i_15_n_0 ,\result_OBUF[23]_inst_i_16_n_0 }));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[23]_inst_i_7 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[23]_inst_i_17_n_0 ),
        .I2(\result_OBUF[24]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[23]),
        .O(\result_OBUF[23]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[23]_inst_i_8 
       (.I0(\result_OBUF[24]_inst_i_9_n_0 ),
        .I1(\result_OBUF[23]_inst_i_18_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[23]_inst_i_19_n_0 ),
        .I5(\result_OBUF[24]_inst_i_8_n_0 ),
        .O(\result_OBUF[23]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[23]_inst_i_9 
       (.I0(op1_IBUF[23]),
        .I1(op2_IBUF[23]),
        .O(\result_OBUF[23]_inst_i_9_n_0 ));
  OBUF \result_OBUF[24]_inst 
       (.I(result_OBUF[24]),
        .O(result[24]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[24]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[24]),
        .I2(op1_IBUF[24]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[24]_inst_i_2_n_0 ),
        .I5(\result_OBUF[24]_inst_i_3_n_0 ),
        .O(result_OBUF[24]));
  LUT6 #(
    .INIT(64'hFFFF0000FFB800B8)) 
    \result_OBUF[24]_inst_i_10 
       (.I0(op1_IBUF[28]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[24]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[31]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[24]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair21" *) 
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[24]_inst_i_11 
       (.I0(op1_IBUF[9]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[1]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[17]),
        .O(\result_OBUF[24]_inst_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT5 #(
    .INIT(32'h000B0008)) 
    \result_OBUF[24]_inst_i_12 
       (.I0(op1_IBUF[28]),
        .I1(op2_IBUF[2]),
        .I2(op2_IBUF[3]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[24]),
        .O(\result_OBUF[24]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[24]_inst_i_2 
       (.I0(\result_OBUF[24]_inst_i_4_n_0 ),
        .I1(data3[24]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[24]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[24]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[24]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[24]_inst_i_5_n_0 ),
        .I4(\result_OBUF[24]_inst_i_6_n_0 ),
        .I5(data2[24]),
        .O(\result_OBUF[24]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[24]_inst_i_4 
       (.I0(op1_IBUF[24]),
        .I1(op2_IBUF[24]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[24]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[24]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[24]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[24]_inst_i_7_n_0 ),
        .I2(\result_OBUF[25]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[24]),
        .O(\result_OBUF[24]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[24]_inst_i_6 
       (.I0(\result_OBUF[25]_inst_i_9_n_0 ),
        .I1(\result_OBUF[24]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[24]_inst_i_9_n_0 ),
        .I5(\result_OBUF[25]_inst_i_8_n_0 ),
        .O(\result_OBUF[24]_inst_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair34" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[24]_inst_i_7 
       (.I0(\result_OBUF[26]_inst_i_10_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[24]_inst_i_10_n_0 ),
        .O(\result_OBUF[24]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[24]_inst_i_8 
       (.I0(\result_OBUF[24]_inst_i_11_n_0 ),
        .I1(\result_OBUF[28]_inst_i_14_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[26]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_27_n_0 ),
        .O(\result_OBUF[24]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hB080FFFFB0800000)) 
    \result_OBUF[24]_inst_i_9 
       (.I0(op1_IBUF[30]),
        .I1(op2_IBUF[2]),
        .I2(\result_OBUF[30]_inst_i_26_n_0 ),
        .I3(op1_IBUF[26]),
        .I4(op2_IBUF[1]),
        .I5(\result_OBUF[24]_inst_i_12_n_0 ),
        .O(\result_OBUF[24]_inst_i_9_n_0 ));
  OBUF \result_OBUF[25]_inst 
       (.I(result_OBUF[25]),
        .O(result[25]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[25]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[25]),
        .I2(op2_IBUF[25]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[25]_inst_i_2_n_0 ),
        .I5(\result_OBUF[25]_inst_i_3_n_0 ),
        .O(result_OBUF[25]));
  LUT6 #(
    .INIT(64'hFFFF0000FFB800B8)) 
    \result_OBUF[25]_inst_i_10 
       (.I0(op1_IBUF[29]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[25]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[31]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[25]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair16" *) 
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[25]_inst_i_11 
       (.I0(op1_IBUF[10]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[2]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[18]),
        .O(\result_OBUF[25]_inst_i_11_n_0 ));
  LUT5 #(
    .INIT(32'h000B0008)) 
    \result_OBUF[25]_inst_i_12 
       (.I0(op1_IBUF[29]),
        .I1(op2_IBUF[2]),
        .I2(op2_IBUF[3]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[25]),
        .O(\result_OBUF[25]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[25]_inst_i_2 
       (.I0(\result_OBUF[25]_inst_i_4_n_0 ),
        .I1(data3[25]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[25]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[25]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[25]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[25]_inst_i_5_n_0 ),
        .I4(\result_OBUF[25]_inst_i_6_n_0 ),
        .I5(data2[25]),
        .O(\result_OBUF[25]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[25]_inst_i_4 
       (.I0(op2_IBUF[25]),
        .I1(op1_IBUF[25]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[25]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[25]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[25]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[25]_inst_i_7_n_0 ),
        .I2(\result_OBUF[26]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[25]),
        .O(\result_OBUF[25]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[25]_inst_i_6 
       (.I0(\result_OBUF[26]_inst_i_9_n_0 ),
        .I1(\result_OBUF[25]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[25]_inst_i_9_n_0 ),
        .I5(\result_OBUF[26]_inst_i_8_n_0 ),
        .O(\result_OBUF[25]_inst_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair29" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[25]_inst_i_7 
       (.I0(\result_OBUF[27]_inst_i_16_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[25]_inst_i_10_n_0 ),
        .O(\result_OBUF[25]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[25]_inst_i_8 
       (.I0(\result_OBUF[25]_inst_i_11_n_0 ),
        .I1(\result_OBUF[29]_inst_i_11_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[27]_inst_i_17_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_33_n_0 ),
        .O(\result_OBUF[25]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hB080FFFFB0800000)) 
    \result_OBUF[25]_inst_i_9 
       (.I0(op1_IBUF[31]),
        .I1(op2_IBUF[2]),
        .I2(\result_OBUF[30]_inst_i_26_n_0 ),
        .I3(op1_IBUF[27]),
        .I4(op2_IBUF[1]),
        .I5(\result_OBUF[25]_inst_i_12_n_0 ),
        .O(\result_OBUF[25]_inst_i_9_n_0 ));
  OBUF \result_OBUF[26]_inst 
       (.I(result_OBUF[26]),
        .O(result[26]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[26]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[26]),
        .I2(op1_IBUF[26]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[26]_inst_i_2_n_0 ),
        .I5(\result_OBUF[26]_inst_i_3_n_0 ),
        .O(result_OBUF[26]));
  LUT6 #(
    .INIT(64'hFFFF0000FFB800B8)) 
    \result_OBUF[26]_inst_i_10 
       (.I0(op1_IBUF[30]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[26]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[31]),
        .I5(op2_IBUF[3]),
        .O(\result_OBUF[26]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair23" *) 
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[26]_inst_i_11 
       (.I0(op1_IBUF[11]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[3]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[19]),
        .O(\result_OBUF[26]_inst_i_11_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[26]_inst_i_2 
       (.I0(\result_OBUF[26]_inst_i_4_n_0 ),
        .I1(data3[26]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[26]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[26]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[26]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[26]_inst_i_5_n_0 ),
        .I4(\result_OBUF[26]_inst_i_6_n_0 ),
        .I5(data2[26]),
        .O(\result_OBUF[26]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[26]_inst_i_4 
       (.I0(op1_IBUF[26]),
        .I1(op2_IBUF[26]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[26]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[26]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[26]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[26]_inst_i_7_n_0 ),
        .I2(\result_OBUF[27]_inst_i_12_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[26]),
        .O(\result_OBUF[26]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[26]_inst_i_6 
       (.I0(\result_OBUF[27]_inst_i_14_n_0 ),
        .I1(\result_OBUF[26]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[26]_inst_i_9_n_0 ),
        .I5(\result_OBUF[27]_inst_i_13_n_0 ),
        .O(\result_OBUF[26]_inst_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair31" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[26]_inst_i_7 
       (.I0(\result_OBUF[28]_inst_i_13_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[26]_inst_i_10_n_0 ),
        .O(\result_OBUF[26]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[26]_inst_i_8 
       (.I0(\result_OBUF[26]_inst_i_11_n_0 ),
        .I1(\result_OBUF[30]_inst_i_27_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[28]_inst_i_14_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_29_n_0 ),
        .O(\result_OBUF[26]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'h30BB000030880000)) 
    \result_OBUF[26]_inst_i_9 
       (.I0(op1_IBUF[28]),
        .I1(op2_IBUF[1]),
        .I2(op1_IBUF[30]),
        .I3(op2_IBUF[2]),
        .I4(\result_OBUF[30]_inst_i_26_n_0 ),
        .I5(op1_IBUF[26]),
        .O(\result_OBUF[26]_inst_i_9_n_0 ));
  OBUF \result_OBUF[27]_inst 
       (.I(result_OBUF[27]),
        .O(result[27]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[27]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[27]),
        .I2(op2_IBUF[27]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[27]_inst_i_2_n_0 ),
        .I5(\result_OBUF[27]_inst_i_3_n_0 ),
        .O(result_OBUF[27]));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[27]_inst_i_10 
       (.I0(op1_IBUF[25]),
        .I1(op2_IBUF[25]),
        .O(\result_OBUF[27]_inst_i_10_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[27]_inst_i_11 
       (.I0(op1_IBUF[24]),
        .I1(op2_IBUF[24]),
        .O(\result_OBUF[27]_inst_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair29" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[27]_inst_i_12 
       (.I0(\result_OBUF[27]_inst_i_15_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[27]_inst_i_16_n_0 ),
        .O(\result_OBUF[27]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[27]_inst_i_13 
       (.I0(\result_OBUF[27]_inst_i_17_n_0 ),
        .I1(\result_OBUF[30]_inst_i_33_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[29]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_32_n_0 ),
        .O(\result_OBUF[27]_inst_i_13_n_0 ));
  LUT6 #(
    .INIT(64'h30BB000030880000)) 
    \result_OBUF[27]_inst_i_14 
       (.I0(op1_IBUF[29]),
        .I1(op2_IBUF[1]),
        .I2(op1_IBUF[31]),
        .I3(op2_IBUF[2]),
        .I4(\result_OBUF[30]_inst_i_26_n_0 ),
        .I5(op1_IBUF[27]),
        .O(\result_OBUF[27]_inst_i_14_n_0 ));
  LUT5 #(
    .INIT(32'hFF00FE02)) 
    \result_OBUF[27]_inst_i_15 
       (.I0(op1_IBUF[29]),
        .I1(op2_IBUF[4]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[2]),
        .O(\result_OBUF[27]_inst_i_15_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair15" *) 
  LUT5 #(
    .INIT(32'hFF00FE02)) 
    \result_OBUF[27]_inst_i_16 
       (.I0(op1_IBUF[27]),
        .I1(op2_IBUF[4]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[2]),
        .O(\result_OBUF[27]_inst_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[27]_inst_i_17 
       (.I0(op1_IBUF[12]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[4]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[20]),
        .O(\result_OBUF[27]_inst_i_17_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[27]_inst_i_2 
       (.I0(\result_OBUF[27]_inst_i_4_n_0 ),
        .I1(data3[27]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[27]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[27]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[27]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[27]_inst_i_6_n_0 ),
        .I4(\result_OBUF[27]_inst_i_7_n_0 ),
        .I5(data2[27]),
        .O(\result_OBUF[27]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[27]_inst_i_4 
       (.I0(op2_IBUF[27]),
        .I1(op1_IBUF[27]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[27]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[27]_inst_i_4_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[27]_inst_i_5 
       (.CI(\result_OBUF[23]_inst_i_5_n_0 ),
        .CO({\result_OBUF[27]_inst_i_5_n_0 ,\NLW_result_OBUF[27]_inst_i_5_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[27:24]),
        .O(data3[27:24]),
        .S({\result_OBUF[27]_inst_i_8_n_0 ,\result_OBUF[27]_inst_i_9_n_0 ,\result_OBUF[27]_inst_i_10_n_0 ,\result_OBUF[27]_inst_i_11_n_0 }));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[27]_inst_i_6 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[27]_inst_i_12_n_0 ),
        .I2(\result_OBUF[28]_inst_i_9_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[27]),
        .O(\result_OBUF[27]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[27]_inst_i_7 
       (.I0(\result_OBUF[28]_inst_i_11_n_0 ),
        .I1(\result_OBUF[27]_inst_i_13_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[27]_inst_i_14_n_0 ),
        .I5(\result_OBUF[28]_inst_i_10_n_0 ),
        .O(\result_OBUF[27]_inst_i_7_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[27]_inst_i_8 
       (.I0(op1_IBUF[27]),
        .I1(op2_IBUF[27]),
        .O(\result_OBUF[27]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[27]_inst_i_9 
       (.I0(op1_IBUF[26]),
        .I1(op2_IBUF[26]),
        .O(\result_OBUF[27]_inst_i_9_n_0 ));
  OBUF \result_OBUF[28]_inst 
       (.I(result_OBUF[28]),
        .O(result[28]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[28]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[28]),
        .I2(op1_IBUF[28]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[28]_inst_i_3_n_0 ),
        .I5(\result_OBUF[28]_inst_i_4_n_0 ),
        .O(result_OBUF[28]));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[28]_inst_i_10 
       (.I0(\result_OBUF[28]_inst_i_14_n_0 ),
        .I1(\result_OBUF[30]_inst_i_29_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[30]_inst_i_27_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_28_n_0 ),
        .O(\result_OBUF[28]_inst_i_10_n_0 ));
  LUT6 #(
    .INIT(64'h0000020200000300)) 
    \result_OBUF[28]_inst_i_11 
       (.I0(op1_IBUF[30]),
        .I1(op2_IBUF[3]),
        .I2(op2_IBUF[4]),
        .I3(op1_IBUF[28]),
        .I4(op2_IBUF[2]),
        .I5(op2_IBUF[1]),
        .O(\result_OBUF[28]_inst_i_11_n_0 ));
  LUT5 #(
    .INIT(32'hFF00FE02)) 
    \result_OBUF[28]_inst_i_12 
       (.I0(op1_IBUF[30]),
        .I1(op2_IBUF[4]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[2]),
        .O(\result_OBUF[28]_inst_i_12_n_0 ));
  LUT5 #(
    .INIT(32'hFF00FE02)) 
    \result_OBUF[28]_inst_i_13 
       (.I0(op1_IBUF[28]),
        .I1(op2_IBUF[4]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[31]),
        .I4(op2_IBUF[2]),
        .O(\result_OBUF[28]_inst_i_13_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair20" *) 
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[28]_inst_i_14 
       (.I0(op1_IBUF[13]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[5]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[21]),
        .O(\result_OBUF[28]_inst_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair33" *) 
  LUT3 #(
    .INIT(8'h01)) 
    \result_OBUF[28]_inst_i_2 
       (.I0(alu_op_IBUF[2]),
        .I1(alu_op_IBUF[1]),
        .I2(alu_op_IBUF[3]),
        .O(\result_OBUF[28]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[28]_inst_i_3 
       (.I0(\result_OBUF[28]_inst_i_5_n_0 ),
        .I1(data3[28]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[28]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[28]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[28]_inst_i_4 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[28]_inst_i_7_n_0 ),
        .I4(\result_OBUF[28]_inst_i_8_n_0 ),
        .I5(data2[28]),
        .O(\result_OBUF[28]_inst_i_4_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[28]_inst_i_5 
       (.I0(op1_IBUF[28]),
        .I1(op2_IBUF[28]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[28]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[28]_inst_i_5_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair30" *) 
  LUT3 #(
    .INIT(8'h04)) 
    \result_OBUF[28]_inst_i_6 
       (.I0(alu_op_IBUF[0]),
        .I1(alu_op_IBUF[1]),
        .I2(alu_op_IBUF[3]),
        .O(\result_OBUF[28]_inst_i_6_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[28]_inst_i_7 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[28]_inst_i_9_n_0 ),
        .I2(\result_OBUF[29]_inst_i_8_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[28]),
        .O(\result_OBUF[28]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[28]_inst_i_8 
       (.I0(\result_OBUF[29]_inst_i_6_n_0 ),
        .I1(\result_OBUF[28]_inst_i_10_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[28]_inst_i_11_n_0 ),
        .I5(\result_OBUF[29]_inst_i_10_n_0 ),
        .O(\result_OBUF[28]_inst_i_8_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair31" *) 
  LUT3 #(
    .INIT(8'hB8)) 
    \result_OBUF[28]_inst_i_9 
       (.I0(\result_OBUF[28]_inst_i_12_n_0 ),
        .I1(op2_IBUF[1]),
        .I2(\result_OBUF[28]_inst_i_13_n_0 ),
        .O(\result_OBUF[28]_inst_i_9_n_0 ));
  OBUF \result_OBUF[29]_inst 
       (.I(result_OBUF[29]),
        .O(result[29]));
  LUT6 #(
    .INIT(64'hFFFFFFAEAAAAAAAA)) 
    \result_OBUF[29]_inst_i_1 
       (.I0(\result_OBUF[29]_inst_i_2_n_0 ),
        .I1(data2[29]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[29]_inst_i_3_n_0 ),
        .I4(\result_OBUF[29]_inst_i_4_n_0 ),
        .I5(\result_OBUF[30]_inst_i_7_n_0 ),
        .O(result_OBUF[29]));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[29]_inst_i_10 
       (.I0(\result_OBUF[29]_inst_i_11_n_0 ),
        .I1(\result_OBUF[30]_inst_i_32_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[30]_inst_i_33_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_34_n_0 ),
        .O(\result_OBUF[29]_inst_i_10_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair14" *) 
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[29]_inst_i_11 
       (.I0(op1_IBUF[14]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[6]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[22]),
        .O(\result_OBUF[29]_inst_i_11_n_0 ));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    \result_OBUF[29]_inst_i_2 
       (.I0(\result_OBUF[29]_inst_i_5_n_0 ),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op2_IBUF[29]),
        .I3(op1_IBUF[29]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(\result_OBUF[29]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAAAAAAAA000088A0)) 
    \result_OBUF[29]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_17_n_0 ),
        .I1(\result_OBUF[30]_inst_i_19_n_0 ),
        .I2(\result_OBUF[29]_inst_i_6_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(op2_IBUF[0]),
        .I5(\result_OBUF[29]_inst_i_7_n_0 ),
        .O(\result_OBUF[29]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'h8A808A808A8A8080)) 
    \result_OBUF[29]_inst_i_4 
       (.I0(\result_OBUF[30]_inst_i_15_n_0 ),
        .I1(data2[29]),
        .I2(alu_op_IBUF[0]),
        .I3(\result_OBUF[30]_inst_i_16_n_0 ),
        .I4(\result_OBUF[29]_inst_i_8_n_0 ),
        .I5(op2_IBUF[0]),
        .O(\result_OBUF[29]_inst_i_4_n_0 ));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    \result_OBUF[29]_inst_i_5 
       (.I0(data3[29]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[29]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(\result_OBUF[29]_inst_i_9_n_0 ),
        .O(\result_OBUF[29]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'h0000020200000300)) 
    \result_OBUF[29]_inst_i_6 
       (.I0(op1_IBUF[31]),
        .I1(op2_IBUF[3]),
        .I2(op2_IBUF[4]),
        .I3(op1_IBUF[29]),
        .I4(op2_IBUF[2]),
        .I5(op2_IBUF[1]),
        .O(\result_OBUF[29]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAAAA0000C0000000)) 
    \result_OBUF[29]_inst_i_7 
       (.I0(\result_OBUF[29]_inst_i_10_n_0 ),
        .I1(\result_OBUF[1]_inst_i_11_n_0 ),
        .I2(op1_IBUF[30]),
        .I3(\result_OBUF[30]_inst_i_26_n_0 ),
        .I4(op2_IBUF[0]),
        .I5(alu_op_IBUF[0]),
        .O(\result_OBUF[29]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hFFFF0000FFFE0004)) 
    \result_OBUF[29]_inst_i_8 
       (.I0(op2_IBUF[1]),
        .I1(op1_IBUF[29]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .I4(op1_IBUF[31]),
        .I5(op2_IBUF[2]),
        .O(\result_OBUF[29]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[29]_inst_i_9 
       (.I0(op2_IBUF[29]),
        .I1(op1_IBUF[29]),
        .O(\result_OBUF[29]_inst_i_9_n_0 ));
  OBUF \result_OBUF[2]_inst 
       (.I(result_OBUF[2]),
        .O(result[2]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[2]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[2]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[2]_inst_i_2_n_0 ),
        .I5(\result_OBUF[2]_inst_i_3_n_0 ),
        .O(result_OBUF[2]));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[2]_inst_i_2 
       (.I0(\result_OBUF[2]_inst_i_4_n_0 ),
        .I1(data3[2]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[2]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[2]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[2]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[2]_inst_i_5_n_0 ),
        .I4(\result_OBUF[2]_inst_i_6_n_0 ),
        .I5(data2[2]),
        .O(\result_OBUF[2]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[2]_inst_i_4 
       (.I0(op1_IBUF[2]),
        .I1(op2_IBUF[2]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[2]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[2]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[2]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[1]_inst_i_16_n_0 ),
        .I2(\result_OBUF[3]_inst_i_12_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[2]),
        .O(\result_OBUF[2]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[2]_inst_i_6 
       (.I0(\result_OBUF[3]_inst_i_14_n_0 ),
        .I1(\result_OBUF[2]_inst_i_7_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[2]_inst_i_8_n_0 ),
        .I5(\result_OBUF[3]_inst_i_13_n_0 ),
        .O(\result_OBUF[2]_inst_i_6_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair7" *) 
  LUT5 #(
    .INIT(32'h00000010)) 
    \result_OBUF[2]_inst_i_7 
       (.I0(op2_IBUF[1]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[1]),
        .I3(op2_IBUF[4]),
        .I4(op2_IBUF[3]),
        .O(\result_OBUF[2]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[2]_inst_i_8 
       (.I0(\result_OBUF[8]_inst_i_11_n_0 ),
        .I1(\result_OBUF[1]_inst_i_19_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[1]_inst_i_20_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[1]_inst_i_21_n_0 ),
        .O(\result_OBUF[2]_inst_i_8_n_0 ));
  OBUF \result_OBUF[30]_inst 
       (.I(result_OBUF[30]),
        .O(result[30]));
  LUT6 #(
    .INIT(64'hFFFFFFAEAAAAAAAA)) 
    \result_OBUF[30]_inst_i_1 
       (.I0(\result_OBUF[30]_inst_i_2_n_0 ),
        .I1(data2[30]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[30]_inst_i_5_n_0 ),
        .I4(\result_OBUF[30]_inst_i_6_n_0 ),
        .I5(\result_OBUF[30]_inst_i_7_n_0 ),
        .O(result_OBUF[30]));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[30]_inst_i_10 
       (.CI(\result_OBUF[23]_inst_i_6_n_0 ),
        .CO({\result_OBUF[30]_inst_i_10_n_0 ,\NLW_result_OBUF[30]_inst_i_10_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[27:24]),
        .O(data2[27:24]),
        .S({\result_OBUF[30]_inst_i_22_n_0 ,\result_OBUF[30]_inst_i_23_n_0 ,\result_OBUF[30]_inst_i_24_n_0 ,\result_OBUF[30]_inst_i_25_n_0 }));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[30]_inst_i_11 
       (.I0(op1_IBUF[31]),
        .I1(op2_IBUF[31]),
        .O(\result_OBUF[30]_inst_i_11_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[30]_inst_i_12 
       (.I0(op2_IBUF[30]),
        .I1(op1_IBUF[30]),
        .O(\result_OBUF[30]_inst_i_12_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[30]_inst_i_13 
       (.I0(op1_IBUF[29]),
        .I1(op2_IBUF[29]),
        .O(\result_OBUF[30]_inst_i_13_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[30]_inst_i_14 
       (.I0(op2_IBUF[28]),
        .I1(op1_IBUF[28]),
        .O(\result_OBUF[30]_inst_i_14_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair33" *) 
  LUT2 #(
    .INIT(4'h8)) 
    \result_OBUF[30]_inst_i_15 
       (.I0(alu_op_IBUF[3]),
        .I1(alu_op_IBUF[1]),
        .O(\result_OBUF[30]_inst_i_15_n_0 ));
  LUT6 #(
    .INIT(64'hFFFF0000FFFE0004)) 
    \result_OBUF[30]_inst_i_16 
       (.I0(op2_IBUF[1]),
        .I1(op1_IBUF[30]),
        .I2(op2_IBUF[4]),
        .I3(op2_IBUF[3]),
        .I4(op1_IBUF[31]),
        .I5(op2_IBUF[2]),
        .O(\result_OBUF[30]_inst_i_16_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair30" *) 
  LUT3 #(
    .INIT(8'h0E)) 
    \result_OBUF[30]_inst_i_17 
       (.I0(alu_op_IBUF[0]),
        .I1(alu_op_IBUF[3]),
        .I2(alu_op_IBUF[1]),
        .O(\result_OBUF[30]_inst_i_17_n_0 ));
  LUT6 #(
    .INIT(64'h000088000000C000)) 
    \result_OBUF[30]_inst_i_18 
       (.I0(op1_IBUF[31]),
        .I1(\result_OBUF[1]_inst_i_11_n_0 ),
        .I2(op1_IBUF[30]),
        .I3(\result_OBUF[30]_inst_i_26_n_0 ),
        .I4(alu_op_IBUF[0]),
        .I5(op2_IBUF[0]),
        .O(\result_OBUF[30]_inst_i_18_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[30]_inst_i_19 
       (.I0(\result_OBUF[30]_inst_i_27_n_0 ),
        .I1(\result_OBUF[30]_inst_i_28_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[30]_inst_i_29_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_30_n_0 ),
        .O(\result_OBUF[30]_inst_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    \result_OBUF[30]_inst_i_2 
       (.I0(\result_OBUF[30]_inst_i_8_n_0 ),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op1_IBUF[30]),
        .I3(op2_IBUF[30]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(\result_OBUF[30]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[30]_inst_i_20 
       (.I0(\result_OBUF[30]_inst_i_31_n_0 ),
        .I1(\result_OBUF[30]_inst_i_32_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[30]_inst_i_33_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_34_n_0 ),
        .O(\result_OBUF[30]_inst_i_20_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[30]_inst_i_21 
       (.I0(op1_IBUF[30]),
        .I1(op2_IBUF[30]),
        .O(\result_OBUF[30]_inst_i_21_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[30]_inst_i_22 
       (.I0(op1_IBUF[27]),
        .I1(op2_IBUF[27]),
        .O(\result_OBUF[30]_inst_i_22_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[30]_inst_i_23 
       (.I0(op2_IBUF[26]),
        .I1(op1_IBUF[26]),
        .O(\result_OBUF[30]_inst_i_23_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[30]_inst_i_24 
       (.I0(op1_IBUF[25]),
        .I1(op2_IBUF[25]),
        .O(\result_OBUF[30]_inst_i_24_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[30]_inst_i_25 
       (.I0(op2_IBUF[24]),
        .I1(op1_IBUF[24]),
        .O(\result_OBUF[30]_inst_i_25_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \result_OBUF[30]_inst_i_26 
       (.I0(op2_IBUF[4]),
        .I1(op2_IBUF[3]),
        .O(\result_OBUF[30]_inst_i_26_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair22" *) 
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[30]_inst_i_27 
       (.I0(op1_IBUF[15]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[7]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[23]),
        .O(\result_OBUF[30]_inst_i_27_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[30]_inst_i_28 
       (.I0(op1_IBUF[27]),
        .I1(op1_IBUF[11]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[3]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[19]),
        .O(\result_OBUF[30]_inst_i_28_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[30]_inst_i_29 
       (.I0(op1_IBUF[25]),
        .I1(op1_IBUF[9]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[1]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[17]),
        .O(\result_OBUF[30]_inst_i_29_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[30]_inst_i_3 
       (.CI(\result_OBUF[30]_inst_i_10_n_0 ),
        .CYINIT(\<const0> ),
        .DI({\<const0> ,op1_IBUF[30:28]}),
        .O(data2[31:28]),
        .S({\result_OBUF[30]_inst_i_11_n_0 ,\result_OBUF[30]_inst_i_12_n_0 ,\result_OBUF[30]_inst_i_13_n_0 ,\result_OBUF[30]_inst_i_14_n_0 }));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[30]_inst_i_30 
       (.I0(op1_IBUF[29]),
        .I1(op1_IBUF[13]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[5]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[21]),
        .O(\result_OBUF[30]_inst_i_30_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[30]_inst_i_31 
       (.I0(op1_IBUF[30]),
        .I1(op1_IBUF[14]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[6]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[22]),
        .O(\result_OBUF[30]_inst_i_31_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[30]_inst_i_32 
       (.I0(op1_IBUF[26]),
        .I1(op1_IBUF[10]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[2]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[18]),
        .O(\result_OBUF[30]_inst_i_32_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[30]_inst_i_33 
       (.I0(op1_IBUF[24]),
        .I1(op1_IBUF[8]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[0]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[16]),
        .O(\result_OBUF[30]_inst_i_33_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[30]_inst_i_34 
       (.I0(op1_IBUF[28]),
        .I1(op1_IBUF[12]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[4]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[20]),
        .O(\result_OBUF[30]_inst_i_34_n_0 ));
  LUT3 #(
    .INIT(8'hAE)) 
    \result_OBUF[30]_inst_i_4 
       (.I0(alu_op_IBUF[3]),
        .I1(alu_op_IBUF[0]),
        .I2(alu_op_IBUF[1]),
        .O(\result_OBUF[30]_inst_i_4_n_0 ));
  LUT6 #(
    .INIT(64'h8A808A808A8A8080)) 
    \result_OBUF[30]_inst_i_5 
       (.I0(\result_OBUF[30]_inst_i_15_n_0 ),
        .I1(data2[30]),
        .I2(alu_op_IBUF[0]),
        .I3(op1_IBUF[31]),
        .I4(\result_OBUF[30]_inst_i_16_n_0 ),
        .I5(op2_IBUF[0]),
        .O(\result_OBUF[30]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hA8A88888AA888888)) 
    \result_OBUF[30]_inst_i_6 
       (.I0(\result_OBUF[30]_inst_i_17_n_0 ),
        .I1(\result_OBUF[30]_inst_i_18_n_0 ),
        .I2(\result_OBUF[30]_inst_i_19_n_0 ),
        .I3(\result_OBUF[30]_inst_i_20_n_0 ),
        .I4(alu_op_IBUF[0]),
        .I5(op2_IBUF[0]),
        .O(\result_OBUF[30]_inst_i_6_n_0 ));
  LUT3 #(
    .INIT(8'h0E)) 
    \result_OBUF[30]_inst_i_7 
       (.I0(alu_op_IBUF[1]),
        .I1(alu_op_IBUF[3]),
        .I2(alu_op_IBUF[2]),
        .O(\result_OBUF[30]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    \result_OBUF[30]_inst_i_8 
       (.I0(data3[30]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[30]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(\result_OBUF[30]_inst_i_21_n_0 ),
        .O(\result_OBUF[30]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'hE)) 
    \result_OBUF[30]_inst_i_9 
       (.I0(alu_op_IBUF[3]),
        .I1(alu_op_IBUF[1]),
        .O(\result_OBUF[30]_inst_i_9_n_0 ));
  OBUF \result_OBUF[31]_inst 
       (.I(result_OBUF[31]),
        .O(result[31]));
  LUT4 #(
    .INIT(16'hBBB8)) 
    \result_OBUF[31]_inst_i_1 
       (.I0(\result_OBUF[31]_inst_i_2_n_0 ),
        .I1(alu_op_IBUF[2]),
        .I2(\result_OBUF[31]_inst_i_3_n_0 ),
        .I3(\result_OBUF[31]_inst_i_4_n_0 ),
        .O(result_OBUF[31]));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[31]_inst_i_10 
       (.I0(op1_IBUF[29]),
        .I1(op2_IBUF[29]),
        .O(\result_OBUF[31]_inst_i_10_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[31]_inst_i_11 
       (.I0(op1_IBUF[28]),
        .I1(op2_IBUF[28]),
        .O(\result_OBUF[31]_inst_i_11_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair15" *) 
  LUT3 #(
    .INIT(8'h10)) 
    \result_OBUF[31]_inst_i_12 
       (.I0(op2_IBUF[3]),
        .I1(op2_IBUF[4]),
        .I2(op1_IBUF[31]),
        .O(\result_OBUF[31]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[31]_inst_i_13 
       (.I0(\result_OBUF[31]_inst_i_14_n_0 ),
        .I1(\result_OBUF[30]_inst_i_28_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[30]_inst_i_29_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_30_n_0 ),
        .O(\result_OBUF[31]_inst_i_13_n_0 ));
  LUT6 #(
    .INIT(64'hFC0CFAFAFC0C0A0A)) 
    \result_OBUF[31]_inst_i_14 
       (.I0(op1_IBUF[31]),
        .I1(op1_IBUF[15]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[7]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[23]),
        .O(\result_OBUF[31]_inst_i_14_n_0 ));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    \result_OBUF[31]_inst_i_2 
       (.I0(data3[31]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[31]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(\result_OBUF[31]_inst_i_6_n_0 ),
        .O(\result_OBUF[31]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'h2323232023202020)) 
    \result_OBUF[31]_inst_i_3 
       (.I0(data2[31]),
        .I1(alu_op_IBUF[3]),
        .I2(alu_op_IBUF[1]),
        .I3(alu_op_IBUF[0]),
        .I4(op2_IBUF[31]),
        .I5(op1_IBUF[31]),
        .O(\result_OBUF[31]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hA2AA80AAA2008000)) 
    \result_OBUF[31]_inst_i_4 
       (.I0(alu_op_IBUF[3]),
        .I1(alu_op_IBUF[0]),
        .I2(data2[31]),
        .I3(alu_op_IBUF[1]),
        .I4(op1_IBUF[31]),
        .I5(\result_OBUF[31]_inst_i_7_n_0 ),
        .O(\result_OBUF[31]_inst_i_4_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[31]_inst_i_5 
       (.CI(\result_OBUF[27]_inst_i_5_n_0 ),
        .CYINIT(\<const0> ),
        .DI({\<const0> ,op1_IBUF[30:28]}),
        .O(data3[31:28]),
        .S({\result_OBUF[31]_inst_i_8_n_0 ,\result_OBUF[31]_inst_i_9_n_0 ,\result_OBUF[31]_inst_i_10_n_0 ,\result_OBUF[31]_inst_i_11_n_0 }));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[31]_inst_i_6 
       (.I0(op2_IBUF[31]),
        .I1(op1_IBUF[31]),
        .O(\result_OBUF[31]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hFF000000F0F08888)) 
    \result_OBUF[31]_inst_i_7 
       (.I0(\result_OBUF[31]_inst_i_12_n_0 ),
        .I1(\result_OBUF[1]_inst_i_11_n_0 ),
        .I2(\result_OBUF[31]_inst_i_13_n_0 ),
        .I3(\result_OBUF[30]_inst_i_20_n_0 ),
        .I4(alu_op_IBUF[0]),
        .I5(op2_IBUF[0]),
        .O(\result_OBUF[31]_inst_i_7_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[31]_inst_i_8 
       (.I0(op2_IBUF[31]),
        .I1(op1_IBUF[31]),
        .O(\result_OBUF[31]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[31]_inst_i_9 
       (.I0(op1_IBUF[30]),
        .I1(op2_IBUF[30]),
        .O(\result_OBUF[31]_inst_i_9_n_0 ));
  OBUF \result_OBUF[3]_inst 
       (.I(result_OBUF[3]),
        .O(result[3]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[3]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[3]),
        .I2(op2_IBUF[3]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[3]_inst_i_2_n_0 ),
        .I5(\result_OBUF[3]_inst_i_3_n_0 ),
        .O(result_OBUF[3]));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[3]_inst_i_10 
       (.I0(op1_IBUF[1]),
        .I1(op2_IBUF[1]),
        .O(\result_OBUF[3]_inst_i_10_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[3]_inst_i_11 
       (.I0(op1_IBUF[0]),
        .I1(op2_IBUF[0]),
        .O(\result_OBUF[3]_inst_i_11_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[3]_inst_i_12 
       (.I0(\result_OBUF[9]_inst_i_10_n_0 ),
        .I1(\result_OBUF[0]_inst_i_12_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[0]_inst_i_13_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[0]_inst_i_14_n_0 ),
        .O(\result_OBUF[3]_inst_i_12_n_0 ));
  LUT6 #(
    .INIT(64'h0000020200000300)) 
    \result_OBUF[3]_inst_i_13 
       (.I0(op1_IBUF[0]),
        .I1(op2_IBUF[3]),
        .I2(op2_IBUF[4]),
        .I3(op1_IBUF[2]),
        .I4(op2_IBUF[2]),
        .I5(op2_IBUF[1]),
        .O(\result_OBUF[3]_inst_i_13_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[3]_inst_i_14 
       (.I0(\result_OBUF[9]_inst_i_11_n_0 ),
        .I1(\result_OBUF[0]_inst_i_12_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[0]_inst_i_13_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[0]_inst_i_14_n_0 ),
        .O(\result_OBUF[3]_inst_i_14_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[3]_inst_i_2 
       (.I0(\result_OBUF[3]_inst_i_4_n_0 ),
        .I1(data3[3]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[3]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[3]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[3]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[3]_inst_i_6_n_0 ),
        .I4(\result_OBUF[3]_inst_i_7_n_0 ),
        .I5(data2[3]),
        .O(\result_OBUF[3]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[3]_inst_i_4 
       (.I0(op2_IBUF[3]),
        .I1(op1_IBUF[3]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[3]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[3]_inst_i_4_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[3]_inst_i_5 
       (.CI(\<const0> ),
        .CO({\result_OBUF[3]_inst_i_5_n_0 ,\NLW_result_OBUF[3]_inst_i_5_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const1> ),
        .DI(op1_IBUF[3:0]),
        .O(data3[3:0]),
        .S({\result_OBUF[3]_inst_i_8_n_0 ,\result_OBUF[3]_inst_i_9_n_0 ,\result_OBUF[3]_inst_i_10_n_0 ,\result_OBUF[3]_inst_i_11_n_0 }));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[3]_inst_i_6 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[3]_inst_i_12_n_0 ),
        .I2(\result_OBUF[4]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[3]),
        .O(\result_OBUF[3]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[3]_inst_i_7 
       (.I0(\result_OBUF[4]_inst_i_8_n_0 ),
        .I1(\result_OBUF[3]_inst_i_13_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[3]_inst_i_14_n_0 ),
        .I5(\result_OBUF[4]_inst_i_9_n_0 ),
        .O(\result_OBUF[3]_inst_i_7_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[3]_inst_i_8 
       (.I0(op1_IBUF[3]),
        .I1(op2_IBUF[3]),
        .O(\result_OBUF[3]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[3]_inst_i_9 
       (.I0(op1_IBUF[2]),
        .I1(op2_IBUF[2]),
        .O(\result_OBUF[3]_inst_i_9_n_0 ));
  OBUF \result_OBUF[4]_inst 
       (.I(result_OBUF[4]),
        .O(result[4]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[4]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[4]),
        .I2(op1_IBUF[4]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[4]_inst_i_2_n_0 ),
        .I5(\result_OBUF[4]_inst_i_3_n_0 ),
        .O(result_OBUF[4]));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[4]_inst_i_2 
       (.I0(\result_OBUF[4]_inst_i_4_n_0 ),
        .I1(data3[4]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[4]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[4]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[4]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[4]_inst_i_5_n_0 ),
        .I4(\result_OBUF[4]_inst_i_6_n_0 ),
        .I5(data2[4]),
        .O(\result_OBUF[4]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[4]_inst_i_4 
       (.I0(op1_IBUF[4]),
        .I1(op2_IBUF[4]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[4]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[4]_inst_i_4_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair4" *) 
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[4]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[4]_inst_i_7_n_0 ),
        .I2(\result_OBUF[5]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[4]),
        .O(\result_OBUF[4]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hFACFFAC00ACF0AC0)) 
    \result_OBUF[4]_inst_i_6 
       (.I0(\result_OBUF[5]_inst_i_8_n_0 ),
        .I1(\result_OBUF[5]_inst_i_9_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[4]_inst_i_8_n_0 ),
        .I5(\result_OBUF[4]_inst_i_9_n_0 ),
        .O(\result_OBUF[4]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[4]_inst_i_7 
       (.I0(\result_OBUF[10]_inst_i_10_n_0 ),
        .I1(\result_OBUF[1]_inst_i_20_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[1]_inst_i_18_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[1]_inst_i_19_n_0 ),
        .O(\result_OBUF[4]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[4]_inst_i_8 
       (.I0(\result_OBUF[10]_inst_i_11_n_0 ),
        .I1(\result_OBUF[1]_inst_i_20_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[8]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[1]_inst_i_19_n_0 ),
        .O(\result_OBUF[4]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'h0000020200000300)) 
    \result_OBUF[4]_inst_i_9 
       (.I0(op1_IBUF[1]),
        .I1(op2_IBUF[3]),
        .I2(op2_IBUF[4]),
        .I3(op1_IBUF[3]),
        .I4(op2_IBUF[2]),
        .I5(op2_IBUF[1]),
        .O(\result_OBUF[4]_inst_i_9_n_0 ));
  OBUF \result_OBUF[5]_inst 
       (.I(result_OBUF[5]),
        .O(result[5]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[5]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[5]),
        .I2(op2_IBUF[5]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[5]_inst_i_2_n_0 ),
        .I5(\result_OBUF[5]_inst_i_3_n_0 ),
        .O(result_OBUF[5]));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[5]_inst_i_2 
       (.I0(\result_OBUF[5]_inst_i_4_n_0 ),
        .I1(data3[5]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[5]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[5]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[5]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[5]_inst_i_5_n_0 ),
        .I4(\result_OBUF[5]_inst_i_6_n_0 ),
        .I5(data2[5]),
        .O(\result_OBUF[5]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[5]_inst_i_4 
       (.I0(op2_IBUF[5]),
        .I1(op1_IBUF[5]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[5]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[5]_inst_i_4_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[5]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[5]_inst_i_7_n_0 ),
        .I2(\result_OBUF[6]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[5]),
        .O(\result_OBUF[5]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[5]_inst_i_6 
       (.I0(\result_OBUF[6]_inst_i_9_n_0 ),
        .I1(\result_OBUF[5]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[5]_inst_i_9_n_0 ),
        .I5(\result_OBUF[6]_inst_i_8_n_0 ),
        .O(\result_OBUF[5]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[5]_inst_i_7 
       (.I0(\result_OBUF[11]_inst_i_20_n_0 ),
        .I1(\result_OBUF[0]_inst_i_13_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[9]_inst_i_10_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[0]_inst_i_12_n_0 ),
        .O(\result_OBUF[5]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h30BB000030880000)) 
    \result_OBUF[5]_inst_i_8 
       (.I0(op1_IBUF[2]),
        .I1(op2_IBUF[1]),
        .I2(op1_IBUF[0]),
        .I3(op2_IBUF[2]),
        .I4(\result_OBUF[30]_inst_i_26_n_0 ),
        .I5(op1_IBUF[4]),
        .O(\result_OBUF[5]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[5]_inst_i_9 
       (.I0(\result_OBUF[11]_inst_i_22_n_0 ),
        .I1(\result_OBUF[0]_inst_i_13_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[9]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[0]_inst_i_12_n_0 ),
        .O(\result_OBUF[5]_inst_i_9_n_0 ));
  OBUF \result_OBUF[6]_inst 
       (.I(result_OBUF[6]),
        .O(result[6]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[6]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[6]),
        .I2(op1_IBUF[6]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[6]_inst_i_2_n_0 ),
        .I5(\result_OBUF[6]_inst_i_3_n_0 ),
        .O(result_OBUF[6]));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[6]_inst_i_2 
       (.I0(\result_OBUF[6]_inst_i_4_n_0 ),
        .I1(data3[6]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[6]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[6]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[6]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[6]_inst_i_5_n_0 ),
        .I4(\result_OBUF[6]_inst_i_6_n_0 ),
        .I5(data2[6]),
        .O(\result_OBUF[6]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[6]_inst_i_4 
       (.I0(op1_IBUF[6]),
        .I1(op2_IBUF[6]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[6]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[6]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[6]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[6]_inst_i_7_n_0 ),
        .I2(\result_OBUF[7]_inst_i_17_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[6]),
        .O(\result_OBUF[6]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[6]_inst_i_6 
       (.I0(\result_OBUF[7]_inst_i_19_n_0 ),
        .I1(\result_OBUF[6]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[6]_inst_i_9_n_0 ),
        .I5(\result_OBUF[7]_inst_i_18_n_0 ),
        .O(\result_OBUF[6]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[6]_inst_i_7 
       (.I0(\result_OBUF[12]_inst_i_10_n_0 ),
        .I1(\result_OBUF[1]_inst_i_18_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[10]_inst_i_10_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[1]_inst_i_20_n_0 ),
        .O(\result_OBUF[6]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'h30BB000030880000)) 
    \result_OBUF[6]_inst_i_8 
       (.I0(op1_IBUF[3]),
        .I1(op2_IBUF[1]),
        .I2(op1_IBUF[1]),
        .I3(op2_IBUF[2]),
        .I4(\result_OBUF[30]_inst_i_26_n_0 ),
        .I5(op1_IBUF[5]),
        .O(\result_OBUF[6]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[6]_inst_i_9 
       (.I0(\result_OBUF[12]_inst_i_12_n_0 ),
        .I1(\result_OBUF[8]_inst_i_11_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[10]_inst_i_11_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[1]_inst_i_20_n_0 ),
        .O(\result_OBUF[6]_inst_i_9_n_0 ));
  OBUF \result_OBUF[7]_inst 
       (.I(result_OBUF[7]),
        .O(result[7]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[7]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[7]),
        .I2(op2_IBUF[7]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[7]_inst_i_2_n_0 ),
        .I5(\result_OBUF[7]_inst_i_3_n_0 ),
        .O(result_OBUF[7]));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[7]_inst_i_10 
       (.I0(op1_IBUF[6]),
        .I1(op2_IBUF[6]),
        .O(\result_OBUF[7]_inst_i_10_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[7]_inst_i_11 
       (.I0(op1_IBUF[5]),
        .I1(op2_IBUF[5]),
        .O(\result_OBUF[7]_inst_i_11_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[7]_inst_i_12 
       (.I0(op1_IBUF[4]),
        .I1(op2_IBUF[4]),
        .O(\result_OBUF[7]_inst_i_12_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[7]_inst_i_13 
       (.I0(op1_IBUF[7]),
        .I1(op2_IBUF[7]),
        .O(\result_OBUF[7]_inst_i_13_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[7]_inst_i_14 
       (.I0(op2_IBUF[6]),
        .I1(op1_IBUF[6]),
        .O(\result_OBUF[7]_inst_i_14_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[7]_inst_i_15 
       (.I0(op1_IBUF[5]),
        .I1(op2_IBUF[5]),
        .O(\result_OBUF[7]_inst_i_15_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \result_OBUF[7]_inst_i_16 
       (.I0(op2_IBUF[4]),
        .I1(op1_IBUF[4]),
        .O(\result_OBUF[7]_inst_i_16_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[7]_inst_i_17 
       (.I0(\result_OBUF[13]_inst_i_10_n_0 ),
        .I1(\result_OBUF[9]_inst_i_10_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[11]_inst_i_20_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[0]_inst_i_13_n_0 ),
        .O(\result_OBUF[7]_inst_i_17_n_0 ));
  LUT6 #(
    .INIT(64'hB080FFFFB0800000)) 
    \result_OBUF[7]_inst_i_18 
       (.I0(op1_IBUF[0]),
        .I1(op2_IBUF[2]),
        .I2(\result_OBUF[30]_inst_i_26_n_0 ),
        .I3(op1_IBUF[4]),
        .I4(op2_IBUF[1]),
        .I5(\result_OBUF[7]_inst_i_20_n_0 ),
        .O(\result_OBUF[7]_inst_i_18_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[7]_inst_i_19 
       (.I0(\result_OBUF[13]_inst_i_12_n_0 ),
        .I1(\result_OBUF[9]_inst_i_11_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[11]_inst_i_22_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[0]_inst_i_13_n_0 ),
        .O(\result_OBUF[7]_inst_i_19_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[7]_inst_i_2 
       (.I0(\result_OBUF[7]_inst_i_4_n_0 ),
        .I1(data3[7]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[7]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[7]_inst_i_2_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair8" *) 
  LUT5 #(
    .INIT(32'h000B0008)) 
    \result_OBUF[7]_inst_i_20 
       (.I0(op1_IBUF[2]),
        .I1(op2_IBUF[2]),
        .I2(op2_IBUF[3]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[6]),
        .O(\result_OBUF[7]_inst_i_20_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[7]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[7]_inst_i_7_n_0 ),
        .I4(\result_OBUF[7]_inst_i_8_n_0 ),
        .I5(data2[7]),
        .O(\result_OBUF[7]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[7]_inst_i_4 
       (.I0(op2_IBUF[7]),
        .I1(op1_IBUF[7]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[7]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[7]_inst_i_4_n_0 ));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[7]_inst_i_5 
       (.CI(\result_OBUF[3]_inst_i_5_n_0 ),
        .CO({\result_OBUF[7]_inst_i_5_n_0 ,\NLW_result_OBUF[7]_inst_i_5_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[7:4]),
        .O(data3[7:4]),
        .S({\result_OBUF[7]_inst_i_9_n_0 ,\result_OBUF[7]_inst_i_10_n_0 ,\result_OBUF[7]_inst_i_11_n_0 ,\result_OBUF[7]_inst_i_12_n_0 }));
  (* OPT_MODIFIED = "SWEEP" *) 
  CARRY4 \result_OBUF[7]_inst_i_6 
       (.CI(\result_OBUF[1]_inst_i_3_n_0 ),
        .CO({\result_OBUF[7]_inst_i_6_n_0 ,\NLW_result_OBUF[7]_inst_i_6_CO_UNCONNECTED [2:0]}),
        .CYINIT(\<const0> ),
        .DI(op1_IBUF[7:4]),
        .O(data2[7:4]),
        .S({\result_OBUF[7]_inst_i_13_n_0 ,\result_OBUF[7]_inst_i_14_n_0 ,\result_OBUF[7]_inst_i_15_n_0 ,\result_OBUF[7]_inst_i_16_n_0 }));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[7]_inst_i_7 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[7]_inst_i_17_n_0 ),
        .I2(\result_OBUF[8]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[7]),
        .O(\result_OBUF[7]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[7]_inst_i_8 
       (.I0(\result_OBUF[8]_inst_i_9_n_0 ),
        .I1(\result_OBUF[7]_inst_i_18_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[7]_inst_i_19_n_0 ),
        .I5(\result_OBUF[8]_inst_i_8_n_0 ),
        .O(\result_OBUF[7]_inst_i_8_n_0 ));
  LUT2 #(
    .INIT(4'h9)) 
    \result_OBUF[7]_inst_i_9 
       (.I0(op1_IBUF[7]),
        .I1(op2_IBUF[7]),
        .O(\result_OBUF[7]_inst_i_9_n_0 ));
  OBUF \result_OBUF[8]_inst 
       (.I(result_OBUF[8]),
        .O(result[8]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[8]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op2_IBUF[8]),
        .I2(op1_IBUF[8]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[8]_inst_i_2_n_0 ),
        .I5(\result_OBUF[8]_inst_i_3_n_0 ),
        .O(result_OBUF[8]));
  (* SOFT_HLUTNM = "soft_lutpair5" *) 
  LUT5 #(
    .INIT(32'h000B0008)) 
    \result_OBUF[8]_inst_i_10 
       (.I0(op1_IBUF[3]),
        .I1(op2_IBUF[2]),
        .I2(op2_IBUF[3]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[7]),
        .O(\result_OBUF[8]_inst_i_10_n_0 ));
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[8]_inst_i_11 
       (.I0(op1_IBUF[16]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[24]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[8]),
        .O(\result_OBUF[8]_inst_i_11_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[8]_inst_i_2 
       (.I0(\result_OBUF[8]_inst_i_4_n_0 ),
        .I1(data3[8]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[8]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[8]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[8]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[8]_inst_i_5_n_0 ),
        .I4(\result_OBUF[8]_inst_i_6_n_0 ),
        .I5(data2[8]),
        .O(\result_OBUF[8]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[8]_inst_i_4 
       (.I0(op1_IBUF[8]),
        .I1(op2_IBUF[8]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[8]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[8]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[8]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[8]_inst_i_7_n_0 ),
        .I2(\result_OBUF[9]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[8]),
        .O(\result_OBUF[8]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[8]_inst_i_6 
       (.I0(\result_OBUF[9]_inst_i_9_n_0 ),
        .I1(\result_OBUF[8]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[8]_inst_i_9_n_0 ),
        .I5(\result_OBUF[9]_inst_i_8_n_0 ),
        .O(\result_OBUF[8]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[8]_inst_i_7 
       (.I0(\result_OBUF[14]_inst_i_10_n_0 ),
        .I1(\result_OBUF[10]_inst_i_10_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[12]_inst_i_10_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[1]_inst_i_18_n_0 ),
        .O(\result_OBUF[8]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hB080FFFFB0800000)) 
    \result_OBUF[8]_inst_i_8 
       (.I0(op1_IBUF[1]),
        .I1(op2_IBUF[2]),
        .I2(\result_OBUF[30]_inst_i_26_n_0 ),
        .I3(op1_IBUF[5]),
        .I4(op2_IBUF[1]),
        .I5(\result_OBUF[8]_inst_i_10_n_0 ),
        .O(\result_OBUF[8]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[8]_inst_i_9 
       (.I0(\result_OBUF[14]_inst_i_12_n_0 ),
        .I1(\result_OBUF[10]_inst_i_11_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[12]_inst_i_12_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[8]_inst_i_11_n_0 ),
        .O(\result_OBUF[8]_inst_i_9_n_0 ));
  OBUF \result_OBUF[9]_inst 
       (.I(result_OBUF[9]),
        .O(result[9]));
  LUT6 #(
    .INIT(64'hFFFFFFFFFFFFA880)) 
    \result_OBUF[9]_inst_i_1 
       (.I0(\result_OBUF[28]_inst_i_2_n_0 ),
        .I1(op1_IBUF[9]),
        .I2(op2_IBUF[9]),
        .I3(\result_OBUF[30]_inst_i_4_n_0 ),
        .I4(\result_OBUF[9]_inst_i_2_n_0 ),
        .I5(\result_OBUF[9]_inst_i_3_n_0 ),
        .O(result_OBUF[9]));
  LUT6 #(
    .INIT(64'hCFC0AFAFCFC0A0A0)) 
    \result_OBUF[9]_inst_i_10 
       (.I0(op1_IBUF[17]),
        .I1(op1_IBUF[31]),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[25]),
        .I4(op2_IBUF[4]),
        .I5(op1_IBUF[9]),
        .O(\result_OBUF[9]_inst_i_10_n_0 ));
  LUT5 #(
    .INIT(32'h30BB3088)) 
    \result_OBUF[9]_inst_i_11 
       (.I0(op1_IBUF[17]),
        .I1(op2_IBUF[3]),
        .I2(op1_IBUF[25]),
        .I3(op2_IBUF[4]),
        .I4(op1_IBUF[9]),
        .O(\result_OBUF[9]_inst_i_11_n_0 ));
  LUT6 #(
    .INIT(64'hEAFFEAEA00000000)) 
    \result_OBUF[9]_inst_i_2 
       (.I0(\result_OBUF[9]_inst_i_4_n_0 ),
        .I1(data3[9]),
        .I2(\result_OBUF[28]_inst_i_6_n_0 ),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(data2[9]),
        .I5(alu_op_IBUF[2]),
        .O(\result_OBUF[9]_inst_i_2_n_0 ));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    \result_OBUF[9]_inst_i_3 
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(\result_OBUF[9]_inst_i_5_n_0 ),
        .I4(\result_OBUF[9]_inst_i_6_n_0 ),
        .I5(data2[9]),
        .O(\result_OBUF[9]_inst_i_3_n_0 ));
  LUT6 #(
    .INIT(64'hFF6F006000000000)) 
    \result_OBUF[9]_inst_i_4 
       (.I0(op2_IBUF[9]),
        .I1(op1_IBUF[9]),
        .I2(alu_op_IBUF[0]),
        .I3(alu_op_IBUF[1]),
        .I4(data2[9]),
        .I5(alu_op_IBUF[3]),
        .O(\result_OBUF[9]_inst_i_4_n_0 ));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    \result_OBUF[9]_inst_i_5 
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[9]_inst_i_7_n_0 ),
        .I2(\result_OBUF[10]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[9]),
        .O(\result_OBUF[9]_inst_i_5_n_0 ));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    \result_OBUF[9]_inst_i_6 
       (.I0(\result_OBUF[10]_inst_i_9_n_0 ),
        .I1(\result_OBUF[9]_inst_i_8_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[9]_inst_i_9_n_0 ),
        .I5(\result_OBUF[10]_inst_i_8_n_0 ),
        .O(\result_OBUF[9]_inst_i_6_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[9]_inst_i_7 
       (.I0(\result_OBUF[15]_inst_i_20_n_0 ),
        .I1(\result_OBUF[11]_inst_i_20_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[13]_inst_i_10_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[9]_inst_i_10_n_0 ),
        .O(\result_OBUF[9]_inst_i_7_n_0 ));
  LUT6 #(
    .INIT(64'hB080FFFFB0800000)) 
    \result_OBUF[9]_inst_i_8 
       (.I0(op1_IBUF[2]),
        .I1(op2_IBUF[2]),
        .I2(\result_OBUF[30]_inst_i_26_n_0 ),
        .I3(op1_IBUF[6]),
        .I4(op2_IBUF[1]),
        .I5(\result_OBUF[11]_inst_i_21_n_0 ),
        .O(\result_OBUF[9]_inst_i_8_n_0 ));
  LUT6 #(
    .INIT(64'hAFA0CFCFAFA0C0C0)) 
    \result_OBUF[9]_inst_i_9 
       (.I0(\result_OBUF[15]_inst_i_22_n_0 ),
        .I1(\result_OBUF[11]_inst_i_22_n_0 ),
        .I2(op2_IBUF[1]),
        .I3(\result_OBUF[13]_inst_i_12_n_0 ),
        .I4(op2_IBUF[2]),
        .I5(\result_OBUF[9]_inst_i_11_n_0 ),
        .O(\result_OBUF[9]_inst_i_9_n_0 ));
  OBUF zero_OBUF_inst
       (.I(zero_OBUF),
        .O(zero));
  LUT6 #(
    .INIT(64'h8000000000000000)) 
    zero_OBUF_inst_i_1
       (.I0(zero_OBUF_inst_i_2_n_0),
        .I1(zero_OBUF_inst_i_3_n_0),
        .I2(zero_OBUF_inst_i_4_n_0),
        .I3(zero_OBUF_inst_i_5_n_0),
        .I4(zero_OBUF_inst_i_6_n_0),
        .I5(zero_OBUF_inst_i_7_n_0),
        .O(zero_OBUF));
  LUT6 #(
    .INIT(64'h000F000F000F0001)) 
    zero_OBUF_inst_i_10
       (.I0(zero_OBUF_inst_i_20_n_0),
        .I1(\result_OBUF[27]_inst_i_3_n_0 ),
        .I2(\result_OBUF[29]_inst_i_2_n_0 ),
        .I3(zero_OBUF_inst_i_19_n_0),
        .I4(zero_OBUF_inst_i_18_n_0),
        .I5(\result_OBUF[28]_inst_i_4_n_0 ),
        .O(zero_OBUF_inst_i_10_n_0));
  LUT6 #(
    .INIT(64'h0000000030333133)) 
    zero_OBUF_inst_i_11
       (.I0(zero_OBUF_inst_i_21_n_0),
        .I1(zero_OBUF_inst_i_22_n_0),
        .I2(alu_op_IBUF[2]),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(zero_OBUF_inst_i_23_n_0),
        .I5(zero_OBUF_inst_i_24_n_0),
        .O(zero_OBUF_inst_i_11_n_0));
  LUT6 #(
    .INIT(64'h000F000F000F0001)) 
    zero_OBUF_inst_i_12
       (.I0(zero_OBUF_inst_i_25_n_0),
        .I1(\result_OBUF[3]_inst_i_3_n_0 ),
        .I2(zero_OBUF_inst_i_26_n_0),
        .I3(\result_OBUF[5]_inst_i_3_n_0 ),
        .I4(zero_OBUF_inst_i_24_n_0),
        .I5(\result_OBUF[4]_inst_i_3_n_0 ),
        .O(zero_OBUF_inst_i_12_n_0));
  LUT6 #(
    .INIT(64'h0000000000000001)) 
    zero_OBUF_inst_i_13
       (.I0(zero_OBUF_inst_i_27_n_0),
        .I1(\result_OBUF[17]_inst_i_3_n_0 ),
        .I2(zero_OBUF_inst_i_28_n_0),
        .I3(\result_OBUF[16]_inst_i_3_n_0 ),
        .I4(\result_OBUF[14]_inst_i_3_n_0 ),
        .I5(zero_OBUF_inst_i_29_n_0),
        .O(zero_OBUF_inst_i_13_n_0));
  LUT6 #(
    .INIT(64'h000F000F000F0001)) 
    zero_OBUF_inst_i_14
       (.I0(zero_OBUF_inst_i_30_n_0),
        .I1(\result_OBUF[18]_inst_i_3_n_0 ),
        .I2(zero_OBUF_inst_i_31_n_0),
        .I3(\result_OBUF[20]_inst_i_3_n_0 ),
        .I4(zero_OBUF_inst_i_32_n_0),
        .I5(\result_OBUF[19]_inst_i_3_n_0 ),
        .O(zero_OBUF_inst_i_14_n_0));
  LUT6 #(
    .INIT(64'hF0F0AAAACCCCCCAA)) 
    zero_OBUF_inst_i_15
       (.I0(data2[23]),
        .I1(\result_OBUF[23]_inst_i_8_n_0 ),
        .I2(\result_OBUF[23]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(alu_op_IBUF[3]),
        .I5(alu_op_IBUF[1]),
        .O(zero_OBUF_inst_i_15_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_16
       (.I0(zero_OBUF_inst_i_33_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op2_IBUF[23]),
        .I3(op1_IBUF[23]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_16_n_0));
  LUT6 #(
    .INIT(64'hF0F0AAAACCCCCCAA)) 
    zero_OBUF_inst_i_17
       (.I0(data2[28]),
        .I1(\result_OBUF[28]_inst_i_8_n_0 ),
        .I2(\result_OBUF[28]_inst_i_7_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(alu_op_IBUF[3]),
        .I5(alu_op_IBUF[1]),
        .O(zero_OBUF_inst_i_17_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_18
       (.I0(zero_OBUF_inst_i_34_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op1_IBUF[28]),
        .I3(op2_IBUF[28]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_18_n_0));
  LUT6 #(
    .INIT(64'hAA2A8A0AA0208000)) 
    zero_OBUF_inst_i_19
       (.I0(\result_OBUF[30]_inst_i_7_n_0 ),
        .I1(alu_op_IBUF[1]),
        .I2(\result_OBUF[30]_inst_i_4_n_0 ),
        .I3(zero_OBUF_inst_i_35_n_0),
        .I4(zero_OBUF_inst_i_36_n_0),
        .I5(data2[29]),
        .O(zero_OBUF_inst_i_19_n_0));
  LUT6 #(
    .INIT(64'h0000000000000001)) 
    zero_OBUF_inst_i_2
       (.I0(result_OBUF[30]),
        .I1(result_OBUF[20]),
        .I2(result_OBUF[19]),
        .I3(result_OBUF[22]),
        .I4(result_OBUF[23]),
        .I5(result_OBUF[21]),
        .O(zero_OBUF_inst_i_2_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_20
       (.I0(zero_OBUF_inst_i_37_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op2_IBUF[27]),
        .I3(op1_IBUF[27]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_20_n_0));
  LUT6 #(
    .INIT(64'hF0F0AAAACCCCCCAA)) 
    zero_OBUF_inst_i_21
       (.I0(data2[2]),
        .I1(\result_OBUF[2]_inst_i_6_n_0 ),
        .I2(\result_OBUF[2]_inst_i_5_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(alu_op_IBUF[3]),
        .I5(alu_op_IBUF[1]),
        .O(zero_OBUF_inst_i_21_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_22
       (.I0(zero_OBUF_inst_i_38_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op1_IBUF[2]),
        .I3(op2_IBUF[2]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_22_n_0));
  LUT6 #(
    .INIT(64'hF0F0AAAACCCCCCAA)) 
    zero_OBUF_inst_i_23
       (.I0(data2[4]),
        .I1(\result_OBUF[4]_inst_i_6_n_0 ),
        .I2(\result_OBUF[4]_inst_i_5_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(alu_op_IBUF[3]),
        .I5(alu_op_IBUF[1]),
        .O(zero_OBUF_inst_i_23_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_24
       (.I0(zero_OBUF_inst_i_39_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op1_IBUF[4]),
        .I3(op2_IBUF[4]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_24_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_25
       (.I0(zero_OBUF_inst_i_40_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op2_IBUF[3]),
        .I3(op1_IBUF[3]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_25_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_26
       (.I0(zero_OBUF_inst_i_41_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op2_IBUF[5]),
        .I3(op1_IBUF[5]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_26_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_27
       (.I0(zero_OBUF_inst_i_42_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op2_IBUF[17]),
        .I3(op1_IBUF[17]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_27_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_28
       (.I0(zero_OBUF_inst_i_43_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op1_IBUF[16]),
        .I3(op2_IBUF[16]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_28_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_29
       (.I0(zero_OBUF_inst_i_44_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op1_IBUF[14]),
        .I3(op2_IBUF[14]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_29_n_0));
  LUT6 #(
    .INIT(64'h0000100000000000)) 
    zero_OBUF_inst_i_3
       (.I0(result_OBUF[26]),
        .I1(result_OBUF[25]),
        .I2(zero_OBUF_inst_i_8_n_0),
        .I3(zero_OBUF_inst_i_9_n_0),
        .I4(result_OBUF[24]),
        .I5(zero_OBUF_inst_i_10_n_0),
        .O(zero_OBUF_inst_i_3_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_30
       (.I0(zero_OBUF_inst_i_45_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op1_IBUF[18]),
        .I3(op2_IBUF[18]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_30_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_31
       (.I0(zero_OBUF_inst_i_46_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op1_IBUF[20]),
        .I3(op2_IBUF[20]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_31_n_0));
  LUT6 #(
    .INIT(64'hAAAA0000AAAAFCC0)) 
    zero_OBUF_inst_i_32
       (.I0(zero_OBUF_inst_i_47_n_0),
        .I1(\result_OBUF[30]_inst_i_4_n_0 ),
        .I2(op2_IBUF[19]),
        .I3(op1_IBUF[19]),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[30]_inst_i_9_n_0 ),
        .O(zero_OBUF_inst_i_32_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_33
       (.I0(data3[23]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[23]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_48_n_0),
        .O(zero_OBUF_inst_i_33_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_34
       (.I0(data3[28]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[28]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_49_n_0),
        .O(zero_OBUF_inst_i_34_n_0));
  LUT5 #(
    .INIT(32'hFFE400E4)) 
    zero_OBUF_inst_i_35
       (.I0(op2_IBUF[0]),
        .I1(\result_OBUF[29]_inst_i_8_n_0 ),
        .I2(\result_OBUF[30]_inst_i_16_n_0 ),
        .I3(alu_op_IBUF[0]),
        .I4(data2[29]),
        .O(zero_OBUF_inst_i_35_n_0));
  LUT6 #(
    .INIT(64'hCFAFCFA0C0AFC0A0)) 
    zero_OBUF_inst_i_36
       (.I0(zero_OBUF_inst_i_50_n_0),
        .I1(\result_OBUF[29]_inst_i_10_n_0 ),
        .I2(op2_IBUF[0]),
        .I3(alu_op_IBUF[0]),
        .I4(\result_OBUF[29]_inst_i_6_n_0 ),
        .I5(\result_OBUF[30]_inst_i_19_n_0 ),
        .O(zero_OBUF_inst_i_36_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_37
       (.I0(data3[27]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[27]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_51_n_0),
        .O(zero_OBUF_inst_i_37_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_38
       (.I0(data3[2]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[2]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_52_n_0),
        .O(zero_OBUF_inst_i_38_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_39
       (.I0(data3[4]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[4]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_53_n_0),
        .O(zero_OBUF_inst_i_39_n_0));
  LUT6 #(
    .INIT(64'h0000230000002323)) 
    zero_OBUF_inst_i_4
       (.I0(result_OBUF[16]),
        .I1(result_OBUF[17]),
        .I2(result_OBUF[15]),
        .I3(result_OBUF[13]),
        .I4(result_OBUF[14]),
        .I5(result_OBUF[12]),
        .O(zero_OBUF_inst_i_4_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_40
       (.I0(data3[3]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[3]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_54_n_0),
        .O(zero_OBUF_inst_i_40_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_41
       (.I0(data3[5]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[5]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_55_n_0),
        .O(zero_OBUF_inst_i_41_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_42
       (.I0(data3[17]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[17]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_56_n_0),
        .O(zero_OBUF_inst_i_42_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_43
       (.I0(data3[16]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[16]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_57_n_0),
        .O(zero_OBUF_inst_i_43_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_44
       (.I0(data3[14]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[14]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_58_n_0),
        .O(zero_OBUF_inst_i_44_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_45
       (.I0(data3[18]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[18]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_59_n_0),
        .O(zero_OBUF_inst_i_45_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_46
       (.I0(data3[20]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[20]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_60_n_0),
        .O(zero_OBUF_inst_i_46_n_0));
  LUT6 #(
    .INIT(64'hC030E2F0C0FCE2F0)) 
    zero_OBUF_inst_i_47
       (.I0(data3[19]),
        .I1(alu_op_IBUF[3]),
        .I2(data2[19]),
        .I3(alu_op_IBUF[1]),
        .I4(alu_op_IBUF[0]),
        .I5(zero_OBUF_inst_i_61_n_0),
        .O(zero_OBUF_inst_i_47_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_48
       (.I0(op2_IBUF[23]),
        .I1(op1_IBUF[23]),
        .O(zero_OBUF_inst_i_48_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_49
       (.I0(op1_IBUF[28]),
        .I1(op2_IBUF[28]),
        .O(zero_OBUF_inst_i_49_n_0));
  LUT6 #(
    .INIT(64'h0000230000002323)) 
    zero_OBUF_inst_i_5
       (.I0(result_OBUF[10]),
        .I1(result_OBUF[11]),
        .I2(result_OBUF[9]),
        .I3(result_OBUF[7]),
        .I4(result_OBUF[8]),
        .I5(result_OBUF[6]),
        .O(zero_OBUF_inst_i_5_n_0));
  LUT5 #(
    .INIT(32'h00000010)) 
    zero_OBUF_inst_i_50
       (.I0(op2_IBUF[1]),
        .I1(op2_IBUF[2]),
        .I2(op1_IBUF[30]),
        .I3(op2_IBUF[4]),
        .I4(op2_IBUF[3]),
        .O(zero_OBUF_inst_i_50_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_51
       (.I0(op2_IBUF[27]),
        .I1(op1_IBUF[27]),
        .O(zero_OBUF_inst_i_51_n_0));
  (* SOFT_HLUTNM = "soft_lutpair8" *) 
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_52
       (.I0(op1_IBUF[2]),
        .I1(op2_IBUF[2]),
        .O(zero_OBUF_inst_i_52_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_53
       (.I0(op1_IBUF[4]),
        .I1(op2_IBUF[4]),
        .O(zero_OBUF_inst_i_53_n_0));
  (* SOFT_HLUTNM = "soft_lutpair5" *) 
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_54
       (.I0(op2_IBUF[3]),
        .I1(op1_IBUF[3]),
        .O(zero_OBUF_inst_i_54_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_55
       (.I0(op2_IBUF[5]),
        .I1(op1_IBUF[5]),
        .O(zero_OBUF_inst_i_55_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_56
       (.I0(op2_IBUF[17]),
        .I1(op1_IBUF[17]),
        .O(zero_OBUF_inst_i_56_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_57
       (.I0(op1_IBUF[16]),
        .I1(op2_IBUF[16]),
        .O(zero_OBUF_inst_i_57_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_58
       (.I0(op1_IBUF[14]),
        .I1(op2_IBUF[14]),
        .O(zero_OBUF_inst_i_58_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_59
       (.I0(op1_IBUF[18]),
        .I1(op2_IBUF[18]),
        .O(zero_OBUF_inst_i_59_n_0));
  LUT6 #(
    .INIT(64'h0000000400000000)) 
    zero_OBUF_inst_i_6
       (.I0(result_OBUF[1]),
        .I1(zero_OBUF_inst_i_11_n_0),
        .I2(result_OBUF[7]),
        .I3(result_OBUF[5]),
        .I4(result_OBUF[0]),
        .I5(zero_OBUF_inst_i_12_n_0),
        .O(zero_OBUF_inst_i_6_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_60
       (.I0(op1_IBUF[20]),
        .I1(op2_IBUF[20]),
        .O(zero_OBUF_inst_i_60_n_0));
  LUT2 #(
    .INIT(4'h9)) 
    zero_OBUF_inst_i_61
       (.I0(op2_IBUF[19]),
        .I1(op1_IBUF[19]),
        .O(zero_OBUF_inst_i_61_n_0));
  LUT6 #(
    .INIT(64'h0000000000000008)) 
    zero_OBUF_inst_i_7
       (.I0(zero_OBUF_inst_i_13_n_0),
        .I1(zero_OBUF_inst_i_14_n_0),
        .I2(result_OBUF[8]),
        .I3(result_OBUF[10]),
        .I4(result_OBUF[11]),
        .I5(result_OBUF[13]),
        .O(zero_OBUF_inst_i_7_n_0));
  LUT6 #(
    .INIT(64'h0000000030333133)) 
    zero_OBUF_inst_i_8
       (.I0(zero_OBUF_inst_i_15_n_0),
        .I1(zero_OBUF_inst_i_16_n_0),
        .I2(alu_op_IBUF[2]),
        .I3(\result_OBUF[30]_inst_i_9_n_0 ),
        .I4(zero_OBUF_inst_i_17_n_0),
        .I5(zero_OBUF_inst_i_18_n_0),
        .O(zero_OBUF_inst_i_8_n_0));
  LUT6 #(
    .INIT(64'h0000000111110001)) 
    zero_OBUF_inst_i_9
       (.I0(zero_OBUF_inst_i_19_n_0),
        .I1(\result_OBUF[29]_inst_i_2_n_0 ),
        .I2(\result_OBUF[31]_inst_i_4_n_0 ),
        .I3(\result_OBUF[31]_inst_i_3_n_0 ),
        .I4(alu_op_IBUF[2]),
        .I5(\result_OBUF[31]_inst_i_2_n_0 ),
        .O(zero_OBUF_inst_i_9_n_0));
endmodule

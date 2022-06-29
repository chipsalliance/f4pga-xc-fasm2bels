`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: BYU (Brigham Young University)
// Engineer: Jake Edvenson
// 
// Create Date: 04/28/2022 
// Design Name: alu
// Project Name: bfasst testing
// Description: A simple ALU design to test on bfasst
// 
// Dependencies: None
// 
// LUT: 493
// IO: 101
//
//////////////////////////////////////////////////////////////////////////////////

module alu(op1, op2, alu_op, zero, result);
input wire[31:0] op1, op2; //Op1 = Operand 1. Op2 = Operand 2.
input wire[3:0] alu_op; //alu_op determines which operation is done between Op1 & Op2.
output reg zero; //This output tells us if the operation results in a zero.
output reg[31:0] result; //This 32 bit output is the resulting value of the operation.

//These parameters define each ALU Operation that can be executed based upon the 4 bit alu_op.
parameter AND = 4'b0000;
parameter OR = 4'b0001;
parameter ADD = 4'b0010;
parameter SUB = 4'b0110;
parameter SLT = 4'b0111;
parameter SRL = 4'b1000;
parameter SLL = 4'b1001;
parameter SRA = 4'b1010;
parameter XOR = 4'b1101;

//These parameters define the two states our zero signal can be in: True or False
parameter TRUE = 1'b1;
parameter FALSE = 1'b0;

//Combinational logic for the ALU Operations
always @(*)
begin
    case (alu_op)
    
        AND : result = op1 & op2; //Bit-wise ANDs op1 & op2.
        
        OR: result = op1 | op2; //Bit-wise ORs op1 & op2.
        
        ADD: result = op1 + op2; //Adds op1 & op2.
        
        SUB: result = op1 - op2; //Subtracts op1 & op2.
        
        SLT: result = $signed(op1) < $signed(op2); //Sets op1 less than op2. Returns 0 or 1. 
        
        SRL: result = op1 >> op2[4:0]; //Shifts op1 right by op2. Extra bits are filled with 0's.
        
        SLL: result = op1 << op2[4:0]; //Shifts op1 left by op2. Extra bits are filled with 0's.
        
        SRA: result = $unsigned($signed(op1) >>> op2[4:0]); //Shifts op1 right by op2. Extra bits are filled with 1's.
        
        XOR: result = op1 ^ op2; //Exclusive ORs op1 & op2. 
        
        default: result = op1 + op2; //By default, if anything else is entered, op1 is added to op2. 
    
    endcase
    
    if(result == 0) //If the result is zero, the zero signal is high, or true.
        zero = TRUE;
    else
        zero = FALSE; //If the result is NOT zero, the zero signal is low, or false. 
    
end



endmodule
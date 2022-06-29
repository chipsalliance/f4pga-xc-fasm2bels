module add32(
    input [31:0] a,
    input [31:0] b,
    input clk,
    input rst,
    output reg [31:0] o
);

always @ (posedge clk) begin
    if (rst)
        o <= 1'b0;
    else 
        o <= a + b;
end

endmodule
//First module

module my_module(
    input logic[1:0] sw,
    output logic led
);
    nand(led,sw[0],sw[1]);

endmodule
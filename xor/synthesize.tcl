#Synthesize the design

read_verilog -sv my_module.sv
read_xdc Master.xdc

synth_design -top my_module -part xc7a35tcpg236-1 -verbose
write_checkpoint -force my_module.dcp
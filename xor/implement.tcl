open_checkpoint my_module.dcp
opt_design
place_design
route_design
report_utilization -file utilization.rpt
write_bitstream -force xor.bit
write_checkpoint -force xor.dcp
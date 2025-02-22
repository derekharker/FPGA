# Clean unneccesary files
clean:
	del *.jou *.pb *.log *.txt
	rmdir /S /Q .Xil xsim.dir
# Test files
test:
	xvlog my_module.sv --sv --nolog
	xelab my_module --nolog -debug typical
	xsim my_module --nolog --gui

#Synthesize files
synth:
	vivado -mode batch -source synthesize.tcl -log synth.log -nojournal -notrace

#Implement
implement:
	vivado -mode batch -source implement.tcl -log implement_logic.log -nojournal -notrace

download:
	vivado -mode tcl
	open_hw
	connect_hw_server
	open_hw_target
	set_property PROGRAM.FILE {xor.bit} [current_hw_device]
	program_hw_devices


# Startup the terminal
startup:
	"C:\Xilinx\Vivado\2024.2\settings64.bat"
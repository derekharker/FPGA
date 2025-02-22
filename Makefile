# Clean unneccesary files
clean:
	del *.jou *.pb *.log *.txt
	rmdir /S /Q .Xil xsim.dir
# Test files
test:
	xvlog my_module.sv --sv --nolog
	xelab my_module --nolog
	xsim my_module --nolog --gui

# Startup the terminal
startup:
	"C:\Xilinx\Vivado\2024.2\settings64.bat"
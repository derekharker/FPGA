clean:
	rm -rf xsim.dir/
test:
	xvlog my_module.sv --sv --nolog
	xelab my_module --nolog
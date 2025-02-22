# XOR 0 0
set_value sw[0] 0
set_value sw[1] 0
run 10 ns

# XOR 0 1
set_value sw[0] 1
set_value sw[1] 0
run 10 ns

# XOR 1 0
set_value sw[0] 0
set_value sw[1] 1
run 10 ns

# XOR 1 1
set_value sw[0] 1
set_value sw[1] 1
run 10 ns
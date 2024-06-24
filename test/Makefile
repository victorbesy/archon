# Makefile
VERILATOR = verilator
VERILATOR_FLAGS = -Wall -cc --exe --timing 
SIM_MAIN = sim_main.cpp
TOP_MODULE = HelloWorld

# Target for building and running the simulation
all: sim

sim: $(TOP_MODULE).sv $(SIM_MAIN)
	$(VERILATOR) $(VERILATOR_FLAGS) $(TOP_MODULE).sv $(SIM_MAIN)
	make -C obj_dir -f V$(TOP_MODULE).mk V$(TOP_MODULE)

# New target for running the simulation
run: sim
	./obj_dir/V$(TOP_MODULE)

clean:
	rm -rf obj_dir

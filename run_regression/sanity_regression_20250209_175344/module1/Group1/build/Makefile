# Makefile
VERILATOR = verilator
VERILATOR_FLAGS = -Wall --trace
SIM_MAIN = sim_main.cpp
TOP_MODULE = Vcs_common 2>&1 | tee test.log

include ./Sim.mk

ifeq (${VERILATOR},)
export VERILATOR = verilator
endif

compile_verilator_sv: clean
	@sleep 5
	${VERILATOR} $(VERILATOR_FLAGS) cs_common.svh $(SHUNT_VERILATOR_FLAGS) top_sim.v --exe $(SIM_MAIN)
	make -C obj_dir -j -f Vcs_common.mk Vcs_common

.PHONY: clean run

run: 
	./obj_dir/$(TOP_MODULE)
clean:	
	rm -rf obj_dir

all: compile_verilator_sv


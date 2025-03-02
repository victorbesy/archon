# Makefile
VERILATOR = verilator
VERILATOR_FLAGS = -Wall --trace
SIM_MAIN = sim_main.cpp
TOP_MODULE = Vcs_common
COMPILATION_LOG_FILE = verilator_comp.log
TEST_LOG_FILE = verilator_test.log

include ./Sim.mk

ifeq (${VERILATOR},)
export VERILATOR = verilator
endif

compile_verilator_sv: clean
	@DELAY=$$(shuf -i 5-7 -n 1); \
	echo "Sleeping for $$DELAY seconds..."; \
	sleep $$DELAY
	@echo "Compiling with Verilator..."
	${VERILATOR} $(VERILATOR_FLAGS) cs_common.svh $(SHUNT_VERILATOR_FLAGS) top_sim.v --exe $(SIM_MAIN) --trace  2>&1 | tee -a $(COMPILATION_LOG_FILE)
	make -C obj_dir -j -f Vcs_common.mk Vcs_common
	@echo "Compilation complete. Compilation log file generated: $(COMPILATION_LOG_FILE)"

.PHONY: clean run

run: 
	@echo "Running simulation..."
	./obj_dir/$(TOP_MODULE) 2>&1 | tee -a $(TEST_LOG_FILE)
	@echo "Simulation complete. Test log file generated: $(TEST_LOG_FILE)"
clean:  
	rm -rf obj_dir
	rm -f $(COMPILATION_LOG_FILE) $(TEST_LOG_FILE)

all: compile_verilator_sv
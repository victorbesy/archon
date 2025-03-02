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
	echo "Sleeping for $$DELAY seconds..." | tee -a $(COMPILATION_LOG_FILE); \
    sleep $$DELAY
	@echo "Compiling with Verilator..." | tee -a $(COMPILATION_LOG_FILE)
	${VERILATOR} --version | tee -a $(COMPILATION_LOG_FILE)
	echo "Command: ${VERILATOR} $(VERILATOR_FLAGS) cs_common.svh $(SHUNT_VERILATOR_FLAGS) top_sim.v --exe $(SIM_MAIN) --trace" | tee -a $(COMPILATION_LOG_FILE)
	{ ${VERILATOR} $(VERILATOR_FLAGS) cs_common.svh $(SHUNT_VERILATOR_FLAGS) top_sim.v --exe $(SIM_MAIN) --trace 2>&1; echo "Verilator exit code: $$?" >&3; } 3>> $(COMPILATION_LOG_FILE) | tee -a $(COMPILATION_LOG_FILE); \
	EXIT_CODE=$$(tail -n 1 $(COMPILATION_LOG_FILE) | grep -o '[0-9]*$$'); \
	if [ $$EXIT_CODE -eq 0 ]; then echo "COMPILE PASS" | tee -a $(COMPILATION_LOG_FILE); else echo "COMPILE FAILED" | tee -a $(COMPILATION_LOG_FILE); exit 1; fi
	echo "Command: make -C obj_dir -j -f Vcs_common.mk Vcs_common" | tee -a $(COMPILATION_LOG_FILE)
	{ make -C obj_dir -j -f Vcs_common.mk Vcs_common 2>&1; MAKE_EXIT_CODE=$$?; echo "Make command exit code: $$MAKE_EXIT_CODE" >&3; if [ $$MAKE_EXIT_CODE -ne 0 ]; then echo "Make command failed with exit code: $$MAKE_EXIT_CODE" >&3; fi } 3>> $(COMPILATION_LOG_FILE) | tee -a $(COMPILATION_LOG_FILE); \
	EXIT_CODE=$$(tail -n 1 $(COMPILATION_LOG_FILE) | grep -o '[0-9]*$$'); \
	if [ $$EXIT_CODE -eq 0 ]; then echo "COMPILE PASS" | tee -a $(COMPILATION_LOG_FILE); else echo "COMPILE FAILED" | tee -a $(COMPILATION_LOG_FILE); exit 1; fi
	@echo "Compilation complete. Compilation log file generated: $(COMPILATION_LOG_FILE)" | tee -a $(COMPILATION_LOG_FILE)

.PHONY: clean run

run:
	@echo "Running simulation..." | tee -a $(TEST_LOG_FILE)
	echo "Command: ./obj_dir/$(TOP_MODULE)" | tee -a $(TEST_LOG_FILE)
	./obj_dir/$(TOP_MODULE) 2>&1 | tee -a $(TEST_LOG_FILE); \
	EXIT_CODE=$$?; \
	echo "Run exit code: $$EXIT_CODE" | tee -a $(TEST_LOG_FILE); \
	if [ $$EXIT_CODE -eq 0]; then echo "RUN PASS" | tee -a $(TEST_LOG_FILE); else echo "RUN FAILED" | tee -a $(TEST_LOG_FILE); exit 1; fi
	@echo "Simulation complete. Test log file generated: $(TEST_LOG_FILE)" | tee -a $(TEST_LOG_FILE)

clean:
	rm -rf obj_dir
	rm -f $(COMPILATION_LOG_FILE) $(TEST_LOG_FILE)

all: compile_verilator_sv


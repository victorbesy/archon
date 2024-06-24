include ./Sim.mk
-include ../../../../utils/makefile.init

export FRNG_N_OF_DST ?= 1

export SHUNT_VERILATOR_FLAGS

ifeq (${VERILATOR},)
export VERILATOR = verilator
endif

ifeq ($(MANIFEST_INC),)
export MANIFEST_INC = inc.f 
endif

export SIM ?= verilator
################
###SHUNT
# check shunt environment setting
check_shunt:
	$(MAKE) -f ${SHUNT_HOME}/utils/makefile.init
# build Shunt 
build_shunt: check_shunt
	cd ${SHUNT_HOME}/utils/makedir && $(MAKE) all

.PHONY: clean_shunt
clean_shunt:
	cd ${SHUNT_HOME}/bin && rm -rf *
################### SV UVM   
.PHONY: make_all_sv
make_all_sv: clean_sv  build_shunt build_sv run_sv

.PHONY: make_sv
make_sv: build_shunt build_sv_sv run_sv

.PHONY: clean_sv
clean_sv:
	cd ../sv/makedir &&  $(MAKE) clean

build_sv: 
ifeq ($(SIM),verilator)
	cd ../sv/makedir && $(MAKE) compile_$(SIM)_sv
endif

.PHONY: run_sv
run_sv:
	cd ../sv/makedir  && ./$(SIM)_run


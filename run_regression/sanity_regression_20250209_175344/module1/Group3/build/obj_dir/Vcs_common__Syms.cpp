// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table implementation internals

#include "Vcs_common__pch.h"
#include "Vcs_common.h"
#include "Vcs_common___024root.h"
#include "Vcs_common_shunt_dpi_pkg.h"
#include "Vcs_common___024unit.h"

// FUNCTIONS
Vcs_common__Syms::~Vcs_common__Syms()
{
}

Vcs_common__Syms::Vcs_common__Syms(VerilatedContext* contextp, const char* namep, Vcs_common* modelp)
    : VerilatedSyms{contextp}
    // Setup internal state of the Syms class
    , __Vm_modelp{modelp}
    // Setup module instances
    , TOP{this, namep}
    , TOP__shunt_dpi_pkg{this, Verilated::catName(namep, "shunt_dpi_pkg")}
{
        // Check resources
        Verilated::stackCheck(51);
    // Configure time unit / time precision
    _vm_contextp__->timeunit(-12);
    _vm_contextp__->timeprecision(-12);
    // Setup each module's pointers to their submodules
    TOP.__PVT__shunt_dpi_pkg = &TOP__shunt_dpi_pkg;
    // Setup each module's pointer back to symbol table (for public functions)
    TOP.__Vconfigure(true);
    TOP__shunt_dpi_pkg.__Vconfigure(true);
    // Setup export functions
    for (int __Vfinal = 0; __Vfinal < 2; ++__Vfinal) {
    }
}

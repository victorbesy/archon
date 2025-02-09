// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vcs_common.h for the primary calling header

#include "Vcs_common__pch.h"
#include "Vcs_common__Syms.h"
#include "Vcs_common_shunt_dpi_pkg.h"

void Vcs_common_shunt_dpi_pkg___ctor_var_reset(Vcs_common_shunt_dpi_pkg* vlSelf);

Vcs_common_shunt_dpi_pkg::Vcs_common_shunt_dpi_pkg(Vcs_common__Syms* symsp, const char* v__name)
    : VerilatedModule{v__name}
    , vlSymsp{symsp}
 {
    // Reset structure values
    Vcs_common_shunt_dpi_pkg___ctor_var_reset(this);
}

void Vcs_common_shunt_dpi_pkg::__Vconfigure(bool first) {
    (void)first;  // Prevent unused variable warning
}

Vcs_common_shunt_dpi_pkg::~Vcs_common_shunt_dpi_pkg() {
}

// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vcs_common.h for the primary calling header

#include "Vcs_common__pch.h"
#include "Vcs_common__Syms.h"
#include "Vcs_common___024root.h"

void Vcs_common___024root___ctor_var_reset(Vcs_common___024root* vlSelf);

Vcs_common___024root::Vcs_common___024root(Vcs_common__Syms* symsp, const char* v__name)
    : VerilatedModule{v__name}
    , vlSymsp{symsp}
 {
    // Reset structure values
    Vcs_common___024root___ctor_var_reset(this);
}

void Vcs_common___024root::__Vconfigure(bool first) {
    (void)first;  // Prevent unused variable warning
}

Vcs_common___024root::~Vcs_common___024root() {
}

// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See Vcs_common.h for the primary calling header

#ifndef VERILATED_VCS_COMMON___024UNIT_H_
#define VERILATED_VCS_COMMON___024UNIT_H_  // guard

#include "verilated.h"


class Vcs_common__Syms;

class alignas(VL_CACHE_LINE_BYTES) Vcs_common___024unit final : public VerilatedModule {
  public:

    // INTERNAL VARIABLES
    Vcs_common__Syms* const vlSymsp;

    // CONSTRUCTORS
    Vcs_common___024unit(Vcs_common__Syms* symsp, const char* v__name);
    ~Vcs_common___024unit();
    VL_UNCOPYABLE(Vcs_common___024unit);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
};


#endif  // guard

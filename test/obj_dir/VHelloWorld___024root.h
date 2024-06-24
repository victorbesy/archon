// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See VHelloWorld.h for the primary calling header

#ifndef VERILATED_VHELLOWORLD___024ROOT_H_
#define VERILATED_VHELLOWORLD___024ROOT_H_  // guard

#include "verilated.h"


class VHelloWorld__Syms;

class alignas(VL_CACHE_LINE_BYTES) VHelloWorld___024root final : public VerilatedModule {
  public:

    // DESIGN SPECIFIC STATE
    CData/*0:0*/ __VactContinue;
    IData/*31:0*/ HelloWorld__DOT__unnamedblk1__DOT__seed;
    IData/*31:0*/ __VactIterCount;
    VlTriggerVec<0> __VactTriggered;
    VlTriggerVec<0> __VnbaTriggered;

    // INTERNAL VARIABLES
    VHelloWorld__Syms* const vlSymsp;

    // CONSTRUCTORS
    VHelloWorld___024root(VHelloWorld__Syms* symsp, const char* v__name);
    ~VHelloWorld___024root();
    VL_UNCOPYABLE(VHelloWorld___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
};


#endif  // guard

// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See Vcs_common.h for the primary calling header

#ifndef VERILATED_VCS_COMMON___024ROOT_H_
#define VERILATED_VCS_COMMON___024ROOT_H_  // guard

#include "verilated.h"
class Vcs_common_shunt_dpi_pkg;


class Vcs_common__Syms;

class alignas(VL_CACHE_LINE_BYTES) Vcs_common___024root final : public VerilatedModule {
  public:
    // CELLS
    Vcs_common_shunt_dpi_pkg* __PVT__shunt_dpi_pkg;

    // DESIGN SPECIFIC STATE
    VL_IN8(clk_i,0,0);
    CData/*0:0*/ top_sim__DOT__reset_n;
    CData/*0:0*/ __Vtrigprevexpr___TOP__clk_i__0;
    CData/*0:0*/ __VactContinue;
    IData/*31:0*/ top_sim__DOT__clk_cnt;
    IData/*31:0*/ __VactIterCount;
    QData/*63:0*/ top_sim__DOT__start_time;
    QData/*63:0*/ top_sim__DOT__event_cnt;
    QData/*63:0*/ top_sim__DOT__startTime;
    VlUnpacked<CData/*0:0*/, 1> __Vm_traceActivity;
    VlTriggerVec<1> __VactTriggered;
    VlTriggerVec<1> __VnbaTriggered;

    // INTERNAL VARIABLES
    Vcs_common__Syms* const vlSymsp;

    // CONSTRUCTORS
    Vcs_common___024root(Vcs_common__Syms* symsp, const char* v__name);
    ~Vcs_common___024root();
    VL_UNCOPYABLE(Vcs_common___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
};


#endif  // guard

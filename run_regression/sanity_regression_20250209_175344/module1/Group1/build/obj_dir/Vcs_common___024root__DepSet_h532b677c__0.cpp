// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vcs_common.h for the primary calling header

#include "Vcs_common__pch.h"
#include "Vcs_common__Syms.h"
#include "Vcs_common___024root.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void Vcs_common___024root___dump_triggers__act(Vcs_common___024root* vlSelf);
#endif  // VL_DEBUG

void Vcs_common___024root___eval_triggers__act(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___eval_triggers__act\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VactTriggered.set(0U, ((IData)(vlSelfRef.clk_i) 
                                       & (~ (IData)(vlSelfRef.__Vtrigprevexpr___TOP__clk_i__0))));
    vlSelfRef.__Vtrigprevexpr___TOP__clk_i__0 = vlSelfRef.clk_i;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vcs_common___024root___dump_triggers__act(vlSelf);
    }
#endif
}

void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_gettimeofday_sec_TOP__shunt_dpi_pkg(QData/*63:0*/ &shunt_dpi_gettimeofday_sec__Vfuncrtn);

VL_INLINE_OPT void Vcs_common___024root___nba_sequent__TOP__0(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___nba_sequent__TOP__0\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    QData/*63:0*/ __Vfunc_shunt_dpi_gettimeofday_sec__1__Vfuncout;
    __Vfunc_shunt_dpi_gettimeofday_sec__1__Vfuncout = 0;
    IData/*31:0*/ __Vdly__top_sim__DOT__clk_cnt;
    __Vdly__top_sim__DOT__clk_cnt = 0;
    // Body
    __Vdly__top_sim__DOT__clk_cnt = vlSelfRef.top_sim__DOT__clk_cnt;
    VL_WRITEF_NX("Current Time(%0d)  Time(%0t)\n",0,
                 64,([&]() {
                    Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_gettimeofday_sec_TOP__shunt_dpi_pkg(__Vfunc_shunt_dpi_gettimeofday_sec__1__Vfuncout);
                }(), __Vfunc_shunt_dpi_gettimeofday_sec__1__Vfuncout),
                 64,VL_TIME_UNITED_Q(1),-12);
    if (VL_UNLIKELY((0x3e8ULL < VL_TIME_UNITED_Q(1)))) {
        VL_FINISH_MT("top_sim.v", 23, "");
    }
    __Vdly__top_sim__DOT__clk_cnt = ((IData)(1U) + vlSelfRef.top_sim__DOT__clk_cnt);
    vlSelfRef.top_sim__DOT__reset_n = (0xaU < vlSelfRef.top_sim__DOT__clk_cnt);
    vlSelfRef.top_sim__DOT__clk_cnt = __Vdly__top_sim__DOT__clk_cnt;
}

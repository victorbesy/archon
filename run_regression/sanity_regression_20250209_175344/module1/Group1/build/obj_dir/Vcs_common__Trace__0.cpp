// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Tracing implementation internals
#include "verilated_vcd_c.h"
#include "Vcs_common__Syms.h"


void Vcs_common___024root__trace_chg_0_sub_0(Vcs_common___024root* vlSelf, VerilatedVcd::Buffer* bufp);

void Vcs_common___024root__trace_chg_0(void* voidSelf, VerilatedVcd::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root__trace_chg_0\n"); );
    // Init
    Vcs_common___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vcs_common___024root*>(voidSelf);
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    if (VL_UNLIKELY(!vlSymsp->__Vm_activity)) return;
    // Body
    Vcs_common___024root__trace_chg_0_sub_0((&vlSymsp->TOP), bufp);
}

void Vcs_common___024root__trace_chg_0_sub_0(Vcs_common___024root* vlSelf, VerilatedVcd::Buffer* bufp) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root__trace_chg_0_sub_0\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    uint32_t* const oldp VL_ATTR_UNUSED = bufp->oldp(vlSymsp->__Vm_baseCode + 1);
    // Body
    if (VL_UNLIKELY(vlSelfRef.__Vm_traceActivity[0U])) {
        bufp->chgQData(oldp+0,(vlSelfRef.top_sim__DOT__start_time),64);
        bufp->chgQData(oldp+2,(vlSelfRef.top_sim__DOT__event_cnt),64);
        bufp->chgQData(oldp+4,(vlSelfRef.top_sim__DOT__startTime),64);
    }
    bufp->chgBit(oldp+6,(vlSelfRef.clk_i));
    bufp->chgBit(oldp+7,(vlSelfRef.top_sim__DOT__reset_n));
    bufp->chgIData(oldp+8,(vlSelfRef.top_sim__DOT__clk_cnt),32);
}

void Vcs_common___024root__trace_cleanup(void* voidSelf, VerilatedVcd* /*unused*/) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root__trace_cleanup\n"); );
    // Init
    Vcs_common___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vcs_common___024root*>(voidSelf);
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    // Body
    vlSymsp->__Vm_activity = false;
    vlSymsp->TOP.__Vm_traceActivity[0U] = 0U;
}

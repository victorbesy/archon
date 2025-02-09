// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vcs_common.h for the primary calling header

#include "Vcs_common__pch.h"
#include "Vcs_common___024root.h"

VL_ATTR_COLD void Vcs_common___024root___eval_static__TOP(Vcs_common___024root* vlSelf);
VL_ATTR_COLD void Vcs_common___024root____Vm_traceActivitySetAll(Vcs_common___024root* vlSelf);

VL_ATTR_COLD void Vcs_common___024root___eval_static(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___eval_static\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    Vcs_common___024root___eval_static__TOP(vlSelf);
    Vcs_common___024root____Vm_traceActivitySetAll(vlSelf);
}

VL_ATTR_COLD void Vcs_common___024root___eval_static__TOP(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___eval_static__TOP\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.top_sim__DOT__clk_cnt = 0U;
    vlSelfRef.top_sim__DOT__start_time = 0ULL;
    vlSelfRef.top_sim__DOT__event_cnt = 0ULL;
    vlSelfRef.top_sim__DOT__startTime = 0ULL;
}

VL_ATTR_COLD void Vcs_common___024root___eval_initial__TOP(Vcs_common___024root* vlSelf);

VL_ATTR_COLD void Vcs_common___024root___eval_initial(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___eval_initial\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    Vcs_common___024root___eval_initial__TOP(vlSelf);
    Vcs_common___024root____Vm_traceActivitySetAll(vlSelf);
    vlSelfRef.__Vtrigprevexpr___TOP__clk_i__0 = vlSelfRef.clk_i;
}

VL_ATTR_COLD void Vcs_common___024root___eval_final(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___eval_final\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

VL_ATTR_COLD void Vcs_common___024root___eval_settle(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___eval_settle\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vcs_common___024root___dump_triggers__act(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___dump_triggers__act\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VactTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
    if ((1ULL & vlSelfRef.__VactTriggered.word(0U))) {
        VL_DBG_MSGF("         'act' region trigger index 0 is active: @(posedge clk_i)\n");
    }
}
#endif  // VL_DEBUG

#ifdef VL_DEBUG
VL_ATTR_COLD void Vcs_common___024root___dump_triggers__nba(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___dump_triggers__nba\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VnbaTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
    if ((1ULL & vlSelfRef.__VnbaTriggered.word(0U))) {
        VL_DBG_MSGF("         'nba' region trigger index 0 is active: @(posedge clk_i)\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD void Vcs_common___024root____Vm_traceActivitySetAll(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root____Vm_traceActivitySetAll\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__Vm_traceActivity[0U] = 1U;
}

VL_ATTR_COLD void Vcs_common___024root___ctor_var_reset(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___ctor_var_reset\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelf->clk_i = VL_RAND_RESET_I(1);
    vlSelf->top_sim__DOT__reset_n = VL_RAND_RESET_I(1);
    vlSelf->top_sim__DOT__clk_cnt = VL_RAND_RESET_I(32);
    vlSelf->top_sim__DOT__start_time = VL_RAND_RESET_Q(64);
    vlSelf->top_sim__DOT__event_cnt = 0;
    vlSelf->top_sim__DOT__startTime = 0;
    vlSelf->__Vtrigprevexpr___TOP__clk_i__0 = VL_RAND_RESET_I(1);
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__Vm_traceActivity[__Vi0] = 0;
    }
}

// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VHelloWorld.h for the primary calling header

#include "VHelloWorld__pch.h"
#include "VHelloWorld___024root.h"

void VHelloWorld___024root___eval_act(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_act\n"); );
}

void VHelloWorld___024root___eval_nba(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_nba\n"); );
}

void VHelloWorld___024root___eval_triggers__act(VHelloWorld___024root* vlSelf);

bool VHelloWorld___024root___eval_phase__act(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_phase__act\n"); );
    // Init
    VlTriggerVec<0> __VpreTriggered;
    CData/*0:0*/ __VactExecute;
    // Body
    VHelloWorld___024root___eval_triggers__act(vlSelf);
    __VactExecute = vlSelf->__VactTriggered.any();
    if (__VactExecute) {
        __VpreTriggered.andNot(vlSelf->__VactTriggered, vlSelf->__VnbaTriggered);
        vlSelf->__VnbaTriggered.thisOr(vlSelf->__VactTriggered);
        VHelloWorld___024root___eval_act(vlSelf);
    }
    return (__VactExecute);
}

bool VHelloWorld___024root___eval_phase__nba(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_phase__nba\n"); );
    // Init
    CData/*0:0*/ __VnbaExecute;
    // Body
    __VnbaExecute = vlSelf->__VnbaTriggered.any();
    if (__VnbaExecute) {
        VHelloWorld___024root___eval_nba(vlSelf);
        vlSelf->__VnbaTriggered.clear();
    }
    return (__VnbaExecute);
}

#ifdef VL_DEBUG
VL_ATTR_COLD void VHelloWorld___024root___dump_triggers__nba(VHelloWorld___024root* vlSelf);
#endif  // VL_DEBUG
#ifdef VL_DEBUG
VL_ATTR_COLD void VHelloWorld___024root___dump_triggers__act(VHelloWorld___024root* vlSelf);
#endif  // VL_DEBUG

void VHelloWorld___024root___eval(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval\n"); );
    // Init
    IData/*31:0*/ __VnbaIterCount;
    CData/*0:0*/ __VnbaContinue;
    // Body
    __VnbaIterCount = 0U;
    __VnbaContinue = 1U;
    while (__VnbaContinue) {
        if (VL_UNLIKELY((0x64U < __VnbaIterCount))) {
#ifdef VL_DEBUG
            VHelloWorld___024root___dump_triggers__nba(vlSelf);
#endif
            VL_FATAL_MT("HelloWorld.sv", 2, "", "NBA region did not converge.");
        }
        __VnbaIterCount = ((IData)(1U) + __VnbaIterCount);
        __VnbaContinue = 0U;
        vlSelf->__VactIterCount = 0U;
        vlSelf->__VactContinue = 1U;
        while (vlSelf->__VactContinue) {
            if (VL_UNLIKELY((0x64U < vlSelf->__VactIterCount))) {
#ifdef VL_DEBUG
                VHelloWorld___024root___dump_triggers__act(vlSelf);
#endif
                VL_FATAL_MT("HelloWorld.sv", 2, "", "Active region did not converge.");
            }
            vlSelf->__VactIterCount = ((IData)(1U) 
                                       + vlSelf->__VactIterCount);
            vlSelf->__VactContinue = 0U;
            if (VHelloWorld___024root___eval_phase__act(vlSelf)) {
                vlSelf->__VactContinue = 1U;
            }
        }
        if (VHelloWorld___024root___eval_phase__nba(vlSelf)) {
            __VnbaContinue = 1U;
        }
    }
}

#ifdef VL_DEBUG
void VHelloWorld___024root___eval_debug_assertions(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_debug_assertions\n"); );
}
#endif  // VL_DEBUG

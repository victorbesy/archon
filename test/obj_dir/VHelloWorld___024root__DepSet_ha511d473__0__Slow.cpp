// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VHelloWorld.h for the primary calling header

#include "VHelloWorld__pch.h"
#include "VHelloWorld___024root.h"

VL_ATTR_COLD void VHelloWorld___024root___eval_static(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_static\n"); );
}

VL_ATTR_COLD void VHelloWorld___024root___eval_initial__TOP(VHelloWorld___024root* vlSelf);

VL_ATTR_COLD void VHelloWorld___024root___eval_initial(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_initial\n"); );
    // Body
    VHelloWorld___024root___eval_initial__TOP(vlSelf);
}

VL_ATTR_COLD void VHelloWorld___024root___eval_initial__TOP(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_initial__TOP\n"); );
    // Body
    if (VL_UNLIKELY((! VL_VALUEPLUSARGS_INI(32, std::string{"seed=%d"}, 
                                            vlSelf->HelloWorld__DOT__unnamedblk1__DOT__seed)))) {
        VL_WRITEF_NX("No seed provided, using default seed.\n",0);
        vlSelf->HelloWorld__DOT__unnamedblk1__DOT__seed 
            = VL_RANDOM_I();
    }
    (void)VL_URANDOM_SEEDED_II(vlSelf->HelloWorld__DOT__unnamedblk1__DOT__seed);
    VL_WRITEF_NX("Starting simulation with a delay of 1 time units.\nHello, World!\n",0);
    VL_FINISH_MT("HelloWorld.sv", 32, "");
}

VL_ATTR_COLD void VHelloWorld___024root___eval_final(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_final\n"); );
}

VL_ATTR_COLD void VHelloWorld___024root___eval_settle(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_settle\n"); );
}

#ifdef VL_DEBUG
VL_ATTR_COLD void VHelloWorld___024root___dump_triggers__act(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___dump_triggers__act\n"); );
    // Body
    if ((1U & (~ (IData)(vlSelf->__VactTriggered.any())))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
}
#endif  // VL_DEBUG

#ifdef VL_DEBUG
VL_ATTR_COLD void VHelloWorld___024root___dump_triggers__nba(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___dump_triggers__nba\n"); );
    // Body
    if ((1U & (~ (IData)(vlSelf->__VnbaTriggered.any())))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD void VHelloWorld___024root___ctor_var_reset(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___ctor_var_reset\n"); );
    // Body
    vlSelf->HelloWorld__DOT__unnamedblk1__DOT__seed = 0;
}

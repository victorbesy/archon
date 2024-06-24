// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VHelloWorld.h for the primary calling header

#include "VHelloWorld__pch.h"
#include "VHelloWorld__Syms.h"
#include "VHelloWorld___024root.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void VHelloWorld___024root___dump_triggers__act(VHelloWorld___024root* vlSelf);
#endif  // VL_DEBUG

void VHelloWorld___024root___eval_triggers__act(VHelloWorld___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VHelloWorld__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VHelloWorld___024root___eval_triggers__act\n"); );
    // Body
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        VHelloWorld___024root___dump_triggers__act(vlSelf);
    }
#endif
}

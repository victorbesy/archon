// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Tracing implementation internals
#include "verilated_vcd_c.h"
#include "Vcs_common__Syms.h"


VL_ATTR_COLD void Vcs_common___024root__trace_init_sub__TOP__0(Vcs_common___024root* vlSelf, VerilatedVcd* tracep) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root__trace_init_sub__TOP__0\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    const int c = vlSymsp->__Vm_baseCode;
    // Body
    tracep->declBit(c+7,0,"clk_i",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->pushPrefix("top_sim", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+7,0,"clk_i",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+8,0,"reset_n",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBus(c+9,0,"clk_cnt",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1, 31,0);
    tracep->declQuad(c+1,0,"start_time",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::TIME, false,-1, 63,0);
    tracep->declQuad(c+3,0,"event_cnt",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LONGINT, false,-1, 63,0);
    tracep->declQuad(c+5,0,"startTime",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LONGINT, false,-1, 63,0);
    tracep->declQuad(c+10,0,"endTime",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LONGINT, false,-1, 63,0);
    tracep->popPrefix();
}

VL_ATTR_COLD void Vcs_common___024root__trace_init_top(Vcs_common___024root* vlSelf, VerilatedVcd* tracep) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root__trace_init_top\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    Vcs_common___024root__trace_init_sub__TOP__0(vlSelf, tracep);
}

VL_ATTR_COLD void Vcs_common___024root__trace_const_0(void* voidSelf, VerilatedVcd::Buffer* bufp);
VL_ATTR_COLD void Vcs_common___024root__trace_full_0(void* voidSelf, VerilatedVcd::Buffer* bufp);
void Vcs_common___024root__trace_chg_0(void* voidSelf, VerilatedVcd::Buffer* bufp);
void Vcs_common___024root__trace_cleanup(void* voidSelf, VerilatedVcd* /*unused*/);

VL_ATTR_COLD void Vcs_common___024root__trace_register(Vcs_common___024root* vlSelf, VerilatedVcd* tracep) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root__trace_register\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    tracep->addConstCb(&Vcs_common___024root__trace_const_0, 0U, vlSelf);
    tracep->addFullCb(&Vcs_common___024root__trace_full_0, 0U, vlSelf);
    tracep->addChgCb(&Vcs_common___024root__trace_chg_0, 0U, vlSelf);
    tracep->addCleanupCb(&Vcs_common___024root__trace_cleanup, vlSelf);
}

VL_ATTR_COLD void Vcs_common___024root__trace_const_0_sub_0(Vcs_common___024root* vlSelf, VerilatedVcd::Buffer* bufp);

VL_ATTR_COLD void Vcs_common___024root__trace_const_0(void* voidSelf, VerilatedVcd::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root__trace_const_0\n"); );
    // Init
    Vcs_common___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vcs_common___024root*>(voidSelf);
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    // Body
    Vcs_common___024root__trace_const_0_sub_0((&vlSymsp->TOP), bufp);
}

VL_ATTR_COLD void Vcs_common___024root__trace_const_0_sub_0(Vcs_common___024root* vlSelf, VerilatedVcd::Buffer* bufp) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root__trace_const_0_sub_0\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    uint32_t* const oldp VL_ATTR_UNUSED = bufp->oldp(vlSymsp->__Vm_baseCode);
    // Body
    bufp->fullQData(oldp+10,(0ULL),64);
}

VL_ATTR_COLD void Vcs_common___024root__trace_full_0_sub_0(Vcs_common___024root* vlSelf, VerilatedVcd::Buffer* bufp);

VL_ATTR_COLD void Vcs_common___024root__trace_full_0(void* voidSelf, VerilatedVcd::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root__trace_full_0\n"); );
    // Init
    Vcs_common___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vcs_common___024root*>(voidSelf);
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    // Body
    Vcs_common___024root__trace_full_0_sub_0((&vlSymsp->TOP), bufp);
}

VL_ATTR_COLD void Vcs_common___024root__trace_full_0_sub_0(Vcs_common___024root* vlSelf, VerilatedVcd::Buffer* bufp) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root__trace_full_0_sub_0\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    uint32_t* const oldp VL_ATTR_UNUSED = bufp->oldp(vlSymsp->__Vm_baseCode);
    // Body
    bufp->fullQData(oldp+1,(vlSelfRef.top_sim__DOT__start_time),64);
    bufp->fullQData(oldp+3,(vlSelfRef.top_sim__DOT__event_cnt),64);
    bufp->fullQData(oldp+5,(vlSelfRef.top_sim__DOT__startTime),64);
    bufp->fullBit(oldp+7,(vlSelfRef.clk_i));
    bufp->fullBit(oldp+8,(vlSelfRef.top_sim__DOT__reset_n));
    bufp->fullIData(oldp+9,(vlSelfRef.top_sim__DOT__clk_cnt),32);
}

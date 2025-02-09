// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vcs_common.h for the primary calling header

#include "Vcs_common__pch.h"
#include "Vcs_common__Syms.h"
#include "Vcs_common___024root.h"

void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_gettimeofday_sec_TOP__shunt_dpi_pkg(QData/*63:0*/ &shunt_dpi_gettimeofday_sec__Vfuncrtn);

VL_ATTR_COLD void Vcs_common___024root___eval_initial__TOP(Vcs_common___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vcs_common__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vcs_common___024root___eval_initial__TOP\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    QData/*63:0*/ __Vfunc_shunt_dpi_gettimeofday_sec__0__Vfuncout;
    __Vfunc_shunt_dpi_gettimeofday_sec__0__Vfuncout = 0;
    // Body
    vlSelfRef.top_sim__DOT__start_time = VL_TIME_UNITED_Q(1);
    Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_gettimeofday_sec_TOP__shunt_dpi_pkg(__Vfunc_shunt_dpi_gettimeofday_sec__0__Vfuncout);
    vlSelfRef.top_sim__DOT__startTime = __Vfunc_shunt_dpi_gettimeofday_sec__0__Vfuncout;
    vlSelfRef.top_sim__DOT__event_cnt = 0ULL;
}

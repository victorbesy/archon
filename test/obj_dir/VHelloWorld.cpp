// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Model implementation (design independent parts)

#include "VHelloWorld__pch.h"

//============================================================
// Constructors

VHelloWorld::VHelloWorld(VerilatedContext* _vcontextp__, const char* _vcname__)
    : VerilatedModel{*_vcontextp__}
    , vlSymsp{new VHelloWorld__Syms(contextp(), _vcname__, this)}
    , rootp{&(vlSymsp->TOP)}
{
    // Register model with the context
    contextp()->addModel(this);
}

VHelloWorld::VHelloWorld(const char* _vcname__)
    : VHelloWorld(Verilated::threadContextp(), _vcname__)
{
}

//============================================================
// Destructor

VHelloWorld::~VHelloWorld() {
    delete vlSymsp;
}

//============================================================
// Evaluation function

#ifdef VL_DEBUG
void VHelloWorld___024root___eval_debug_assertions(VHelloWorld___024root* vlSelf);
#endif  // VL_DEBUG
void VHelloWorld___024root___eval_static(VHelloWorld___024root* vlSelf);
void VHelloWorld___024root___eval_initial(VHelloWorld___024root* vlSelf);
void VHelloWorld___024root___eval_settle(VHelloWorld___024root* vlSelf);
void VHelloWorld___024root___eval(VHelloWorld___024root* vlSelf);

void VHelloWorld::eval_step() {
    VL_DEBUG_IF(VL_DBG_MSGF("+++++TOP Evaluate VHelloWorld::eval_step\n"); );
#ifdef VL_DEBUG
    // Debug assertions
    VHelloWorld___024root___eval_debug_assertions(&(vlSymsp->TOP));
#endif  // VL_DEBUG
    vlSymsp->__Vm_deleter.deleteAll();
    if (VL_UNLIKELY(!vlSymsp->__Vm_didInit)) {
        vlSymsp->__Vm_didInit = true;
        VL_DEBUG_IF(VL_DBG_MSGF("+ Initial\n"););
        VHelloWorld___024root___eval_static(&(vlSymsp->TOP));
        VHelloWorld___024root___eval_initial(&(vlSymsp->TOP));
        VHelloWorld___024root___eval_settle(&(vlSymsp->TOP));
    }
    VL_DEBUG_IF(VL_DBG_MSGF("+ Eval\n"););
    VHelloWorld___024root___eval(&(vlSymsp->TOP));
    // Evaluate cleanup
    Verilated::endOfEval(vlSymsp->__Vm_evalMsgQp);
}

//============================================================
// Events and timing
bool VHelloWorld::eventsPending() { return false; }

uint64_t VHelloWorld::nextTimeSlot() {
    VL_FATAL_MT(__FILE__, __LINE__, "", "%Error: No delays in the design");
    return 0;
}

//============================================================
// Utilities

const char* VHelloWorld::name() const {
    return vlSymsp->name();
}

//============================================================
// Invoke final blocks

void VHelloWorld___024root___eval_final(VHelloWorld___024root* vlSelf);

VL_ATTR_COLD void VHelloWorld::final() {
    VHelloWorld___024root___eval_final(&(vlSymsp->TOP));
}

//============================================================
// Implementations of abstract methods from VerilatedModel

const char* VHelloWorld::hierName() const { return vlSymsp->name(); }
const char* VHelloWorld::modelName() const { return "VHelloWorld"; }
unsigned VHelloWorld::threads() const { return 1; }
void VHelloWorld::prepareClone() const { contextp()->prepareClone(); }
void VHelloWorld::atClone() const {
    contextp()->threadPoolpOnClone();
}

//============================================================
// Trace configuration

VL_ATTR_COLD void VHelloWorld::trace(VerilatedVcdC* tfp, int levels, int options) {
    vl_fatal(__FILE__, __LINE__, __FILE__,"'VHelloWorld::trace()' called on model that was Verilated without --trace option");
}

// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table internal header
//
// Internal details; most calling programs do not need this header,
// unless using verilator public meta comments.

#ifndef VERILATED_VCS_COMMON__SYMS_H_
#define VERILATED_VCS_COMMON__SYMS_H_  // guard

#include "verilated.h"

// INCLUDE MODEL CLASS

#include "Vcs_common.h"

// INCLUDE MODULE CLASSES
#include "Vcs_common___024root.h"
#include "Vcs_common_shunt_dpi_pkg.h"
#include "Vcs_common___024unit.h"

// DPI TYPES for DPI Export callbacks (Internal use)

// SYMS CLASS (contains all model state)
class alignas(VL_CACHE_LINE_BYTES)Vcs_common__Syms final : public VerilatedSyms {
  public:
    // INTERNAL STATE
    Vcs_common* const __Vm_modelp;
    bool __Vm_activity = false;  ///< Used by trace routines to determine change occurred
    uint32_t __Vm_baseCode = 0;  ///< Used by trace routines when tracing multiple models
    VlDeleter __Vm_deleter;
    bool __Vm_didInit = false;

    // MODULE INSTANCE STATE
    Vcs_common___024root           TOP;
    Vcs_common_shunt_dpi_pkg       TOP__shunt_dpi_pkg;

    // CONSTRUCTORS
    Vcs_common__Syms(VerilatedContext* contextp, const char* namep, Vcs_common* modelp);
    ~Vcs_common__Syms();

    // METHODS
    const char* name() { return TOP.name(); }
};

#endif  // guard

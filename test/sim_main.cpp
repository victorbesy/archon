// sim_main.cpp
#include "VHelloWorld.h"
#include "verilated.h"

int main(int argc, char **argv, char **env) {
    Verilated::commandArgs(argc, argv);
    VHelloWorld* top = new VHelloWorld;
    while (!Verilated::gotFinish()) { top->eval(); }
    delete top;
    return 0;
}


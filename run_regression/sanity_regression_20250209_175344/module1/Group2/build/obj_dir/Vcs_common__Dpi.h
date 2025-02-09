// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Prototypes for DPI import and export functions.
//
// Verilator includes this file in all generated .cpp files that use DPI functions.
// Manually include this file where DPI .c import functions are declared to ensure
// the C functions match the expectations of the DPI imports.

#ifndef VERILATED_VCS_COMMON__DPI_H_
#define VERILATED_VCS_COMMON__DPI_H_  // guard

#include "svdpi.h"

#ifdef __cplusplus
extern "C" {
#endif


    // DPI IMPORTS
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:131:33
    extern void shunt_dpi_close_socket(int fd);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:180:33
    extern int shunt_dpi_get_status_socket(int fd, int evnt);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1614:35
    extern long long shunt_dpi_gettimeofday_sec();
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1627:36
    extern long long shunt_dpi_gettimeofday_usec();
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1033:36
    extern long long shunt_dpi_hash(const char* str);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1316:32
    extern int shunt_dpi_hs_recv_string(int sockid, const svBitVecVal* h_trnx, const char** String);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1295:32
    extern int shunt_dpi_hs_send_string(int sockid, const svBitVecVal* h_trnx, const char* String);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:82:32
    extern int shunt_dpi_initiator_init(int portno);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:215:32
    extern int shunt_dpi_listener_init(int portno);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:526:32
    extern int shunt_dpi_recv_bit(int sockid, svBit* Bit);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:415:32
    extern int shunt_dpi_recv_byte(int sockid, char* Byte);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1076:32
    extern int shunt_dpi_recv_header(int sockid, svBitVecVal* h);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:343:32
    extern int shunt_dpi_recv_int(int sockid, int* Int);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:798:32
    extern int shunt_dpi_recv_intV(int sockid, int size, const svOpenArrayHandle Int);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:453:32
    extern int shunt_dpi_recv_integer(int sockid, svLogicVecVal* Integer);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:601:32
    extern int shunt_dpi_recv_logic(int sockid, svLogic* Logic);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:379:32
    extern int shunt_dpi_recv_long(int sockid, long long* Long);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:875:32
    extern int shunt_dpi_recv_longV(int sockid, int size, const svOpenArrayHandle Int);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1598:32
    extern int shunt_dpi_recv_pkt_longV(int sockid, svBitVecVal* h, const svOpenArrayHandle Int);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:640:32
    extern int shunt_dpi_recv_real(int sockid, double* Real);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:564:32
    extern int shunt_dpi_recv_reg(int sockid, svLogic* Reg);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:307:32
    extern int shunt_dpi_recv_short(int sockid, short* Short);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:837:32
    extern int shunt_dpi_recv_shortV(int sockid, int size, const svOpenArrayHandle Int);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:758:32
    extern int shunt_dpi_recv_string(int sockid, int size, const char** String);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:508:32
    extern int shunt_dpi_send_bit(int sockid, svBit Bit);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:397:32
    extern int shunt_dpi_send_byte(int sockid, char Byte);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1055:32
    extern int shunt_dpi_send_header(int sockid, const svBitVecVal* h);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:325:32
    extern int shunt_dpi_send_int(int sockid, int Int);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:779:32
    extern int shunt_dpi_send_intV(int sockid, int size, const svOpenArrayHandle Int);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:433:32
    extern int shunt_dpi_send_integer(int sockid, const svLogicVecVal* Integer);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:582:32
    extern int shunt_dpi_send_logic(int sockid, svLogic Logic);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:361:32
    extern int shunt_dpi_send_long(int sockid, long long Long);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:856:32
    extern int shunt_dpi_send_longV(int sockid, int size, const svOpenArrayHandle Int);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1580:32
    extern int shunt_dpi_send_pkt_longV(int sockid, const svBitVecVal* h_trnx, const svOpenArrayHandle Int);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:622:32
    extern int shunt_dpi_send_real(int sockid, double Real);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:546:32
    extern int shunt_dpi_send_reg(int sockid, svLogic Reg);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:289:32
    extern int shunt_dpi_send_short(int sockid, short Short);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:818:32
    extern int shunt_dpi_send_shortV(int sockid, int size, const svOpenArrayHandle Int);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:740:32
    extern int shunt_dpi_send_string(int sockid, int size, const char* String);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:114:32
    extern int shunt_dpi_target_init(int portno, const char* hostname);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:231:32
    extern int shunt_dpi_tcp_connect(int parentfd);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:251:32
    extern int shunt_dpi_tcp_get_port(int socket);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:199:34
    extern void shunt_dpi_tcp_nodelay_socket(int flag, int sockfd);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:269:32
    extern int shunt_dpi_tcp_parent_init_initiator_dpa();
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1868:36
    extern long long shunt_dpi_tlm_axi3_ext_id();
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1850:37
    extern long long shunt_dpi_tlm_data_id();
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1831:36
    extern long long shunt_dpi_tlm_header_id();
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1967:33
    extern void shunt_dpi_tlm_recv_axi3_header(int sockid, svBitVecVal* h);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1997:33
    extern void shunt_dpi_tlm_recv_gp_data(int sockid, const svBitVecVal* h, const svOpenArrayHandle data, const svOpenArrayHandle byte_enable);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1937:34
    extern void shunt_dpi_tlm_recv_gp_header(int sockid, svBitVecVal* h);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1922:35
    extern void shunt_dpi_tlm_recv_gp_transport(int sockid, svBitVecVal* h, const svOpenArrayHandle data, const svOpenArrayHandle byte_enable);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1982:33
    extern void shunt_dpi_tlm_send_axi3_header(int sockid, svBitVecVal* h);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1813:34
    extern void shunt_dpi_tlm_send_command(int socket, int Com);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1952:34
    extern void shunt_dpi_tlm_send_gp_header(int sockid, svBitVecVal* h);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1906:33
    extern void shunt_dpi_tlm_send_gp_transport(int sockid, svBitVecVal* h, const svOpenArrayHandle data, const svOpenArrayHandle byte_enable);
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:1887:37
    extern long long shunt_dpi_tlm_signal_id();
    // DPI import at /home/v/workspace/Shunt/utils/dpi/src/shunt_dpi_pkg.sv:149:33
    extern void shunt_dpi_unblock_socket(int flag, int fd);

#ifdef __cplusplus
}
#endif

#endif  // guard

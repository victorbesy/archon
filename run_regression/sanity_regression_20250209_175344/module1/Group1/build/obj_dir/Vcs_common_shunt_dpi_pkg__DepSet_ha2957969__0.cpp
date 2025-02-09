// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vcs_common.h for the primary calling header

#include "Vcs_common__pch.h"
#include "Vcs_common__Syms.h"
#include "Vcs_common_shunt_dpi_pkg.h"

extern "C" int shunt_dpi_initiator_init(int portno);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_initiator_init_TOP__shunt_dpi_pkg(IData/*31:0*/ portno, IData/*31:0*/ &shunt_dpi_initiator_init__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_initiator_init_TOP__shunt_dpi_pkg\n"); );
    // Body
    int portno__Vcvt;
    for (size_t portno__Vidx = 0; portno__Vidx < 1; ++portno__Vidx) portno__Vcvt = portno;
    int shunt_dpi_initiator_init__Vfuncrtn__Vcvt;
    shunt_dpi_initiator_init__Vfuncrtn__Vcvt = shunt_dpi_initiator_init(portno__Vcvt);
    shunt_dpi_initiator_init__Vfuncrtn = shunt_dpi_initiator_init__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_target_init(int portno, const char* hostname);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_target_init_TOP__shunt_dpi_pkg(IData/*31:0*/ portno, std::string hostname, IData/*31:0*/ &shunt_dpi_target_init__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_target_init_TOP__shunt_dpi_pkg\n"); );
    // Body
    int portno__Vcvt;
    for (size_t portno__Vidx = 0; portno__Vidx < 1; ++portno__Vidx) portno__Vcvt = portno;
    const char* hostname__Vcvt;
    for (size_t hostname__Vidx = 0; hostname__Vidx < 1; ++hostname__Vidx) hostname__Vcvt = hostname.c_str();
    int shunt_dpi_target_init__Vfuncrtn__Vcvt;
    shunt_dpi_target_init__Vfuncrtn__Vcvt = shunt_dpi_target_init(portno__Vcvt, hostname__Vcvt);
    shunt_dpi_target_init__Vfuncrtn = shunt_dpi_target_init__Vfuncrtn__Vcvt;
}

extern "C" void shunt_dpi_close_socket(int fd);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_close_socket_TOP__shunt_dpi_pkg(IData/*31:0*/ fd) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_close_socket_TOP__shunt_dpi_pkg\n"); );
    // Body
    int fd__Vcvt;
    for (size_t fd__Vidx = 0; fd__Vidx < 1; ++fd__Vidx) fd__Vcvt = fd;
    shunt_dpi_close_socket(fd__Vcvt);
}

extern "C" void shunt_dpi_unblock_socket(int flag, int fd);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_unblock_socket_TOP__shunt_dpi_pkg(IData/*31:0*/ flag, IData/*31:0*/ fd) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_unblock_socket_TOP__shunt_dpi_pkg\n"); );
    // Body
    int flag__Vcvt;
    for (size_t flag__Vidx = 0; flag__Vidx < 1; ++flag__Vidx) flag__Vcvt = flag;
    int fd__Vcvt;
    for (size_t fd__Vidx = 0; fd__Vidx < 1; ++fd__Vidx) fd__Vcvt = fd;
    shunt_dpi_unblock_socket(flag__Vcvt, fd__Vcvt);
}

extern "C" int shunt_dpi_get_status_socket(int fd, int evnt);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_get_status_socket_TOP__shunt_dpi_pkg(IData/*31:0*/ fd, IData/*31:0*/ evnt, IData/*31:0*/ &shunt_dpi_get_status_socket__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_get_status_socket_TOP__shunt_dpi_pkg\n"); );
    // Body
    int fd__Vcvt;
    for (size_t fd__Vidx = 0; fd__Vidx < 1; ++fd__Vidx) fd__Vcvt = fd;
    int evnt__Vcvt;
    for (size_t evnt__Vidx = 0; evnt__Vidx < 1; ++evnt__Vidx) evnt__Vcvt = evnt;
    int shunt_dpi_get_status_socket__Vfuncrtn__Vcvt;
    shunt_dpi_get_status_socket__Vfuncrtn__Vcvt = shunt_dpi_get_status_socket(fd__Vcvt, evnt__Vcvt);
    shunt_dpi_get_status_socket__Vfuncrtn = shunt_dpi_get_status_socket__Vfuncrtn__Vcvt;
}

extern "C" void shunt_dpi_tcp_nodelay_socket(int flag, int sockfd);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tcp_nodelay_socket_TOP__shunt_dpi_pkg(IData/*31:0*/ flag, IData/*31:0*/ sockfd) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tcp_nodelay_socket_TOP__shunt_dpi_pkg\n"); );
    // Body
    int flag__Vcvt;
    for (size_t flag__Vidx = 0; flag__Vidx < 1; ++flag__Vidx) flag__Vcvt = flag;
    int sockfd__Vcvt;
    for (size_t sockfd__Vidx = 0; sockfd__Vidx < 1; ++sockfd__Vidx) sockfd__Vcvt = sockfd;
    shunt_dpi_tcp_nodelay_socket(flag__Vcvt, sockfd__Vcvt);
}

extern "C" int shunt_dpi_listener_init(int portno);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_listener_init_TOP__shunt_dpi_pkg(IData/*31:0*/ portno, IData/*31:0*/ &shunt_dpi_listener_init__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_listener_init_TOP__shunt_dpi_pkg\n"); );
    // Body
    int portno__Vcvt;
    for (size_t portno__Vidx = 0; portno__Vidx < 1; ++portno__Vidx) portno__Vcvt = portno;
    int shunt_dpi_listener_init__Vfuncrtn__Vcvt;
    shunt_dpi_listener_init__Vfuncrtn__Vcvt = shunt_dpi_listener_init(portno__Vcvt);
    shunt_dpi_listener_init__Vfuncrtn = shunt_dpi_listener_init__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_tcp_connect(int parentfd);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tcp_connect_TOP__shunt_dpi_pkg(IData/*31:0*/ parentfd, IData/*31:0*/ &shunt_dpi_tcp_connect__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tcp_connect_TOP__shunt_dpi_pkg\n"); );
    // Body
    int parentfd__Vcvt;
    for (size_t parentfd__Vidx = 0; parentfd__Vidx < 1; ++parentfd__Vidx) parentfd__Vcvt = parentfd;
    int shunt_dpi_tcp_connect__Vfuncrtn__Vcvt;
    shunt_dpi_tcp_connect__Vfuncrtn__Vcvt = shunt_dpi_tcp_connect(parentfd__Vcvt);
    shunt_dpi_tcp_connect__Vfuncrtn = shunt_dpi_tcp_connect__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_tcp_get_port(int socket);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tcp_get_port_TOP__shunt_dpi_pkg(IData/*31:0*/ socket, IData/*31:0*/ &shunt_dpi_tcp_get_port__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tcp_get_port_TOP__shunt_dpi_pkg\n"); );
    // Body
    int socket__Vcvt;
    for (size_t socket__Vidx = 0; socket__Vidx < 1; ++socket__Vidx) socket__Vcvt = socket;
    int shunt_dpi_tcp_get_port__Vfuncrtn__Vcvt;
    shunt_dpi_tcp_get_port__Vfuncrtn__Vcvt = shunt_dpi_tcp_get_port(socket__Vcvt);
    shunt_dpi_tcp_get_port__Vfuncrtn = shunt_dpi_tcp_get_port__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_tcp_parent_init_initiator_dpa();

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tcp_parent_init_initiator_dpa_TOP__shunt_dpi_pkg(IData/*31:0*/ &shunt_dpi_tcp_parent_init_initiator_dpa__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tcp_parent_init_initiator_dpa_TOP__shunt_dpi_pkg\n"); );
    // Body
    int shunt_dpi_tcp_parent_init_initiator_dpa__Vfuncrtn__Vcvt;
    shunt_dpi_tcp_parent_init_initiator_dpa__Vfuncrtn__Vcvt = shunt_dpi_tcp_parent_init_initiator_dpa();
    shunt_dpi_tcp_parent_init_initiator_dpa__Vfuncrtn 
        = shunt_dpi_tcp_parent_init_initiator_dpa__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_short(int sockid, short Short);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_short_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, SData/*15:0*/ Short, IData/*31:0*/ &shunt_dpi_send_short__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_short_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    short Short__Vcvt;
    for (size_t Short__Vidx = 0; Short__Vidx < 1; ++Short__Vidx) Short__Vcvt = Short;
    int shunt_dpi_send_short__Vfuncrtn__Vcvt;
    shunt_dpi_send_short__Vfuncrtn__Vcvt = shunt_dpi_send_short(sockid__Vcvt, Short__Vcvt);
    shunt_dpi_send_short__Vfuncrtn = shunt_dpi_send_short__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_short(int sockid, short* Short);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_short_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, SData/*15:0*/ &Short, IData/*31:0*/ &shunt_dpi_recv_short__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_short_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    short Short__Vcvt;
    int shunt_dpi_recv_short__Vfuncrtn__Vcvt;
    shunt_dpi_recv_short__Vfuncrtn__Vcvt = shunt_dpi_recv_short(sockid__Vcvt, &Short__Vcvt);
    Short = (0xffffU & Short__Vcvt);
    shunt_dpi_recv_short__Vfuncrtn = shunt_dpi_recv_short__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_int(int sockid, int Int);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_int_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, IData/*31:0*/ Int, IData/*31:0*/ &shunt_dpi_send_int__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_int_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    int Int__Vcvt;
    for (size_t Int__Vidx = 0; Int__Vidx < 1; ++Int__Vidx) Int__Vcvt = Int;
    int shunt_dpi_send_int__Vfuncrtn__Vcvt;
    shunt_dpi_send_int__Vfuncrtn__Vcvt = shunt_dpi_send_int(sockid__Vcvt, Int__Vcvt);
    shunt_dpi_send_int__Vfuncrtn = shunt_dpi_send_int__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_int(int sockid, int* Int);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_int_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, IData/*31:0*/ &Int, IData/*31:0*/ &shunt_dpi_recv_int__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_int_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    int Int__Vcvt;
    int shunt_dpi_recv_int__Vfuncrtn__Vcvt;
    shunt_dpi_recv_int__Vfuncrtn__Vcvt = shunt_dpi_recv_int(sockid__Vcvt, &Int__Vcvt);
    Int = Int__Vcvt;
    shunt_dpi_recv_int__Vfuncrtn = shunt_dpi_recv_int__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_long(int sockid, long long Long);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_long_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, QData/*63:0*/ Long, IData/*31:0*/ &shunt_dpi_send_long__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_long_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    long long Long__Vcvt;
    for (size_t Long__Vidx = 0; Long__Vidx < 1; ++Long__Vidx) Long__Vcvt = Long;
    int shunt_dpi_send_long__Vfuncrtn__Vcvt;
    shunt_dpi_send_long__Vfuncrtn__Vcvt = shunt_dpi_send_long(sockid__Vcvt, Long__Vcvt);
    shunt_dpi_send_long__Vfuncrtn = shunt_dpi_send_long__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_long(int sockid, long long* Long);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_long_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, QData/*63:0*/ &Long, IData/*31:0*/ &shunt_dpi_recv_long__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_long_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    long long Long__Vcvt;
    int shunt_dpi_recv_long__Vfuncrtn__Vcvt;
    shunt_dpi_recv_long__Vfuncrtn__Vcvt = shunt_dpi_recv_long(sockid__Vcvt, &Long__Vcvt);
    Long = Long__Vcvt;
    shunt_dpi_recv_long__Vfuncrtn = shunt_dpi_recv_long__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_byte(int sockid, char Byte);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_byte_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, CData/*7:0*/ Byte, IData/*31:0*/ &shunt_dpi_send_byte__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_byte_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    char Byte__Vcvt;
    for (size_t Byte__Vidx = 0; Byte__Vidx < 1; ++Byte__Vidx) Byte__Vcvt = Byte;
    int shunt_dpi_send_byte__Vfuncrtn__Vcvt;
    shunt_dpi_send_byte__Vfuncrtn__Vcvt = shunt_dpi_send_byte(sockid__Vcvt, Byte__Vcvt);
    shunt_dpi_send_byte__Vfuncrtn = shunt_dpi_send_byte__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_byte(int sockid, char* Byte);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_byte_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, CData/*7:0*/ &Byte, IData/*31:0*/ &shunt_dpi_recv_byte__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_byte_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    char Byte__Vcvt;
    int shunt_dpi_recv_byte__Vfuncrtn__Vcvt;
    shunt_dpi_recv_byte__Vfuncrtn__Vcvt = shunt_dpi_recv_byte(sockid__Vcvt, &Byte__Vcvt);
    Byte = (0xffU & Byte__Vcvt);
    shunt_dpi_recv_byte__Vfuncrtn = shunt_dpi_recv_byte__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_integer(int sockid, const svLogicVecVal* Integer);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_integer_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, IData/*31:0*/ Integer, IData/*31:0*/ &shunt_dpi_send_integer__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_integer_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svLogicVecVal Integer__Vcvt[1];
    for (size_t Integer__Vidx = 0; Integer__Vidx < 1; ++Integer__Vidx) VL_SET_SVLV_I(32, Integer__Vcvt + 1 * Integer__Vidx, Integer);
    int shunt_dpi_send_integer__Vfuncrtn__Vcvt;
    shunt_dpi_send_integer__Vfuncrtn__Vcvt = shunt_dpi_send_integer(sockid__Vcvt, Integer__Vcvt);
    shunt_dpi_send_integer__Vfuncrtn = shunt_dpi_send_integer__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_integer(int sockid, svLogicVecVal* Integer);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_integer_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, IData/*31:0*/ &Integer, IData/*31:0*/ &shunt_dpi_recv_integer__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_integer_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svLogicVecVal Integer__Vcvt[1];
    for (size_t Integer__Vidx = 0; Integer__Vidx < 1; ++Integer__Vidx) VL_SET_SVLV_I(32, Integer__Vcvt + 1 * Integer__Vidx, Integer);
    int shunt_dpi_recv_integer__Vfuncrtn__Vcvt;
    shunt_dpi_recv_integer__Vfuncrtn__Vcvt = shunt_dpi_recv_integer(sockid__Vcvt, Integer__Vcvt);
    Integer = VL_SET_I_SVLV(Integer__Vcvt);
    shunt_dpi_recv_integer__Vfuncrtn = shunt_dpi_recv_integer__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_bit(int sockid, svBit Bit);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_bit_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, CData/*0:0*/ Bit, IData/*31:0*/ &shunt_dpi_send_bit__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_bit_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svBit Bit__Vcvt;
    for (size_t Bit__Vidx = 0; Bit__Vidx < 1; ++Bit__Vidx) Bit__Vcvt = Bit;
    int shunt_dpi_send_bit__Vfuncrtn__Vcvt;
    shunt_dpi_send_bit__Vfuncrtn__Vcvt = shunt_dpi_send_bit(sockid__Vcvt, Bit__Vcvt);
    shunt_dpi_send_bit__Vfuncrtn = shunt_dpi_send_bit__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_bit(int sockid, svBit* Bit);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_bit_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, CData/*0:0*/ &Bit, IData/*31:0*/ &shunt_dpi_recv_bit__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_bit_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svBit Bit__Vcvt;
    for (size_t Bit__Vidx = 0; Bit__Vidx < 1; ++Bit__Vidx) Bit__Vcvt = Bit;
    int shunt_dpi_recv_bit__Vfuncrtn__Vcvt;
    shunt_dpi_recv_bit__Vfuncrtn__Vcvt = shunt_dpi_recv_bit(sockid__Vcvt, &Bit__Vcvt);
    Bit = (1U & Bit__Vcvt);
    shunt_dpi_recv_bit__Vfuncrtn = shunt_dpi_recv_bit__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_reg(int sockid, svLogic Reg);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_reg_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, CData/*0:0*/ Reg, IData/*31:0*/ &shunt_dpi_send_reg__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_reg_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svLogic Reg__Vcvt;
    for (size_t Reg__Vidx = 0; Reg__Vidx < 1; ++Reg__Vidx) Reg__Vcvt = Reg;
    int shunt_dpi_send_reg__Vfuncrtn__Vcvt;
    shunt_dpi_send_reg__Vfuncrtn__Vcvt = shunt_dpi_send_reg(sockid__Vcvt, Reg__Vcvt);
    shunt_dpi_send_reg__Vfuncrtn = shunt_dpi_send_reg__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_reg(int sockid, svLogic* Reg);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_reg_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, CData/*0:0*/ &Reg, IData/*31:0*/ &shunt_dpi_recv_reg__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_reg_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svLogic Reg__Vcvt;
    for (size_t Reg__Vidx = 0; Reg__Vidx < 1; ++Reg__Vidx) Reg__Vcvt = Reg;
    int shunt_dpi_recv_reg__Vfuncrtn__Vcvt;
    shunt_dpi_recv_reg__Vfuncrtn__Vcvt = shunt_dpi_recv_reg(sockid__Vcvt, &Reg__Vcvt);
    Reg = (1U & Reg__Vcvt);
    shunt_dpi_recv_reg__Vfuncrtn = shunt_dpi_recv_reg__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_logic(int sockid, svLogic Logic);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_logic_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, CData/*0:0*/ Logic, IData/*31:0*/ &shunt_dpi_send_logic__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_logic_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svLogic Logic__Vcvt;
    for (size_t Logic__Vidx = 0; Logic__Vidx < 1; ++Logic__Vidx) Logic__Vcvt = Logic;
    int shunt_dpi_send_logic__Vfuncrtn__Vcvt;
    shunt_dpi_send_logic__Vfuncrtn__Vcvt = shunt_dpi_send_logic(sockid__Vcvt, Logic__Vcvt);
    shunt_dpi_send_logic__Vfuncrtn = shunt_dpi_send_logic__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_logic(int sockid, svLogic* Logic);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_logic_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, CData/*0:0*/ &Logic, IData/*31:0*/ &shunt_dpi_recv_logic__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_logic_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svLogic Logic__Vcvt;
    for (size_t Logic__Vidx = 0; Logic__Vidx < 1; ++Logic__Vidx) Logic__Vcvt = Logic;
    int shunt_dpi_recv_logic__Vfuncrtn__Vcvt;
    shunt_dpi_recv_logic__Vfuncrtn__Vcvt = shunt_dpi_recv_logic(sockid__Vcvt, &Logic__Vcvt);
    Logic = (1U & Logic__Vcvt);
    shunt_dpi_recv_logic__Vfuncrtn = shunt_dpi_recv_logic__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_real(int sockid, double Real);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_real_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, double Real, IData/*31:0*/ &shunt_dpi_send_real__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_real_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    double Real__Vcvt;
    for (size_t Real__Vidx = 0; Real__Vidx < 1; ++Real__Vidx) Real__Vcvt = Real;
    int shunt_dpi_send_real__Vfuncrtn__Vcvt;
    shunt_dpi_send_real__Vfuncrtn__Vcvt = shunt_dpi_send_real(sockid__Vcvt, Real__Vcvt);
    shunt_dpi_send_real__Vfuncrtn = shunt_dpi_send_real__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_real(int sockid, double* Real);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_real_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, double &Real, IData/*31:0*/ &shunt_dpi_recv_real__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_real_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    double Real__Vcvt;
    int shunt_dpi_recv_real__Vfuncrtn__Vcvt;
    shunt_dpi_recv_real__Vfuncrtn__Vcvt = shunt_dpi_recv_real(sockid__Vcvt, &Real__Vcvt);
    Real = Real__Vcvt;
    shunt_dpi_recv_real__Vfuncrtn = shunt_dpi_recv_real__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_string(int sockid, int size, const char* String);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_string_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, IData/*31:0*/ size, std::string String, IData/*31:0*/ &shunt_dpi_send_string__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_string_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    int size__Vcvt;
    for (size_t size__Vidx = 0; size__Vidx < 1; ++size__Vidx) size__Vcvt = size;
    const char* String__Vcvt;
    for (size_t String__Vidx = 0; String__Vidx < 1; ++String__Vidx) String__Vcvt = String.c_str();
    int shunt_dpi_send_string__Vfuncrtn__Vcvt;
    shunt_dpi_send_string__Vfuncrtn__Vcvt = shunt_dpi_send_string(sockid__Vcvt, size__Vcvt, String__Vcvt);
    shunt_dpi_send_string__Vfuncrtn = shunt_dpi_send_string__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_string(int sockid, int size, const char** String);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_string_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, IData/*31:0*/ size, std::string &String, IData/*31:0*/ &shunt_dpi_recv_string__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_string_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    int size__Vcvt;
    for (size_t size__Vidx = 0; size__Vidx < 1; ++size__Vidx) size__Vcvt = size;
    const char* String__Vcvt;
    for (size_t String__Vidx = 0; String__Vidx < 1; ++String__Vidx) String__Vcvt = String.c_str();
    int shunt_dpi_recv_string__Vfuncrtn__Vcvt;
    shunt_dpi_recv_string__Vfuncrtn__Vcvt = shunt_dpi_recv_string(sockid__Vcvt, size__Vcvt, &String__Vcvt);
    String = VL_CVT_N_CSTR(String__Vcvt);
    shunt_dpi_recv_string__Vfuncrtn = shunt_dpi_recv_string__Vfuncrtn__Vcvt;
}

extern "C" long long shunt_dpi_hash(const char* str);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_hash_TOP__shunt_dpi_pkg(std::string str, QData/*63:0*/ &shunt_dpi_hash__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_hash_TOP__shunt_dpi_pkg\n"); );
    // Body
    const char* str__Vcvt;
    for (size_t str__Vidx = 0; str__Vidx < 1; ++str__Vidx) str__Vcvt = str.c_str();
    long long shunt_dpi_hash__Vfuncrtn__Vcvt;
    shunt_dpi_hash__Vfuncrtn__Vcvt = shunt_dpi_hash(str__Vcvt);
    shunt_dpi_hash__Vfuncrtn = shunt_dpi_hash__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_send_header(int sockid, const svBitVecVal* h);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_header_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, VlWide<8>/*255:0*/ h, IData/*31:0*/ &shunt_dpi_send_header__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_send_header_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svBitVecVal h__Vcvt[8];
    for (size_t h__Vidx = 0; h__Vidx < 1; ++h__Vidx) VL_SET_SVBV_W(256, h__Vcvt + 8 * h__Vidx, h);
    int shunt_dpi_send_header__Vfuncrtn__Vcvt;
    shunt_dpi_send_header__Vfuncrtn__Vcvt = shunt_dpi_send_header(sockid__Vcvt, h__Vcvt);
    shunt_dpi_send_header__Vfuncrtn = shunt_dpi_send_header__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_recv_header(int sockid, svBitVecVal* h);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_header_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, VlWide<8>/*255:0*/ &h, IData/*31:0*/ &shunt_dpi_recv_header__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_recv_header_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svBitVecVal h__Vcvt[8];
    int shunt_dpi_recv_header__Vfuncrtn__Vcvt;
    shunt_dpi_recv_header__Vfuncrtn__Vcvt = shunt_dpi_recv_header(sockid__Vcvt, h__Vcvt);
    VL_SET_W_SVBV(256,h,h__Vcvt + 0);
shunt_dpi_recv_header__Vfuncrtn = shunt_dpi_recv_header__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_hs_send_string(int sockid, const svBitVecVal* h_trnx, const char* String);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_hs_send_string_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, VlWide<8>/*255:0*/ h_trnx, std::string String, IData/*31:0*/ &shunt_dpi_hs_send_string__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_hs_send_string_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svBitVecVal h_trnx__Vcvt[8];
    for (size_t h_trnx__Vidx = 0; h_trnx__Vidx < 1; ++h_trnx__Vidx) VL_SET_SVBV_W(256, h_trnx__Vcvt + 8 * h_trnx__Vidx, h_trnx);
    const char* String__Vcvt;
    for (size_t String__Vidx = 0; String__Vidx < 1; ++String__Vidx) String__Vcvt = String.c_str();
    int shunt_dpi_hs_send_string__Vfuncrtn__Vcvt;
    shunt_dpi_hs_send_string__Vfuncrtn__Vcvt = shunt_dpi_hs_send_string(sockid__Vcvt, h_trnx__Vcvt, String__Vcvt);
    shunt_dpi_hs_send_string__Vfuncrtn = shunt_dpi_hs_send_string__Vfuncrtn__Vcvt;
}

extern "C" int shunt_dpi_hs_recv_string(int sockid, const svBitVecVal* h_trnx, const char** String);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_hs_recv_string_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, VlWide<8>/*255:0*/ h_trnx, std::string &String, IData/*31:0*/ &shunt_dpi_hs_recv_string__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_hs_recv_string_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svBitVecVal h_trnx__Vcvt[8];
    for (size_t h_trnx__Vidx = 0; h_trnx__Vidx < 1; ++h_trnx__Vidx) VL_SET_SVBV_W(256, h_trnx__Vcvt + 8 * h_trnx__Vidx, h_trnx);
    const char* String__Vcvt;
    for (size_t String__Vidx = 0; String__Vidx < 1; ++String__Vidx) String__Vcvt = String.c_str();
    int shunt_dpi_hs_recv_string__Vfuncrtn__Vcvt;
    shunt_dpi_hs_recv_string__Vfuncrtn__Vcvt = shunt_dpi_hs_recv_string(sockid__Vcvt, h_trnx__Vcvt, &String__Vcvt);
    String = VL_CVT_N_CSTR(String__Vcvt);
    shunt_dpi_hs_recv_string__Vfuncrtn = shunt_dpi_hs_recv_string__Vfuncrtn__Vcvt;
}

extern "C" long long shunt_dpi_gettimeofday_sec();

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_gettimeofday_sec_TOP__shunt_dpi_pkg(QData/*63:0*/ &shunt_dpi_gettimeofday_sec__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_gettimeofday_sec_TOP__shunt_dpi_pkg\n"); );
    // Body
    long long shunt_dpi_gettimeofday_sec__Vfuncrtn__Vcvt;
    shunt_dpi_gettimeofday_sec__Vfuncrtn__Vcvt = shunt_dpi_gettimeofday_sec();
    shunt_dpi_gettimeofday_sec__Vfuncrtn = shunt_dpi_gettimeofday_sec__Vfuncrtn__Vcvt;
}

extern "C" long long shunt_dpi_gettimeofday_usec();

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_gettimeofday_usec_TOP__shunt_dpi_pkg(QData/*63:0*/ &shunt_dpi_gettimeofday_usec__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_gettimeofday_usec_TOP__shunt_dpi_pkg\n"); );
    // Body
    long long shunt_dpi_gettimeofday_usec__Vfuncrtn__Vcvt;
    shunt_dpi_gettimeofday_usec__Vfuncrtn__Vcvt = shunt_dpi_gettimeofday_usec();
    shunt_dpi_gettimeofday_usec__Vfuncrtn = shunt_dpi_gettimeofday_usec__Vfuncrtn__Vcvt;
}

extern "C" void shunt_dpi_tlm_send_command(int socket, int Com);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_send_command_TOP__shunt_dpi_pkg(IData/*31:0*/ socket, IData/*31:0*/ Com) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_send_command_TOP__shunt_dpi_pkg\n"); );
    // Body
    int socket__Vcvt;
    for (size_t socket__Vidx = 0; socket__Vidx < 1; ++socket__Vidx) socket__Vcvt = socket;
    int Com__Vcvt;
    for (size_t Com__Vidx = 0; Com__Vidx < 1; ++Com__Vidx) Com__Vcvt = Com;
    shunt_dpi_tlm_send_command(socket__Vcvt, Com__Vcvt);
}

extern "C" long long shunt_dpi_tlm_header_id();

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_header_id_TOP__shunt_dpi_pkg(QData/*63:0*/ &shunt_dpi_tlm_header_id__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_header_id_TOP__shunt_dpi_pkg\n"); );
    // Body
    long long shunt_dpi_tlm_header_id__Vfuncrtn__Vcvt;
    shunt_dpi_tlm_header_id__Vfuncrtn__Vcvt = shunt_dpi_tlm_header_id();
    shunt_dpi_tlm_header_id__Vfuncrtn = shunt_dpi_tlm_header_id__Vfuncrtn__Vcvt;
}

extern "C" long long shunt_dpi_tlm_data_id();

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_data_id_TOP__shunt_dpi_pkg(QData/*63:0*/ &shunt_dpi_tlm_data_id__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_data_id_TOP__shunt_dpi_pkg\n"); );
    // Body
    long long shunt_dpi_tlm_data_id__Vfuncrtn__Vcvt;
    shunt_dpi_tlm_data_id__Vfuncrtn__Vcvt = shunt_dpi_tlm_data_id();
    shunt_dpi_tlm_data_id__Vfuncrtn = shunt_dpi_tlm_data_id__Vfuncrtn__Vcvt;
}

extern "C" long long shunt_dpi_tlm_axi3_ext_id();

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_axi3_ext_id_TOP__shunt_dpi_pkg(QData/*63:0*/ &shunt_dpi_tlm_axi3_ext_id__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_axi3_ext_id_TOP__shunt_dpi_pkg\n"); );
    // Body
    long long shunt_dpi_tlm_axi3_ext_id__Vfuncrtn__Vcvt;
    shunt_dpi_tlm_axi3_ext_id__Vfuncrtn__Vcvt = shunt_dpi_tlm_axi3_ext_id();
    shunt_dpi_tlm_axi3_ext_id__Vfuncrtn = shunt_dpi_tlm_axi3_ext_id__Vfuncrtn__Vcvt;
}

extern "C" long long shunt_dpi_tlm_signal_id();

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_signal_id_TOP__shunt_dpi_pkg(QData/*63:0*/ &shunt_dpi_tlm_signal_id__Vfuncrtn) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_signal_id_TOP__shunt_dpi_pkg\n"); );
    // Body
    long long shunt_dpi_tlm_signal_id__Vfuncrtn__Vcvt;
    shunt_dpi_tlm_signal_id__Vfuncrtn__Vcvt = shunt_dpi_tlm_signal_id();
    shunt_dpi_tlm_signal_id__Vfuncrtn = shunt_dpi_tlm_signal_id__Vfuncrtn__Vcvt;
}

extern "C" void shunt_dpi_tlm_recv_gp_header(int sockid, svBitVecVal* h);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_recv_gp_header_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, VlWide<24>/*767:0*/ &h) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_recv_gp_header_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svBitVecVal h__Vcvt[24];
    for (size_t h__Vidx = 0; h__Vidx < 1; ++h__Vidx) VL_SET_SVBV_W(768, h__Vcvt + 24 * h__Vidx, h);
    shunt_dpi_tlm_recv_gp_header(sockid__Vcvt, h__Vcvt);
    VL_SET_W_SVBV(768,h,h__Vcvt + 0);
}

extern "C" void shunt_dpi_tlm_send_gp_header(int sockid, svBitVecVal* h);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_send_gp_header_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, VlWide<24>/*767:0*/ &h) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_send_gp_header_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svBitVecVal h__Vcvt[24];
    for (size_t h__Vidx = 0; h__Vidx < 1; ++h__Vidx) VL_SET_SVBV_W(768, h__Vcvt + 24 * h__Vidx, h);
    shunt_dpi_tlm_send_gp_header(sockid__Vcvt, h__Vcvt);
    VL_SET_W_SVBV(768,h,h__Vcvt + 0);
}

extern "C" void shunt_dpi_tlm_recv_axi3_header(int sockid, svBitVecVal* h);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_recv_axi3_header_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, VlWide<18>/*575:0*/ &h) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_recv_axi3_header_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svBitVecVal h__Vcvt[18];
    for (size_t h__Vidx = 0; h__Vidx < 1; ++h__Vidx) VL_SET_SVBV_W(576, h__Vcvt + 18 * h__Vidx, h);
    shunt_dpi_tlm_recv_axi3_header(sockid__Vcvt, h__Vcvt);
    VL_SET_W_SVBV(576,h,h__Vcvt + 0);
}

extern "C" void shunt_dpi_tlm_send_axi3_header(int sockid, svBitVecVal* h);

VL_INLINE_OPT void Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_send_axi3_header_TOP__shunt_dpi_pkg(IData/*31:0*/ sockid, VlWide<18>/*575:0*/ &h) {
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vcs_common_shunt_dpi_pkg____Vdpiimwrap_shunt_dpi_tlm_send_axi3_header_TOP__shunt_dpi_pkg\n"); );
    // Body
    int sockid__Vcvt;
    for (size_t sockid__Vidx = 0; sockid__Vidx < 1; ++sockid__Vidx) sockid__Vcvt = sockid;
    svBitVecVal h__Vcvt[18];
    for (size_t h__Vidx = 0; h__Vidx < 1; ++h__Vidx) VL_SET_SVBV_W(576, h__Vcvt + 18 * h__Vidx, h);
    shunt_dpi_tlm_send_axi3_header(sockid__Vcvt, h__Vcvt);
    VL_SET_W_SVBV(576,h,h__Vcvt + 0);
}

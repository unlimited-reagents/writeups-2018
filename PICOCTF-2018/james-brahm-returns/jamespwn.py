from __future__ import print_function
from pwn import *

vuln = process(['nc', '2018shell2.picoctf.com', '15608'])
#vuln = remote('2018shell2.picoctf.com', 15608)
while "006" not in vuln.readline():
    pass
for i in range(3):
    vuln.readline()

bashLen = 32
block = 7
initBegin = ''
initEnd = 'a'*(14+bashLen)
answer = ''

for i in range(0, bashLen):
    while True:
        try:
            print(".", end='')
            vuln.sendline("e")
            vuln.sendline(initBegin)
            vuln.sendline(initEnd)
            encStr = vuln.recvline().split(" ")[-1].rstrip()
            sendStr = encStr[:-32]+encStr[block*32:block*32+32]
            for j in range(3):
                vuln.readline()
            vuln.sendline("s")
            vuln.sendline(sendStr)
            status = vuln.readline().strip()
            for j in range(3):
                vuln.readline()
            if "Successful decryption" in status:
                lastChar = chr(int(encStr[-34:-32], 16)^16^int(encStr[block*32-2:block*32], 16))
                print(lastChar)
                answer = lastChar+answer
                break
        except EOFError:
            vuln = process(['nc', '2018shell2.picoctf.com', '15608'])
            while "006" not in vuln.readline():
                pass
            for i in range(3):
                vuln.readline()
    initBegin+='a'
    initEnd = initEnd[:-1]
print(answer)

#!/usr/bin/env python3
import socket as S

addr = "127.1" # server ip
port = 4000 # server port

s = S.socket(S.AF_INET, S.SOCK_DGRAM)

query = [] 

print("1. DNS")
print("2. RDNS")
opt = int(input("Enter Selection: "))

if opt == 1:
    query.append("N:")
else:
    query.append("R:")

value = str(input("Enter the Domain/IP: "))
query.append(value)
s.sendto("".join(query).encode(), (addr, port))
resp, _ = s.recvfrom(1024)

print("Response: {}".format(resp.decode()))

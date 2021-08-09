#!/usr/bin/env python3
import socket as S

addr = "127.1" # server ip
port = 4000 # server port

s = S.socket(S.AF_INET, S.SOCK_DGRAM)

query = input("Enter the Physical Address (MAC): ")
s.sendto(query.encode(), (addr, port))
resp, _ = s.recvfrom(1024)
print("The Logical Address (IP): {}".format(resp.decode()))

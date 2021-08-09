#!/usr/bin/env python3
import sys
import socket as S

host = "127.1" # Standard loopback (localhost)
port = 4000 # should be the same one given in server.py


with S.socket(S.AF_INET, S.SOCK_STREAM) as s:
    s.connect((host, port))
    msg = None
    reply = None
    try:
        msg = input("Enter the Logical Address(IP): ")
        msg.strip()
    except:
        sys.exit(0)
    s.sendall(msg.encode())
    reply = s.recv(1024)
    reply = reply.decode()
    if len(reply) < 1:
        sys.exit(0)
    print("The Physical Address: {}".format(reply))

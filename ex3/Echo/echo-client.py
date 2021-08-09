#!/usr/bin/env python3
import sys
import socket as S

host = "127.1" # Standard loopback (localhost)
port = 4000 # should be the same one given in echo-server.py

with S.socket(S.AF_INET, S.SOCK_STREAM) as s:
    s.connect((host, port))

    while True:
        msg = None
        reply = None
        try:
            msg = input("Client: ")
            msg.strip()
        except:
            sys.exit(0)
        s.sendall(msg.encode())
        s.settimeout(2)
        try:
            reply = str(s.recv(1024).decode())
        except:
            sys.exit(0)
        s.settimeout(None)
        print("Server: {}".format(reply))

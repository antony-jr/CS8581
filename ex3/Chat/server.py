#!/usr/bin/env python3
import sys
import socket as S

HOST = '127.1'  # Standard loopback interface address (localhost)
PORT = 4000   # Port to listen on (non-privileged ports are > 1023)

with S.socket(S.AF_INET, S.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Client: {}".format(str(data.decode())))
            msg = input("Server: ")
            conn.sendall(msg.encode())

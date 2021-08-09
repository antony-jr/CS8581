#!/usr/bin/env python3
import sys
import socket as S

HOST = '127.1'  # Standard loopback interface address (localhost)
PORT = 4001   # Port to listen on (non-privileged ports are > 1023)

def get_data(f):
    try:
     with open(f, "rb") as fp:
        return fp.read()
    except:
        print("File Not Found, Sending Bad Response.")
        return "File not found".encode()

with S.socket(S.AF_INET, S.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for client to request file.... ")
    conn, addr = s.accept()
    
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Client at {}  requested {}... Sending File."
                  .format(addr, data.decode()))
            conn.sendall(get_data(data.decode()))
            print("File Sent Successfully!")

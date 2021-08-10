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

with S.socket(S.AF_INET, S.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("Waiting for client to request file.... ")
   
    while True:
     msg, faddr = s.recvfrom(1024)
     msg = msg.decode()
     print("Client at {}  requested {}... Sending File."
             .format(faddr, msg))
    
     s.sendto(get_data(msg), faddr)

     print("File Sent Successfully!")

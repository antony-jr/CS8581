#!/usr/bin/env python3
import sys
import socket as S

host = "127.1" # Standard loopback (localhost)
port = 4001 # should be the same one given in server.py


with S.socket(S.AF_INET, S.SOCK_STREAM) as s:
    s.connect((host, port))

    file = input("Enter File To Request: ")
    s.sendall(file.encode())
    s.settimeout(2)
    chunks = []
    while True:
        try:
         data = s.recv(1024)
         chunks.append(data)
        except:
         with open("{}.out".format(file), "wb") as fp:        
          for chunk in chunks:
              fp.write(chunk)
         print("File Saved to '{}.out'.".format(file))
         sys.exit(0)
        

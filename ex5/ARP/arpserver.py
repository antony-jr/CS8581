#!/usr/bin/env python3
import socket as S

# IP to Physical Address db
db = {
 "192.168.1.1": "6A:08:AA:C2",
 "192.168.1.2": "8A:D8:BA:A2"
}

HOST = "127.1"  # Standard loopback interface address (localhost)
PORT = 4000   # Port to listen on (non-privileged ports are > 1023)

with S.socket(S.AF_INET, S.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Simulating ARP Server at {}:{}".format(HOST, PORT))
    while True:
     conn, addr = s.accept()
     with conn:
        print("Connection from {}... ".format(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode().lower()
            print(data)
            reply = "Device Not Found"
            if data in db:
                reply = db[data]
            conn.sendall(reply.encode())

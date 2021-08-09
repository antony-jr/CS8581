import socket as S

# Physical Address to IP db
db = {
 "6A:08:AA:C2": "192.168.1.1",
 "8A:D8:BA:A2": "192.168.1.2"
}

addr = "127.1"
port = 4000

s = S.socket(S.AF_INET, S.SOCK_DGRAM)
s.bind((addr, port))

print("Simulating RARP Server at {}:{}".format(addr, port))

while True:
  msg, faddr = s.recvfrom(1024)
  msg = msg.decode().upper()
  reply = "Device not found"
  print("Requested {} IP... ".format(msg))
  if msg in db:
      reply = db[msg]
  print(reply)
  s.sendto(reply.encode(), faddr)

import socket as S

# DNS Records
dns_records = {
   "example.com": "93.184.216.34",
   "google.com": "142.250.193.174",
   "kernel.org": "198.145.29.83",
   "github.com": "13.234.210.38"
}

addr = "127.1"
port = 4000

s = S.socket(S.AF_INET, S.SOCK_DGRAM)
s.bind((addr, port))

print("Simulating DNS Server at {}:{}".format(addr, port))

while True:
  msg, faddr = s.recvfrom(1024)
  msg = msg.decode().lower()
  reply = "Host Not Found"
  print("Requested {} host... ".format(msg))
  if msg in dns_records:
      reply = dns_records[msg]
  print(reply)
  s.sendto(reply.encode(), faddr)

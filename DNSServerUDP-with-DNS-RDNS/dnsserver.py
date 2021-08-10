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

def get_value(data):
  d = data.split(':')
  if len(d) == 2:
      return d[1]
  else:
      return ""

s = S.socket(S.AF_INET, S.SOCK_DGRAM)
s.bind((addr, port))

print("Simulating DNS Server at {}:{}".format(addr, port))

while True:
  msg, faddr = s.recvfrom(1024)
  msg = msg.decode().lower()
  reply = "Not Found"
  if len(msg) > 3 and msg[1] == ':':
      if msg[0] == 'n':
        domain = get_value(msg)
        print("Requested IP address of {}... ".format(domain))
        if domain in dns_records:
            reply = dns_records[domain]
      elif msg[0] == 'r':
        ip = get_value(msg)
        print("Requested Domain of {}... ".format(ip))
        for i in dns_records:
            if dns_records[i] == ip:
                reply = i
                break;
  print(reply)
  s.sendto(reply.encode(), faddr)

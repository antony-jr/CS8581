#!/usr/bin/env python3 
import socket as S

# You can use example.com without any written permissions
# in educational text
target_host = "www.example.com" 
target_port = 80 # 80 => HTTP

def mold_http_message(host):
    return bytes("GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(host), encoding='utf-8')

with S.socket(S.AF_INET, S.SOCK_STREAM) as fp:
    fp.connect((target_host, target_port))
    
    http_request = mold_http_message(target_host)
    print("[HTTP Request] -- ")
    print(http_request.decode())
    print("--")

    fp.send(mold_http_message(target_host))

    response_raw = []

    fp.settimeout(2)
    while True:
        # Receive 1kib of response data from example.com
        try:
         data = fp.recv(1024)
         response_raw.append(data.decode())
        except:
         break

    fp.settimeout(None)

    response = "".join(response_raw)
    length = len(response)

    parts = response.split('\r\n')
    count = 0

    print("[HTTP Response] Length: {}".format(length))

    print("[HTTP Response HEADER] -- ")
    for i in parts:
        print(i)
        count += 1
        if len(i) == 0:
            break;
    print("--\n\n")

    print("[HTTP Response BODY] (Saved Webpage to out.html) -- ")
    for i in parts[count:]:
        print(i)
    print("--")

    ### This is optional.
    with open("out.html", "w") as outfile:
        for chunk in parts[count:]:
            outfile.write(chunk)

# How to Run

You need to run the server first. Don't close it. 

```
 python3 arpserver.py
```

Now in a new terminal, run client.py

```
 python3 client.py
```

Now type the IP address you want MAC Address in the client.py

The ARP has **192.168.1.1** and **192.168.1.2** record so you can use
it in your examples.

# Output

**arpserver.py**

```
Simulating ARP Server at 127.1:4000
Connection from ('127.0.0.1', 49688)... 
192.168.1.1
```

**client.py**

```
Enter the Logical Address(IP): 192.168.1.1
The Physical Address: 6A:08:AA:C2
```

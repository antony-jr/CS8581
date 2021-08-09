# How to use

Run the rarpserver.py in a terminal.

```
 python3 rarpserver.py
```

Now in a new terminal run the client and enter the mac you want to 
resolve using the simulated RARP using UDP.

```
 python3 client.py
 Enter the Physical Address (MAC): 6A:08:AA:C2
 The Logical Address (IP): 192.168.1.1
```


You can use **6A:08:AA:C2** for example.

# Output

**rarpserver.py**

```
Simulating RARP Server at 127.1:4000
Requested 6A:08:AA:C2 IP... 
192.168.1.1

```


**client.py**

```
Enter the Physical Address (MAC): 6A:08:AA:C2
The Logical Address (IP): 192.168.1.1
```

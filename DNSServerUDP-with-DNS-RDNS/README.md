# How to use

Run the dnsserver.py in a terminal.

```
 python3 dnsserver.py
```

Now in a new terminal run the client and enter the hostname you want to 
resolve using the simulated DNS using UDP.

```
 python3 client.py
 Enter the Hostname: google.com
 IP Address: 
```

# Output

**dnsserver.py**

```
imulating DNS Server at 127.1:4000
Requested google.com host... 
142.250.193.174

```


**client.py**

```
Enter the Hostname: google.com
IP Address: 142.250.193.174
```

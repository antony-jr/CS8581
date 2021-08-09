# Network Commands

### TCPDUMP

**Display Traffic Between 2 Hosts:**

You can install tcpdump in linux with ```apt install tcpdump```.


*You need to use sudo for tcpdump*

```
 tcpdump host 192.168.1.1 and 192.168.1.5
```

Here we see the tcpdump between my router (192.168.1.1) and my computer which sits
at 192.168.1.5



**Display Specified Protocol:**

```
 tcpdump tcp
```

to write to a file

```
 tcpdump -w dump.pcap tcp
```

to read the stored pcap file.

```
 tcpdump -r dump.pcap
```

**Filtering based on source or destination port:**

```
 tcpdump src port http
```

### NETSTAT

Shows all connection that you are currently connected.

```
 netstat
```

### ifconfig (or ipconfig in windows)

ifconfig is deprecated in linux2 so use ```ip addr``` instead.

```
 ifconfig
``` 

```
 ip addr # will run in any modern linux distro.
```

### NSLOOKUP

Nameserver lookup.

```
 nslookup antonyjr.in
```

### TRACEPATH (or traceroute in windows)

```
 tracepath antonyjr.in
```

Shows the path taken to get to google servers.


### PING

```
 ping -c3 antonyjr.in
```

Check if a host is down or up



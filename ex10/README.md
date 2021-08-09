# How to use

```
 python3 crc.py
```

# Output

When you enter **Message to Send** and **Message to Receive** the same then
CRC matches. And you know that the transmission had no bad bits.

**No Change in Data Output**

```
CRC Simulation.
Message to Send (in Binary): 110111011011
Divisor (in Binary): 1011

Output Code: 100
Enter the Message Received (in Binary): 110111011011
Success! CRC matches.
```


**Change in Data Output**

```
CRC Simulation.
Message to Send (in Binary): 110111011011
Divisor (in Binary): 1011

Output Code: 100
Enter the Message Received (in Binary): 110111011010  
Failed! CRC Mismatch!
```

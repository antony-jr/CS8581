# How to Run

You need to run the server first. Don't close it. 

```
 python3 server.py
```

Now in a new terminal, run client.py

```
 python3 client.py
```

Now you need to type the file name you want to download from the server. The server
serves files from it's current directory that is this directory.
So in this directory we have a example file called **file.txt**

Try requesting that. The client saves it's output with **.out** suffix.

### Output

The server will first wait for the first message by the client.

**server.py**

```
Waiting for client to request file.... 
Client at ('127.0.0.1', 48244)  requested file.txt... Sending File.
File Sent Successfully!
```

**client.py**
```
Enter File To Request: file.txt
File Saved to 'file.txt.out'.
```

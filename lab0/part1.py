# Used this resource to help: https://zetcode.com/python/socket/#:~:text=The%20recv()%20method%20receives,returns%20an%20empty%20byte%20string
"""
Bodnar, Jan. “Python Socket Tutorial.” Python Socket Tutorial - Python Network Programming with Sockets, zetcode.com/python/socket/#:~:text=The%20recv()%20method%20receives,returns%20an%20empty%20byte%20string. 
"""
#!/usr/bin/env python

import socket # import socket library

# The request and host defined here

request = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1" 
host = "gaia.cs.umass.edu"

# Print to user

print("Request: " + request)
print("Host:" + host + "\n\n")


# Accessing the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Connecting to host, with port 80
    s.connect((host , 80))

    # Server sends request to user
    s.sendall(b"GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n")

    # collect data using recieve function
    data = s.recv(4096)

    # print the total length of the complete data, as well as the decoded information of that data
    print("[RECV] - length: " + str(len(data)))
    print(data.decode())
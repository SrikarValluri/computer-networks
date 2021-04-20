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

# Variables that will concatenate all the buffers, to print out total info in the end

data_sum = 0
data_string = ""

# Accessing the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Connecting to host, with port 80
    s.connect((host , 80))

    # Server sends request to user
    s.sendall(b"GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n")

    # Loop so that large pools of data can be captured  
    while True:

        # collect data using recieve function
        data = s.recv(4096)

        # if no more data is left, break the loop
        if not data:
            break

        # decode the information while concatenating that information into a variable
        data_string += data.decode()

        # keeping track of the total recv length
        data_sum += len(data)

    # print the total length of the complete data, as well as the decoded information of that data
    print("[RECV] - length: " + str(data_sum))
    print(data_string)
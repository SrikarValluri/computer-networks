# Used this resource to help: https://zetcode.com/python/socket/#:~:text=The%20recv()%20method%20receives,returns%20an%20empty%20byte%20string
"""
Bodnar, Jan. “Python Socket Tutorial.” Python Socket Tutorial - Python Network Programming with Sockets, zetcode.com/python/socket/#:~:text=The%20recv()%20method%20receives,returns%20an%20empty%20byte%20string. 
"""
#!/usr/bin/env python

import socket # import socket library
import time # import time

# data message that is sent as an encoded message   

data = "HTTP/1.1 200 OK\r\n"\
 "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
 "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

# Accessing the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # setting the variables of our localhost and port
    host = '127.0.0.1'
    port = 8080


    # server creation with the host and port
    s.bind((host, port))

    # connection successful message
    print("Connected by " + str((host, port)))
    print(f'socket binded to {port}\n\n')

    # server ready to recieve message  
    s.listen()

   
    while True:
        # server wanting to accepting the message
        con, addr = s.accept()

        # server recieving the message
        data_ = con.recv(1024)
        data__ = data

        # server being sent the decoded data information
        con.send(data__.encode())
        print("Recieved: "+ str(data_) + "\n\n")
        print("Sending>>>>>>>>\n\n")
        print(data__)
        print("<<<<<<<<\n\n")

        break

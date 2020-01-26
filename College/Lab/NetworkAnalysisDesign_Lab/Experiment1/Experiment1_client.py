#  Write a program to transfer the contents of a requested file from server to the client using TCP/IP Sockets
# (using TCP/IP Socket programming).


import socket

LOOPBACK_HOST = '127.0.0.1'  # server address.
PORT = 8080  # port used by server.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((LOOPBACK_HOST, PORT))  # Connect to the server.
    s.sendall(b'data2')  # sending file name as query.
    data = s.recv(1024)

print('Receiving Data From Server...\n', repr(data))

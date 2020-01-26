#  Write a program to transfer the contents of a requested file from server to the client using TCP/IP Sockets
# (using TCP/IP Socket programming).
from pathlib import Path
import socket

LOOPBACK_HOST = '127.0.0.1'  # server address.
PORT = 8080  # port used by server.

with socket.socket(socket.AF_INET) as s:
    s.bind((LOOPBACK_HOST, PORT))
    s.listen()
    conn, client_addr = s.accept()
    # accept() blocks and waits for incoming-connections.
    # new socket object is returned by accept, client_addr is a tuple(host, port) (since IPv4 family).
    # conn is clinet socket object.
    with conn:
        print(' \n Connected by Client :', client_addr)
        # looping over blocking calls
        while True:
            # buffersize : 1024 Bytes ,recv() will read all data.
            data = conn.recv(1024)
            if not data:
                break
            # conn.sendall(data) # echo all the data received.
            source = Path(
                r"C:\Users\Vishal Ramane\Documents\GitHub\treasure-trove\College\Lab\NetworkAnalysisDesign_Lab\Experiment1")

            # need to convert data from bytes to string (must mention decoding format)
            target = source / f"{str(data,'utf-8')}.txt"
            # print(target.read_bytes())
            conn.sendall(target.read_bytes())

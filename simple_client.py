
# Import socket module
import socket            

HOST = '127.0.0.1'
PORT = 7001

with socket.socket() as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(4096)
        msg = (data)
        print(msg)

        break
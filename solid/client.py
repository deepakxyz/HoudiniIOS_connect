import socket            


# HOST = '192.168.1.1'
PORT = 6060

HOST = '127.0.0.1'
# PORT = 7001


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


full_msg = ''
while True:
    msg = s.recv(4096)
    if len(msg) <= 0:
        break

    print(msg)
    # break
# print(msg)


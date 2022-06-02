import time
import random
import socket
import math

# random float
def generate_random(range_start, range_end):
    return (random.uniform(range_start, range_end))


HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

while True:
    conn, address = s.accept()
    print(f"Connection extablished: {address}")
    i = 1
    while True:
        # time.sleep(0.000001)
        # random_num = str(generate_random(0.5,10.5))
        v = str(math.sin(i))
        data = bytes(v, 'utf-8')
        conn.send(data)
        i += 1
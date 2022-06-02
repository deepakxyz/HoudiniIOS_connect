# GENERATE RANDOM NUMBER AND SEND VIA SOCKET
import os
import time
import random 
import socket
joint1 = b'0 Wuda 90.00 134.11 -44.50 22.12 163.78 172.44 -11.00 0.00 -0.00 22.97 -52.02 -41.06 -0.00 -45.06 0.00 161.81 99.33 163.56 -0.00 -42.06 -0.00 175.37 -170.96 -178.46 11.00 -0.00 0.00 26.64 -61.81 -16.72 0.00 -45.06 0.00 7.16 107.37 3.48 -0.00 -42.06 -0.00 179.91 -174.01 171.68 -0.00 15.35 0.00 178.12 178.01 -177.66 0.00 10.39 0.00 178.06 178.00 -176.36 -0.00 10.82 -0.00 170.74 177.50 -175.70 0.00 10.39 -0.00 0.00 0.00 0.00 0.00 11.11 -0.00 0.55 -15.53 7.03 -0.00 8.50 0.00 46.68 -5.68 -2.98 -2.90 5.25 0.00 170.73 178.62 177.09 -16.10 -0.00 0.00 146.04 -150.11 -125.48 -28.00 -0.00 -0.00 103.84 -7.02 7.10 -26.00 -0.00 0.00 29.16 19.70 -30.89 -2.62 0.20 3.28 43.48 -0.00 12.84 -3.87 0.00 0.00 177.00 180.00 -160.74 -2.69 0.00 0.00 0.76 0.00 -0.00 -3.39 0.53 2.08 180.00 -180.00 180.00 -5.49 -0.10 1.05 15.00 -0.00 22.98 -3.81 0.00 0.00 180.00 -180.00 -161.20 -2.16 0.00 0.00 0.00 0.00 13.16 -3.56 0.54 0.80 180.00 -180.00 -180.00 -5.44 -0.09 0.33 0.00 0.00 28.29 -4.15 0.00 0.00 0.00 -0.00 34.10 -2.60 0.00 0.00 180.00 -180.00 -157.29 -3.54 0.57 -0.14 180.00 -180.00 180.00 -4.87 -0.02 -0.50 170.00 -180.00 -152.11 -3.62 0.00 0.00 180.00 180.00 -148.69 -2.51 0.00 0.00 0.00 0.00 20.85 -3.32 0.49 -1.26 180.00 -180.00 180.00 -4.35 -0.02 -1.15 160.00 -180.00 -155.13 -2.90 0.00 0.00 180.00 180.00 -142.70 -1.83 0.00 0.00 180.00 -180.00 -155.16 2.90 5.25 0.00 178.10 177.64 -174.68 16.10 0.00 -0.00 21.91 -26.58 -63.30 28.00 -0.00 0.00 89.73 -173.74 174.21 26.00 0.00 0.00 144.36 168.93 -156.05 2.62 0.20 3.28 136.52 -180.00 167.16 3.87 0.00 0.00 3.00 0.00 -19.26 2.69 0.00 0.00 0.76 0.00 -0.00 3.39 0.53 2.08 0.00 -0.00 0.00 5.49 -0.10 1.05 165.00 -180.00 157.02 3.81 0.00 0.00 0.00 -0.00 -18.80 2.16 0.00 0.00 180.00 180.00 166.84 3.56 0.54 0.80 0.00 -0.00 0.00 5.44 -0.09 0.33 180.00 180.00 151.71 4.15 0.00 0.00 180.00 -180.00 145.90 2.60 0.00 0.00 0.00 -0.00 -22.71 3.54 0.57 -0.14 0.00 -0.00 0.00 4.87 -0.02 -0.50 10.00 -0.00 -27.89 3.62 0.00 0.00 0.00 0.00 -31.31 2.51 0.00 0.00 180.00 180.00 159.15 3.32 0.49 -1.26 0.00 -0.00 0.00 4.35 -0.02 -1.15 20.00 -0.00 -24.87 2.90 0.00 0.00 0.00 0.00 -37.30 1.83 0.00 0.00 0.00 -0.00 -24.84 ||'
joint2 = b'0 Wuda -74.62 83.73 -14.81 93.75 17.88 -6.57 -11.00 0.00 0.00 4.11 -36.63 -4.92 0.00 -45.06 0.00 177.37 122.19 -177.34 -0.00 -42.06 -0.00 173.06 -142.88 -175.31 11.00 -0.00 -0.00 179.47 -136.58 175.99 0.00 -45.06 0.00 42.29 83.11 40.11 0.00 -42.06 0.00 8.93 -10.48 -2.82 0.00 15.35 -0.00 179.35 174.64 -176.21 0.00 10.39 0.00 179.24 174.71 -173.87 0.00 10.82 0.00 175.50 175.56 -172.37 0.00 10.39 0.00 0.00 0.00 0.00 0.00 11.11 0.00 179.29 -139.56 -176.32 0.00 8.50 -0.00 15.98 -15.78 -3.01 -2.90 5.25 -0.00 179.20 -175.40 -179.63 -16.10 0.00 -0.00 166.67 179.52 -115.87 -28.00 0.00 -0.00 56.16 11.40 22.70 -26.00 0.00 -0.00 21.01 39.93 -31.84 -2.62 0.20 3.28 43.48 -0.00 12.84 -3.87 0.00 0.00 177.00 180.00 -160.74 -2.69 0.00 0.00 0.76 0.00 -0.00 -3.39 0.53 2.08 180.00 -180.00 180.00 -5.49 -0.10 1.05 15.00 -0.00 22.98 -3.81 0.00 0.00 180.00 -180.00 -161.20 -2.16 0.00 0.00 0.00 0.00 13.16 -3.56 0.54 0.80 180.00 -180.00 -180.00 -5.44 -0.09 0.33 0.00 0.00 28.29 -4.15 0.00 0.00 0.00 -0.00 34.10 -2.60 0.00 0.00 180.00 -180.00 -157.29 -3.54 0.57 -0.14 180.00 -180.00 180.00 -4.87 -0.02 -0.50 170.00 -180.00 -152.11 -3.62 0.00 0.00 180.00 180.00 -148.69 -2.51 0.00 0.00 0.00 0.00 20.85 -3.32 0.49 -1.26 180.00 -180.00 180.00 -4.35 -0.02 -1.15 160.00 -180.00 -155.13 -2.90 0.00 0.00 180.00 180.00 -142.70 -1.83 0.00 0.00 180.00 -180.00 -155.16 2.90 5.25 0.00 175.75 -170.44 -172.41 16.10 0.00 0.00 3.84 -2.96 -71.99 28.00 0.00 0.00 126.60 171.28 158.79 26.00 -0.00 -0.00 147.35 160.46 -156.63 2.62 0.20 3.28 136.52 -180.00 167.16 3.87 0.00 0.00 3.00 0.00 -19.26 2.69 0.00 0.00 0.76 0.00 -0.00 3.39 0.53 2.08 0.00 -0.00 0.00 5.49 -0.10 1.05 165.00 -180.00 157.02 3.81 0.00 0.00 0.00 -0.00 -18.80 2.16 0.00 0.00 180.00 180.00 166.84 3.56 0.54 0.80 0.00 -0.00 0.00 5.44 -0.09 0.33 180.00 180.00 151.71 4.15 0.00 0.00 180.00 -180.00 145.90 2.60 0.00 0.00 0.00 -0.00 -22.71 3.54 0.57 -0.14 0.00 -0.00 0.00 4.87 -0.02 -0.50 10.00 -0.00 -27.89 3.62 0.00 0.00 0.00 0.00 -31.31 2.51 0.00 0.00 180.00 180.00 159.15 3.32 0.49 -1.26 0.00 -0.00 0.00 4.35 -0.02 -1.15 20.00 -0.00 -24.87 2.90 0.00 0.00 0.00 0.00 -37.30 1.83 0.00 0.00 0.00 -0.00 -24.84 ||'

# generate random code
def generate_random(i, range):
    count = 0
    while count < i:
        n = random.randint(0,range)
        time.sleep(1)
        print(n)
        count +=1




HOST = '127.0.0.1'
PORT = 6060

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

i = 1
start = time.time()
while True:
    conn, address = s.accept()
    print(f"Connection extablished: {address}")
    while True:
        time.sleep(1)
        conn.send(joint2)
        time.sleep(1)
        conn.send(joint1)



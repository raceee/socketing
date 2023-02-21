import socket
import time

fileoutput = "listener_logs_{}.txt".format(time.time())

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

with open(fileoutput,"w") as f:
    print("Listener is listening on UDP_IP: {} \nPORT: {}".format(UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        f.write(data.decode('utf-8'))
        f.write("\n")
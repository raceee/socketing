import socket
buffer_size = 1024
UPDServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UPDServer.bind((socket.gethostname(), 9998))

while True:
    print("UDP Server is up.")
    message, address = UPDServer.recvfrom(buffer_size)
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while True:
    MESSAGE = 0
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    MESSAGE += 1
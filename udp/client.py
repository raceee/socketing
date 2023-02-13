import socket



UDPClient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClient.sendto()
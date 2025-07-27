import socket

# create raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind(("localhost", 0))  # use your IP

s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

while True:
    data, addr = s.recvfrom(65535)
    print(f"Packet received from {addr}: {data[:60]}")

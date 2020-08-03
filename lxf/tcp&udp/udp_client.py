import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'mecheal',b'tracy', b'sarah']:
    s.sendto(data, ('127.0.0.1', 9999))
    print(s.recvfrom(1024))
s.close()

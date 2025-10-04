import socket

target_host = "localhost"
target_port = 90

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"HELLO!",(target_host, target_port))

data, addr = client.recvfrom(4096)

print(data)
print(addr)
client.close()

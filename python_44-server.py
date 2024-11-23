import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 12345

server_socket.bind((HOST, PORT))
server_socket.listen(2)
print(f"TCP Server is listening on {HOST}:{PORT}")

client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

while True:
    data = client_socket.recv(1024)
    if data.decode() == 'exit':
        client_socket.close()
        break

    print(f"Received Data: {data.decode()}")
    client_socket.sendall(b'Hello, Client!')

server_socket.close()
print("TCP Server closed")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = '127.0.0.1'
PORT = 12345

server_socket.bind((HOST, PORT))
print(f"UDP Server is listening on {HOST}:{PORT}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    if data.decode() == 'exit':
        break

    print(f"Received Data: {data.decode()}")
    server_socket.sendto(b'Hello, Client!', client_address)

server_socket.close()
print("UDP Server closed")
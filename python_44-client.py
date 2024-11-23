import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 12345

client_socket.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT}")

while True:
    data = input("Enter Data: ")
    client_socket.sendall(data.encode())

    if data == 'exit':
        break

    response = client_socket.recv(1024)
    print(f"Received Response: {response.decode()}")

client_socket.close()
print("TCP Client closed")


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = '127.0.0.1'
PORT = 12345

print(f"\nUDP Client is sending to {HOST}:{PORT}")

while True:
    data = input("Enter Data: ")
    socket.sendto(data.encode(), (HOST, PORT))

    if data == 'exit':
        break

    response, _ = socket.recvfrom(1024)
    print(f"Received Response: {response.decode()}")

socket.close()
print("UDP Client closed")
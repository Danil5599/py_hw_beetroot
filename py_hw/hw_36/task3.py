import socket
from multiprocessing import Process

def handle_client(client_socket):
    request = client_socket.recv(1024)
    client_socket.send(request)
    client_socket.close()

def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Server listening on port 9999")

    while True:
        client_sock, addr = server.accept()
        print(f"Accepted connection from: {addr[0]}:{addr[1]}")
        client_handler = Process(target=handle_client, args=(client_sock,))
        client_handler.start()

if __name__ == '__main__':
    server()
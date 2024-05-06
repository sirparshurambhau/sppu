import socket

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345  # Use a custom port number
def read_uptime_data():
    with open('uptime_data.tsv', 'r') as file:
        return file.read()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        uptime_data = read_uptime_data()

        client_socket.sendall(uptime_data.encode())

        client_socket.close()


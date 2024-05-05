import socket

# Define the server host and port
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345  # Use a custom port number

# Function to read the uptime data from the file
def read_uptime_data():
    with open('uptime_data.tsv', 'r') as file:
        return file.read()

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        # Accept incoming connections
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Read uptime data from the file
        uptime_data = read_uptime_data()

        # Send the data to the client
        client_socket.sendall(uptime_data.encode())

        # Close the client socket
        client_socket.close()


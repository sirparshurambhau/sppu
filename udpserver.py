import socket

# Define the server host and port
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345  # Use a custom port number

# Function to read the uptime data from the file
def read_uptime_data():
    with open('uptime_data.tsv', 'r') as file:
        return file.read()

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))

    print(f"UDP Server listening on {HOST}:{PORT}")

    while True:
        # Receive data from the client
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received request from {client_address}")

        # Read uptime data from the file
        uptime_data = read_uptime_data()

        # Send the data to the client
        server_socket.sendto(uptime_data.encode(), client_address)


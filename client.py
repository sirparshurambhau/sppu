import socket

# Define the server host and port
SERVER_HOST = '15.206.148.16'  # Replace 'ec2-instance-ip' with your EC2 instance's public IP or DNS
SERVER_PORT = 12345  # Use the same port number as the server

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Receive data from the server
    uptime_data = client_socket.recv(1024).decode()

    # Display the received data
    print("Latest Uptime Data:")
    print(uptime_data)


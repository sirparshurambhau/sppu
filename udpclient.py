import socket

SERVER_HOST = '15.206.148.16'  # Replace 'ec2-instance-ip' with your EC2 instance's public IP or DNS
SERVER_PORT = 12345  # Use the same port number as the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    # Send a request to the server
    client_socket.sendto(b'Requesting Uptime Data', (SERVER_HOST, SERVER_PORT))

    uptime_data, server_address = client_socket.recvfrom(1024)

    print("Latest Uptime Data:")
    print(uptime_data.decode())


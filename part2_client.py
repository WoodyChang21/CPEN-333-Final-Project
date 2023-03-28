import time
from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  # Set timeout to 1 second

for i in range(1, 6):
    message = f"PING {i} - hello world"
    start_time = time.time()
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        modified_message, server_address = clientSocket.recvfrom(2048)
        end_time = time.time()
        rtt = (end_time - start_time) * 1000  # Calculate RTT in milliseconds
        print(f"Received: {modified_message.decode()} with RTT {rtt:.2f} ms")
    except timeout:
        print("Request timed out")

clientSocket.close()
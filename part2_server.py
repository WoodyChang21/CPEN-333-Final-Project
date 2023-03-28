import random
import time
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, client_address = serverSocket.recvfrom(2048)
    random_delay = random.uniform(0.005, 0.05)  # Random delay between 5ms to 50ms
    time.sleep(random_delay)
    
    if random.random() < 0.1:  # Simulate 10% packet loss
        continue

    modified_message = message.decode().replace("hello world", "ditto")
    serverSocket.sendto(modified_message.encode(), client_address)

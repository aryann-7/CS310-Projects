# Import the required libraries
from socket import *

# Address for the server
serverName = '192.168.56.1'

# Server's listening port
serverPort = 12000

# Create the socket object
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Prompt user for a message once
message = input('Input lowercase sentence: ')

# Counter to track replies received
repliesReceived = 0

# Send the same message 100 times
for i in range(1, 101):
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
    
    try:
        clientSocket.settimeout(1)
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(f"Reply {i}: {modifiedMessage.decode('utf-8')}")
        repliesReceived += 1
    except timeout:
        print(f"Message {i}: No reply received (lost)")

print(f"\n--- Summary ---")
print(f"Messages sent: 100")
print(f"Replies received: {repliesReceived}")
print(f"Messages lost: {100 - repliesReceived}")

clientSocket.close()
# Import the required libraries
from socket import *

# Address for the server
serverName = '192.168.56.1'

# Server's listening port
serverPort = 12000

# Create the socket object
clientSocket = socket(AF_INET, SOCK_DGRAM)

## Prompt user for input
# For python 2.x use raw_input() to get user input
#message = raw_input('Input lowercase sentence:')

# For python 3.x use input() to get user input
message = input('Input lowercase sentence:')

## Send the message
# For python 2.x use the following (no need to convert from unicode to byte string):
#clientSocket.sendto(message,(serverName, serverPort))

# For python 3.x use the following
# (explicit conversion from unicode to byte string using .encode() method):
clientSocket.sendto(message.encode(),(serverName, serverPort))

## Receive the reply
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# For python 2.x use the following syntax for displaying strings:
#print (modifiedMessage)

# For python 3.x use the following syntax for displaying strings:
print('Reply from server:', modifiedMessage.decode())

# Close the socket
clientSocket.close() 
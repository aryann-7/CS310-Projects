# Import the required libraries
from socket import *

# Listening port for the server
serverPort = 12000

# Create the server socket object
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the server socket to the port
serverSocket.bind(('', serverPort))


# For python 2.x use the following syntax for displaying strings:
#print ('The server is ready to receive messages')

# For python 3.x use the following syntax for displaying strings:
print('The server is ready to receive messages')


while 1:
        # Accept a connection from a client & retrieve the message sent
        message, clientAddress = serverSocket.recvfrom(2048)
        print ('Received message from client:', clientAddress, message)

        # For python 2.x use the following (no need to convert from byte string to unicode):
        #modifiedMessage = message.upper()

        # For python 3.x use the following
        # (explicit conversion from byte string to unicode using .encode() method):
        modifiedMessage = message.decode().upper()

        ## Send the modified message to the client

        # For python 2.x use the following (no need to convert from unicode to byte string):
        #serverSocket.sendto(modifiedMessage, clientAddress)	

        # For python 3.x use the following
        # (explicit conversion from unicode to byte string using .encode() method):
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
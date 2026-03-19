# Import the required libraries
from socket import *

# Listening port for the server
serverPort = 12000

# Create the server socket object
serverSocket = socket(AF_INET,SOCK_STREAM)

# Bind the server socket to the port
serverSocket.bind(('',serverPort))

# Start listening for new connections
serverSocket.listen(1)


# For python 2.x use the following syntax for displaying strings:
#print ('The server is ready to receive messages')

# For python 3.x use the following syntax for displaying strings:
print('The server is ready to receive messages')


while 1:
        # Accept a connection from a client
        connectionSocket, addr = serverSocket.accept()

## Retrieve the message sent by the client

# For python 2.x use the following (no need to convert from byte string to unicode):
#sentence = connectionSocket.recv(1024)

# For python 3.x use the following
# (explicit conversion from byte string to unicode using .encode() method):
sentence = connectionSocket.decode().recv(1024)
	
#Modify the message
capitalizedSentence = sentence.upper()

## Send the modified message back to the client
# For python 2.x use the following (no need to convert from unicode to byte string):
#connectionSocket.send(capitalizedSentence)

# For python 3.x use the following
# (explicit conversion from unicode to byte string using .encode() method):
connectionSocket.send(capitalizedSentence.encode())

# Close the connection
connectionSocket.close()

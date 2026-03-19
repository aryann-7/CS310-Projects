# Import the required libraries
from socket import *

# Address for the server
serverName = 'localhost'

# Server's listening port
serverPort = 12000

# Create the socket object
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server at the specified port
clientSocket.connect((serverName,serverPort))

## Prompt user for input
# For python 2.x use raw_input() to get user input
sentence = raw_input('Input lowercase sentence:')

# For python 3.x use input() to get user input
#sentence = input('Input lowercase sentence:')

## Send the message

# For python 2.x use the following (no need to convert from unicode to byte string):
clientSocket.send(sentence)

# For python 3.x use the following
# (explicit conversion from unicode to byte string using .encode() method):
#clientSocket.send(sentence.encode())

## Receive the reply

# For python 2.x use the following (no need to convert from byte string to unicode):
modifiedSentence = clientSocket.recv(1024)

# For python 3.x use the following
# (explicit conversion from byte string to unicode using .encode() method):
#modifiedSentence = clientSocket.recv(1024).decode()

# For python 2.x use the following syntax for displaying strings:
print 'From Server:', modifiedSentence

# For python 3.x use the following syntax for displaying strings:
#print('From Server:', modifiedSentence)

# Close the socket
clientSocket.close() 

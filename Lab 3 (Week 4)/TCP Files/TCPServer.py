from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# store chat history
chatHistory = ""

print('The server is ready to receive messages')

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        sentence = connectionSocket.recv(1024).decode()
        if not sentence:
            continue
        
        # add new msg to history
        chatHistory += f"{addr} : {sentence}\n"
        
        # send full history back to client
        connectionSocket.send(chatHistory.encode())
        
    finally:
        connectionSocket.close()
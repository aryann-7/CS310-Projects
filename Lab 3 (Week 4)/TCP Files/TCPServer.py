from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

chatHistory = ""

print('The server is ready to receive messages')

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        sentence = connectionSocket.recv(1024).decode()
        if not sentence:
            continue

        if sentence == '__HISTORY__':
            connectionSocket.send(chatHistory.encode())
        else:
            # add msg to history
            chatHistory += f"{addr} : {sentence}\n"
            connectionSocket.send("OK".encode())

    finally:
        connectionSocket.close()
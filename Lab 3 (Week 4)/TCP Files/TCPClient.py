from socket import *

serverName = '192.168.56.1'
serverPort = 12000

while True:
    sentence = input('Input message: ')

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(sentence.encode())
    clientSocket.shutdown(SHUT_WR)
    
    clientSocket.recv(4096)
    clientSocket.close()

    another = input('Send another message? (yes/no): ')
    if another.lower() == 'no':
        # reconnect to fetch chat history
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))

        clientSocket.send('__HISTORY__'.encode())
        clientSocket.shutdown(SHUT_WR)
        
        chatHistory = clientSocket.recv(4096).decode()
        print('\n Client Chat History')
        print(chatHistory)
        clientSocket.close()
        break
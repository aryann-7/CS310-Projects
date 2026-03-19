from socket import *

serverName = '192.168.56.1'
serverPort = 12000

while True:
    # new connection per msg
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    sentence = input('Input message (or type "quit" to exit): ')
    
    if sentence.lower() == 'quit':
        print("Exiting chat.")
        clientSocket.close()
        break

    clientSocket.send(sentence.encode())

    clientSocket.shutdown(SHUT_WR)
    
    # show chats
    chatHistory = clientSocket.recv(4096).decode()
    print('\nChat History')
    print(chatHistory)
    
    clientSocket.close()
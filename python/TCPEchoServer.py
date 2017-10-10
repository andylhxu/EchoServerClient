from socket import socket, AF_INET, SOCK_STREAM

if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print 'The server is ready to receive'
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        print ("server handled: " + str(addr) + " with message: " + sentence)
        connectionSocket.close()

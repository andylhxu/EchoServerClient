from socket import socket, AF_INET, SOCK_DGRAM

if __name__ == '__main__':
    serverName = '127.0.0.1'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = raw_input('Input lowercase sentence:')
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print modifiedMessage.decode()
    clientSocket.close()

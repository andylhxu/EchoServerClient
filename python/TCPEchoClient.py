from socket import socket, AF_INET, SOCK_STREAM

if __name__ == '__main__':
    serverName = '127.0.0.1'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    sentence = raw_input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print ('From Server:' +  modifiedSentence.decode())
    clientSocket.close()

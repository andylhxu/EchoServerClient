CC=gcc

default: server client

server: TCPEchoServer.c DieWithError.c
	$(CC) TCPEchoServer.c DieWithError.c -o server

client: TCPEchoClient.c DieWithError.c
	$(CC) TCPEchoClient.c DieWithError.c -o client

.PHONY:

clean:
	rm -rf server client

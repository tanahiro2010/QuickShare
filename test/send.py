import socket

port = int(input('PORT : '))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', port))
s.send(b'Hello World')
import socket
import json

class Client:
    def __init__(self, port, host="127.0.0.1"):
        self.port = port
        self.host = host
        pass

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        return

    def send(self, data):
        self.s.send(data)

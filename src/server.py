import json
import socket
import base64

class Server():
    def __init__(self, port):
        self.port = port
        with open(file='./data/config.json', mode='r') as f:
            config = json.load(f)
        self.host = config['host']
        data = {
            'host': self.host,
            'port': self.port,
        }

        return

    def Begin_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1024)
                    data = str(data.decode())
                    print(data)
                    file_info = json.loads(data)
                    print(file_info)
        return
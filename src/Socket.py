import socket
class Socket:
    def __init__(self):
        return
    def receive_full_data(client_socket: socket.socket):
        buffer_size = 1024
        data = b''
        while True:
            part = client_socket.recv(buffer_size)
            data += part
            if data.endswith(b'END'):
                break
        return data.decode('utf-8').rstrip('END')
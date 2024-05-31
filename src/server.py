import json
import socket
import base64
from src.colors import TerminalColor as TC
import time

def log(txt):
    print('{}INFO{} {}: {}'.format(TC.INFO_BLUE, TC._END, time.time_ns(), txt))

class Server():
    def __init__(self, port):
        self.port = port
        with open(file='./data/config.json', mode='r') as f:
            config = json.load(f)
        self.host = config['host']

        needToken_input = input('Do you need a token? (y/n) $ ').lower().replace('\n', '')

        if needToken_input == "y" or needToken_input == "yes":
            data_obj = {
                'host': self.host,
                'port': self.port,
            }
            data_str = json.dumps(data_obj)
            token = base64.b64encode(data_str.encode()).decode()
            print('Token : {}'.format(token))
        elif needToken_input == "n" or needToken_input == "no":
            pass
        else:
            print('Please enter either "y" or "n"')


        return

    def Begin_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1024)
                    data = data.decode('utf-8')
                    log('Send file from {}'.format(addr))

                    file_info = json.loads(data)

                    keys: list = file_info.keys()
                    info_length = len(file_info)
                    # info = {'file': 'filename', 'description': '.txt?', 'byte': 'file-byte'}
                    if info_length == 3:
                        if 'file' in keys and 'description' in keys and 'byte' in keys:
                            file_name = file_info['file']
                            file_type = file_info['description']
                            file_byte = bytes(base64.b64decode(file_info['byte'].encode()))
                            log('File INFO====\nTitle: {}\nType: {}\n'.format(file_name, file_type))
                            isSave = input('Do you save (y/n) $ ').lower()
                            if isSave == "y" or isSave == "yes":
                                log('Try saving file...')
                                with open('./' + file_name, mode='wb') as f:
                                    f.write(file_byte)
                                    f.close()
                                    pass
                                log('File saved!')

                            pass

                    print('keys : {}'.format(keys))
        return
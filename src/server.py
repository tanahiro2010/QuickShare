import json
import socket
import base64
from src.colors import TerminalColor as TC
from src.Socket import Socket as sk
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
                    data: bytes = sk.receive_full_data(conn)
                    # base64.b64encode(json.dumps(data_obj).encode('utf-8'))
                    data_byte: bytes = base64.b64decode(data)
                    data_str: str = data_byte.decode()
                    log('Send file from {}'.format(addr))

                    file_info = json.loads(data_str)
                    print(file_info)

                    keys: list = file_info.keys()
                    info_length = len(file_info)
                    # info = {'file': 'filename', 'description': '.txt?', 'byte': 'file-byte'}
                    if info_length == 3:
                        if 'file' in keys and 'description' in keys and 'byte' in keys:
                            file_name = file_info['file']
                            file_type = file_info['description']
                            file_byte = bytes(base64.b64decode(file_info['byte'].encode()))
                            log('File INFO => Title: {} && Type: {}'.format(file_name, file_type))
                            isSave = input('Do you save (y/n) $ ').lower()
                            if isSave == "y" or isSave == "yes":
                                log('Try saving file...')
                                with open('./' + file_name, mode='wb') as f:
                                    f.write(file_byte)
                                    f.close()
                                    pass
                                log('File saved!')

                            pass

                        else:
                            print('[{}WARNING!!{}] We might be under a DOS attack!!'.format(TC.WARN, TC._END))
                            pass
                    else:
                        print('[{}WARNING!!{}] We might be under a DOS attack!!'.format(TC.WARN, TC._END))
                        pass

                    isContinue = input('Do you want to continue? (y/n) $ ')
                    if isContinue == "y" or isContinue == "yes":
                        pass
                    else:
                        exit()
        return
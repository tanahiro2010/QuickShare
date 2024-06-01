import base64
import json
import os.path
from tkinter import *
from sys import argv
from src.server import Server
from src.client import Client
from src.colors import TerminalColor as TC
import time

def log(txt):
    print('{}INFO{} {}: {}'.format(TC.INFO_GREEN, TC._END, time.time_ns(), txt))

def main():
    # Promotion
    ## Get Promotion text
    with open(file='./data/Promotion', mode='r') as file:
        Promotion = file.read()
    print(Promotion)

    argv_len = len(argv)
    if argv_len == 1:
        mode = input('Mode $')
    else:
        mode = argv[1]
    mode = mode.lower()
    print('Mode: {}'.format(mode))
    if mode == 'server':
        if argv_len == 1:
            port = int(input('PORT $ '))
        else:
            port = int(argv[2])
        soft_client = Server(port=port)
        print('Server IP_Address: {}\nPORT: {}'.format(soft_client.host, soft_client.port))
        soft_client.Begin_server()
        return

    elif mode == "send_file":
        host = "127.0.0.1"
        if argv_len == 1:
            port = int(input('PORT $ '))
        else:
            port = int(argv[2])
            if argv_len == 3:
                host = argv[3]

        file_path = input('Send File Path: ')
        if os.path.isfile(file_path):
            log('{} File is Exists.'.format(file_path))
            log('Making client method...')
            soft_client = Client(port=port, host=host)
            log('Done...')
            log('Try connecting to server...')
            try:
                soft_client.connect()
            except Exception as e:
                print('Error connecting to server: {}'.format(e))
                return

            log('Done...')
            log('Preparing to send file...')
            with open(file_path, 'rb') as file:
                file_byte = file.read()
            # info = {'file': 'filename', 'description': '.txt?', 'byte': 'file-byte'}
            file_name = os.path.basename(file_path)
            file_type = file_name.split('.')[-1]
            data_obj = {
                "file": file_name,
                "description": file_type,
                "byte": base64.b64encode(file_byte).decode('utf-8'),
            }
            data: bytes = base64.b64encode(json.dumps(data_obj).encode('utf-8')) + b"END"
            soft_client.send(data=data)


        pass
    elif mode == "help":
        print()

    return

if __name__ == '__main__':
    main()
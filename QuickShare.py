import json
from sys import argv
from src.server import Server
from src.client import Client

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

        soft_client = Client(port=port, host=host)
        soft_client.connect()
        soft_client.send(data=bytes("{'Title': 'Test'}", 'utf-8'))

    return

if __name__ == '__main__':
    main()
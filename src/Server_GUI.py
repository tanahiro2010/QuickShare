import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from src.Socket import Socket as sk

import socket
import json
import base64
import time
import os


class ServerGUI:
    def __init__(self, host, port):
        print("ServerGUI is initialized")
        self.host = host
        self.port = port
        self.root = tk.Tk()
        self.root.geometry('750x500')
        self.root.title('QuickShare - Server Controller')
        self.root.resizable(False, False)

        self.Title_label = tk.Label(self.root, text='QuickShare - Server Controller', font=('Cascadia Mono', 24))
        self.FileName = tk.Label(self.root, text='File Name: ', font=('Helvetica', 20))
        self.FileType = tk.Label(self.root, text='File Type: ', font=('Helvetica', 20))
        self.SaveButton = tk.Button(self.root, text='Save', font=('Helvetica', 20), command=lambda: self.Save())

        self.root.destroy()
        return

    def Begin_Server(self, controll_root, host: str, port: int):
        controll_root.destroy()
        print('Begin_Server')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Socket:
            root = tk.Tk()
            root.geometry('750x500')
            root.title('QuickShare - Server Controller')
            root.resizable(False, False)
            print('Host: {}\nPort: {}'.format(host, port))
            Socket.bind((host, port))
            Socket.listen()
            print('Begin Server')
            while True:
                conn, addr = Socket.accept()
                with conn:
                    data = sk.receive_full_data(conn)
                    data_bytes: bytes = base64.b64decode(data)
                    data_str: str = data_bytes.decode()
                    self.file_info = json.loads(data_str)
                    file_name = self.file_info['file']
                    file_type = self.file_info['description']

                    self.Title_label.grid(row=0, column=0)
                    self.FileName.grid(row=1, column=0)
                    self.FileType.grid(row=2, column=0)

                    self.FileName.config(text=f'FileName : {file_name}')
                    self.FileType.config(text=f'FileType: {file_type}')
                    self.FileName.update()
                    self.FileType.update()

                    self.root.mainloop()

    def Save(self):
        file_title = self.file_info['file']
        file_bytes: bytes = bytes(base64.b64decode(self.file_info['byte'].encode()))

        folder_path = filedialog.askdirectory()
        file_path = os.path.join(folder_path, file_title)

        with open(file=file_path, mode='wb') as f:
            f.write(file_bytes)
            f.close()
            pass

        messagebox.showinfo('Save', 'File Saved Successfully!')
        return
    def display(self):
        self.FileName.config(text=f'FileName :')
        self.FileType.config(text=f'File Type:')
        self.FileType.pack()
        self.FileName.pack()

        self.root.mainloop()
        return

    def test_gui(self):
        root = tk.Tk()
        root.geometry('750x500')
        root.title('QuickShare - Server Controller')
        root.resizable(False, False)
        tk.Label(root, text='Control PANEL', font=('Cascadia Mono', 20)).pack()
        tk.Label(root, text='HOST', font=('Cascadia Mono', 20)).pack()
        host_input = (tk.Entry(root, font=('Helvetica', 20), justify='center', validate='all'))
        host_input.pack()
        tk.Label(root, text='PORT', font=('Helvetica', 20)).pack()
        port_input = (tk.Entry(root, font=('Cascadia Mono', 20), justify='center'))
        port_input.pack()

        enter_button = tk.Button(root, text="Boot server", justify='center', font=('Helvetica', 20), command=lambda: self.Begin_Server(root, host_input.get(), int(port_input.get()))).pack()


        root.mainloop()

        return



serverGUI = ServerGUI('localhost', 5050)
serverGUI.test_gui()
#serverGUI.Save()
#serverGUI.display()
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

        self.Title_label.grid(row=0, column=0)
        self.FileName.grid(row=1, column=0)
        self.FileType.grid(row=2, column=0)
        return

    def Begin_Server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Socket:
            Socket.bind((self.host, self.port))
            Socket.listen()

            while True:
                conn, addr = Socket.accept()
                with conn:
                    data = sk.receive_full_data(conn)
                    data_bytes: bytes = base64.b64decode(data)
                    data_str: str = data_bytes.decode()
                    self.file_info = json.loads(data_str)
                    file_name = self.file_info['file']
                    file_type = self.file_info['description']
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
        self.FileName.update()
        self.FileType.update()

        self.root.mainloop()


"""serverGUI = ServerGUI('localhost', 5000)
serverGUI.Save()
serverGUI.display()"""
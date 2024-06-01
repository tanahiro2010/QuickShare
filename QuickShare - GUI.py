# Tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import filedialog
# MyPrograms
from src.client import Client
from src.Server_GUI import ServerGUI as Server
from src.Socket import Socket
from src.GUI import *
# Other
import socket
import base64
import os.path

def main():
    # Window design
    root = tk.Tk()
    root.title('QuickShare')
    root.geometry('600x400')
    root.resizable(False, False)

    # Application
    App = Application(root)

    # Objects
    Title = tk.Label(root, text='QuickShare', font=('Cascadia Mono', 24))
    BeginServer_button = tk.Button(root, text='Begin Server', command=lambda: ServerSettings(root))
    fileSelectButton = tk.Button(root, text='Select File', command=lambda: App.fileSelect())


    print(fileSelectButton)


    # Move Objects


    # Pack
    Title.pack()
    fileSelectButton.pack()
    BeginServer_button.pack()

    # mainLoop
    root.mainloop()
    return

if __name__ == '__main__':
    main()
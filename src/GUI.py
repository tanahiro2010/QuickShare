import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import filedialog

class ServerSettings:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x400')
        self.root.title('QuickShare - Server Settings')
        self.root.resizable(False, False)

        # Create Objects
        self.Port_label = tk.Label(self.root, text='Port : ', font=('Helvetica 16 bold', 30))
        self.Port_entry = tk.Entry(self.root, font=('Helvetica 16 bold', 25))
        self.Hostname = tk.Label(self.root, text='Hostname : ', font=('Helvetica 16 bold', 30))
        self.Hostname_entry = tk.Entry(self.root, font=('Helvetica 16 bold', 25))
        Config_Enter = tk.Button(self.root, text="Config Enter")

        # Objects Place
        Port_label.place(x=0, y=0)
        Port_entry.place(x=200, y=10, width=300, height=30)
        Hostname.place(x=0, y=55, width=200, height=30)
        Hostname_entry.place(x=200, y=55, width=300, height=30)
        Config_Enter.place(x=300, y=60, width=300, height=30, command=lambda: EnterConfig())
        return

    def EnterConfig(self):


class Application():
    def __init__(self, root):
        self.root = root
        return

    def fileSelect(self):
        self.send_target_file = filedialog.askopenfilename()
        return

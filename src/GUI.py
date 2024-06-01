# Tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import filedialog

# MyPrograms
from src.Server_GUI import ServerGUI as Server
from src.client import Client
from src.Socket import Socket

class ServerSettings:
    def __init__(self, root):
        root.destroy()
        self.root = tk.Tk()
        self.root.geometry('600x400')
        self.root.title('QuickShare - Server Settings')
        self.root.resizable(False, False)

        # Create Objects
        self.Port_label = tk.Label(self.root, text='Port : ', font=('Helvetica 16 bold', 30))
        self.Hostname_entry = tk.Entry(self.root, font=('Helvetica 16 bold', 25))
        self.Hostname = tk.Label(self.root, text='Hostname : ', font=('Helvetica 16 bold', 30))
        self.Port_entry = tk.Entry(self.root, font=('Helvetica 16 bold', 25))
        self.Config_Enter = tk.Button(self.root, text="Config Enter and Begin Server.", command=lambda: self.EnterConfig())

        # Objects Place
        self.Port_label.place(x=0, y=0)
        self.Port_entry.place(x=200, y=10, width=300, height=30)
        self.Hostname.place(x=0, y=55, width=200, height=30)
        self.Hostname_entry.place(x=200, y=55, width=300, height=30)
        self.Config_Enter.place(x=150, y=100, width=300, height=30)

        self.root.mainloop()
        return

    def EnterConfig(self):
        self.hostname = str(self.Hostname_entry.get())
        self.port: int = int(self.Port_entry.get())

        if (self.port < 0 and self.port > 65535):
            messagebox.showwarning('Warning', 'Port must be between 0 and 65535')
            return

        messagebox.showinfo('Config Entered', 'HostName: {}\nPort: {}'.format(self.hostname, self.port))
        self.root.destroy()
        messagebox.showinfo('Begin Server.', 'Server Started.')
        Server_obj = Server(port=self.port, host=self.hostname)
        Server_obj.Begin_Server()

        return


class Application():
    def __init__(self, root):
        self.root = root
        return

    def fileSelect(self):
        self.send_target_file = filedialog.askopenfilename()
        return

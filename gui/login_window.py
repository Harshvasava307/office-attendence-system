import tkinter as tk
from tkinter import messagebox
from core.admin_core import AdminCore
from gui.admin_panel import AdminPanel

class AdminLoginWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)

        self.admin_core = AdminCore()

        self.window.geometry("300x300")
        self.window.resizable(False, False)

        self.window.title("Admin Login")

        tk.Label(self.window, text="Username").pack()
        self.user = tk.Entry(self.window)
        self.user.pack()

        tk.Label(self.window, text="Password").pack()
        self.pwd = tk.Entry(self.window, show="*")
        self.pwd.pack()

        tk.Button(self.window, text="Login", command=self.validate).pack(pady=10)

    def validate(self):
        u = self.user.get()
        p = self.pwd.get()

        if self.admin_core.validate(u, p):
            AdminPanel(self.window)
        else:
            messagebox.showerror("Error", "Invalid admin credentials")

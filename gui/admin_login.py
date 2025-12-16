import tkinter as tk
from tkinter import messagebox
from gui.admin_panel import AdminPanel


class AdminLogin(tk.Frame):
    def __init__(self, parent, switch_callback, back_callback):
        super().__init__(parent, bg="#2A2A3D")
        self.switch_callback = switch_callback
        self.back_callback = back_callback

        self.pack(fill=tk.BOTH, expand=True)

        # ---------- UI ----------
        tk.Label(
            self,
            text="Admin Login",
            font=("Helvetica", 20, "bold"),
            bg="#2A2A3D",
            fg="#FF7B02"
        ).pack(pady=30)

        tk.Label(
            self,
            text="Admin ID",
            font=("Arial", 14),
            bg="#2A2A3D",
            fg="white"
        ).pack(pady=5)

        self.id_entry = tk.Entry(self, font=("Arial", 14), width=25)
        self.id_entry.pack(pady=5)

        tk.Label(
            self,
            text="Password",
            font=("Arial", 14),
            bg="#2A2A3D",
            fg="white"
        ).pack(pady=5)

        self.pass_entry = tk.Entry(self, font=("Arial", 14), width=25, show="*")
        self.pass_entry.pack(pady=5)

        tk.Button(
            self,
            text="Login",
            font=("Arial", 14),
            bg="#FF7B02",
            fg="white",
            bd=0,
            width=20,
            pady=10,
            command=self.login
        ).pack(pady=20)

        tk.Button(
            self,
            text="← Back",
            font=("Arial", 12),
            bg="#444",
            fg="white",
            bd=0,
            width=15,
            command=self.back_callback
        ).pack(pady=10)

    # ---------- LOGIN LOGIC ----------
    def login(self):
        admin_id = self.id_entry.get().strip()
        password = self.pass_entry.get().strip()

        if admin_id == "admin" and password == "admin@123":
            self.switch_callback(AdminPanel)
        else:
            messagebox.showerror("Login Failed", "Invalid Admin ID or Password")

import tkinter as tk
from tkinter import messagebox


class AdminLogin(tk.Frame):
    def __init__(self, parent, on_success, on_back):
        super().__init__(parent, bg="#2A2A3D")
        self.on_success = on_success
        self.on_back = on_back

        self.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            self,
            text="Admin Login",
            font=("Helvetica", 20, "bold"),
            bg="#2A2A3D",
            fg="#FF7B02"
        ).pack(pady=30)

        tk.Label(self, text="Admin ID", fg="white", bg="#2A2A3D").pack()
        self.id_entry = tk.Entry(self, font=("Arial", 14))
        self.id_entry.pack(pady=5)

        tk.Label(self, text="Password", fg="white", bg="#2A2A3D").pack()
        self.pass_entry = tk.Entry(self, font=("Arial", 14), show="*")
        self.pass_entry.pack(pady=5)

        tk.Button(
            self,
            text="Login",
            font=("Arial", 14),
            bg="#FF7B02",
            fg="white",
            bd=0,
            width=20,
            command=self.login
        ).pack(pady=20)

        tk.Button(
            self,
            text="← Back",
            command=self.on_back,
            bg="#444",
            fg="white",
            bd=0,
            width=15
        ).pack()

    def login(self):
        if self.id_entry.get() == "admin" and self.pass_entry.get() == "admin@123":
            self.on_success()
        else:
            messagebox.showerror("Error", "Invalid Admin Credentials")

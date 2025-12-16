import tkinter as tk
from tkinter import messagebox
from gui.admin_panel import AdminPanel
from gui.ui_theme import *


class AdminLogin(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg=PRIMARY_BG)
        self.pack(fill=tk.BOTH, expand=True)
        self.back_callback = back_callback

        # ---------- CARD ----------
        card = tk.Frame(
            self,
            bg=CARD_BG,
            highlightbackground=BORDER,
            highlightthickness=1
        )
        card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=340)

        # ---------- TITLE ----------
        tk.Label(
            card,
            text="Admin Login",
            font=FONT_TITLE,
            bg=CARD_BG,
            fg=TEXT_PRIMARY
        ).pack(pady=20)

        # ---------- INPUTS ----------
        self.user = self.entry(card, "Username")
        self.pwd = self.entry(card, "Password", show="*")

        # ---------- LOGIN ----------
        tk.Button(
            card,
            text="Login",
            command=self.login,
            bg=SECONDARY,
            fg="white",
            font=FONT_BUTTON,
            activebackground=ACCENT_HOVER,
            bd=0,
            pady=10
        ).pack(pady=20, fill=tk.X, padx=40)

        # ---------- BACK ----------
        tk.Button(
            card,
            text="← Back",
            command=self.back_callback,
            bg=CARD_BG,
            fg=TEXT_MUTED,
            font=FONT_SMALL,
            bd=0
        ).pack()

    # ---------- ENTRY ----------
    def entry(self, parent, label, show=None):
        tk.Label(
            parent,
            text=label,
            bg=CARD_BG,
            fg=TEXT_MUTED,
            font=FONT_SMALL
        ).pack(anchor="w", padx=40)

        e = tk.Entry(parent, font=FONT_NORMAL, show=show)
        e.pack(fill=tk.X, padx=40, pady=6)
        return e

    # ---------- LOGIN LOGIC ----------
    def login(self):
        if self.user.get() == "admin" and self.pwd.get() == "admin@123":
            self.destroy()
            AdminPanel(self.master)
        else:
            messagebox.showerror("Access Denied", "Invalid credentials")

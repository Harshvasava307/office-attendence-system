import tkinter as tk
from PIL import Image, ImageTk
from gui.add_employee_window import AddEmployeeGUI
from gui.employee_attendance_window import EmployeeAttendanceWindow
from gui.admin_login import AdminLogin
from gui.ui_theme import *


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Astra Infotech – Attendance System")
        self.root.geometry("1000x650")
        self.root.configure(bg=PRIMARY_BG)

        self.container = tk.Frame(root, bg=PRIMARY_BG)
        self.container.pack(fill=tk.BOTH, expand=True)

        self.show_home()

    def clear(self):
        for w in self.container.winfo_children():
            w.destroy()

    def show_home(self):
        self.clear()

        # ---------- LOGO ----------
        logo_img = Image.open("logo/logo.png").resize((90, 90))
        self.logo = ImageTk.PhotoImage(logo_img)
        tk.Label(self.container, image=self.logo, bg=PRIMARY_BG).pack(pady=10)

        # ---------- BRAND ----------
        tk.Label(
            self.container,
            text="Astra Infotech",
            font=FONT_TITLE,
            bg=PRIMARY_BG,
            fg=TEXT_PRIMARY
        ).pack()

        tk.Label(
            self.container,
            text="Smart Face Attendance System",
            font=FONT_SUBTITLE,
            bg=PRIMARY_BG,
            fg=TEXT_MUTED
        ).pack(pady=5)

        # ---------- BUTTONS ----------
        self.action_button("Add Employee", lambda: AddEmployeeGUI(self.root))
        self.action_button("Mark Attendance", lambda: EmployeeAttendanceWindow(self.root))
        self.action_button("Admin Panel", self.open_admin)

        # ---------- COPYRIGHT ----------
        tk.Label(
            self.container,
            text="© 2025 Astra Infotech. All rights reserved.",
            font=("Inter", 9),
            bg=PRIMARY_BG,
            fg=TEXT_MUTED
        ).pack(side=tk.BOTTOM, pady=10)


    def action_button(self, text, command):
        tk.Button(
            self.container,
            text=text,
            command=command,
            font=FONT_BUTTON,
            bg=SECONDARY,
            fg="white",
            activebackground="#5B56C8",
            bd=0,
            width=26,
            pady=12,
            cursor="hand2"
        ).pack(pady=12)

    def open_admin(self):
        self.clear()
        AdminLogin(self.container, self.show_home)

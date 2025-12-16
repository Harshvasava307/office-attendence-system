import tkinter as tk
from gui.add_employee_window import AddEmployeeGUI
from gui.employee_attendance_window import EmployeeAttendanceWindow
from gui.admin_login import AdminLogin
from gui.admin_panel import AdminPanel


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Office Attendance System")
        self.root.geometry("900x600")
        self.root.configure(bg="#1E1E2F")

        self.container = tk.Frame(self.root, bg="#1E1E2F")
        self.container.pack(fill=tk.BOTH, expand=True)

        self.show_home()

    # ---------- SCREEN HANDLER ----------
    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def switch_screen(self, screen_class):
        self.clear_screen()
        screen_class(self.container, inline=True)

    def go_home(self):
        self.show_home()

    # ---------- HOME ----------
    def show_home(self):
        self.clear_screen()

        tk.Label(
            self.container,
            text="Office Attendance System",
            font=("Helvetica", 22, "bold"),
            bg="#1E1E2F",
            fg="#FF7B02"
        ).pack(pady=30)

        btn_style = {
            "font": ("Arial", 14),
            "bg": "#FF7B02",
            "fg": "white",
            "bd": 0,
            "width": 25,
            "pady": 10
        }

        tk.Button(
            self.container,
            text="Add Employee",
            command=lambda: self.switch_screen(AddEmployeeGUI),
            **btn_style
        ).pack(pady=10)

        tk.Button(
            self.container,
            text="Mark Attendance",
            command=lambda: EmployeeAttendanceWindow(self.root),
            **btn_style
        ).pack(pady=10)

        tk.Button(
            self.container,
            text="Admin",
            command=self.open_admin_login,
            **btn_style
        ).pack(pady=10)

    # ---------- ADMIN ----------
    def open_admin_login(self):
        self.clear_screen()
        AdminLogin(
            self.container,
            self.switch_screen,
            self.go_home
        )

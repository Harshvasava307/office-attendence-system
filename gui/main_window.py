import tkinter as tk
from gui.login_window import AdminLoginWindow
from gui.admin_panel import AdminPanel
from gui.employee_attendance_window import EmployeeAttendanceWindow

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Office Attendance System")
        self.root.geometry("300x300")

        tk.Label(self.root, text="Attendance System", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Login", width=20, command=self.login).pack(pady=10)
        tk.Button(self.root, text="Logout", width=20, command=self.logout).pack(pady=10)
        tk.Button(self.root, text="Admin", width=20, command=self.open_admin).pack(pady=10)

    def login(self):
        EmployeeAttendanceWindow(self.root)

    def logout(self):
        print("Logout pressed")

    def open_admin(self):
        AdminLoginWindow(self.root)

    def run(self):
        self.root.mainloop()

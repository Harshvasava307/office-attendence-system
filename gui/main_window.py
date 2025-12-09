import tkinter as tk
from gui.add_employee_window import AddEmployeeGUI
from gui.employee_attendance_window import EmployeeAttendanceWindow
from gui.admin_panel import AdminPanel

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Office Attendance System")
        self.root.geometry("400x300")

        tk.Button(root, text="Add Employee", font=("Arial", 14),
                  width=25, command=self.open_add).pack(pady=20)

        tk.Button(root, text="Mark Attendance", font=("Arial", 14),
                  width=25, command=self.open_attendance).pack(pady=20)

        tk.Button(root, text="Admin", font=("Arial", 14),
                  width=25, command=self.open_admin_pannel).pack(pady=20)

    def open_add(self):
        AddEmployeeGUI(self.root)

    def open_attendance(self):
        EmployeeAttendanceWindow(self.root)

    def open_admin_pannel(self):
        AdminPanel(self.root)

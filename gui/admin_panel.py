import tkinter as tk
from gui.add_employee_gui import AddEmployeeGUI
from gui.remove_employee_gui import RemoveEmployeeGUI
from gui.attendance_sheet_gui import AttendanceSheetGUI

class AdminPanel:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Admin Panel")

        tk.Button(self.window, text="Attendance Sheet", width=25,
                  command=self.open_sheet).pack(pady=10)

        tk.Button(self.window, text="Add Employee", width=25,
                  command=self.add_employee).pack(pady=10)

        tk.Button(self.window, text="Remove Employee", width=25,
                  command=self.remove_employee).pack(pady=10)

    def open_sheet(self):
        AttendanceSheetGUI(self.window)

    def add_employee(self):
        AddEmployeeGUI(self.window)

    def remove_employee(self):
        RemoveEmployeeGUI(self.window)

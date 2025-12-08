import tkinter as tk
from core.employee_core import EmployeeCore

class RemoveEmployeeGUI:
    def __init__(self, parent):
        self.employee_core = EmployeeCore()

        self.window = tk.Toplevel(parent)
        self.window.title("Remove Employee")

        tk.Label(self.window, text="Enter Employee Name").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        tk.Button(self.window, text="Remove", command=self.remove).pack(pady=10)

    def remove(self):
        name = self.name_entry.get()
        self.employee_core.remove_employee(name)
        print("Employee removed")

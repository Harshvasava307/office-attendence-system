import tkinter as tk
import cv2
from core.employee_core import EmployeeCore

class AddEmployeeGUI:
    def __init__(self, parent):
        self.employee_core = EmployeeCore()

        self.window = tk.Toplevel(parent)
        self.window.title("Add Employee")

        tk.Label(self.window, text="Enter Employee Name").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        tk.Button(self.window, text="Capture Face", command=self.capture).pack(pady=10)

    def capture(self):
        name = self.name_entry.get()
        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()
        cap.release()

        if ret:
            self.employee_core.add_employee(name, frame)
            print("Employee added successfully")

import tkinter as tk
import csv
from core.attendance_core import AttendanceCore

class AttendanceSheetGUI:
    def __init__(self, parent):
        self.core = AttendanceCore()

        self.window = tk.Toplevel(parent)
        self.window.title("Attendance Sheet")

        file_path = self.core.get_today_file()

        text = tk.Text(self.window, width=50, height=20)
        text.pack()

        try:
            with open(file_path) as f:
                data = f.read()
                text.insert(tk.END, data)
        except:
            text.insert(tk.END, "No attendance marked today yet.")

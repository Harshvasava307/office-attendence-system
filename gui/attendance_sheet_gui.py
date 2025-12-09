import tkinter as tk
import csv
from core.attendance_core import AttendanceCore

class AttendanceSheetGUI:
    def __init__(self, parent):
        self.core = AttendanceCore()

        self.window = tk.Toplevel(parent)
        self.window.title("Monthly Attendance Sheet")

        # Monthly attendance file
        file_path = "attendance.csv"

        text = tk.Text(self.window, width=80, height=25, font=("Arial", 12))
        text.pack(padx=10, pady=10)

        try:
            with open(file_path, newline='') as f:
                reader = csv.reader(f)
                headers = next(reader)  # Read header row
                text.insert(tk.END, "\t".join(headers) + "\n")
                text.insert(tk.END, "-"*80 + "\n")

                for row in reader:
                    line = "\t".join(row)
                    text.insert(tk.END, line + "\n")
        except FileNotFoundError:
            text.insert(tk.END, "No attendance recorded yet.")

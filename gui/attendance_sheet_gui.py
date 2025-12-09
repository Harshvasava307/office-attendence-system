import tkinter as tk
from tkinter import scrolledtext
import csv

class AttendanceSheetGUI(tk.Frame):
    def __init__(self, parent, inline=False):
        super().__init__(parent, bg="#2A2A3D")
        self.inline = inline

        if not inline:
            self.window = tk.Toplevel(parent)
            self.window.title("Monthly Attendance Sheet")
            self.window.geometry("900x600")
            self.window.resizable(False, False)
            self.container = self.window
        else:
            self.container = self
            self.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        header = tk.Label(self.container, text="Monthly Attendance Sheet",
                          font=("Helvetica", 18, "bold"),
                          bg="#2A2A3D", fg="#FF7B02")
        header.pack(pady=15)

        # Scrollable Text Widget
        self.text_area = scrolledtext.ScrolledText(self.container,
                                                   width=100, height=25,
                                                   font=("Arial", 12),
                                                   bg="#1C1C2E", fg="white",
                                                   insertbackground="white")
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.text_area.configure(state='disabled')

        self.load_attendance()

        if not inline:
            self.window.protocol("WM_DELETE_WINDOW", self.close_window)

    def load_attendance(self):
        self.text_area.configure(state='normal')
        self.text_area.delete(1.0, tk.END)

        file_path = "attendance.csv"  # Monthly attendance file

        try:
            with open(file_path, newline='') as f:
                reader = csv.reader(f)
                headers = next(reader)
                self.text_area.insert(tk.END, "\t".join(headers) + "\n")
                self.text_area.insert(tk.END, "-"*100 + "\n")
                for row in reader:
                    line = "\t".join(row)
                    self.text_area.insert(tk.END, line + "\n")
        except FileNotFoundError:
            self.text_area.insert(tk.END, "No attendance recorded yet.")

        self.text_area.configure(state='disabled')

    def close_window(self):
        self.destroy()
        if not self.inline:
            self.window.destroy()

import tkinter as tk
from gui.add_employee_window import AddEmployeeGUI
from gui.remove_employee_gui import RemoveEmployeeGUI
from gui.attendance_sheet_gui import AttendanceSheetGUI

class AdminPanel(tk.Frame):
    def __init__(self, parent, inline=False):
        super().__init__(parent, bg="#2A2A3D")
        self.inline = inline

        if not inline:
            # Backward compatibility with Toplevel window
            self.window = tk.Toplevel(parent)
            self.window.title("Admin Panel")
            self.window.geometry("400x400")
            self.window.resizable(False, False)
            self.container = self.window
        else:
            self.container = self
            self.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        header = tk.Label(self.container, text="Admin Panel",
                          font=("Helvetica", 18, "bold"),
                          bg="#2A2A3D", fg="#FF7B02")
        header.pack(pady=15)

        btn_style = {"font": ("Arial", 14), "bg": "#FF7B02", "fg": "white",
                     "activebackground": "#FF9E4B", "width": 25, "bd": 0, "pady": 10}

        tk.Button(self.container, text="Attendance Sheet", command=self.open_sheet, **btn_style).pack(pady=10)
        tk.Button(self.container, text="Add Employee", command=self.add_employee, **btn_style).pack(pady=10)
        tk.Button(self.container, text="Remove Employee", command=self.remove_employee, **btn_style).pack(pady=10)

        if not inline:
            self.window.protocol("WM_DELETE_WINDOW", self.close_window)

    def open_sheet(self):
        AttendanceSheetGUI(self.container, inline=True)

    def add_employee(self):
        AddEmployeeGUI(self.container, inline=True)

    def remove_employee(self):
        RemoveEmployeeGUI(self.container, inline=True)

    def close_window(self):
        self.destroy()
        if not self.inline:
            self.window.destroy()

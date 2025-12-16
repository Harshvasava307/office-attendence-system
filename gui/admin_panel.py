import tkinter as tk
from gui.add_employee_window import AddEmployeeGUI
from gui.remove_employee_gui import RemoveEmployeeGUI
from gui.attendance_sheet_gui import AttendanceSheetGUI


class AdminPanel(tk.Frame):
    def __init__(self, parent, inline=False):
        super().__init__(parent, bg="#2A2A3D")

        self.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            self,
            text="Admin Panel",
            font=("Helvetica", 20, "bold"),
            bg="#2A2A3D",
            fg="#FF7B02"
        ).pack(pady=20)

        btn_style = {
            "font": ("Arial", 14),
            "bg": "#FF7B02",
            "fg": "white",
            "bd": 0,
            "width": 25,
            "pady": 10
        }

        tk.Button(
            self,
            text="Attendance Sheet",
            command=lambda: AttendanceSheetGUI(self),
            **btn_style
        ).pack(pady=10)

        tk.Button(
            self,
            text="Add Employee",
            command=lambda: AddEmployeeGUI(self, inline=True),
            **btn_style
        ).pack(pady=10)

        tk.Button(
            self,
            text="Remove Employee",
            command=lambda: RemoveEmployeeGUI(self),
            **btn_style
        ).pack(pady=10)

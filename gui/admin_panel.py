import tkinter as tk
from gui.add_employee_window import AddEmployeeGUI
from gui.attendance_sheet_gui import AttendanceSheetGUI
from gui.ui_theme import *


class AdminPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=PRIMARY_BG)
        self.pack(fill=tk.BOTH, expand=True)

        tk.Label(self, text="Admin Panel",
                 font=FONT_TITLE, bg=PRIMARY_BG).pack(pady=20)

        self.btn("Attendance Sheet", self.open_sheet)
        self.btn("Add Employee", lambda: AddEmployeeGUI(parent))

    def btn(self, text, cmd):
        tk.Button(
            self,
            text=text,
            command=cmd,
            font=FONT_BUTTON,
            bg=SECONDARY,
            fg="white",
            bd=0,
            pady=12,
            width=25
        ).pack(pady=10)

    def open_sheet(self):
        AttendanceSheetGUI(self)

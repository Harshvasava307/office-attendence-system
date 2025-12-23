import tkinter as tk

from gui.add_employee_window import AddEmployeeGUI
from gui.admin_attendance_dashboard import AdminAttendanceDashboard
from gui.ui_theme import *


class AdminPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=PRIMARY_BG)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)

        # ===============================
        # TITLE
        # ===============================
        tk.Label(
            self,
            text="Admin Panel",
            font=FONT_TITLE,
            bg=PRIMARY_BG,
            fg=TEXT_PRIMARY
        ).pack(pady=30)

        # ===============================
        # BUTTONS
        # ===============================
        self._create_button("Attendance Sheet", self.open_attendance_dashboard)
        self._create_button("Add Employee", self.open_add_employee)

    # ===============================
    # BUTTON FACTORY
    # ===============================
    def _create_button(self, text, command):
        tk.Button(
            self,
            text=text,
            command=command,
            font=FONT_BUTTON,
            bg=SECONDARY,
            fg="white",
            bd=0,
            pady=12,
            width=25,
            activebackground=SECONDARY
        ).pack(pady=12)

    # ===============================
    # ACTIONS
    # ===============================
    def open_attendance_dashboard(self):
        """
        Opens the new Admin Attendance Dashboard
        """
        AdminAttendanceDashboard(self.parent)

    def open_add_employee(self):
        """
        Opens Add Employee Window
        """
        AddEmployeeGUI(self.parent)

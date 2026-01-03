import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import datetime
import os
import sys
import subprocess

from gui.ui_theme import *
from gui.attendance_service import (
    get_all_employees,
    get_employee_attendance,
    ATTENDANCE_FILE
)
from gui.employee_list_panel import EmployeeListPanel


class AdminAttendanceDashboard(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Admin Attendance Dashboard")
        self.geometry("1200x700")
        self.configure(bg=PRIMARY_BG)

        self.selected_employee = None  # Show all by default

        self._create_top_cards()
        self._create_main_layout()

    # -------------------- Top Cards --------------------
    def _create_top_cards(self):
        top_frame = tk.Frame(self, bg=PRIMARY_BG)
        top_frame.pack(fill=tk.X, padx=20, pady=15)

        self.total_emp_card = self._create_card(top_frame, "Total Employees", "0")
        self.present_card = self._create_card(top_frame, "Present", "0")
        self.absent_card = self._create_card(top_frame, "Absent", "0")
        self.half_day_card = self._create_card(top_frame, "Half Day", "0")

    def _create_card(self, parent, title, value):
        card = tk.Frame(parent, bg=CARD_BG, width=220, height=100, bd=1, relief="ridge")
        card.pack(side=tk.LEFT, padx=15)
        card.pack_propagate(False)

        tk.Label(
            card,
            text=title,
            bg=CARD_BG,
            fg=TEXT_SECONDARY,
            font=("Segoe UI", 11)
        ).pack(anchor="w", padx=15, pady=(15, 0))

        value_lbl = tk.Label(
            card,
            text=value,
            bg=CARD_BG,
            fg=TEXT_PRIMARY,
            font=("Segoe UI", 22, "bold")
        )
        value_lbl.pack(anchor="w", padx=15, pady=(5, 10))

        return value_lbl

    # -------------------- Main Layout --------------------
    def _create_main_layout(self):
        body = tk.Frame(self, bg=PRIMARY_BG)
        body.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left Panel - Employee List
        self.left_panel = EmployeeListPanel(body, self.on_employee_select)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        # Right Panel
        self.right_panel = tk.Frame(body, bg=CARD_BG, bd=1, relief="ridge")
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self._right_panel_content()

    # -------------------- Right Panel Content --------------------
    def _right_panel_content(self):
        # Header
        top_frame = tk.Frame(self.right_panel, bg=CARD_BG)
        top_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(
            top_frame,
            text="Attendance Dashboard",
            bg=CARD_BG,
            fg=TEXT_PRIMARY,
            font=("Segoe UI", 14, "bold")
        ).pack(side=tk.LEFT)

        tk.Button(
            top_frame,
            text="Open Attendance CSV",
            command=self.open_attendance_file,
            bg=ACCENT,
            fg="white",
            activebackground=ACCENT_HOVER,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            padx=12,
            pady=4
        ).pack(side=tk.RIGHT)

        # Body
        rp_body = tk.Frame(self.right_panel, bg=CARD_BG)
        rp_body.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Calendar
        cal_frame = tk.Frame(rp_body, bg=CARD_BG)
        cal_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        self.calendar = Calendar(cal_frame, selectmode="day")
        self.calendar.pack()
        self.calendar.bind("<<CalendarSelected>>", self.load_attendance)

        # Attendance Table
        table_frame = tk.Frame(rp_body, bg=CARD_BG)
        table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        columns = ("Employee Name", "Status")
        self.att_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=20
        )

        for col in columns:
            self.att_table.heading(col, text=col)
            self.att_table.column(col, width=180, anchor="center")

        self.att_table.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Load initial attendance
        self.load_attendance()

    # -------------------- Load Attendance --------------------
    def load_attendance(self, event=None):
        date_str = self.calendar.get_date()  # mm/dd/yy
        dt = datetime.datetime.strptime(date_str, "%m/%d/%y")
        formatted_date = dt.strftime("%d-%m-%Y")

        # Clear table
        for row in self.att_table.get_children():
            self.att_table.delete(row)

        employees = (
            get_all_employees()
            if not self.selected_employee
            else [self.selected_employee]
        )

        total_present = total_absent = total_half = 0

        for emp in employees:
            emp_records = get_employee_attendance(emp)

            status_for_day = next(
                (r["Status"] for r in emp_records if r["Date"] == formatted_date),
                "Absent"
            )

            self.att_table.insert("", "end", values=(emp, status_for_day))

            if status_for_day == "Present":
                total_present += 1
            elif status_for_day == "Half Day":
                total_half += 1
            else:
                total_absent += 1

        # Update summary cards
        self.total_emp_card.config(text=str(len(employees)))
        self.present_card.config(text=str(total_present))
        self.absent_card.config(text=str(total_absent))
        self.half_day_card.config(text=str(total_half))

    # -------------------- Open Attendance CSV --------------------
    def open_attendance_file(self):
        file_path = ATTENDANCE_FILE

        if not os.path.exists(file_path):
            messagebox.showerror(
                "File Not Found",
                "Attendance file not found.\nNo attendance recorded yet."
            )
            return

        try:
            if sys.platform.startswith("win"):
                os.startfile(file_path)
            elif sys.platform == "darwin":
                subprocess.call(["open", file_path])
            else:
                subprocess.call(["xdg-open", file_path])
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open file:\n{e}")

    # -------------------- Employee Selection --------------------
    def on_employee_select(self, name):
        self.selected_employee = name
        self.load_attendance()

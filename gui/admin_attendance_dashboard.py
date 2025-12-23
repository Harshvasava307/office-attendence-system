import tkinter as tk
from tkinter import ttk
from gui.ui_theme import *

class AdminAttendanceDashboard(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Admin Attendance Dashboard")
        self.geometry("1200x700")
        self.configure(bg=PRIMARY_BG)

        self._create_top_cards()
        self._create_main_layout()

    # ===============================
    # TOP SUMMARY CARDS
    # ===============================
    def _create_top_cards(self):
        top_frame = tk.Frame(self, bg=PRIMARY_BG)
        top_frame.pack(fill=tk.X, padx=20, pady=10)

        self.total_emp_card = self._create_card(top_frame, "Total Employees", "0")
        self.present_card = self._create_card(top_frame, "Present", "0")
        self.absent_card = self._create_card(top_frame, "Absent", "0")
        self.half_day_card = self._create_card(top_frame, "Half Day", "0")

    def _create_card(self, parent, title, value):
        card = tk.Frame(parent, bg=CARD_BG, width=200, height=80)
        card.pack(side=tk.LEFT, padx=10)
        card.pack_propagate(False)

        tk.Label(
            card, text=title,
            bg=CARD_BG, fg=TEXT_SECONDARY,
            font=("Segoe UI", 10)
        ).pack(anchor="w", padx=10, pady=(10, 0))

        value_lbl = tk.Label(
            card, text=value,
            bg=CARD_BG, fg=TEXT_PRIMARY,
            font=("Segoe UI", 18, "bold")
        )
        value_lbl.pack(anchor="w", padx=10)

        return value_lbl

    # ===============================
    # MAIN BODY
    # ===============================
    def _create_main_layout(self):
        body = tk.Frame(self, bg=PRIMARY_BG)
        body.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left panel (employee list)
        self.left_panel = tk.Frame(body, bg=CARD_BG, width=300)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)
        self.left_panel.pack_propagate(False)

        # Right panel (attendance details)
        self.right_panel = tk.Frame(body, bg=CARD_BG)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self._placeholder_left()
        self._placeholder_right()

    # ===============================
    # PLACEHOLDERS
    # ===============================
    def _placeholder_left(self):
        tk.Label(
            self.left_panel,
            text="Employee List\n(Coming Next)",
            bg=CARD_BG,
            fg=TEXT_SECONDARY,
            font=("Segoe UI", 12)
        ).pack(expand=True)

    def _placeholder_right(self):
        tk.Label(
            self.right_panel,
            text="Attendance Sheet & Calendar\n(Coming Next)",
            bg=CARD_BG,
            fg=TEXT_SECONDARY,
            font=("Segoe UI", 12)
        ).pack(expand=True)

import tkinter as tk
from tkinter import scrolledtext
import csv
from gui.ui_theme import *


class AttendanceSheetGUI(tk.Frame):
    def __init__(self, parent, inline=False):
        super().__init__(parent, bg=PRIMARY_BG)
        self.inline = inline

        # ---------- CONTAINER ----------
        if not inline:
            self.window = tk.Toplevel(parent)
            self.window.title("Astra Infotech – Monthly Attendance")
            self.window.geometry("1000x650")
            self.window.configure(bg=PRIMARY_BG)
            self.window.resizable(False, False)
            self.container = self.window
        else:
            self.container = self
            self.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        # ---------- HEADER ----------
        header_frame = tk.Frame(self.container, bg=PRIMARY_BG)
        header_frame.pack(fill=tk.X, pady=(0, 15))

        tk.Label(
            header_frame,
            text="Monthly Attendance Sheet",
            font=FONT_TITLE,
            bg=PRIMARY_BG,
            fg=TEXT_PRIMARY
        ).pack(anchor="w")

        tk.Label(
            header_frame,
            text="Astra Infotech",
            font=FONT_SUBTITLE,
            bg=PRIMARY_BG,
            fg=TEXT_MUTED
        ).pack(anchor="w")

        # ---------- CARD ----------
        card = tk.Frame(
            self.container,
            bg=CARD_BG,
            highlightbackground=BORDER,
            highlightthickness=1
        )
        card.pack(fill=tk.BOTH, expand=True)

        # ---------- SCROLLABLE TEXT ----------
        self.text_area = scrolledtext.ScrolledText(
            card,
            font=("Consolas", 11),
            bg="white",
            fg=TEXT_PRIMARY,
            insertbackground=TEXT_PRIMARY,
            padx=10,
            pady=10
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.configure(state="disabled")

        self.load_attendance()

        if not inline:
            self.window.protocol("WM_DELETE_WINDOW", self.close_window)

    # ---------- LOAD CSV ----------
    def load_attendance(self):
        self.text_area.configure(state="normal")
        self.text_area.delete(1.0, tk.END)

        file_path = "attendance.csv"

        try:
            with open(file_path, newline="") as f:
                reader = csv.reader(f)
                headers = next(reader)

                self.text_area.insert(
                    tk.END,
                    " | ".join(headers) + "\n"
                )
                self.text_area.insert(
                    tk.END,
                    "-" * 120 + "\n"
                )

                for row in reader:
                    self.text_area.insert(
                        tk.END,
                        " | ".join(row) + "\n"
                    )

        except FileNotFoundError:
            self.text_area.insert(
                tk.END,
                "No attendance recorded yet."
            )

        self.text_area.configure(state="disabled")

    # ---------- CLOSE ----------
    def close_window(self):
        self.destroy()
        if not self.inline:
            self.window.destroy()

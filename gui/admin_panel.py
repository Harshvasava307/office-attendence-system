import tkinter as tk


class AdminPanel(tk.Frame):
    def __init__(self, parent, switch_screen, go_home):
        super().__init__(parent, bg="#2A2A3D")
        self.switch_screen = switch_screen
        self.go_home = go_home

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
            text="Add Employee",
            command=lambda: self.switch_screen("add_employee"),
            **btn_style
        ).pack(pady=10)

        tk.Button(
            self,
            text="Attendance Sheet",
            command=lambda: self.switch_screen("attendance_sheet"),
            **btn_style
        ).pack(pady=10)

        tk.Button(
            self,
            text="← Logout",
            command=self.go_home,
            **btn_style
        ).pack(pady=30)

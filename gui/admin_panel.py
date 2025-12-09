import tkinter as tk
from gui.add_employee_window import AddEmployeeGUI
from gui.remove_employee_gui import RemoveEmployeeGUI
from gui.attendance_sheet_gui import AttendanceSheetGUI

class AdminPanel(tk.Frame):
    def __init__(self, parent, inline=False):
        super().__init__(parent, bg="#2A2A3D")
        self.inline = inline

        if not inline:
            self.window = tk.Toplevel(parent)
            self.window.title("Admin Panel")
            self.window.geometry("800x500")
            self.window.resizable(False, False)
            self.container = self.window
        else:
            self.container = self
            self.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header
        header = tk.Label(self.container, text="Admin Panel",
                          font=("Helvetica", 18, "bold"),
                          bg="#2A2A3D", fg="#FF7B02")
        header.pack(pady=15)

        # Main layout frames
        self.sidebar = tk.Frame(self.container, bg="#1C1C2E", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.content = tk.Frame(self.container, bg="#2A2A3D")
        self.content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Buttons
        btn_style = {"font": ("Arial", 14), "bg": "#FF7B02", "fg": "white",
                     "activebackground": "#FF9E4B", "width": 18, "bd": 0, "pady": 10}

        tk.Button(self.sidebar, text="Attendance Sheet", command=self.open_sheet, **btn_style).pack(pady=10)

        if not inline:
            self.window.protocol("WM_DELETE_WINDOW", self.close_window)

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def open_sheet(self):
        self.clear_content()
        AttendanceSheetGUI(self.content, inline=True)

    def add_employee(self):
        self.clear_content()
        AddEmployeeGUI(self.content, inline=True)

    def remove_employee(self):
        self.clear_content()
        RemoveEmployeeGUI(self.content, inline=True)

    def close_window(self):
        self.destroy()
        if not self.inline:
            self.window.destroy()

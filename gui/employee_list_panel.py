import tkinter as tk
from gui.ui_theme import *
from gui.attendance_service import get_all_employees


class EmployeeListPanel(tk.Frame):
    def __init__(self, parent, select_callback):
        super().__init__(parent, bg=CARD_BG, bd=1, relief="ridge")
        self.select_callback = select_callback

        self.pack_propagate(False)
        self.config(width=250)

        tk.Label(
            self,
            text="Employees",
            bg=CARD_BG,
            fg=TEXT_PRIMARY,
            font=("Segoe UI", 12, "bold")
        ).pack(pady=10)

        self.listbox = tk.Listbox(
            self,
            font=("Segoe UI", 10),
            selectbackground=ACCENT
        )
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        self.refresh_list()   # Load employees initially

    # ✅ NEW METHOD (This fixes your error)
    def refresh_list(self):
        self.listbox.delete(0, tk.END)

        employees = get_all_employees()
        for emp in employees:
            self.listbox.insert(tk.END, emp)

    def _on_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            selected_name = self.listbox.get(selection[0])
            self.select_callback(selected_name)
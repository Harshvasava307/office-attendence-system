import tkinter as tk
from gui.ui_theme import *
from gui.attendance_service import get_all_employees


class EmployeeListPanel(tk.Frame):
    def __init__(self, parent, on_employee_select):
        super().__init__(parent, bg="white")

        self.on_employee_select = on_employee_select
        self.employees = get_all_employees()

        self._build_ui()
        self._load_employees(self.employees)

    # ===============================
    # UI
    # ===============================
    def _build_ui(self):
        # Title
        tk.Label(
            self,
            text="Employees",
            bg="white",
            fg="black",
            font=FONT_SUBTITLE
        ).pack(anchor="w", padx=12, pady=(12, 6))

        # Search box
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(
            self,
            textvariable=self.search_var,
            font=FONT_NORMAL,
            bg="white",
            fg="black",
            relief="solid"
        )
        search_entry.pack(fill=tk.X, padx=12, pady=(0, 10))
        search_entry.bind("<KeyRelease>", self._filter)

        # List container
        list_frame = tk.Frame(self, bg="white")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        # Listbox
        self.listbox = tk.Listbox(
            list_frame,
            font=FONT_NORMAL,
            bg="white",
            fg="black",
            selectbackground=SECONDARY,
            selectforeground="white",
            bd=1,
            activestyle="none"
        )

        scrollbar = tk.Scrollbar(list_frame, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.bind("<<ListboxSelect>>", self._on_select)

    # ===============================
    # DATA
    # ===============================
    def _load_employees(self, employees):
        self.listbox.delete(0, tk.END)
        for emp in employees:
            self.listbox.insert(tk.END, emp)

    def _filter(self, event=None):
        query = self.search_var.get().lower()
        filtered = [emp for emp in self.employees if query in emp.lower()]
        self._load_employees(filtered)

    def _on_select(self, event):
        if not self.listbox.curselection():
            return
        index = self.listbox.curselection()[0]
        name = self.listbox.get(index)
        self.on_employee_select(name)

import tkinter as tk
from tkinter import messagebox
import os
import shutil

from gui.ui_theme import *

# Adjust if your dataset path is different
DATASET_DIR = "dataset"
ATTENDANCE_FILE = os.path.join("data", "attendance.csv")


class DeleteEmployeeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Delete Employee")
        self.geometry("400x400")
        self.configure(bg=PRIMARY_BG)
        self.resizable(False, False)

        tk.Label(
            self,
            text="Delete Employee",
            font=FONT_TITLE,
            bg=PRIMARY_BG,
            fg=TEXT_PRIMARY
        ).pack(pady=20)

        self.employee_listbox = tk.Listbox(self, font=("Inter", 12))
        self.employee_listbox.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        self.load_employees()

        tk.Button(
            self,
            text="Delete Selected",
            font=FONT_BUTTON,
            bg="#E53935",
            fg="white",
            bd=0,
            pady=10,
            command=self.delete_employee
        ).pack(pady=20)

    # ===============================
    # Load Employee Names
    # ===============================
    def load_employees(self):
        if not os.path.exists(DATASET_DIR):
            return

        for folder in os.listdir(DATASET_DIR):
            self.employee_listbox.insert(tk.END, folder)

    # ===============================
    # Delete Employee
    # ===============================
    def delete_employee(self):
        selected = self.employee_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an employee")
            return

        employee_name = self.employee_listbox.get(selected[0])

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete {employee_name}?"
        )

        if not confirm:
            return

        # Delete dataset folder
        employee_path = os.path.join(DATASET_DIR, employee_name)
        if os.path.exists(employee_path):
            shutil.rmtree(employee_path)

        # Remove from attendance CSV
        if os.path.exists(ATTENDANCE_FILE):
            import csv
            rows = []
            with open(ATTENDANCE_FILE, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["EmployeeName"] != employee_name:
                        rows.append(row)

            with open(ATTENDANCE_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=["EmployeeName", "Date", "CheckIn", "CheckOut", "Status"]
                )
                writer.writeheader()
                writer.writerows(rows)

        messagebox.showinfo("Success", f"{employee_name} deleted successfully")
        self.destroy()
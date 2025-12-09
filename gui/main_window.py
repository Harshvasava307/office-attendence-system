import tkinter as tk
from tkinter import ttk
from gui.add_employee_window import AddEmployeeGUI
from gui.employee_attendance_window import EmployeeAttendanceWindow
from gui.admin_panel import AdminPanel

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Office Attendance System")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E2F")  # modern dark background

        # Header
        header = tk.Label(root, text="Office Attendance System", font=("Helvetica", 20, "bold"),
                          bg="#1E1E2F", fg="#FF7B02", pady=20)
        header.pack(fill=tk.X)

        # Main frame to switch between pages
        self.main_frame = tk.Frame(root, bg="#2A2A3D")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Sidebar for buttons
        self.sidebar = tk.Frame(self.main_frame, bg="#1E1E2F", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Container for pages
        self.container = tk.Frame(self.main_frame, bg="#2A2A3D")
        self.container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Buttons in sidebar
        btn_style = {"font": ("Arial", 14), "bg": "#FF7B02", "fg": "white",
                     "activebackground": "#FF9E4B", "width": 18, "bd": 0, "pady": 10}

        tk.Button(self.sidebar, text="Add Employee", command=self.show_add_employee, **btn_style).pack(pady=10)
        tk.Button(self.sidebar, text="Mark Attendance", command=self.show_attendance, **btn_style).pack(pady=10)
        tk.Button(self.sidebar, text="Admin Panel", command=self.show_admin_panel, **btn_style).pack(pady=10)

        # Initialize empty current page
        self.current_page = None

    def clear_container(self):
        """Destroy current page in the container."""
        if self.current_page:
            self.current_page.destroy()
            self.current_page = None

    def show_add_employee(self):
        self.clear_container()
        self.current_page = AddEmployeeGUI(self.container, inline=True)

    def show_attendance(self):
        self.clear_container()
        self.current_page = EmployeeAttendanceWindow(self.container, inline=True)

    def show_admin_panel(self):
        self.clear_container()
        self.current_page = AdminPanel(self.container, inline=True)


# To run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

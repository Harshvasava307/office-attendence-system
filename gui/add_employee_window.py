import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from core.employee_core import EmployeeCore

class AddEmployeeGUI(tk.Frame):
    def __init__(self, parent, inline=False):
        super().__init__(parent, bg="#2A2A3D")  # Modern dark frame background
        self.employee_core = EmployeeCore()
        self.inline = inline

        if not inline:
            # For backward compatibility, create a Toplevel window
            self.window = tk.Toplevel(parent)
            self.window.title("Add Employee")
            self.window.geometry("1280x720")
            self.window.resizable(False, False)
            self.container = self.window
        else:
            # Inline mode: attach directly to parent frame
            self.container = self
            self.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # ---------- UI Elements ----------
        header = tk.Label(self.container, text="Add Employee",
                          font=("Helvetica", 18, "bold"),
                          bg="#2A2A3D", fg="#FF7B02")
        header.pack(pady=10)

        tk.Label(self.container, text="Enter Employee Name:",
                 font=("Arial", 14), bg="#2A2A3D", fg="white").pack(pady=5)
        self.name_entry = tk.Entry(self.container, font=("Arial", 14), width=30)
        self.name_entry.pack(pady=5)

        # Camera Frame
        self.camera_frame = tk.Label(self.container, bg="#1E1E2F")
        self.camera_frame.pack(pady=10)

        # Buttons
        btn_style = {"font": ("Arial", 14), "bg": "#FF7B02", "fg": "white",
                     "activebackground": "#FF9E4B", "width": 20, "bd": 0, "pady": 10}
        tk.Button(self.container, text="Start Camera", command=self.start_camera, **btn_style).pack(pady=5)
        tk.Button(self.container, text="Capture Face", command=self.capture, **btn_style).pack(pady=5)

        self.cap = None
        self.running = False

        # Handle window close if Toplevel
        if not inline:
            self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    # ---------- Camera Methods ----------
    def start_camera(self):
        if self.running:
            return

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 680)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        if not self.cap.isOpened():
            messagebox.showerror("Camera Error", "Cannot access camera!")
            return

        self.running = True
        self.show_frame()

    def show_frame(self):
        if not self.running:
            return

        ret, frame = self.cap.read()
        if not ret:
            return

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(rgb))

        self.camera_frame.img = img
        self.camera_frame.configure(image=img)

        self.container.after(10, self.show_frame)

    def capture(self):
        if not self.running:
            messagebox.showwarning("Warning", "Camera not running!")
            return

        ret, frame = self.cap.read()
        if not ret:
            messagebox.showerror("Error", "Cannot read from camera!")
            return

        name = self.name_entry.get().strip()
        if name == "":
            messagebox.showwarning("Input Error", "Employee name cannot be empty!")
            return

        success = self.employee_core.add_employee(name, frame)
        if success:
            messagebox.showinfo("Success", f"Employee '{name}' added successfully!")
        else:
            messagebox.showerror("Error", "No face detected! Try again.")

    def on_close(self):
        self.running = False
        if self.cap and self.cap.isOpened():
            self.cap.release()
        if not self.inline:
            self.window.destroy()
        else:
            self.destroy()

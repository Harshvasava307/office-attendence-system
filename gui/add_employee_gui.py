import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from core.employee_core import EmployeeCore

class AddEmployeeGUI:
    def __init__(self, parent):
        self.employee_core = EmployeeCore()

        self.window = tk.Toplevel(parent)
        self.window.title("Add Employee")
        self.window.geometry("1280x720")
        self.window.resizable(False, False)

        tk.Label(self.window, text="Enter Employee Name").pack(pady=10)
        self.name_entry = tk.Entry(self.window, font=("Arial", 14))
        self.name_entry.pack(pady=5)

        self.camera_frame = tk.Label(self.window)
        self.camera_frame.pack(pady=10)

        tk.Button(self.window, text="Start Camera", width=20, command=self.start_camera).pack(pady=5)
        tk.Button(self.window, text="Capture Face", width=20, command=self.capture).pack(pady=5)

        self.cap = None
        self.running = False

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def start_camera(self):
        if self.running:
            return

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 680)
        self.cap.set(4, 480)

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

        self.window.after(10, self.show_frame)

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

        self.window.destroy()

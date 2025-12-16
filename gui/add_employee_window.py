import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import face_recognition
from core.employee_core import EmployeeCore

class AddEmployeeGUI(tk.Frame):
    def __init__(self, parent, inline=False):
        super().__init__(parent, bg="#2A2A3D")
        self.employee_core = EmployeeCore()
        self.inline = inline
        self.face_detected = False

        if not inline:
            self.window = tk.Toplevel(parent)
            self.window.title("Add Employee")
            self.window.geometry("1280x720")
            self.window.resizable(False, False)
            self.container = self.window
        else:
            self.container = self
            self.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # ---------- HEADER ----------
        tk.Label(
            self.container,
            text="Add Employee",
            font=("Helvetica", 20, "bold"),
            bg="#2A2A3D",
            fg="#FF7B02"
        ).pack(pady=10)

        # ---------- NAME ----------
        tk.Label(
            self.container,
            text="Employee Name",
            font=("Arial", 14),
            bg="#2A2A3D",
            fg="white"
        ).pack()

        self.name_entry = tk.Entry(self.container, font=("Arial", 14), width=30)
        self.name_entry.pack(pady=5)

        # ---------- CAMERA ----------
        self.camera_frame = tk.Label(self.container, bg="#000000")
        self.camera_frame.pack(pady=10)

        self.status_label = tk.Label(
            self.container,
            text="No face detected",
            font=("Arial", 14),
            bg="#2A2A3D",
            fg="red"
        )
        self.status_label.pack(pady=5)

        # ---------- BUTTONS ----------
        btn_style = {
            "font": ("Arial", 14),
            "bg": "#FF7B02",
            "fg": "white",
            "activebackground": "#FF9E4B",
            "width": 20,
            "bd": 0,
            "pady": 10
        }

        tk.Button(self.container, text="Start Camera", command=self.start_camera, **btn_style).pack(pady=5)
        tk.Button(self.container, text="Capture Face", command=self.capture, **btn_style).pack(pady=5)

        self.cap = None
        self.running = False

        if not inline:
            self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    # ---------- CAMERA ----------
    def start_camera(self):
        if self.running:
            return

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
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
            self.container.after(10, self.show_frame)
            return

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 🔥 FACE DETECTION
        face_locations = face_recognition.face_locations(rgb)

        self.face_detected = False

        for top, right, bottom, left in face_locations:
            self.face_detected = True

            # Draw rectangle
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Show label
            name = self.name_entry.get().strip() or "Face Detected"
            cv2.putText(
                frame,
                name,
                (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        # Update status
        if self.face_detected:
            self.status_label.config(text="Face detected ✔", fg="lightgreen")
        else:
            self.status_label.config(text="No face detected", fg="red")

        img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        self.camera_frame.img = img
        self.camera_frame.configure(image=img)

        self.container.after(10, self.show_frame)

    # ---------- CAPTURE ----------
    def capture(self):
        if not self.running:
            messagebox.showwarning("Warning", "Camera not running!")
            return

        if not self.face_detected:
            messagebox.showerror("Error", "No face detected! Please align your face.")
            return

        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Employee name is required!")
            return

        ret, frame = self.cap.read()
        if not ret:
            messagebox.showerror("Error", "Camera read failed!")
            return

        success = self.employee_core.add_employee(name, frame)

        if success:
            messagebox.showinfo("Success", f"{name} added successfully!")
        else:
            messagebox.showerror("Error", "Face encoding failed. Try again.")

    # ---------- CLOSE ----------
    def on_close(self):
        self.running = False
        if self.cap and self.cap.isOpened():
            self.cap.release()
        if not self.inline:
            self.window.destroy()
        else:
            self.destroy()

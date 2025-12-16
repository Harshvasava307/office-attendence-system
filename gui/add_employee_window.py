import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import face_recognition
from core.employee_core import EmployeeCore


class AddEmployeeGUI:
    def __init__(self, root):
        self.employee_core = EmployeeCore()
        self.face_detected = False

        self.window = tk.Toplevel(root)
        self.window.title("Add Employee")
        self.window.geometry("1400x900")
        self.window.configure(bg="#2A2A3D")
        self.window.resizable(False, False)

        # ---------- HEADER ----------
        tk.Label(
            self.window,
            text="Add Employee",
            font=("Helvetica", 20, "bold"),
            bg="#2A2A3D",
            fg="#FF7B02"
        ).pack(pady=10)

        # ---------- NAME ----------
        tk.Label(
            self.window,
            text="Employee Name",
            font=("Arial", 14),
            bg="#2A2A3D",
            fg="white"
        ).pack()

        self.name_entry = tk.Entry(self.window, font=("Arial", 14), width=30)
        self.name_entry.pack(pady=5)

        # ---------- CAMERA ----------
        self.camera_label = tk.Label(self.window, bg="black")
        self.camera_label.pack(pady=10)

        self.status_label = tk.Label(
            self.window,
            text="No face detected",
            font=("Arial", 14),
            bg="#2A2A3D",
            fg="red"
        )
        self.status_label.pack()

        # ---------- BUTTONS ----------
        btn_style = {
            "font": ("Arial", 14),
            "bg": "#FF7B02",
            "fg": "white",
            "bd": 0,
            "width": 20,
            "pady": 10
        }

        tk.Button(self.window, text="Start Camera",
                  command=self.start_camera, **btn_style).pack(pady=5)

        tk.Button(self.window, text="Capture Face",
                  command=self.capture, **btn_style).pack(pady=5)

        self.cap = None
        self.running = False

        self.window.protocol("WM_DELETE_WINDOW", self.close)

    # ---------- CAMERA ----------
    def start_camera(self):
        if self.running:
            return

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        if not self.cap.isOpened():
            messagebox.showerror("Camera Error", "Camera not accessible")
            return

        self.running = True
        self.update_frame()

    def update_frame(self):
        if not self.running:
            return

        ret, frame = self.cap.read()
        if not ret:
            self.window.after(10, self.update_frame)
            return

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb)

        self.face_detected = False

        for top, right, bottom, left in faces:
            self.face_detected = True
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            name = self.name_entry.get().strip() or "Face"
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        self.status_label.config(
            text="Face detected ✔" if self.face_detected else "No face detected",
            fg="lightgreen" if self.face_detected else "red"
        )

        img = ImageTk.PhotoImage(Image.fromarray(rgb))
        self.camera_label.configure(image=img)
        self.camera_label.image = img

        self.window.after(10, self.update_frame)

    # ---------- CAPTURE ----------
    def capture(self):
        if not self.face_detected:
            messagebox.showerror("Error", "No face detected")
            return

        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Enter employee name")
            return

        ret, frame = self.cap.read()
        if not ret:
            messagebox.showerror("Error", "Camera read failed")
            return

        if self.employee_core.add_employee(name, frame):
            messagebox.showinfo("Success", f"{name} added successfully")
        else:
            messagebox.showerror("Error", "Face encoding failed")

    # ---------- CLOSE ----------
    def close(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.window.destroy()

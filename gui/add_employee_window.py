import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import face_recognition
from core.employee_core import EmployeeCore

PRIMARY = "#6A64DA"
BG = "#FFFFFF"
TEXT = "#1F2937"
CARD = "#F3F4F6"


class AddEmployeeGUI:
    def __init__(self, root):
        self.employee_core = EmployeeCore()
        self.face_detected = False

        self.window = tk.Toplevel(root)
        self.window.title("Add Employee | Astra Infotech")
        self.window.geometry("1400x900")
        self.window.configure(bg=BG)
        self.window.resizable(False, False)

        self.build_ui()
        self.cap = None
        self.running = False

        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def build_ui(self):
        tk.Label(
            self.window,
            text="Astra Infotech – Add Employee",
            font=("Segoe UI", 20, "bold"),
            bg=BG,
            fg=PRIMARY
        ).pack(pady=10)

        form = tk.Frame(self.window, bg=CARD)
        form.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(form, text="Employee Name", bg=CARD, fg=TEXT,
                 font=("Segoe UI", 14)).pack()

        self.name_entry = tk.Entry(form, font=("Segoe UI", 14), width=30)
        self.name_entry.pack(pady=5)

        self.camera_label = tk.Label(form, bg="black")
        self.camera_label.pack(pady=10)

        self.status_label = tk.Label(form, text="No face detected",
                                     bg=CARD, fg="red",
                                     font=("Segoe UI", 13))
        self.status_label.pack()

        tk.Button(form, text="Start Camera", bg=PRIMARY, fg="white",
                  font=("Segoe UI", 14), width=20, bd=0,
                  command=self.start_camera).pack(pady=5)

        tk.Button(form, text="Capture Face", bg=PRIMARY, fg="white",
                  font=("Segoe UI", 14), width=20, bd=0,
                  command=self.capture).pack(pady=5)

    def start_camera(self):
        if self.running:
            return

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Camera not accessible")
            return

        self.running = True
        self.update_frame()

    def update_frame(self):
        if not self.running:
            return

        ret, frame = self.cap.read()
        if not ret:
            return

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb)

        self.face_detected = False
        for top, right, bottom, left in faces:
            self.face_detected = True
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, self.name_entry.get() or "Employee",
                        (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        self.status_label.config(
            text="Face detected ✔" if self.face_detected else "No face detected",
            fg="green" if self.face_detected else "red"
        )

        img = ImageTk.PhotoImage(Image.fromarray(rgb))
        self.camera_label.configure(image=img)
        self.camera_label.image = img

        self.window.after(10, self.update_frame)

    def capture(self):
        if not self.face_detected:
            messagebox.showerror("Error", "No face detected")
            return

        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Warning", "Enter employee name")
            return

        ret, frame = self.cap.read()
        if self.employee_core.add_employee(name, frame):
            messagebox.showinfo("Success", "Employee added successfully")
        else:
            messagebox.showerror("Error", "Face capture failed")

    def close(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.window.destroy()

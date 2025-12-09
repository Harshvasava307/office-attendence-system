import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
from utils.face_recognition_module import recognize_employee
from utils.attendance import mark_attendance

class EmployeeAttendanceWindow:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.window.title("Employee Attendance")
        self.window.geometry("660x560")
        self.window.resizable(False, False)

        # VIDEO FRAME
        self.video_frame = tk.Label(self.window)
        self.video_frame.pack()

        # BUTTON
        self.btn_login = tk.Button(
            self.window,
            text="Mark Attendance",
            font=("Arial", 14),
            width=20,
            command=self.save_attendance
        )
        self.btn_login.pack(pady=10)

        # CAMERA
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        if not self.cap.isOpened():
            messagebox.showerror("Camera Error", "Cannot access camera.")
            self.window.destroy()
            return

        self.employee_name = "Unknown"

        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.window.after(10, self.update_frame)
            return

        # Recognize face
        name = recognize_employee(frame)
        if name is not None:
            self.employee_name = name

        # Overlay text
        now = datetime.datetime.now()
        cv2.putText(frame, f"Name: {self.employee_name}", (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Date: {now.strftime('%d-%m-%Y')}", (10, 55),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        cv2.putText(frame, f"Time: {now.strftime('%H:%M:%S')}", (10, 85),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

        # Convert to Tkinter
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        tk_image = ImageTk.PhotoImage(Image.fromarray(rgb))
        self.video_frame.configure(image=tk_image)
        self.video_frame.image = tk_image

        self.window.after(10, self.update_frame)

    def save_attendance(self):
        if self.employee_name == "Unknown":
            messagebox.showerror("Error", "Face not recognized!")
            return

        mark_attendance(self.employee_name)
        messagebox.showinfo("Success", f"Attendance marked for {self.employee_name}")
        self.close_window()

    def close_window(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()
        self.window.destroy()

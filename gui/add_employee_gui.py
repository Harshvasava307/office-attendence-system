import tkinter as tk
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

        tk.Label(self.window, text="Enter Employee Name").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        # Camera Frame
        self.camera_frame = tk.Label(self.window)
        self.camera_frame.pack(pady=10)

        # Start Camera Button
        tk.Button(self.window, text="Start Camera", command=self.start_camera).pack(pady=5)

        tk.Button(self.window, text="Capture Face", command=self.capture).pack(pady=5)

        self.cap = None
        self.running = False

        # Close event
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def start_camera(self):
        if self.running:
            return

        self.cap = cv2.VideoCapture(0)

        # HD resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 680)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        self.running = True
        self.show_frame()

    def show_frame(self):
        if not self.running:
            return

        ret, frame = self.cap.read()
        if not ret:
            return

        # Convert for Tkinter display
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(rgb))

        self.camera_frame.img = img
        self.camera_frame.configure(image=img)

        # Continue updating frame
        self.window.after(10, self.show_frame)

    def capture(self):
        if not self.running:
            return

        ret, frame = self.cap.read()
        if not ret:
            print("Camera error!")
            return

        name = self.name_entry.get().strip()

        if name == "":
            print("Name cannot be empty!")
            return

        self.employee_core.add_employee(name, frame)
        print("Employee added successfully!")

    def on_close(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.window.destroy()

import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime

from utils.face_recognition_module import recognize_employee
from utils.attendance import mark_attendance
from gui.ui_theme import *


class EmployeeAttendanceWindow(tk.Frame):
    def __init__(self, parent, inline=False):
        super().__init__(parent, bg=PRIMARY_BG)
        self.inline = inline
        self.cap = None
        self.employee_name = "Unknown"

        # ---------- CONTAINER ----------
        if not inline:
            self.window = tk.Toplevel(parent)
            self.window.title("Astra Infotech – Employee Attendance")
            self.window.geometry("1100x750")
            self.window.configure(bg=PRIMARY_BG)
            self.window.resizable(False, False)
            self.container = self.window
        else:
            self.container = self
            self.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        # ---------- HEADER ----------
        header = tk.Frame(self.container, bg=PRIMARY_BG)
        header.pack(fill=tk.X, pady=(0, 15))

        tk.Label(
            header,
            text="Employee Attendance",
            font=FONT_TITLE,
            bg=PRIMARY_BG,
            fg=TEXT_PRIMARY
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Astra Infotech",
            font=FONT_SUBTITLE,
            bg=PRIMARY_BG,
            fg=TEXT_MUTED
        ).pack(anchor="w")

        # ---------- CAMERA CARD ----------
        card = tk.Frame(
            self.container,
            bg=CARD_BG,
            highlightbackground=BORDER,
            highlightthickness=1
        )
        card.pack(fill=tk.BOTH, expand=True)

        self.video_label = tk.Label(card, bg="black")
        self.video_label.pack(pady=15)

        self.info_label = tk.Label(
            card,
            text="Detecting face...",
            font=FONT_BODY,
            bg=CARD_BG,
            fg=TEXT_MUTED
        )
        self.info_label.pack(pady=5)

        tk.Button(
            card,
            text="Mark Attendance",
            font=FONT_BUTTON,
            bg=ACCENT,
            fg="white",
            activebackground=ACCENT_HOVER,
            width=25,
            bd=0,
            pady=12,
            command=self.save_attendance
        ).pack(pady=15)

        # ---------- CAMERA ----------
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        if not self.cap.isOpened():
            messagebox.showerror("Camera Error", "Cannot access camera.")
            self.close_window()
            return

        if not inline:
            self.window.protocol("WM_DELETE_WINDOW", self.close_window)

        self.update_frame()

    # ---------- CAMERA LOOP ----------
    def update_frame(self):
        if not self.cap or not self.cap.isOpened():
            return

        ret, frame = self.cap.read()
        if not ret:
            self.container.after(15, self.update_frame)
            return

        name = recognize_employee(frame)

        if name:
            self.employee_name = name
            self.info_label.config(
                text=f"Face detected: {name}",
                fg=SUCCESS
            )
        else:
            self.employee_name = "Unknown"
            self.info_label.config(
                text="Detecting face...",
                fg=TEXT_MUTED
            )

        now = datetime.datetime.now()
        cv2.putText(
            frame,
            now.strftime("%d-%m-%Y  %H:%M:%S"),
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (106, 100, 218),
            2
        )

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(rgb))
        self.video_label.configure(image=img)
        self.video_label.image = img

        self.container.after(15, self.update_frame)

    # ---------- SAVE ----------
    def save_attendance(self):
        if self.employee_name == "Unknown":
            messagebox.showerror("Error", "Face not recognized!")
            return

        mark_attendance(self.employee_name)
        messagebox.showinfo(
            "Success",
            f"Attendance marked for {self.employee_name}"
        )
        self.close_window()

    # ---------- CLOSE ----------
    def close_window(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()
        if not self.inline:
            self.window.destroy()
        else:
            self.destroy()

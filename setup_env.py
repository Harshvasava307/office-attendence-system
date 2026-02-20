import subprocess
import sys
import importlib
import os
import threading
import tkinter as tk
from tkinter import ttk

# Import your theme
from gui.ui_theme import *

# -------------------------
# Required packages
# -------------------------
required_packages = {
    "numpy": "numpy",
    "opencv-python": "cv2",
    "face_recognition": "face_recognition",
    "Pillow": "PIL",
    "tkcalendar": "tkcalendar"
}

prebuilt_wheels = {
    "dlib": "dlib-19.24.6-cp310-cp310-win_amd64.whl",
    "face_recognition_models": "face_recognition_models-0.3.0-py3-none-any.whl"
}

# -------------------------
# UI Setup Class
# -------------------------
class SetupUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Astra Infotech – Setup Installer")
        self.root.geometry("700x500")
        self.root.configure(bg=PRIMARY_BG)
        self.root.resizable(False, False)

        self.build_ui()

        # Run installation in separate thread
        threading.Thread(target=self.run_setup, daemon=True).start()

    def build_ui(self):
        tk.Label(
            self.root,
            text="Astra Infotech – Environment Setup",
            font=FONT_TITLE,
            bg=PRIMARY_BG,
            fg=TEXT_PRIMARY
        ).pack(pady=20)

        self.progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=500,
            mode="determinate"
        )
        self.progress.pack(pady=10)

        self.log_box = tk.Text(
            self.root,
            height=15,
            bg=CARD_BG,
            fg=TEXT_PRIMARY,
            insertbackground="white"
        )
        self.log_box.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.status_label = tk.Label(
            self.root,
            text="Starting setup...",
            font=FONT_BODY,
            bg=PRIMARY_BG,
            fg=TEXT_MUTED
        )
        self.status_label.pack(pady=10)

    def log(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)
        self.root.update()

    def check_module(self, module_name):
        try:
            importlib.import_module(module_name)
            self.log(f"{module_name} already installed.")
            return True
        except ImportError:
            self.log(f"{module_name} not found.")
            return False

    def install_package(self, pip_name):
        try:
            self.log(f"Installing {pip_name}...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", pip_name],
                stdout=subprocess.DEVNULL
            )
            self.log(f"{pip_name} installed successfully.")
            return True
        except:
            self.log(f"Failed to install {pip_name}")
            return False

    def install_wheel(self, wheel_path):
        if not os.path.exists(wheel_path):
            self.log(f"Wheel {wheel_path} not found.")
            return False
        return self.install_package(wheel_path)

    def run_setup(self):
        total_steps = len(prebuilt_wheels) + len(required_packages)
        step = 0

        # Install wheels
        for pkg, wheel in prebuilt_wheels.items():
            if not self.check_module(pkg):
                self.install_wheel(wheel)
            step += 1
            self.progress["value"] = (step / total_steps) * 100

        # Install packages
        for pip_name, module_name in required_packages.items():
            if not self.check_module(module_name):
                self.install_package(pip_name)
            step += 1
            self.progress["value"] = (step / total_steps) * 100

        self.status_label.config(
            text="Setup Complete ✔",
            fg=SUCCESS
        )

        self.log("\nAll dependencies processed.")

        # Auto launch main.py
        if os.path.exists("main.py"):
            self.log("Launching main.py...")
            subprocess.Popen([sys.executable, "main.py"])
            self.root.after(2000, self.root.destroy)


# -------------------------
# Run Installer
# -------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SetupUI(root)
    root.mainloop()
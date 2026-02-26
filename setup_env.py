import subprocess
import sys
import importlib
import os
import threading
import tkinter as tk
from tkinter import ttk
from gui.ui_theme import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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


class SetupUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Astra Infotech – Setup Installer")
        self.root.geometry("700x500")
        self.root.configure(bg=PRIMARY_BG)
        self.root.resizable(False, False)

        self.build_ui()
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
            self.log(f"{module_name} already installed ✔")
            return True
        except ImportError:
            self.log(f"{module_name} not found.")
            return False

    def install_package(self, package):
        try:
            self.log(f"Installing {package}...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package]
            )
            self.log(f"{package} installed successfully ✔")
            return True
        except Exception as e:
            self.log(f"Error installing {package}: {e}")
            return False

    def run_setup(self):

        # Simple Python version check
        if not (sys.version_info.major == 3 and sys.version_info.minor == 10):
            self.status_label.config(
                text="Python 3.10 Required ❌",
                fg="red"
            )
            self.log("Please install Python 3.10 from the 'Python Installer' folder.")
            return

        total_steps = len(prebuilt_wheels) + len(required_packages)
        step = 0

        # Install Wheels
        for module, wheel in prebuilt_wheels.items():
            if not self.check_module(module):
                if not self.install_package(os.path.join(BASE_DIR, wheel)):
                    self.setup_failed()
                    return

            step += 1
            self.progress["value"] = (step / total_steps) * 100

        # Install Normal Packages
        for pip_name, module_name in required_packages.items():
            if not self.check_module(module_name):
                if not self.install_package(pip_name):
                    self.setup_failed()
                    return

            step += 1
            self.progress["value"] = (step / total_steps) * 100

        self.status_label.config(text="Setup Complete ✔", fg=SUCCESS)
        self.log("\nAll dependencies installed successfully.")

        main_path = os.path.join(BASE_DIR, "main.py")
        if os.path.exists(main_path):
            subprocess.Popen([sys.executable, main_path])
            self.root.after(2000, self.root.destroy)

    def setup_failed(self):
        self.status_label.config(text="Setup Failed ❌", fg="red")
        self.log("\nInstallation failed.")
        self.log("Please install Python 3.10 from the 'Python Installer' folder and run setup again.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SetupUI(root)
    root.mainloop()
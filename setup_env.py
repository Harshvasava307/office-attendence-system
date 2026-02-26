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

    # -------------------------
    # Python 3.10 Enforcement
    # -------------------------
    def ensure_python_310(self):
        if sys.version_info.major == 3 and sys.version_info.minor == 10:
            self.log("Python 3.10 verified ✔")
            return True

        installer_path = os.path.join(BASE_DIR, "python-3.10.11-amd64.exe")

        if not os.path.exists(installer_path):
            self.log("Python 3.10 installer not found in root ❌")
            self.status_label.config(text="Python Installer Missing", fg="red")
            return False

        self.log("Installing Python 3.10...")

        subprocess.run([
            installer_path,
            "/quiet",
            "InstallAllUsers=1",
            "PrependPath=1"
        ])

        self.log("Python installed. Please restart setup.")
        self.status_label.config(text="Restart Required", fg="orange")
        return False

    # -------------------------
    # Module Check
    # -------------------------
    def check_module(self, module_name):
        try:
            importlib.import_module(module_name)
            self.log(f"{module_name} already installed.")
            return True
        except ImportError:
            self.log(f"{module_name} not found.")
            return False

    # -------------------------
    # Install Wheel (ROOT SAFE)
    # -------------------------
    def install_wheel(self, wheel_name):
        wheel_path = os.path.join(BASE_DIR, wheel_name)

        if not os.path.exists(wheel_path):
            self.log(f"Wheel {wheel_name} not found in root ❌")
            return False

        try:
            self.log(f"Installing {wheel_name}...")
            subprocess.check_call([
                sys.executable,
                "-m",
                "pip",
                "install",
                wheel_path
            ])
            self.log(f"{wheel_name} installed successfully ✔")
            return True
        except Exception as e:
            self.log(f"Failed to install {wheel_name}: {e}")
            return False

    # -------------------------
    # Install Normal Packages
    # -------------------------
    def install_package(self, pip_name):
        try:
            self.log(f"Installing {pip_name}...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", pip_name]
            )
            self.log(f"{pip_name} installed successfully ✔")
            return True
        except Exception as e:
            self.log(f"Failed to install {pip_name}: {e}")
            return False

    # -------------------------
    # Main Setup Process
    # -------------------------
    def run_setup(self):

        if not self.ensure_python_310():
            return

        total_steps = len(prebuilt_wheels) + len(required_packages)
        step = 0

        # Install prebuilt wheels
        for module, wheel in prebuilt_wheels.items():
            if not self.check_module(module):
                self.install_wheel(wheel)

            step += 1
            self.progress["value"] = (step / total_steps) * 100

        # Install pip packages
        for pip_name, module_name in required_packages.items():
            if not self.check_module(module_name):
                self.install_package(pip_name)

            step += 1
            self.progress["value"] = (step / total_steps) * 100

        self.status_label.config(text="Setup Complete ✔", fg=SUCCESS)
        self.log("\nAll dependencies processed successfully.")

        # Launch main
        main_path = os.path.join(BASE_DIR, "main.py")

        if os.path.exists(main_path):
            self.log("Launching main.py...")
            subprocess.Popen([sys.executable, main_path])
            self.root.after(2000, self.root.destroy)


if __name__ == "__main__":
    root = tk.Tk()
    app = SetupUI(root)
    root.mainloop()
import subprocess
import sys
import importlib
import os

# -------------------------
# List of required packages
# -------------------------
required_packages = {
    "numpy": "numpy",  # pip_name : module_name
    "opencv-python": "cv2",
    "face_recognition": "face_recognition",
    "dlib": "dlib",
    "Pillow": "PIL",
    # tkinter is included in standard Python
}

# -------------------------
# Log file
# -------------------------
log_file = "setup_install_log.txt"


def log(message):
    print(message)
    with open(log_file, "a") as f:
        f.write(message + "\n")


# -------------------------
# Install a package
# -------------------------
def install_package(pip_name):
    try:
        log(f"Installing {pip_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
        log(f"{pip_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        log(f"Failed to install {pip_name}: {e}")
        return False
    return True


# -------------------------
# Check if module exists
# -------------------------
def check_module(module_name):
    try:
        importlib.import_module(module_name)
        log(f"{module_name} already installed.")
        return True
    except ImportError:
        log(f"{module_name} not found.")
        return False


# -------------------------
# Main installation process
# -------------------------
def main():
    log("=== Setup Environment Started ===\n")

    for pip_name, module_name in required_packages.items():
        if not check_module(module_name):
            success = install_package(pip_name)
            if not success:
                log(f"ERROR: Could not install {pip_name}. Please install manually.")

    log("\n=== All dependencies processed ===")

    # Optional: Run main.py automatically
    main_script = "main.py"
    if os.path.exists(main_script):
        try:
            log(f"Launching {main_script}...")
            subprocess.run([sys.executable, main_script])
        except Exception as e:
            log(f"Failed to run {main_script}: {e}")
    else:
        log(f"{main_script} not found. Please make sure it is in the same folder as this setup script.")


if __name__ == "__main__":
    main()

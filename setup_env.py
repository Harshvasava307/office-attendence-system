import subprocess
import sys
import importlib
import os

# -------------------------
# Required packages with module names
# -------------------------
required_packages = {
    "numpy": "numpy",
    "opencv-python": "cv2",
    "face_recognition": "face_recognition",
    "Pillow": "PIL",
    "tkcalendar": "tkcalendar"  # ← Add this line
}

# Prebuilt wheels for Windows
prebuilt_wheels = {
    "dlib": "dlib-19.24.6-cp310-cp310-win_amd64.whl",
    "face_recognition_models": "face_recognition_models-0.3.0-py3-none-any.whl"
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
# Install a package via pip
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
# Install from wheel
# -------------------------
def install_wheel(wheel_path):
    if not os.path.exists(wheel_path):
        log(f"Wheel {wheel_path} not found. Please download it manually.")
        return False
    return install_package(wheel_path)

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

    # 1️⃣ Install prebuilt wheels first (dlib, face_recognition_models)
    for pkg_name, wheel_file in prebuilt_wheels.items():
        module_name = pkg_name
        if not check_module(module_name):
            success = install_wheel(wheel_file)
            if not success:
                log(f"ERROR: Could not install {pkg_name}. Please install manually.")

    # 2️⃣ Install regular packages via pip
    for pip_name, module_name in required_packages.items():
        if not check_module(module_name):
            success = install_package(pip_name)
            if not success:
                log(f"ERROR: Could not install {pip_name}. Please install manually.")

    # 3️⃣ Check tkinter
    try:
        import tkinter
        log("tkinter available")
    except ImportError:
        log("tkinter not found. Please install via your Python installation.")

    log("\n=== All dependencies processed ===\n")

    # 4️⃣ Run main.py automatically
    main_script = "main.py"
    if os.path.exists(main_script):
        try:
            log(f"Launching {main_script}...")
            subprocess.run([sys.executable, main_script], check=True)
        except subprocess.CalledProcessError as e:
            log(f"Failed to run {main_script}: {e}")
    else:
        log(f"{main_script} not found. Please make sure it is in the same folder as this setup script.")

if __name__ == "__main__":
    main()

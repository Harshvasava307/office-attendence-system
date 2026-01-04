# 🧑‍💼 Office Attendance System – Installation Guide (Windows)

This document explains **step‑by‑step installation** of all required tools and Python packages for running the **Office Attendance System with Face Recognition** on **Windows**.

> ⚠️ This project has **complex native dependencies** (dlib, face_recognition). Follow steps **exactly in order**.

---

## 📌 System Requirements

* OS: **Windows 10 / 11 (64‑bit)**
* Python: **3.10.x (MANDATORY)**
* Architecture: **64‑bit only**
* Internet connection

---

## 1️⃣ Install Python 3.10 (IMPORTANT)

### 🔗 Download

Official Python 3.10.11 (64‑bit):

[https://www.python.org/downloads/release/python-31011/](https://www.python.org/downloads/release/python-31011/)

Download:

```
python-3.10.11-amd64.exe
```

### ✅ During Installation

* ✔️ **Check:** Add Python to PATH
* ✔️ Install for current user

### 🔍 Verify

```bash
python --version
```

Expected:

```
Python 3.10.x
```

---

## 2️⃣ Create & Activate Virtual Environment

From project root:

```bash
cd C:\laragon\www\office-attendence-system
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

You should see:

```
(.venv)
```

---

## 3️⃣ Upgrade Build Tools (Inside venv)

```bash
python -m pip install --upgrade pip setuptools wheel
```

---

## 4️⃣ Install Core Dependencies

```bash
python -m pip install numpy pillow cmake
```

---

## 5️⃣ Install dlib (PRECOMPILED – REQUIRED)

### ❗ Do NOT install `dlib`

It fails to compile on Windows.

### ✅ Install precompiled binary

```bash
python -m pip install dlib-bin==19.24.6
```

### 🔍 Verify

```bash
python -c "import dlib; print(dlib.__version__)"
```

---

## 6️⃣ Install face_recognition (SAFE MODE)

⚠️ Install **without dependencies** to prevent rebuilding dlib.

```bash
python -m pip install face_recognition --no-deps
```

---

## 7️⃣ Install face_recognition Models (REQUIRED)

```bash
python -m pip install face-recognition-models
```

---

## 8️⃣ Install GUI Dependencies

```bash
python -m pip install tkcalendar
```

(Tkinter comes bundled with Python on Windows)

---

## 9️⃣ Verify Full Setup

```bash
python - <<EOF
import dlib
import face_recognition
from tkcalendar import Calendar
print("All dependencies installed successfully")
EOF
```

---

## 🔟 Run the Application

```bash
python main.py
```

---

## ⚠️ Known Warning (Safe to Ignore)

```
UserWarning: pkg_resources is deprecated as an API
```

This warning:

* Does NOT break the app
* Comes from `face_recognition_models`
* Is safe until at least **2025**

### Optional: Suppress Warning

Add at top of `main.py`:

```python
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
```

---

## 🧪 Troubleshooting

### ❌ face_recognition not found

✔ Ensure `.venv` is activated

### ❌ dlib build error

✔ Ensure you installed `dlib-bin`, NOT `dlib`

### ❌ Python version mismatch

✔ Must be Python 3.10 (64‑bit)

---

## 📦 Final Installed Packages

```text
Python              3.10.x
numpy               latest
pillow              latest
cmake               latest
dlib-bin            19.24.6
face_recognition    latest
face-recognition-models latest
tkcalendar          latest
```

---

## ✅ Installation Status

If the app starts and loads employees without crashing:

🎉 **INSTALLATION SUCCESSFUL** 🎉

---

## 👨‍💻 Maintainer Notes

This setup avoids:

* Visual C++ build tools
* Manual wheel hunting
* Windows compilation errors

Recommended for:

* College projects
* Production demos
* Attendance systems

---

Happy Coding 🚀

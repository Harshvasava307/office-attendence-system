# main.spec — for Face Attendance System
# Automatically includes all required folders and files

import os
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Absolute paths
project_dir = os.path.abspath("C:/Harsh/office-attendence-system")
face_models_dir = os.path.abspath(
    "C:/Users/Shiv/AppData/Local/Programs/Python/Python311/Lib/site-packages/face_recognition_models/models"
)

# Collect all hidden imports for face_recognition
hidden_imports = collect_submodules('face_recognition')

a = Analysis(
    ['main.py'],
    pathex=[project_dir],
    binaries=[],
    datas=[
        (os.path.join(project_dir, 'gui'), 'gui'),
        (os.path.join(project_dir, 'assets'), 'assets'),
        (os.path.join(project_dir, 'storage/employees/encodings'), 'encodings'),
        (os.path.join(project_dir, 'storage/employees/images'), 'storage/employees/images'),
        (os.path.join(project_dir, 'haarcascade_frontalface_default.xml'), '.'),
        (face_models_dir, 'face_recognition_models/models'),
    ],
    hiddenimports=hidden_imports + [
        'dlib', 'cv2', 'PIL', 'tkinter', 'numpy', 'cv2.data'
    ],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='FaceAttendanceSystem',
    debug=False,
    strip=False,
    upx=True,
    console=False,  # set True if you want terminal visible
    icon=None  # set icon path if you have one
)

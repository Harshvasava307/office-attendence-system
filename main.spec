# -*- mode: python ; coding: utf-8 -*-
import sys
import os
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Include all hidden imports from face_recognition
hidden_imports = collect_submodules('face_recognition')

# Project root
project_root = os.path.abspath('.')

a = Analysis(
    ['main.py'],
    pathex=[project_root],
    binaries=[],
    datas=[
        # Include all necessary folders
        (os.path.join(project_root, 'gui'), 'gui'),
        (os.path.join(project_root, 'assets'), 'assets'),
        (os.path.join(project_root, 'storage/employees/images'), 'storage/employees/images'),
        (os.path.join(project_root, 'encodings'), 'encodings'),
        (os.path.join(project_root, 'haarcascade_frontalface_default.xml'), '.'),

        # Face recognition models
        ('C:/Users/Shiv/AppData/Local/Programs/Python/Python311/Lib/site-packages/face_recognition_models/models',
         'face_recognition_models/models'),
    ],
    hiddenimports=hidden_imports + [
        'cv2', 'PIL', 'tkinter', 'numpy'
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
    console=False,
    icon=None
)

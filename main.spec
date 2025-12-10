# main.spec — for Face Attendance System
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('gui/', 'gui'),
        ('assets/', 'assets'),
        ('models/', 'models'),
        ('encodings/', 'encodings'),
        ('haarcascade_frontalface_default.xml', '.'),
    ],
    hiddenimports=[
        'face_recognition',
        'dlib',
        'cv2',
        'PIL',
        'tkinter',
        'numpy'
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
    console=False,  # hide console screen
    icon='assets/app_icon.ico'  # if you have an icon
)

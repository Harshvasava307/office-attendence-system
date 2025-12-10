# utils/resource_path.py
import sys
import os

def resource_path(relative_path):
    """
    Get absolute path to resource, works for Python script or PyInstaller EXE.
    """
    try:
        # PyInstaller stores files in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMPLOYEE_IMAGES_DIR = os.path.join(BASE_DIR, "storage", "employees", "images")
EMPLOYEE_ENCODINGS_DIR = os.path.join(BASE_DIR, "storage", "employees", "encodings")
ATTENDANCE_DIR = os.path.join(BASE_DIR, "storage", "attendance")

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"  # Change this later

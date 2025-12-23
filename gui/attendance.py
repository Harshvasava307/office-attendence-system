import csv
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ATTENDANCE_FILE = os.path.join(BASE_DIR, "data", "attendance.csv")

def mark_attendance(name):
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    file_exists = os.path.isfile(ATTENDANCE_FILE)

    with open(ATTENDANCE_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "EmployeeName",
                "Date",
                "CheckIn",
                "CheckOut",
                "Status"
            ])

        writer.writerow([
            name,
            date,
            time,
            "",
            "Present"
        ])

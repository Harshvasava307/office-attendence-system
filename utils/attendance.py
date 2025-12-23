import csv
import os
import datetime

# Always get the folder relative to THIS script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, "..", "data")  # relative to gui folder
ATTENDANCE_FILE = os.path.join(DATA_DIR, "attendance.csv")

# Ensure data folder exists
os.makedirs(DATA_DIR, exist_ok=True)

def mark_attendance(name):
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    existing_records = []
    if os.path.isfile(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_records = [r for r in reader]

        # Prevent duplicate
        if any(r["EmployeeName"]==name and r["Date"]==date for r in existing_records):
            print(f"{name} is already marked today")
            return

    # Append attendance
    file_exists = os.path.isfile(ATTENDANCE_FILE)
    with open(ATTENDANCE_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["EmployeeName","Date","CheckIn","CheckOut","Status"])
        writer.writerow([name, date, time, "", "Present"])
        print(f"{name} marked present for {date}")

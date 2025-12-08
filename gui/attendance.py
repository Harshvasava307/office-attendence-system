import csv
import os
import datetime

ATTENDANCE_FILE = "C:\\Harsh\\office-attendence-system\\data\\attendance.csv"

def mark_attendance(name):
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    file_exists = os.path.isfile(ATTENDANCE_FILE)

    with open(ATTENDANCE_FILE, "a", newline='') as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Name", "Date", "Time"])

        writer.writerow([name, date, time])

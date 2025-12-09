import csv
import datetime
import os

def mark_attendance(name):
    file = "attendance.csv"
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    file_exists = os.path.exists(file)

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Name", "Date", "Time"])

        writer.writerow([name, date, time])

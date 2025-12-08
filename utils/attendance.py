import csv
import os
import datetime

# Folder to store daily attendance files
ATTENDANCE_FOLDER = "storage/attendance"

if not os.path.exists(ATTENDANCE_FOLDER):
    os.makedirs(ATTENDANCE_FOLDER)


def get_today_file():
    """Return the CSV filepath for today"""
    today_str = datetime.datetime.now().strftime("%Y-%m-%d")
    return os.path.join(ATTENDANCE_FOLDER, f"{today_str}.csv")


def mark_attendance(name, action="Login"):
    """
    Marks attendance for an employee
    action: "Login" or "Logout"
    """
    filepath = get_today_file()
    file_exists = os.path.isfile(filepath)

    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%Y-%m-%d")

    with open(filepath, "a", newline="") as f:
        writer = csv.writer(f)

        # Write headers if file does not exist
        if not file_exists:
            writer.writerow(["Name", "Date", "Time", "Action"])

        writer.writerow([name, date_str, time_str, action])


def check_attendance(name):
    """
    Check if employee has already marked attendance today.
    Returns list of actions logged today (["Login", "Logout"]) or empty list
    """
    filepath = get_today_file()
    actions = []
    if os.path.isfile(filepath):
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Name"] == name:
                    actions.append(row["Action"])
    return actions

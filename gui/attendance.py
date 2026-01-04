import csv
import os
import datetime

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, "..", "data")
ATTENDANCE_FILE = os.path.join(DATA_DIR, "attendance.csv")

os.makedirs(DATA_DIR, exist_ok=True)


def _read_records():
    if not os.path.exists(ATTENDANCE_FILE):
        return []

    with open(ATTENDANCE_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _write_records(records):
    with open(ATTENDANCE_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["EmployeeName", "Date", "CheckIn", "CheckOut", "Status"]
        )
        writer.writeheader()
        writer.writerows(records)


def get_today_record(name):
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    records = _read_records()
    for r in records:
        if r["EmployeeName"] == name and r["Date"] == today:
            return r
    return None


def mark_check_in(name):
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    records = _read_records()

    if any(r["EmployeeName"] == name and r["Date"] == date for r in records):
        return False, "Already checked in"

    records.append({
        "EmployeeName": name,
        "Date": date,
        "CheckIn": time,
        "CheckOut": "",
        "Status": "Present"
    })

    _write_records(records)
    return True, time


def mark_check_out(name):
    now = datetime.datetime.now()
    time_out = now.strftime("%H:%M:%S")

    records = _read_records()
    today = now.strftime("%d-%m-%Y")

    for r in records:
        if r["EmployeeName"] == name and r["Date"] == today:
            if r["CheckOut"]:
                return False, "Already checked out"

            # calculate working hours
            check_in_time = datetime.datetime.strptime(
                r["CheckIn"], "%H:%M:%S"
            )
            duration = (now - check_in_time).seconds / 3600

            r["CheckOut"] = time_out
            r["Status"] = "Present" if duration >= 6 else "Half Day"

            _write_records(records)
            return True, time_out

    return False, "No check-in found"

import csv
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ATTENDANCE_FILE = os.path.join(BASE_DIR, "data", "attendance.csv")

def _read_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        return []

    with open(ATTENDANCE_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def get_all_employees():
    records = _read_attendance()
    return sorted(set(r["EmployeeName"] for r in records))

def get_employee_attendance(employee_name):
    records = _read_attendance()
    return [r for r in records if r["EmployeeName"] == employee_name]

def get_attendance_stats(employee_name, month, year):
    records = get_employee_attendance(employee_name)
    present = absent = half_day = 0
    total_days = set()
    for r in records:
        date_obj = datetime.datetime.strptime(r["Date"], "%d-%m-%Y")
        if date_obj.month == month and date_obj.year == year:
            total_days.add(r["Date"])
            if r["Status"] == "Present":
                present += 1
            elif r["Status"] == "Half Day":
                half_day += 1
    absent = max(0, len(total_days) - present - half_day)
    return {"present": present, "absent": absent, "half_day": half_day, "total_days": len(total_days)}

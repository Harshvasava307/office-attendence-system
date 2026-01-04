import csv
import os
import datetime

# Paths
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, "..", "data")
ATTENDANCE_FILE = os.path.join(DATA_DIR, "attendance.csv")

os.makedirs(DATA_DIR, exist_ok=True)


# -------------------- Helpers --------------------
def _read_all():
    if not os.path.isfile(ATTENDANCE_FILE):
        return []

    with open(ATTENDANCE_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _write_all(records):
    with open(ATTENDANCE_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["EmployeeName", "Date", "CheckIn", "CheckOut", "Status"]
        )
        writer.writeheader()
        writer.writerows(records)


# -------------------- Get Today's Record --------------------
def get_today_record(employee_name):
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    for r in _read_all():
        if r["EmployeeName"] == employee_name and r["Date"] == today:
            return r
    return None


# -------------------- Check In --------------------
def mark_check_in(employee_name):
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    records = _read_all()

    # Prevent duplicate check-in
    for r in records:
        if r["EmployeeName"] == employee_name and r["Date"] == date:
            return False

    records.append({
        "EmployeeName": employee_name,
        "Date": date,
        "CheckIn": time,
        "CheckOut": "",
        "Status": "Present"
    })

    _write_all(records)
    print(f"[INFO] {employee_name} checked in at {time}")
    return True


# -------------------- Check Out --------------------
def mark_check_out(employee_name):
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    checkout_time = now.strftime("%H:%M:%S")

    records = _read_all()

    for r in records:
        if r["EmployeeName"] == employee_name and r["Date"] == date:
            if r["CheckOut"]:
                return False

            check_in_dt = datetime.datetime.strptime(
                f"{date} {r['CheckIn']}", "%d-%m-%Y %H:%M:%S"
            )
            hours = (now - check_in_dt).total_seconds() / 3600

            # Business rules
            if hours < 4:
                status = "Half Day"
            elif hours < 6:
                status = "Short Leave"
            else:
                status = "Present"

            r["CheckOut"] = checkout_time
            r["Status"] = status

            _write_all(records)
            print(f"[INFO] {employee_name} checked out ({hours:.2f} hrs) → {status}")
            return True

    return False

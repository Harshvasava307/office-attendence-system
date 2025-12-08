import csv
import os
from datetime import datetime
from config.config import ATTENDANCE_DIR

class AttendanceCore:

    def get_today_file(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return os.path.join(ATTENDANCE_DIR, f"{today}.csv")

    def mark_attendance(self, name, mode):
        """
        mode = "login" or "logout"
        """
        file_path = self.get_today_file()
        time_now = datetime.now().strftime("%H:%M:%S")

        file_exists = os.path.isfile(file_path)

        with open(file_path, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Name", "Mode", "Time"])
            writer.writerow([name, mode, time_now])

        return True

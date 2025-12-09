import cv2
import os

EMPLOYEE_IMAGES_DIR = "storage/employees/images"

class EmployeeCore:
    def __init__(self):
        os.makedirs(EMPLOYEE_IMAGES_DIR, exist_ok=True)
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

    def add_employee(self, name, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0:
            return False

        x, y, w, h = faces[0]
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        cv2.imwrite(os.path.join(EMPLOYEE_IMAGES_DIR, f"{name}.jpg"), face)
        return True

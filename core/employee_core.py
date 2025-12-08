import cv2
import os

EMPLOYEE_IMAGES_DIR = "storage/employees/images"

# Ensure directory exists
os.makedirs(EMPLOYEE_IMAGES_DIR, exist_ok=True)

# Haarcascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

class EmployeeCore:
    def __init__(self):
        pass

    def add_employee(self, name, frame):
        """
        Detect face in frame, crop, resize, and save
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) == 0:
            print("No face detected! Cannot add employee.")
            return False

        # Take the first detected face
        x, y, w, h = faces[0]
        face_roi = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face_roi, (200, 200))

        # Save image
        filename = f"{name}.png"
        path = os.path.join(EMPLOYEE_IMAGES_DIR, filename)
        cv2.imwrite(path, face_resized)

        print(f"Saved employee face for {name} at {path}")
        return True

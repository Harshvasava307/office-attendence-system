import cv2
import os
import numpy as np

EMPLOYEE_IMAGES_DIR = "storage/employees/images"

# Haarcascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load employee images into memory
employee_data = []
employee_names = []

for file in os.listdir(EMPLOYEE_IMAGES_DIR):
    if file.endswith((".png", ".jpg")):
        path = os.path.join(EMPLOYEE_IMAGES_DIR, file)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            employee_data.append(img)
            employee_names.append(os.path.splitext(file)[0])

def recognize_employee(frame):
    """
    Detects face in frame and returns employee name if matched with stored images.
    """
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.1, 5)

    if len(faces) == 0:
        return None

    x, y, w, h = faces[0]
    face_roi = gray_frame[y:y+h, x:x+w]
    face_resized = cv2.resize(face_roi, (200, 200))

    best_match_name = None
    best_score = -1

    for i, emp_img in enumerate(employee_data):
        emp_resized = cv2.resize(emp_img, (200, 200))

        # Compare using Mean Squared Error
        diff = cv2.absdiff(emp_resized, face_resized)
        score = -np.mean(diff)  # lower difference -> higher score

        if score > best_score:
            best_score = score
            best_match_name = employee_names[i]

    # Threshold to consider as match
    if best_score > -1000:  # tweak this depending on lighting/quality
        return best_match_name

    return None

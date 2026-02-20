import cv2
import os
import numpy as np
import face_recognition
import sys


# PyInstaller compatible path
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


EMPLOYEE_IMAGES_DIR = resource_path("storage/employees/images")

known_face_encodings = []
known_face_names = []


def load_known_faces():
    global known_face_encodings, known_face_names

    known_face_encodings = []
    known_face_names = []

    if not os.path.exists(EMPLOYEE_IMAGES_DIR):
        return

    for file in os.listdir(EMPLOYEE_IMAGES_DIR):
        if file.endswith((".jpg", ".png")):
            path = os.path.join(EMPLOYEE_IMAGES_DIR, file)
            image = face_recognition.load_image_file(path)
            encodings = face_recognition.face_encodings(image)

            if len(encodings) > 0:
                known_face_encodings.append(encodings[0])
                known_face_names.append(os.path.splitext(file)[0])
            else:
                print(f"[WARNING] No face found in {file}")

    print(f"[INFO] Loaded {len(known_face_encodings)} employee(s)")


# 🔥 Load once at startup
load_known_faces()


def recognize_employee(frame, tolerance=0.6):
    """
    Recognize employee from a webcam frame.
    Returns employee name or None.
    """

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame, model='hog')
    if len(face_locations) == 0:
        return None

    encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    if len(encodings) == 0:
        return None

    for face_enc in encodings:
        matches = face_recognition.compare_faces(
            known_face_encodings,
            face_enc,
            tolerance=tolerance
        )

        face_distances = face_recognition.face_distance(
            known_face_encodings,
            face_enc
        )

        if len(face_distances) == 0:
            continue

        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            return known_face_names[best_match_index]

    return None
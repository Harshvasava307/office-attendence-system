import cv2
import os
import numpy as np
import face_recognition

# Folder where employee images are stored
EMPLOYEE_IMAGES_DIR = "storage/employees/images"

# Load known faces
known_face_encodings = []
known_face_names = []

for file in os.listdir(EMPLOYEE_IMAGES_DIR):
    if file.endswith((".jpg", ".png")):
        path = os.path.join(EMPLOYEE_IMAGES_DIR, file)
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_face_encodings.append(encodings[0])
            known_face_names.append(os.path.splitext(file)[0])


def recognize_employee(frame):
    """
    Recognize employee from a webcam frame.
    Returns employee name or None.
    """
    # Convert BGR -> RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    if len(face_locations) == 0:
        return None

    # Get encodings
    encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    if len(encodings) == 0:
        return None

    face_enc = encodings[0]

    # Compare with known faces
    matches = face_recognition.compare_faces(known_face_encodings, face_enc)
    face_distances = face_recognition.face_distance(known_face_encodings, face_enc)

    if len(face_distances) == 0:
        return None

    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        return known_face_names[best_match_index]

    return None

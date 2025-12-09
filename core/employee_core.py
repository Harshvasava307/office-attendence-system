import os
import cv2
import face_recognition
import numpy as np

class EmployeeCore:
    def __init__(self):
        self.image_dir = "data/images"
        self.encoding_dir = "data/encodings"

        os.makedirs(self.image_dir, exist_ok=True)
        os.makedirs(self.encoding_dir, exist_ok=True)

    def add_employee(self, name, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_frame)
        if len(face_locations) == 0:
            return False

        # Get encoding
        encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]

        # Save image
        image_path = os.path.join(self.image_dir, f"{name}.jpg")
        cv2.imwrite(image_path, frame)

        # Save encoding as npy file
        encoding_path = os.path.join(self.encoding_dir, f"{name}.npy")
        np.save(encoding_path, encoding)

        return True

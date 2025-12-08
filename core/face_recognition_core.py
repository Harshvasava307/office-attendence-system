import cv2
import numpy as np
import os
from config.config import EMPLOYEE_ENCODINGS_DIR

class FaceRecognitionCore:

    def encode_face(self, image):
        """Return face encoding (dummy placeholder)."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray.flatten()[:128]  # fake 128 dims

    def save_encoding(self, name, encoding):
        path = os.path.join(EMPLOYEE_ENCODINGS_DIR, f"{name}.npy")
        np.save(path, encoding)

    def load_all_encodings(self):
        encodings = {}
        for file in os.listdir(EMPLOYEE_ENCODINGS_DIR):
            if file.endswith(".npy"):
                encodings[file.replace(".npy", "")] = np.load(
                    os.path.join(EMPLOYEE_ENCODINGS_DIR, file)
                )
        return encodings

    def match_face(self, test_encoding, stored_encodings):
        """Dummy matching logic."""
        min_dist = float("inf")
        matched_name = None

        for name, encoding in stored_encodings.items():
            dist = np.linalg.norm(test_encoding - encoding)
            if dist < min_dist:
                min_dist = dist
                matched_name = name

        return matched_name if min_dist < 5000 else None

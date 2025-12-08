import cv2
import os
from config.config import EMPLOYEE_IMAGES_DIR
from core.face_recognition_core import FaceRecognitionCore

class EmployeeCore:
    def __init__(self):
        self.face_core = FaceRecognitionCore()

    def add_employee(self, name, image):
        img_path = os.path.join(EMPLOYEE_IMAGES_DIR, f"{name}.jpg")
        cv2.imwrite(img_path, image)

        encoding = self.face_core.encode_face(image)
        self.face_core.save_encoding(name, encoding)

    def remove_employee(self, name):
        img_path = os.path.join(EMPLOYEE_IMAGES_DIR, f"{name}.jpg")
        enc_path = os.path.join(EMPLOYEE_IMAGES_DIR.replace("images", "encodings"), f"{name}.npy")

        if os.path.exists(img_path):
            os.remove(img_path)
        if os.path.exists(enc_path):
            os.remove(enc_path)

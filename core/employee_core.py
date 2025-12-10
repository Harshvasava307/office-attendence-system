import cv2
import os
import face_recognition

class EmployeeCore:
    def __init__(self):
        # Directory to store employee images
        self.EMPLOYEE_IMAGES_DIR = "storage/employees/images"
        os.makedirs(self.EMPLOYEE_IMAGES_DIR, exist_ok=True)

    def add_employee(self, name, frame):
        """
        Detects a face in the frame and saves it as an image file.
        Returns True if a face is detected and saved, else False.
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame, model='hog')

        if len(face_locations) == 0:
            # No face detected
            return False

        # Get face encoding to ensure a face is present
        encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        if len(encodings) == 0:
            return False

        # Save the first detected face as image
        safe_name = name.replace(" ", "_")
        filename = os.path.join(self.EMPLOYEE_IMAGES_DIR, f"{safe_name}.jpg")
        cv2.imwrite(filename, frame)
        return True

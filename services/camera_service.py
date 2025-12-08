import cv2

class CameraService:

    def get_frame(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        return frame if ret else None

import sys
import cv2
import dlib
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap

# 顔検出と特徴点検出を行うクラス
class FaceDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)
        return faces

    def draw_landmarks(self, frame, faces):
        for face in faces:
            landmarks = self.predictor(frame, face)
            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)
        return frame

class CameraApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebCam Application with Face Detection")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        self.capture = cv2.VideoCapture(0)
        self.face_detector = FaceDetector()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = self.face_detector.detect_faces(frame)
            frame_with_landmarks = self.face_detector.draw_landmarks(frame, faces)
            image = QImage(frame_with_landmarks.data, frame_with_landmarks.shape[1], frame_with_landmarks.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.image_label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.capture.release()
        super().closeEvent(event)
def main():
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

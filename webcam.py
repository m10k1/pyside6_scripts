import sys
import cv2
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap

class CameraApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebCam Application")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        self.capture = cv2.VideoCapture(0)

        ret, frame = self.capture.read()
        if ret:
            self.resize_window(frame)


        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def resize_window(self, frame):
        height, width, _ = frame.shape
        self.setFixedSize(width, height)

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
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

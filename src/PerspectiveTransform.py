import sys
import numpy as np
import cv2
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog)
# from PySide6.QtCore import ()
from PySide6.QtGui import (
    QImage, QPixmap, QAction
)

from ui.UI_MainWindow import Ui_MainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open_file)
    

    def open_file(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'Image files (*.png *.jpg *.bmp)')
        if fname:
            img = read_image_japanese_path(fname)
            # img = cv2.resize(img, (640, 480))
            self.show_image(img)
    
    def show_image(self, img):
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.ui.lblImage.setPixmap(QPixmap.fromImage(qImg))


def read_image_japanese_path(file_path):
    # バイトデータとして画像を読み込み
    with open(file_path, 'rb') as f:
        image_data = np.frombuffer(f.read(), dtype=np.uint8)

    # バイトデータを画像としてデコード
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

    return image
def main():
    app  = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
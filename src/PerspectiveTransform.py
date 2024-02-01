import sys
import numpy as np
import cv2
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog)
# from PySide6.QtCore import ()
from PySide6.QtGui import (
    QImage, QPixmap, QAction, QDoubleValidator, QIntValidator
)

from ui.Ui_MainWindow import Ui_MainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.btnClose.clicked.connect(self.closeWindow)


        self.rotRange = 180
        self.perspectiveRange = 90

        # Slider Event Hander
        self.ui.rotSlider.sliderMoved.connect(self.rotSliderMoved)

        #self.moveXRange=1000
        self.ui.horizntalSlider.sliderMoved.connect(self.horizontalSliderMoved)

        self.ui.verticalSlider.sliderMoved.connect(self.verticalSliderMoved)

        self.perspectiveRange = 90
        self.ui.perspectiveSlider.sliderMoved.connect(self.perspectiveSliderMoved)

        self.outputHeightRange = 5
        self.ui.outputHeightSlider.sliderMoved.connect(self.outputHeightSliderMoved)

        # line edit event handler
        leRotValidator = QDoubleValidator(-self.rotRange, self.rotRange, 3 )
        self.ui.leRot.setValidator(leRotValidator) 
        self.ui.leRot.textEdited.connect(self.leRotEdited)

        leMoveXValidator = QIntValidator(-self.ui.horizntalSlider.maximum(), self.ui.horizntalSlider.maximum())
        self.ui.leMoveX.setValidator(leMoveXValidator)
        self.ui.leMoveX.textEdited.connect(self.leMoveXEdited)

        leMoveYValidator = QIntValidator(-self.ui.verticalSlider.maximum(), self.ui.verticalSlider.maximum())
        self.ui.leMoveY.setValidator(leMoveYValidator)
        self.ui.leMoveY.textEdited.connect(self.leMoveYEdited)
    

        lePerspectiveValidator = QDoubleValidator(-self.perspectiveRange, self.perspectiveRange, 3)
        self.ui.lePerspective.setValidator(lePerspectiveValidator)
        self.ui.lePerspective.textEdited.connect(self.lePerspectiveEdited)

        leOutputHeightValidator = QDoubleValidator(0, self.ui.outputHeightSlider.maximum(), 3)
        self.ui.leOutputHeight.setValidator(leOutputHeightValidator)
        self.ui.leOutputHeight.textEdited.connect(self.leOutputHeightEdited)
    

        self.ui.btnUpdate.pressed.connect(self.update_image)

        self.fname = ""

    def open_file(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'Image files (*.png *.jpg *.bmp)')
        if self.fname:
            img = self.read_image_japanese_path(self.fname)
            self.show_image(img)
    
    def update_image(self):
        img = self.read_image_japanese_path(self.fname)

        # Move
        valX = int(self.ui.leMoveX.text())
        valY = int(self.ui.leMoveY.text())

        trM = np.float32([[1, 0, valX], [0, 1, valY]])
        img = cv2.warpAffine(img, trM, (img.shape[1], img.shape[0]))

        # Rotation
        valRot = float(self.ui.leRot.text())
        rotM = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), valRot, 1)
        img = cv2.warpAffine(img, rotM, (img.shape[1], img.shape[0]))

        # Perspective
        valHeight = float(self.ui.leOutputHeight.text())
        valPerspective = float(self.ui.lePerspective.text())

        w = img.shape[1]
        h = img.shape[0]

        dst_w = w
        dst_h = h * valHeight

        delta_w = np.tan(valPerspective * np.pi / 180) * dst_h
        dst = np.float32([[0, 0], [w + 2 * delta_w, 0], [delta_w, dst_h], [w + delta_w, dst_h]])

        persMat = cv2.getPerspectiveTransform(np.float32([[0, 0], [w, 0], [0, h], [w, h]]),dst)

        img = cv2.warpPerspective(img, persMat, (int(w + 2 * delta_w), int(dst_h)))

        self.show_image(img)

    def show_image(self, img):
        qImg = self.convert_cvimage_to_qimage(img)
        self.ui.lblImage.setPixmap(QPixmap.fromImage(qImg))

    def convert_cvimage_to_qimage(self, cv_image):
        height, width, channel = cv_image.shape
        bytesPerLine = 3 * width
        qImg = QImage(cv_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        return qImg

    def closeWindow(self):
        self.close()

    def rotSliderMoved(self, value):
        val = self.rotRange * value / self.ui.rotSlider.maximum()
        self.ui.leRot.setText(str(val))
        
    def horizontalSliderMoved(self, value):
        val = value
        self.ui.leMoveX.setText(str(val))

    def verticalSliderMoved(self, value):
        val = value
        self.ui.leMoveY.setText(str(val))
        
    def perspectiveSliderMoved(self, value):
        val = self.perspectiveRange * value  / self.ui.perspectiveSlider.maximum()
        self.ui.lePerspective.setText(str(val))

    def outputHeightSliderMoved(self, value):
        val = self.outputHeightRange * value / self.ui.outputHeightSlider.maximum() 
        self.ui.leOutputHeight.setText(str(val))


    # leRot Event Handler
    def leRotEdited(self):
        val = float(self.ui.leRot.text())

        # val が範囲内か確認
        if val < -self.rotRange or val > self.rotRange:
            # val を範囲内にクリップする
            val = np.clip(val, -self.rotRange, self.rotRange)
            self.ui.leRot.setText(str(val))

        self.ui.rotSlider.setValue(int(val * self.ui.rotSlider.maximum() / self.rotRange))

    def leMoveXEdited(self):
        val = float(self.ui.leMoveX.text())
        max_val = self.ui.horizntalSlider.maximum()

        # val が範囲内か確認
        if val < -max_val or val > max_val:
            # val を範囲内にクリップする
            val = np.clip(val, -max_val, max_val)
            self.ui.leMoveX.setText(str(val))

        self.ui.horizntalSlider.setValue(val)

    def leMoveYEdited(self):
        val = float(self.ui.leMoveY.text())
        max_val = self.ui.verticalSlider.maximum()

        # val が範囲内か確認
        if val < -max_val or val > max_val:
            # val を範囲内にクリップする
            val = np.clip(val, -max_val, max_val)
            self.ui.leMoveY.setText(str(val))

        self.ui.verticalSlider.setValue(val)

    def lePerspectiveEdited(self):
        val = float(self.ui.lePerspective.text())

        if val < -self.perspectiveRange or val > self.perspectiveRange:
            val = np.clip(val, -self.perspectiveRange, self.perspectiveRange)
            self.ui.lePerspective.setText(str(val))
        
        self.ui.perspectiveSlider.setValue(int(val * self.ui.perspectiveSlider.maximum() / self.perspectiveRange))

    def leOutputHeightEdited(self):
        val = float(self.ui.leOutputHeight.text())

        if val < 1 or val > self.outputHeightRange:
            val = np.clip(val, 1, self.outputHeightRange)
            self.ui.leOutputHeight.setText(str(val))

        self.ui.outputHeightSlider.setValue(int(self.outputHeightRange * val / self.ui.outputHeightSlider.maximum()))


    def read_image_japanese_path(self, file_path):
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
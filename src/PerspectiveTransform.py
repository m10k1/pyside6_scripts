import sys
import numpy as np
import os
import cv2
from PIL import Image

import json

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox)
from PySide6.QtCore import (Qt)
from PySide6.QtGui import (
    QImage, QKeyEvent, QPixmap, QAction, QDoubleValidator, QIntValidator,
)

from ui.Ui_MainWindow import Ui_MainWindow 
import json

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
    
        IntValidator = QIntValidator()
        self.ui.leTrimTop.setValidator(IntValidator)
        self.ui.leTrimLeft.setValidator(IntValidator)
        self.ui.leTrimBottom.setValidator(IntValidator)
        self.ui.leTrimRight.setValidator(IntValidator)
        

        self.ui.btnUpdate.pressed.connect(self.update_action)

        self.ui.actionBatch_Folder.triggered.connect(self.batchFolder)

        self.fname = ""
        self.scale_factor = 1.0

        self.load_settings()

    def open_file(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'Image files (*.png *.jpg *.bmp)')
        if self.fname:
            img = self.read_image_japanese_path(self.fname)
            self.show_image(img)
    
    def batchFolder(self):
        srcFolderPath = QFileDialog.getExistingDirectory(self, "処理対象のフォルダを選択してください")

        if srcFolderPath:
            print(f"{srcFolderPath}")

            destFolderPath = QFileDialog.getExistingDirectory(self, "保存先のフォルダを選択してください")
            if destFolderPath :
                self.processFolder(srcFolderPath, destFolderPath)
        

    def processFolder(self, srcFolder, destFolder):
        # フォルダの確認
        # 絶対パスに変換して同じパスが設定されていないか確認する

        absSrcFolder = os.path.abspath(srcFolder)
        absDestFolder = os.path.abspath(destFolder)
        if absSrcFolder == destFolder:
            raise ValueError("ソースフォルダと保存先フォルダが同じです")

        for root, dirs, files in os.walk(srcFolder):
            for file in files:

                if file.lower().endswith(('.jpg','*.jpeg')):
                    srcPath = os.path.join(root, file)

                    #保存先のパスを作成
                    relativePath = os.path.relpath(root, srcFolder)
                    destPath = os.path.join(destFolder, relativePath)

                    if not os.path.exists(destPath):
                        os.makedirs(destPath)
                    
                    print(f"destpath: {os.path.join(destPath, file)}")


                    # processImage
                    self.save_image(srcPath, os.path.join(destPath, file))    

                    # save image


    def processImage(self, fname):
        img = self.read_image_japanese_path(fname)

        # Move
        valX = int(self.ui.leMoveX.text())
        valY = int(self.ui.leMoveY.text())
        valRot = float(self.ui.leRot.text())
        valHeight = float(self.ui.leOutputHeight.text())
        valPerspective = float(self.ui.lePerspective.text())

        center = (img.shape[1] / 2, img.shape[0] / 2 )
        rotM = cv2.getRotationMatrix2D(center, valRot, 1)
        rotM[0, 2] += valX
        rotM[1, 2] += valY

        img = cv2.warpAffine(img, rotM, (img.shape[1], img.shape[0]), flags=cv2.INTER_LANCZOS4)

        w = img.shape[1]
        h = img.shape[0]

        dst_h = h * valHeight
        delta_w = np.tan(valPerspective * np.pi / 180) * dst_h

        dest = np.float32([[0, 0], [w + 2 * delta_w, 0], [delta_w, dst_h], [w + delta_w, dst_h]])
        dst = np.float32([[0, 0], [w + 2 * delta_w, 0], [delta_w, dst_h], [w + delta_w, dst_h]])
        src = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

        persMat = cv2.getPerspectiveTransform(src, dst)
        img = cv2.warpPerspective(img, persMat, (int(w + 2 * delta_w), int(dst_h)),flags=cv2.INTER_LANCZOS4)


        flagTrim = self.ui.cbTrimming.isChecked()

        if flagTrim:
            trimTop = int(self.ui.leTrimTop.text())
            trimLeft = int(self.ui.leTrimLeft.text())
            trimBottom = int(self.ui.leTrimBottom.text()) 
            trimRight = int(self.ui.leTrimRight.text())   

            img = img[trimTop:img.shape[0] - trimBottom, trimLeft:img.shape[1] - trimRight]


        flagCopyExif = self.ui.cbCopyExif.isChecked()
        
        if flagCopyExif:
            img = self.copy_exif(img)


        return img

    def copy_exif(self, img):
        return img

    def update_image(self, fname):
        img = self.processImage(fname)
        # 最終的な画像のスケーリングを適用
        img = cv2.resize(img, (int(img.shape[1] * self.scale_factor), int(img.shape[0] * self.scale_factor)))
        self.show_image(img)

    def show_image(self, img):
        qImg = self.convert_cvimage_to_qimage(img)
        self.ui.lblImage.setPixmap(QPixmap.fromImage(qImg))

    def convert_cvimage_to_qimage(self, cv_image):
        height, width, channel = cv_image.shape
        bytesPerLine = 3 * width
        qImg = QImage(cv_image.data, width, height, bytesPerLine, QImage.Format_BGR888)
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

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Plus and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.scale_factor = min(self.scale_factor+ 0.1, 5)
            self.update_image(self.fname)

        elif event.key() == Qt.Key_Minus and event.modifiers() & Qt.KeyboardModifier.ControlModifier:

            self.scale_factor =  max(self.scale_factor-0.1, 0.1)
            self.update_image(self.fname)

        elif event.key() == Qt.Key_S and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            """
            現在表示している画像を保存する
            """
            if self.fname != "":
                save_fname, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'Image files (*.jpg)')

            if save_fname != "":
                self.save_image(self.fname, save_fname)    
                self.update_image(self.fname)
    

    

    def save_image(self, fname, save_fname):

        save_image = self.processImage(fname)
        save_image = self.cv2_to_pil(save_image)
        exif_data = self.get_exif_data(fname)  


        # 保存先のファイル名を選択するダイアログを表示
        if save_fname:
            # ファイルの拡張子に応じて正しいフォーマットを選択
            #ext = os.path.splitext(fname)[1]
            #format = ext[1:].upper()  # 拡張子からピリオドを除去し、大文字に変換

            self.save_image_with_exif(save_fname, save_image, exif_data)

    def cv2_to_pil(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(image)
        return pil_img

    def get_exif_data(self, img_path):
        img = Image.open(img_path)
        exif_data = img.info.get('exif')
        return exif_data

    def save_image_with_exif(self, img_path, transformed_img, exif_data):
        if exif_data:
            #exif_bytes = piexif.dump(exif_data)
            transformed_img.save(img_path, "JPEG", exif=exif_data, quality=80)
        else:
            transformed_img.save(img_path, quality=80)

    def save_settings(self):
        settings = {
            'lineEditMoveX': self.ui.leMoveX.text(),
            'lineEditMoveY': self.ui.leMoveY.text(),
            'lineEditRotate': self.ui.leRot.text(),
            'lineEditPerspective': self.ui.lePerspective.text(),
            'lineEditOutputHeight': self.ui.leOutputHeight.text(),
            'checkBoxTrimming': self.ui.cbTrimming.isChecked(),
            'checkBoxCopyExif': self.ui.cbCopyExif.isChecked(),
            'lineEditTrimTop': self.ui.leTrimTop.text(),
            'lineEditTrimLeft': self.ui.leTrimLeft.text(),
            'lineEditTrimBottom': self.ui.leTrimBottom.text(),
            'lineEditTrimRight': self.ui.leTrimRight.text(),
        }

        with open('settings.json', 'w') as f:
            json.dump(settings, f)
    
    def load_settings(self):
        try:
            with open('settings.json', 'r') as f:
                settings = json.load(f)

                self.ui.leMoveX.setText(settings['lineEditMoveX'])
                self.ui.leMoveY.setText(settings['lineEditMoveY'])
                self.ui.leRot.setText(settings['lineEditRotate'])
                self.ui.lePerspective.setText(settings['lineEditPerspective'])
                self.ui.leOutputHeight.setText(settings['lineEditOutputHeight'])
                self.ui.cbTrimming.setChecked(settings['checkBoxTrimming'])
                self.ui.cbCopyExif.setChecked(settings['checkBoxCopyExif'])
                self.ui.leTrimTop.setText(settings['lineEditTrimTop'])
                self.ui.leTrimLeft.setText(settings['lineEditTrimLeft'])
                self.ui.leTrimBottom.setText(settings['lineEditTrimBottom'])
                self.ui.leTrimRight.setText(settings['lineEditTrimRight'])

                if self.fname != "":  # 画像が開かれている場合のみ設定を適用する
                    self.update_image(self.fname)  # 設定を適用した後に画像を再表示する

        except FileNotFoundError:
            pass
    
    def update_action(self):
        if self.fname != "" :
            self.update_image(self.fname) 

    def closeEvent(self, event):
        self.save_settings()
        super().closeEvent(event)

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
import sys
from PySide6.QtWidgets import QApplication, QMainWindow,  QFileDialog, QColorDialog, QLabel
from PySide6.QtGui import QPainter, QPen, QImage, QColor, QIcon, QAction
from PySide6.QtCore import Qt, QPoint

class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brushSize = 3
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('ファイル')
        brushMenu = mainMenu.addMenu('ブラシ')

        saveAction = QAction(QIcon('save.png'), '保存', self)
        saveAction.setShortcut('Ctrl+S')
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon('clear.png'), 'クリア', self)
        clearAction.setShortcut('Ctrl+C')
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        brushSizeAction = QAction('ブラシサイズ', self)
        brushSizeAction.setShortcut('Ctrl+B')
        brushMenu.addAction(brushSizeAction)
        brushSizeAction.triggered.connect(self.selectBrushSize)

        brushColorAction = QAction('ブラシカラー', self)
        brushColorAction.setShortcut('Ctrl+Shift+C')
        brushMenu.addAction(brushColorAction)
        brushColorAction.triggered.connect(self.selectBrushColor)

        self.statusBar()

        self.setWindowTitle('ペイントアプリ')
        self.setGeometry(100, 100, 800, 600)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() == Qt.MouseButton.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "画像を保存", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def selectBrushSize(self):
        pass  # ここにブラシサイズを選択するコードを追加

    def selectBrushColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.brushColor = color

def main():
    app = QApplication(sys.argv)
    mainWin = PaintApp()
    mainWin.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

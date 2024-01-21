import sys
from PySide6.QtWidgets import (
    QApplication,QMainWindow
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
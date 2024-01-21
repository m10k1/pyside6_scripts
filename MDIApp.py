import sys
from PySide6.QtWidgets import (
    QApplication,QMainWindow, 
    QMdiArea, QMdiSubWindow, QTextEdit
)
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 800, 600)
        self.create_menu()

        self.mid_area = QMdiArea()
        self.setCentralWidget(self.mid_area)


    def create_menu(self):
        menu_bar = self.menuBar()

        # file menu
        file_menu = menu_bar.addMenu("ファイル")

        open_action = QAction("開く", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
    
    def create_sub_window(self):
        sub_window = QMdiSubWindow()
        text_edit = QTextEdit()
        sub_window.setWidget(text_edit)
        sub_window.setWindowTitle("New Document")
        self.mid_area.addSubWindow(sub_window)
        sub_window.show()


    def open_file(self):
        self.create_sub_window()


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
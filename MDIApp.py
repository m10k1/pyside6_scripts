import sys
from PySide6.QtWidgets import (
    QApplication,QMainWindow, 
    QMdiArea, QMdiSubWindow, QTextEdit,
    QFileDialog,
    QLabel
)
from PySide6.QtGui import (
    QAction,
    QPixmap
)

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
    

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "", "Open File", "", "Image Files (*.jpeg, *.jpg, *.bmp, *.gif, *.png)")
        if file_name:
            self.show_image(file_name)

    def show_image(self, file_name):
        # Load Image
        image = QPixmap(file_name)

        # QLabel
        label = QLabel()
        label.setPixmap(image)
    
        sub_window = QMdiSubWindow()
        sub_window.setWidget(label)
        sub_window.setWindowTitle(file_name.split('/')[-1])
        self.mid_area.addSubWindow(sub_window)
        sub_window.show()



def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
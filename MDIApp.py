import sys
from PySide6.QtWidgets import (
    QApplication,QMainWindow, 
    QMdiArea, QMdiSubWindow, QTextEdit,
    QFileDialog,
    QLabel,
    QScrollArea
)
from PySide6.QtGui import (
    QAction,
    QPixmap,
    QColorConstants, QColor,
    QPalette
)
class ImageSubWindow(QMdiSubWindow):
    def __init__(self, file_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle(file_name.split('/')[-1])  # ファイル名をウィンドウタイトルに設定
        
        self.image_label = QLabel()  # 画像を表示するためのラベル
        self.image_label.setPixmap(QPixmap(file_name))
        self.image_label.setScaledContents(False)  # 画像のサイズをラベルのサイズに合わせる

        self.scroll_area = QScrollArea()  # スクロールエリアを作成
        self.scroll_area.setWidget(self.image_label)  # ラベルをスクロールエリアに設定
        #self.scroll_area.setBackgroundRole(QPalette.ColorRole.Window)  # 背景色を白に設定
        
        palette = self.scroll_area.palette()
        palette.setColor( QPalette.ColorRole.Window, QColorConstants.White)
        self.scroll_area.setPalette(palette)

        self.setWidget(self.scroll_area)  # スクロールエリアをサブウィンドウのメインウィジェットとして設定

        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 800, 600)

        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)
        self.create_menu()


    def create_menu(self):
        menu_bar = self.menuBar()

        # file menu
        file_menu = menu_bar.addMenu("ファイル")

        open_action = QAction("開く", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
    
            # 表示メニュー
        view_menu = menu_bar.addMenu("表示")

        # 整列サブメニュー
        arrange_menu = view_menu.addMenu("整列")

        # タイル表示アクション
        tile_action = QAction("タイル表示", self)
        tile_action.triggered.connect(self.mdi_area.tileSubWindows)
        arrange_menu.addAction(tile_action)

        # カスケード表示アクション
        cascade_action = QAction("カスケード表示", self)
        cascade_action.triggered.connect(self.mdi_area.cascadeSubWindows)
        arrange_menu.addAction(cascade_action)
    

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Images (*jpeg *.jpg *.bmp *.gif *.png)")
        if file_name:
            self.show_image(file_name)

    def show_image(self, file_name):
        # Load Image
        image = QPixmap(file_name)

        # QLabel
        sub_window = ImageSubWindow(file_name, self)
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()



    

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Images (*jpeg *.jpg *.bmp *.gif *.png)")
        if file_name:
            self.show_image(file_name)

    def show_image(self, file_name):
        # Load Image
        image = QPixmap(file_name)

        # QLabel
        sub_window = ImageSubWindow(file_name, self)
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()



def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
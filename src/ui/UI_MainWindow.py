# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1890, 1193)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionBatch_Folder = QAction(MainWindow)
        self.actionBatch_Folder.setObjectName(u"actionBatch_Folder")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.rotSlider = QSlider(self.centralwidget)
        self.rotSlider.setObjectName(u"rotSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotSlider.sizePolicy().hasHeightForWidth())
        self.rotSlider.setSizePolicy(sizePolicy)
        self.rotSlider.setMinimum(-1000)
        self.rotSlider.setMaximum(1000)
        self.rotSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.rotSlider, 1, 0, 1, 3)

        self.lePerspective = QLineEdit(self.centralwidget)
        self.lePerspective.setObjectName(u"lePerspective")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lePerspective.sizePolicy().hasHeightForWidth())
        self.lePerspective.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lePerspective, 10, 3, 1, 1)

        self.outputHeightSlider = QSlider(self.centralwidget)
        self.outputHeightSlider.setObjectName(u"outputHeightSlider")
        self.outputHeightSlider.setMinimum(1)
        self.outputHeightSlider.setMaximum(1000)
        self.outputHeightSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.outputHeightSlider, 8, 0, 1, 3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 4)

        self.leTrimLeft = QLineEdit(self.centralwidget)
        self.leTrimLeft.setObjectName(u"leTrimLeft")
        sizePolicy1.setHeightForWidth(self.leTrimLeft.sizePolicy().hasHeightForWidth())
        self.leTrimLeft.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.leTrimLeft, 12, 3, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 12, 0, 1, 1)

        self.leTrimTop = QLineEdit(self.centralwidget)
        self.leTrimTop.setObjectName(u"leTrimTop")
        sizePolicy1.setHeightForWidth(self.leTrimTop.sizePolicy().hasHeightForWidth())
        self.leTrimTop.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.leTrimTop, 12, 1, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)

        self.leOutputHeight = QLineEdit(self.centralwidget)
        self.leOutputHeight.setObjectName(u"leOutputHeight")
        sizePolicy1.setHeightForWidth(self.leOutputHeight.sizePolicy().hasHeightForWidth())
        self.leOutputHeight.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.leOutputHeight, 8, 3, 1, 1)

        self.leTrimRight = QLineEdit(self.centralwidget)
        self.leTrimRight.setObjectName(u"leTrimRight")
        sizePolicy1.setHeightForWidth(self.leTrimRight.sizePolicy().hasHeightForWidth())
        self.leTrimRight.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.leTrimRight, 13, 3, 1, 1)

        self.horizntalSlider = QSlider(self.centralwidget)
        self.horizntalSlider.setObjectName(u"horizntalSlider")
        self.horizntalSlider.setMinimum(-1000)
        self.horizntalSlider.setMaximum(1000)
        self.horizntalSlider.setPageStep(9)
        self.horizntalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizntalSlider, 4, 0, 1, 3)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 13, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 18, 0, 1, 1)

        self.leTrimBottom = QLineEdit(self.centralwidget)
        self.leTrimBottom.setObjectName(u"leTrimBottom")
        sizePolicy1.setHeightForWidth(self.leTrimBottom.sizePolicy().hasHeightForWidth())
        self.leTrimBottom.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.leTrimBottom, 13, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 4)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 4)

        self.btnRest = QPushButton(self.centralwidget)
        self.btnRest.setObjectName(u"btnRest")

        self.gridLayout.addWidget(self.btnRest, 17, 3, 1, 1)

        self.perspectiveSlider = QSlider(self.centralwidget)
        self.perspectiveSlider.setObjectName(u"perspectiveSlider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.perspectiveSlider.sizePolicy().hasHeightForWidth())
        self.perspectiveSlider.setSizePolicy(sizePolicy2)
        self.perspectiveSlider.setMinimum(-1000)
        self.perspectiveSlider.setMaximum(1000)
        self.perspectiveSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.perspectiveSlider, 10, 0, 1, 3)

        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMinimum(-1000)
        self.verticalSlider.setMaximum(1000)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.verticalSlider, 6, 0, 1, 3)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 1)

        self.leMoveY = QLineEdit(self.centralwidget)
        self.leMoveY.setObjectName(u"leMoveY")
        sizePolicy1.setHeightForWidth(self.leMoveY.sizePolicy().hasHeightForWidth())
        self.leMoveY.setSizePolicy(sizePolicy1)
        self.leMoveY.setMinimumSize(QSize(15, 0))

        self.gridLayout.addWidget(self.leMoveY, 6, 3, 1, 1)

        self.leMoveX = QLineEdit(self.centralwidget)
        self.leMoveX.setObjectName(u"leMoveX")
        sizePolicy1.setHeightForWidth(self.leMoveX.sizePolicy().hasHeightForWidth())
        self.leMoveX.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.leMoveX, 4, 3, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 12, 2, 1, 1)

        self.leRot = QLineEdit(self.centralwidget)
        self.leRot.setObjectName(u"leRot")
        sizePolicy1.setHeightForWidth(self.leRot.sizePolicy().hasHeightForWidth())
        self.leRot.setSizePolicy(sizePolicy1)
        self.leRot.setMinimumSize(QSize(15, 0))

        self.gridLayout.addWidget(self.leRot, 1, 3, 1, 1)

        self.btnUpdate = QPushButton(self.centralwidget)
        self.btnUpdate.setObjectName(u"btnUpdate")

        self.gridLayout.addWidget(self.btnUpdate, 17, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 7, 0, 1, 4)

        self.cbTrimming = QCheckBox(self.centralwidget)
        self.cbTrimming.setObjectName(u"cbTrimming")
        self.cbTrimming.setChecked(True)

        self.gridLayout.addWidget(self.cbTrimming, 11, 3, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 16, 0, 1, 1)

        self.cbCopyExif = QCheckBox(self.centralwidget)
        self.cbCopyExif.setObjectName(u"cbCopyExif")
        self.cbCopyExif.setChecked(True)

        self.gridLayout.addWidget(self.cbCopyExif, 16, 3, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.lblImage = QLabel(self.centralwidget)
        self.lblImage.setObjectName(u"lblImage")
        self.lblImage.setMinimumSize(QSize(1440, 1080))

        self.horizontalLayout_2.addWidget(self.lblImage)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(self.centralwidget)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1890, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menu.addAction(self.actionBatch_Folder)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionBatch_Folder.setText(QCoreApplication.translate("MainWindow", u"Process Folder", None))
        self.lePerspective.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u3042\u304a\u308a\u88dc\u6b63", None))
        self.leTrimLeft.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Top", None))
        self.leTrimTop.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Bottom", None))
        self.leOutputHeight.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.leTrimRight.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u56de\u8ee2", None))
        self.leTrimBottom.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u52d5\uff08X\uff09", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u52d5\uff08Y)", None))
        self.btnRest.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u30c8\u30ea\u30df\u30f3\u30b0", None))
        self.leMoveY.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.leMoveX.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.leRot.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u529b\u753b\u50cf\u9ad8\u3055\u30b9\u30b1\u30fc\u30eb", None))
        self.cbTrimming.setText(QCoreApplication.translate("MainWindow", u"Trimming", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Copy Exif", None))
        self.cbCopyExif.setText(QCoreApplication.translate("MainWindow", u"Copy Exif", None))
        self.lblImage.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u30d0\u30c3\u30c1\u51e6\u7406", None))
    # retranslateUi


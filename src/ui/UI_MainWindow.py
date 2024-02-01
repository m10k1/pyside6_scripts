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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1890, 1193)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
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
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 9, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 12, 0, 1, 1)

        self.leMoveX = QLineEdit(self.centralwidget)
        self.leMoveX.setObjectName(u"leMoveX")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leMoveX.sizePolicy().hasHeightForWidth())
        self.leMoveX.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.leMoveX, 4, 3, 1, 1)

        self.leRot = QLineEdit(self.centralwidget)
        self.leRot.setObjectName(u"leRot")
        sizePolicy.setHeightForWidth(self.leRot.sizePolicy().hasHeightForWidth())
        self.leRot.setSizePolicy(sizePolicy)
        self.leRot.setMinimumSize(QSize(15, 0))

        self.gridLayout.addWidget(self.leRot, 1, 3, 1, 1)

        self.leMoveY = QLineEdit(self.centralwidget)
        self.leMoveY.setObjectName(u"leMoveY")
        sizePolicy.setHeightForWidth(self.leMoveY.sizePolicy().hasHeightForWidth())
        self.leMoveY.setSizePolicy(sizePolicy)
        self.leMoveY.setMinimumSize(QSize(15, 0))

        self.gridLayout.addWidget(self.leMoveY, 6, 3, 1, 1)

        self.lePerspective = QLineEdit(self.centralwidget)
        self.lePerspective.setObjectName(u"lePerspective")
        sizePolicy.setHeightForWidth(self.lePerspective.sizePolicy().hasHeightForWidth())
        self.lePerspective.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lePerspective, 8, 3, 1, 1)

        self.perspectiveSlider = QSlider(self.centralwidget)
        self.perspectiveSlider.setObjectName(u"perspectiveSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.perspectiveSlider.sizePolicy().hasHeightForWidth())
        self.perspectiveSlider.setSizePolicy(sizePolicy1)
        self.perspectiveSlider.setMinimum(-1000)
        self.perspectiveSlider.setMaximum(1000)
        self.perspectiveSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.perspectiveSlider, 8, 0, 1, 3)

        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMinimum(-1000)
        self.verticalSlider.setMaximum(1000)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.verticalSlider, 6, 0, 1, 3)

        self.horizntalSlider = QSlider(self.centralwidget)
        self.horizntalSlider.setObjectName(u"horizntalSlider")
        self.horizntalSlider.setMinimum(-1000)
        self.horizntalSlider.setMaximum(1000)
        self.horizntalSlider.setPageStep(9)
        self.horizntalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizntalSlider, 4, 0, 1, 3)

        self.rotSlider = QSlider(self.centralwidget)
        self.rotSlider.setObjectName(u"rotSlider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rotSlider.sizePolicy().hasHeightForWidth())
        self.rotSlider.setSizePolicy(sizePolicy2)
        self.rotSlider.setMinimum(-1000)
        self.rotSlider.setMaximum(1000)
        self.rotSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.rotSlider, 1, 0, 1, 3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 4)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 4)

        self.btnUpdate = QPushButton(self.centralwidget)
        self.btnUpdate.setObjectName(u"btnUpdate")

        self.gridLayout.addWidget(self.btnUpdate, 9, 1, 1, 1)

        self.btnRest = QPushButton(self.centralwidget)
        self.btnRest.setObjectName(u"btnRest")

        self.gridLayout.addWidget(self.btnRest, 9, 3, 1, 1)


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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.leMoveX.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.leRot.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.leMoveY.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lePerspective.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u3042\u304a\u308a\u88dc\u6b63", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u52d5\uff08Y)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u52d5\uff08X\uff09", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u56de\u8ee2", None))
        self.btnUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btnRest.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.lblImage.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi


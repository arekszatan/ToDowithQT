# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.entryPage = QWidget()
        self.entryPage.setObjectName(u"entryPage")
        self.entryPage.setAutoFillBackground(True)
        self.entryPage.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.entryPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.entryPage)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.startButton = QPushButton(self.entryPage)
        self.startButton.setObjectName(u"startButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.startButton, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.entryPage)
        self.mainToDo = QWidget()
        self.mainToDo.setObjectName(u"mainToDo")
        self.gridLayout_2 = QGridLayout(self.mainToDo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.addButton = QPushButton(self.mainToDo)
        self.addButton.setObjectName(u"addButton")

        self.gridLayout_2.addWidget(self.addButton, 0, 0, 1, 1)

        self.removeButton = QPushButton(self.mainToDo)
        self.removeButton.setObjectName(u"removeButton")

        self.gridLayout_2.addWidget(self.removeButton, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.mainToDo)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"image", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"dodaj", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"usun", None))
    # retranslateUi


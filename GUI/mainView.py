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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet(u"QLabel{\n"
"	\n"
"}\n"
"\n"
"QWidget{\n"
"background-color:#555;\n"
"color:white;\n"
"font-size:20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#121212;\n"
"padding:10px;\n"
"border:solid;\n"
"border-radius: 2px;\n"
"border-color:#555555;\n"
"}")
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
        self.entryPage.setAutoFillBackground(False)
        self.entryPage.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.entryPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.image = QLabel(self.entryPage)
        self.image.setObjectName(u"image")
        self.image.setScaledContents(True)
        self.image.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.image, 0, 0, 1, 1)

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
        self.scrollArea = QScrollArea(self.mainToDo)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1180, 664))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.toDoWidget = QWidget(self.scrollAreaWidgetContents)
        self.toDoWidget.setObjectName(u"toDoWidget")
        self.gridLayout_4 = QGridLayout(self.toDoWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.gridLayout_3.addWidget(self.toDoWidget, 0, 0, 1, 1)

        self.spacerWidget = QWidget(self.scrollAreaWidgetContents)
        self.spacerWidget.setObjectName(u"spacerWidget")
        self.verticalLayout_2 = QVBoxLayout(self.spacerWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 601, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_3.addWidget(self.spacerWidget, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 2)

        self.addButton = QPushButton(self.mainToDo)
        self.addButton.setObjectName(u"addButton")

        self.gridLayout_2.addWidget(self.addButton, 3, 0, 1, 2)

        self.newToDoLineEdit = QLineEdit(self.mainToDo)
        self.newToDoLineEdit.setObjectName(u"newToDoLineEdit")

        self.gridLayout_2.addWidget(self.newToDoLineEdit, 2, 0, 1, 2)

        self.toDoName = QLabel(self.mainToDo)
        self.toDoName.setObjectName(u"toDoName")
        sizePolicy.setHeightForWidth(self.toDoName.sizePolicy().hasHeightForWidth())
        self.toDoName.setSizePolicy(sizePolicy)
        self.toDoName.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.toDoName, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.mainToDo)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image.setText("")
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.toDoName.setText(QCoreApplication.translate("MainWindow", u"-", None))
    # retranslateUi


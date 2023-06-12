from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton
from GUI.mainView import Ui_MainWindow
import qasync
import sys
import logging as log


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ToDo application")
        self.stackedWidget.setCurrentIndex(0)
        self.startButton.clicked.connect(self.start_button_clicked)
        self.addButton.clicked.connect(self.add_button_clicked)

    def start_button_clicked(self):
        log.info("Button start_button_clicked was clicked")
        self.stackedWidget.setCurrentIndex(1)

    def add_button_clicked(self):
        log.info("Button add_button_clicked was clicked")


def start_application():  # Start Application with qasync
    app = QtWidgets.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    window = MainWindow()
    window.show()
    log.info("Start front to application")
    with loop:
        loop.run_forever()

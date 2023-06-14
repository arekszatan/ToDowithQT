from PySide6 import QtWidgets
from PySide6.QtWidgets import (QPushButton, QLabel, QCheckBox, QSpacerItem, QSizePolicy, QWidget, QGridLayout)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt, Signal, QObject, Slot
from GUI.mainView import Ui_MainWindow
import qasync
import sys
import logging as log
import json


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ToDo application")
        self.stackedWidget.setCurrentIndex(0)
        self.image.setText("<img src='GUI/img/zdjecieToDo.jpg' height='700' width='1000'/>")
        self.startButton.clicked.connect(self.start_button_clicked)
        self.addButton.clicked.connect(self.add_button_clicked)
        self.id_num = 0
        self.data = {}
        self.open_json_file()

    def open_json_file(self):
        try:
            f = open("data.json", "r", encoding="utf-8")
            self.data = json.load(f)
            f.close()
        except FileNotFoundError:
            log.exception("Cant open data file")
            return
        self.toDoName.setText(self.data["name"])
        for i in self.data['toDoList']:
            self.id_num = int(i['id'])
            item = ToDoItemsWidgets(self.id_num, i['toDo'], i['isChecked'])
            self.gridLayout_4.addWidget(item)

    def change_json_file(self, new_data, filename='data.json'):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data["toDoList"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
        self.data = file_data

    def start_button_clicked(self):
        log.info("Button start_button_clicked was clicked")
        self.stackedWidget.setCurrentIndex(1)

    def add_button_clicked(self):
        log.info("Button add_button_clicked was clicked")
        new_text = self.newToDoLineEdit.text()
        if not new_text:
            return
        self.id_num += 1
        item = ToDoItemsWidgets(self.id_num, new_text)
        self.gridLayout_4.addWidget(item)
        new_to_do = {"id": str(self.id_num),
                     "toDo": new_text,
                     "isChecked": str(0)
                     }
        self.change_json_file(new_to_do)
        self.newToDoLineEdit.clear()


def start_application():  # Start Application with qasync
    app = QtWidgets.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    window = MainWindow()
    window.show()
    log.info("Start front to application")
    with loop:
        loop.run_forever()


class ToDoItemsWidgets(QWidget, QObject):

    def __init__(self, id_int=0, new_text="", is_checked=0, parent=None):
        super(ToDoItemsWidgets, self).__init__(parent)
        log.info(f'Object QWidget was creating with id {str(id_int)}')
        self.i = id_int
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        title = QLabel(str(self.i))
        title.setFixedWidth(60)
        title.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(title, 0, 0)
        self.text_to_do = QLabel(new_text)
        self.main_layout.addWidget(self.text_to_do, 0, 1)
        check_box = QCheckBox("Gotowe")
        check_box.clicked.connect(self.check_box_checked)
        check_box.setFixedWidth(100)
        check_box.setChecked(True) if is_checked == "1" else check_box.setChecked(False)
        self.setStyleSheet("QLabel{color:gray}") if is_checked == "1" else self.setStyleSheet("QLabel{color:white}")
        self.main_layout.addWidget(check_box, 0, 2)
        close_button = QPushButton("Usuń")
        close_button.setFixedWidth(100)
        close_button.clicked.connect(self._close_widget)
        self.main_layout.addWidget(close_button, 0, 3)

    def _close_widget(self):
        log.info(f'Object QWidget was deleting with id {str(self.i)}')
        self.remove_item(self.i)
        self.deleteLater()

    def check_box_checked(self, is_checked):
        log.info(f'QCheckBox was clicked with id {str(self.i)}')

        if is_checked:
            self.setStyleSheet("QLabel{color:gray}")
            self.update_check_state(self.i, is_checked=str(1))
        else:
            self.update_check_state(self.i, is_checked=str(0))
            self.setStyleSheet("QLabel{color:white}")

    def remove_item(self, index, filename='data.json'):
        with open(filename, 'r') as file:
            file_data = json.load(file)
            for idx, obj in enumerate(file_data["toDoList"]):
                if int(obj['id']) == index:
                    file_data["toDoList"].pop(idx)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(file_data, indent=2))

    def update_check_state(self, index, filename='data.json', is_checked=str(0)):
        with open(filename, 'r') as file:
            file_data = json.load(file)
            for idx, obj in enumerate(file_data["toDoList"]):
                if int(obj['id']) == index:
                    file_data["toDoList"].pop(idx)
                    text = {"id": index,
                            "toDo": self.text_to_do.text(),
                            "isChecked": is_checked
                            }
                    file_data["toDoList"].insert(idx, text)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(file_data, indent=2))

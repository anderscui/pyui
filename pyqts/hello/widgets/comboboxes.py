# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        items = {'one': 1, 'two': 2, 'three': 3}
        box = QComboBox()
        box.addItems(tuple(f'{k}: {v}' for k, v in items.items()))

        box.setEditable(True)
        box.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        box.setMaxCount(5)

        box.currentIndexChanged.connect(self.index_changed)
        box.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(box)

    def index_changed(self, i):
        # i is an int
        print(f'index: {i}')

    def text_changed(self, text):
        # txt is a str
        print(f'text: {text}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

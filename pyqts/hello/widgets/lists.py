# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        items = {'one': 1, 'two': 2, 'three': 3}
        box = QListWidget()
        box.addItems(tuple(f'{k}: {v}' for k, v in items.items()))

        box.currentItemChanged.connect(self.item_changed)
        box.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(box)

    def item_changed(self, i: QListWidgetItem):
        print(f'item: {i.text()}, {i}')

    def text_changed(self, text):
        # txt is a str
        print(f'text: {text}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

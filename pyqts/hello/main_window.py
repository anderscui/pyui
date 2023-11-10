# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        # always add this call.
        super().__init__()

        self.setWindowTitle('My app')

        # self.setFixedSize(QSize(500, 300))
        self.setMinimumSize(QSize(300, 300))
        self.setMaximumSize(QSize(600, 600))

        button = QPushButton('Press me!')
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

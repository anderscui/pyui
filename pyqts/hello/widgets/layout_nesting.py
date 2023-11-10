# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel

from pyqts.hello.widgets.color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        layout1 = QHBoxLayout()

        layout1_1 = QVBoxLayout()
        layout1_1.addWidget(Color('red'))
        layout1_1.addWidget(Color('green'))
        layout1_1.addWidget(Color('blue'))

        layout1_2 = QVBoxLayout()
        layout1_2.addWidget(Color('green'))
        # layout1_2.addWidget(Color('red'))
        layout1_2.addWidget(Color('purple'))

        layout1.addLayout(layout1_1)
        layout1.addWidget(Color('green'))
        layout1.addLayout(layout1_2)

        layout1.setContentsMargins(1, 1, 1, 1)
        layout1.setSpacing(5)

        container = QWidget()
        container.setLayout(layout1)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

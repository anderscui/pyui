# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        label = QLabel('Hello')
        # widget's default font
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)

        label.setPixmap(QPixmap('../resources/chatgpt.png'))
        # stretch and scale to fit the window
        label.setScaledContents(True)

        self.setCentralWidget(label)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

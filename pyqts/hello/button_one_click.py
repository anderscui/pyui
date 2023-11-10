# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        # self.setFixedSize(QSize(500, 300))
        self.setMinimumSize(QSize(300, 300))
        self.setMaximumSize(QSize(600, 600))

        button = QPushButton('Press me!')
        button.clicked.connect(self.button_clicked)

        self.button = button
        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.button.setText('You already clicked me.')
        self.button.setEnabled(False)

        self.setWindowTitle('My Oneshot app')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

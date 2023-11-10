# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        # always add this call.
        super().__init__()

        # states
        self.button_is_checked = True

        self.setWindowTitle('My app')

        # self.setFixedSize(QSize(500, 300))
        self.setMinimumSize(QSize(300, 300))
        self.setMaximumSize(QSize(600, 600))

        button = QPushButton('Press me!')
        button.setCheckable(True)
        button.setChecked(self.button_is_checked)

        button.clicked.connect(self.button_clicked)
        button.clicked.connect(self.button_toggled)
        button.released.connect(self.button_released)

        self.button = button
        self.setCentralWidget(self.button)

    def button_clicked(self):
        print('clicked!')

    def button_toggled(self, checked):
        self.button_is_checked = checked
        print(f'checked? {self.button_is_checked}')

    def button_released(self):
        self.button_is_checked = self.button.isChecked()
        print(f'checked(released) ? {self.button_is_checked}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

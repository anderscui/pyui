# coding=utf-8
import sys
from random import randint

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QStyle


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel(f'Another window {randint(0, 100)}')
        layout.addWidget(self.label)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        self.w = None

        self.button = QPushButton('Push me')
        style = self.button.style()
        icon = style.standardIcon(QStyle.StandardPixmap.SP_MessageBoxCritical)
        self.button.setIcon(icon)

        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

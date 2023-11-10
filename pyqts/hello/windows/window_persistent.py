# coding=utf-8
import sys
from random import randint

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit


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

        self.w = AnotherWindow()

        self.button = QPushButton('Toggle window')
        self.button.clicked.connect(self.show_new_window)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.w.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.input)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def show_new_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

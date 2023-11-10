# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        label = QLabel()
        input = QLineEdit()
        input.setMaxLength(5)
        input.setPlaceholderText('your name:')
        # input.setReadOnly(True)
        # input.setInputMask('000.000;_')

        input.textChanged.connect(label.setText)
        input.textChanged.connect(self.text_changed)
        input.textEdited.connect(self.text_edited)
        input.returnPressed.connect(self.return_pressed)
        input.selectionChanged.connect(self.selection_changed)

        self.label = label
        self.input = input

        layout = QVBoxLayout()
        layout.addWidget(input)
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def return_pressed(self):
        print('return pressed')
        self.input.setText('OK?')

    def selection_changed(self):
        print('selection changed')
        self.label.setText(self.input.selectedText())

    def text_changed(self, s):
        print(f'changed to {s}')

    def text_edited(self, s):
        print(f'edited to {s}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        box = QSpinBox()
        # box.setMinimum(-1)
        # box.setMaximum(1)
        box.setRange(0, 6)
        box.setPrefix('$')
        # box.setSuffix('c')
        box.setSingleStep(2)
        box.valueChanged.connect(self.value_changed)
        box.textChanged.connect(self.text_changed)

        box2 = QDoubleSpinBox()
        box2.setRange(-1, 5)
        box2.valueChanged.connect(self.value_changed2)
        box2.textChanged.connect(self.text_changed)

        layout = QVBoxLayout()
        layout.addWidget(box)
        layout.addWidget(box2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def value_changed(self, i):
        # value is an int
        print(f'value: {i}')

    def text_changed(self, text):
        # txt is a str
        print(f'text: {text}')

    def value_changed2(self, i):
        # value is an float
        print(f'value: {i}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

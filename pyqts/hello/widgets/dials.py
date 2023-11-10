# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QDial, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        label = QLabel('Dial')
        dial = QDial()
        dial.setRange(0, 10)
        dial.setSingleStep(1)

        dial.valueChanged.connect(self.value_changed)
        dial.sliderMoved.connect(self.slider_moved)
        dial.sliderPressed.connect(self.slider_pressed)
        dial.sliderReleased.connect(self.slider_released)

        self.label = label
        self.dial = dial

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(dial)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def value_changed(self, val: int):
        print(f'value changed: {type(val)} {val}')
        self.label.setText(str(val))

    def slider_moved(self, pos: int):
        print(f'position: {type(pos)}, {pos}')

    def slider_pressed(self):
        print(f'pressed')

    def slider_released(self):
        print(f'released')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

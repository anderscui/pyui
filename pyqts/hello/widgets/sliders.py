# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        label = QLabel('Slider')
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(0, 10)

        slider.valueChanged.connect(self.value_changed)
        slider.sliderMoved.connect(self.slider_moved)
        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)

        self.label = label
        self.slider = slider

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(slider)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def value_changed(self, val: int):
        print(f'value changed: {val}')
        self.label.setText(str(val))

    def slider_moved(self, pos: int):
        print(f'position: {pos}')

    def slider_pressed(self):
        print(f'pressed')

    def slider_released(self):
        print(f'released')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

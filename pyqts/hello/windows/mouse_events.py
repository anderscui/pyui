# coding=utf-8
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QTextEdit, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        # TODO: doesn't work?
        # self.setMouseTracking(True)

        self.label = QLabel('Click here')
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e: QMouseEvent):
        self.label.setText('mouseMoveEvent')

    def mousePressEvent(self, e: QMouseEvent):
        self.label.setText('mousePressEvent')
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText('left')
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('middle')
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText('right')

    def mouseReleaseEvent(self, e: QMouseEvent):
        self.label.setText('mouseReleaseEvent')

    def mouseDoubleClickEvent(self, e: QMouseEvent):
        self.label.setText('mouseDoubleClickEvent')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

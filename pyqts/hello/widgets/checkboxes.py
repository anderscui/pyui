# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        box = QCheckBox('Hello')

        # box.setCheckState(Qt.CheckState.Checked)
        box.setTristate(True)
        box.setCheckState(Qt.CheckState.PartiallyChecked)

        box.stateChanged.connect(self.show_state)
        self.setCentralWidget(box)

    def show_state(self, s):
        # s is an int
        # 0: Unchecked, 1: PartiallyChecked, 2: Checked
        print(Qt.CheckState(s) == Qt.CheckState.Checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

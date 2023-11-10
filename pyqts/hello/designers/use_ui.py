# coding=utf-8
import random
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication

from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.show()

        f = self.label.font()
        f.setPointSize(25)
        self.label.setFont(f)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pushButton.pressed.connect(self.update_label)

    def update_label(self):
        n = random.randint(1, 6)
        self.label.setText(f'{n}')


app = QApplication(sys.argv)

window = MainWindow()
# window.show()

app.exec()

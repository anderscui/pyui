# coding=utf-8
import sys

from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)
palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, QColor(0, 128, 128))
palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
app.setPalette(palette)

w = QLabel('Palette text')
w.show()

app.exec()

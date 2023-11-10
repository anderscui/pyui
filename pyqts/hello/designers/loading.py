# coding=utf-8
import os
import sys

from PyQt6 import QtWidgets, uic


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi(os.path.expanduser('~/github/qt_designer/mainwindow.ui'))
window.show()
app.exec()

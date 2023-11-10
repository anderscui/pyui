# coding=utf-8
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow

# you need one and only one app instance per app.
# you can pass [] when you are sure no args are needed.
# an app object holds the event loop (only one per app) of your app,
app = QApplication(sys.argv)

# in qt, all top widgets are windows
# window = QWidget()
# use a pre-made window
window = QMainWindow()
# windows are hidden by default
window.show()

# start the event loop
app.exec()

# coding=utf-8
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent, QAction, QContextMenuEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QTextEdit, QWidget, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        self.label = QLabel('Click here')

        # alternative
        # self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.on_context_menu)

        self.setCentralWidget(self.label)

    def contextMenuEvent(self, e: QContextMenuEvent):
        print(f'{type(e)}, e')
        context = QMenu(self)
        context.addAction(QAction('action 1', self))
        context.addAction(QAction('action 2', self))
        context.addAction(QAction('action 3', self))
        context.exec(e.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

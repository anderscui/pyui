# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget, QLabel, QStatusBar, QCheckBox

from pyqts.hello.widgets.color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        label = QLabel('Tools')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        toolbar = QToolBar('main')
        toolbar.setIconSize(QSize(16, 16))
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(toolbar)

        # self as the parent QObject
        button_action = QAction(QIcon('../resources/guitar.png'), 'Guitar', self)
        button_action.setStatusTip('My guitar')
        button_action.setCheckable(True)
        button_action.triggered.connect(self.toolbar_clicked)
        button_action.setShortcut(QKeySequence('Ctrl+g'))
        toolbar.addAction(button_action)

        toolbar.addSeparator()
        button_action2 = QAction(QIcon('../resources/fruit.png'), 'Fruit', self)
        button_action2.setStatusTip('My fruit')
        button_action2.setCheckable(True)
        button_action2.triggered.connect(self.toolbar_clicked)
        button_action2.setShortcut(QKeySequence('Ctrl+f'))
        toolbar.addAction(button_action2)

        # and you can add any widget
        toolbar.addSeparator()
        toolbar.addWidget(QLabel('Tool'))
        toolbar.addSeparator()
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        # add menu
        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

        file_submenu = file_menu.addMenu('Sub')
        file_submenu.addAction(button_action2)

        self.setCentralWidget(label)

    def toolbar_clicked(self, s: bool):
        # s: is checked?
        print(f'toolbar_clicked: {type(s)}, {s}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

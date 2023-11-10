# coding=utf-8
import sys
import random

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
    'My App',
    'Still My App',
    'What on earth',
    'This is surprising',
    'Something went wrong',
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # states
        self.n_times_clicked = 0

        self.setWindowTitle(random.choice(window_titles))

        button = QPushButton('Press me!')
        button.clicked.connect(self.button_clicked)

        self.button = button
        self.setCentralWidget(self.button)

        self.windowTitleChanged.connect(self.window_title_changed)

    def button_clicked(self):
        print('Clicked')
        new_title = random.choice(window_titles)
        print(f'set title to: {new_title}')
        self.setWindowTitle(new_title)

    def window_title_changed(self, window_title):
        print(f'title changed to: {window_title}')
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# coding=utf-8
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        button = QPushButton('Press me for a dialog')
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self, s):
        print(f'click {type(s)}: {s}')

        # dlg = QMessageBox(self)
        # dlg.setWindowTitle('A question...')
        # dlg.setText('Here is a simple dialog.')
        # dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        # dlg.setIcon(QMessageBox.Icon.Question)
        # button = dlg.exec()
        # button = QMessageBox.StandardButton(button)

        button = QMessageBox.question(self, 'A question', 'simple dialog...')
        if button == QMessageBox.StandardButton.Ok:
            print('OK...')
        elif button == QMessageBox.StandardButton.Yes:
            print('Yes...')
        elif button == QMessageBox.StandardButton.No:
            print('No...')
        else:
            print('What are you doing now?')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

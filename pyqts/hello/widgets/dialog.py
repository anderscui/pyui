# coding=utf-8
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QVBoxLayout, QLabel


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Simple Dialog')

        buttons = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.buttons = QDialogButtonBox(buttons)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        msg = QLabel('Something happened, it that OK?')
        self.layout.addWidget(msg)
        self.layout.addWidget(self.buttons)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My app')

        button = QPushButton('Press me for a dialog')
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self, s):
        print(f'click {type(s)}: {s}')

        # dlg = QDialog(self)
        # dlg.setWindowTitle('Hello!')
        # dlg.exec()

        dlg = CustomDialog(self)
        if dlg.exec():
            print('OK...')
        else:
            print('Cancel...')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

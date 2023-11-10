# coding=utf-8
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableView

db = QSqlDatabase('QSQLITE')
db.setDatabaseName('../data/chinook.sqlite')
db.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sqlite app')

        model = QSqlTableModel(db=db)

        table = QTableView()
        table.setModel(model)

        model.setTable('Track')
        model.select()
        model.setEditStrategy(QSqlTableModel.EditStrategy.OnRowChange)

        self.table = table

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

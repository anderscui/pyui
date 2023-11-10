# coding=utf-8
import json
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QModelIndex

from todolist import Ui_MainWindow

tick = QtGui.QImage('../resources/tick.png')


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == Qt.ItemDataRole.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Simple TODO List')

        self.data_file = '../data/todo_list.json'
        self.model = TodoModel()
        self.load()
        self.listView.setModel(self.model)

        self.btn_add.pressed.connect(self.add)
        self.btn_delete.pressed.connect(self.delete)
        self.btn_complete.pressed.connect(self.complete)

    def load(self):
        try:
            with open(self.data_file, 'r') as f:
                todos = json.load(f) or []
                self.model.todos = todos
        except Exception as e:
            print(f'loading error failed: {e}.')
            pass

    def save(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.model.todos, f, ensure_ascii=False, indent=2)

    def add(self):
        text = self.lineEdit.text().strip()
        if text and not self.todo_exists(text):
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.lineEdit.setText('')
            self.save()

    def delete(self):
        indices = self.listView.selectedIndexes()
        if indices:
            index = indices[0]
            # print(index.row(), index.column(), index.data())
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.listView.clearSelection()
            self.save()

            if not self.model.todos:
                return

            if index.row() >= len(self.model.todos):
                index = self.model.index(len(self.model.todos)-1, 0)
            self.listView.setCurrentIndex(index)

    def complete(self):
        indices = self.listView.selectedIndexes()
        if indices:
            index = indices[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.listView.clearSelection()
            self.save()

    def todo_exists(self, todo_text):
        return any(todo_text.lower() == text.lower() for status, text in self.model.todos)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

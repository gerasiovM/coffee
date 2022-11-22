import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

    def load_table(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        films = cur.execute("""SELECT * FROM films coffee""").fetchall()
        headers = list(map(lambda x: x[0], cur.description))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        for i, row in enumerate(films):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                item = QTableWidgetItem(str(elem))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.tableWidget.setItem(i, j, item)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
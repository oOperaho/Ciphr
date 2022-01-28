import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow


class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi,self).__init__()
        self.setWindowTitle("Ciphr")
        self.setGeometry(500, 500, 450, 450)
        self.setStyleSheet("background-color: #052321;")
        self.innic = QtWidgets.QLabel(self)
        self.opc = QPushButton(self)


def display():
    w = QApplication(sys.argv)
    w.setStyle("Oxygen")
    ui = MainUi()
    ui.show()
    sys.exit(w.exec_())


display()

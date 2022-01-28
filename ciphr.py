import sys

from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QSizePolicy


class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        self.setWindowTitle("Ciphr")
        self.setGeometry(500, 500, 450, 450)
        self.setStyleSheet("background-color: #052321;")
        self.innic = QtWidgets.QLabel(self)
        self.opc = QPushButton(self)
        self.window()

    def window(self):
        self.innic.setText("CIPHR")
        self.innic.setStyleSheet("color: #ADD45A;")
        self.innic.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.innic.setGeometry(200, 200, 250, 250)
        self.innic.setAlignment(Qt.AlignCenter)


def display():
    w = QApplication(sys.argv)
    w.setStyle("Oxygen")
    ui = MainUi()
    ui.show()
    sys.exit(w.exec_())


display()

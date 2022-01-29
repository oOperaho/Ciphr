

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow


class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        self.setWindowTitle("Ciphr")
        self.setGeometry(500, 500, 450, 450)
        self.setStyleSheet("background-color: #052321;")
        self.innic = QtWidgets.QHBoxLayout(self)
        self.innic.setContentsMargins(100, 100, 100, 100)
        self.innic.setSpacing(90)
        self.inn = QtWidgets.QLabel()
        self.opc = QPushButton(self)
        self.window()

    def window(self):
        self.inn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.inn.setText("CIPHR")
        self.inn.setStyleSheet("color: #ADD45A;")
        self.inn.setFont(QFont("Impact", 25))


def display():
    import sys
    w = QApplication(sys.argv)
    w.setStyle("Oxygen")
    ui = MainUi()
    ui.show()
    sys.exit(w.exec_())


display()

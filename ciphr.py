import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow


class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        self.setWindowTitle("Ciphr")
        self.setGeometry(500, 500, 450, 450)
        self.innic = QtWidgets.QLabel(self)
        self.opc = QPushButton(self)
        self.window()

    def window(self):
        self.innic.setText("CIPHR")
        self.innic.setGeometry(100, 90, 250, 15)


def display():
    w = QApplication(sys.argv)
    w.setStyle("Oxygen")
    ui = MainUi()
    ui.show()
    sys.exit(w.exec_())


display()

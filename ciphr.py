

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
        self.innic.setContentsMargins(10, 10, 10, 10)
        self.innic.setSpacing(10)
        self.innic.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.opc = QPushButton(self)
        self.window()

    def window(self):
        self.innic.setText("CIPHR")
        self.innic.setStyleSheet("color: #ADD45A;")
        self.innic.setFont(QFont("Impact", 25))



def display():
    import sys
    w = QApplication(sys.argv)
    w.setStyle("Oxygen")
    ui = MainUi()
    ui.show()
    sys.exit(w.exec_())


display()

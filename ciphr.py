from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow


class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        self.setWindowTitle("Ciphr")
        self.setGeometry(500, 500, 450, 450)
        self.setStyleSheet("background-color: #052321;")
        self.vig = QtWidgets.QPushButton()
        self.innic = QtWidgets.QLabel(self)
        self.opc = QPushButton(self)
        self.window()

    def window(self):
        self.innic.setText("CIPHR")
        self.innic.setStyleSheet("color: #ADD45A;")
        self.innic.setFont(QFont("Impact", 25))
        self.innic.setGeometry(180, 100, 100, 30)

    def vigenere_button(self):
        self.vig.setText("Vigenere")
        self.vig.setStyleSheet("color: #ADD45A;")
        self.vig.setGeometry(100, 100, 100, 100)


def display():
    import sys
    w = QApplication(sys.argv)
    w.setStyle("Oxygen")
    ui = MainUi()
    ui.show()
    sys.exit(w.exec_())


display()

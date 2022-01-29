from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow


class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        self.innic = QtWidgets.QLabel(self)
        self.vig = QPushButton(self)
        self.cae = QPushButton(self)
        self.setWindowTitle("Ciphr")
        self.setGeometry(100, 100, 520, 400)
        self.setStyleSheet("background-color: #052321;")
        self.window()

    def window(self):
        self.innic.setText("CIPHR")
        self.innic.setStyleSheet("color: #ADD45A;")
        self.innic.setGeometry(163, 40, 200, 100)
        self.innic.setFont(QFont("Impact", 25))
        self.innic.setAlignment(Qt.AlignCenter)

        self.vig.setText("Vigenere")
        self.vig.setGeometry(227, 180, 70, 25)
        self.vig.setFont(QFont("Helvetica", 10))
        self.vig.setStyleSheet("""background-color: #042c18; color: #ADD45A""")

        self.cae.setText("Caesar")
        self.cae.setGeometry(227, 150, 70, 25)
        self.cae.setFont(QFont("Helvetica", 10))
        self.cae.setStyleSheet("""background-color: #042c18; color: #acbf4d""")


def display():
    import sys
    w = QApplication(sys.argv)
    w.setStyle("Oxygen")
    ui = MainUi()
    ui.show()
    sys.exit(w.exec_())


display()
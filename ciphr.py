from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow


class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        self.url = "https://github.com/oOperaho/Ciphr"
        self.innic = QtWidgets.QLabel(self)
        self.ciphr_repo = QPushButton(self)
        self.vig = QPushButton(self)
        self.cae = QPushButton(self)
        self.setWindowTitle("Ciphr")
        self.setGeometry(100, 100, 520, 400)
        self.setStyleSheet("background-color: #052321;")
        self.window()

    def window(self):
        self.innic.setText("• CIPHR •")
        self.innic.setStyleSheet("color: #ADD45A;")
        self.innic.setGeometry(163, 40, 190, 100)
        self.innic.setFont(QFont("Impact", 25))
        self.innic.setAlignment(Qt.AlignCenter)

        self.vig.setText("Vigenere")
        self.vig.setGeometry(227, 180, 60, 25)
        self.vig.setFont(QFont("Helvetica", 10))
        self.vig.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black""")

        self.cae.setText("Caesar")
        self.cae.setGeometry(227, 150, 60, 25)
        self.cae.setFont(QFont("Helvetica", 10))
        self.cae.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")

        self.ciphr_repo.setGeometry(10, 10, 20, 20)
        self.ciphr_repo.setStyleSheet("""background-color: #ADD45A; border: 1px solid black; border-radius: 5; 
                                        background-image: url(icons/gh.png);""")
        self.ciphr_repo.clicked.connect(self.open_repo)

    def open_repo(self):
        import webbrowser
        webbrowser.open_new(self.url)


def display():
    import sys
    w = QApplication(sys.argv)
    w.setStyle("Oxygen")
    ui = MainUi()
    ui.show()
    sys.exit(w.exec_())


display()

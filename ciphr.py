from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QIcon
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
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(500, 250, 520, 400)
        self.setStyleSheet("background-color: #052321;")
        self.showMaximized()
        self.window()

    def window(self):
        self.innic.setText("• CIPHR •")
        self.innic.setStyleSheet("color: #ADD45A;")
        self.innic.setGeometry(620, 120, 190, 100)
        self.innic.setFont(QFont("Impact", 35))
        self.innic.setAlignment(Qt.AlignCenter)

        self.cae.setText("Caesar")
        self.cae.setGeometry(665, 230, 100, 40)
        self.cae.setFont(QFont("Helvetica", 15))
        self.cae.setStyleSheet("""QPushButton {
                            background-color: #042c18; 
                            color: #dbf45c; 
                            border: 2px solid black;
                            }
                            QPushButton::hover {
                            background-color: #8ac431;
                            color: black;
                            }""")

        self.vig.setText("Vigenere")
        self.vig.setGeometry(665, 280, 100, 40)
        self.vig.setFont(QFont("Helvetica", 15))
        self.vig.setStyleSheet("""QPushButton {
                                background-color: #042c18;
                                border: 2px solid black;
                                color: #dbf45c;
                                }
                                QPushButton::hover {
                                background-color: #8ac431;
                                color: black;
                                }""")

        self.ciphr_repo.setGeometry(10, 800, 20, 20)
        self.ciphr_repo.setStyleSheet("""background-color: #ADD45A; border: 1px solid black; border-radius: 5; 
                                        background-image: url(icons/gh.png);""")
        self.ciphr_repo.clicked.connect(self.open_repo)

    def open_repo(self):
        import webbrowser
        webbrowser.open_new(self.url)


def display():
    import sys
    w = QApplication(sys.argv)
    w.setStyle("Breeze")
    ui = MainUi()
    ui.show()
    sys.exit(w.exec_())


display()

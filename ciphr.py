from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit


class MainUi(QWidget):
    switch_tabs = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
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
        self.manu()

    def manu(self):
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
                                border: 4px solid black;
                                }""")
        self.cae.clicked.connect(self.caesar_toggle)

        self.vig.setText("Vigenere")
        self.vig.setGeometry(665, 280, 100, 40)
        self.vig.setFont(QFont("Helvetica", 15))
        self.vig.setStyleSheet("""QPushButton {
                                background-color: #042c18;
                                color: #dbf45c;
                                border: 2px solid black;
                                }
                                QPushButton::hover {
                                background-color: #8ac431;
                                color: black;
                                border: 4px solid black;
                                }""")

        self.ciphr_repo.setGeometry(10, 800, 20, 20)
        self.ciphr_repo.setStyleSheet("""QPushButton {
                                        background-color: #ADD45A; 
                                        border: 1px solid black; 
                                        border-radius: 5; 
                                        background-image: url(icons/gh.png);
                                        }
                                        QPushButton::hover {
                                        background-color: #ADD45A; 
                                        border: 1px solid black; 
                                        border-radius: 10; 
                                        background-image: url(icons/gh.png);
                                        }""")
        self.ciphr_repo.clicked.connect(self.open_repo)

    def caesar_toggle(self):
        self.switch_tabs.emit()

    def open_repo(self):
        import webbrowser
        webbrowser.open_new(self.url)


class CaesarTab(QWidget):
    switch_tabs = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.backbutton = QPushButton(self)
        self.cryptbutton = QPushButton(self)
        self.caesarinput = QLineEdit(self)
        self.caesarkey = QLineEdit(self)
        self.result = QtWidgets.QLabel(self)
        self.setWindowTitle("Ciphr")
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(500, 250, 520, 400)
        self.setStyleSheet("background-color: #052321;")
        self.showMaximized()
        self.vigenere_window()

    def vigenere_window(self):
        self.backbutton.setText("←")
        self.backbutton.setGeometry(10, 10, 60, 35)
        self.backbutton.setFont(QFont("Helvetica", 15))
        self.backbutton.setStyleSheet("""QPushButton {
                                        background-color: #052321;
                                        color: #70ff03;
                                        }
                                        QPushButton::hover {
                                        background-color: #8ac431;
                                        color: black;
                                        border: 3px solid black;
                                        }""")
        self.backbutton.clicked.connect(self.menu_toggle)

        self.result.setText("")
        self.result.setGeometry(640, 410, 150, 20)
        self.result.setStyleSheet("""background-color: #042c18; color: #dbf45c;""")
        self.result.setFont(QFont("Helvetica", 12))

        self.caesarkey.setText("3")
        self.caesarkey.setGeometry(685, 320, 50, 30)
        self.caesarkey.setFont(QFont("Arial", 8))
        self.caesarkey.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")

        self.caesarinput.setText("word")
        self.caesarinput.setGeometry(655, 280, 120, 30)
        self.caesarinput.setFont(QFont("Arial", 10))
        self.caesarinput.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")

        self.cryptbutton.setText("Encode/Decode")
        self.cryptbutton.setGeometry(640, 360, 150, 40)
        self.cryptbutton.setFont(QFont("Helvetica", 12))
        self.cryptbutton.setStyleSheet("""QPushButton {
                                        background-color: #042c18;
                                        color: #dbf45c;
                                        border: 2px solid black;
                                        }
                                        QPushButton::hover {
                                        background-color: #8ac431;
                                        color: black;
                                        border: 4px solid black;
                                        }""")
        self.cryptbutton.clicked.connect(self.execcaesar)

    def execcaesar(self):
        from Caesar.caesar import caesarencoder
        word = self.caesarinput.text()
        key = self.caesarkey.text()
        self.result.setText(caesarencoder(word, int(key)))

    def menu_toggle(self):
        self.switch_tabs.emit()


class Remote:
    def __init__(self):
        self.cae_tab = CaesarTab()
        self.mwindow = MainUi()

    def main_window(self):
        self.mwindow.switch_tabs.connect(self.caesar_tab)
        self.cae_tab.close()
        self.mwindow.show()

    def caesar_tab(self):
        self.cae_tab.switch_tabs.connect(self.main_window)
        self.mwindow.close()
        self.cae_tab.show()


def display():
    import sys
    w = QApplication(sys.argv)
    w.setStyle("Breeze")
    ui = Remote()
    ui.main_window()
    sys.exit(w.exec_())


display()

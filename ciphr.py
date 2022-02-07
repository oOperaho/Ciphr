import tools
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit, QDesktopWidget


class MainUi(QWidget):

    switch_tab1 = QtCore.pyqtSignal()
    switch_tab2 = QtCore.pyqtSignal()
    switch_tab3 = QtCore.pyqtSignal()
    switch_tab4 = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        self.url = "https://github.com/oOperaho/Ciphr"
        self.innic = QtWidgets.QLabel(self)
        self.ciphr_repo = QPushButton(self)
        self.biny = QPushButton(self)
        self.cae = QPushButton(self)
        self.vig = QPushButton(self)
        self.mor = QPushButton(self)
        self.setWindowTitle("Ciphr")
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(0, 0, 520, 400)
        self.move(qtRectangle.topLeft())
        self.setStyleSheet("background-color: #052321;")
        self.setFixedSize(self.size())  # disable resizing
        self.menu()

    def menu(self):
        self.innic.setText("• CIPHR •")
        self.innic.setStyleSheet("color: #ADD45A;")
        self.innic.setGeometry(0, 0, 190, 100)
        self.innic.setFont(QFont("Impact", 35))
        self.innic.setAlignment(Qt.AlignCenter)
        pos_x = self.width() - self.innic.width()
        self.innic.move(int(pos_x / 2), 40)

        self.biny.setText("Binary")
        self.biny.setGeometry(0, 0, 100, 40)
        self.biny.setFont(QFont("Helvetica", 15))
        self.biny.setStyleSheet("""QPushButton {
                                        background-color: #042c18; 
                                        color: #dbf45c; 
                                        border: 2px solid black;
                                        }
                                        QPushButton::hover {
                                        background-color: #8ac431;
                                        color: black;
                                        border: 4px solid black;
                                        }""")
        self.biny.clicked.connect(self.bin_toggle)
        pos_x = self.width() - self.biny.width()
        self.biny.move(int(pos_x / 2), 140)

        self.cae.setText("Caesar")
        self.cae.setGeometry(0, 0, 100, 40)
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
        self.cae.clicked.connect(self.cae_toggle)
        pos_x = self.width() - self.cae.width()
        self.cae.move(int(pos_x / 2), 190)

        self.vig.setText("Vigenere")
        self.vig.setGeometry(0, 0, 100, 40)
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
        self.vig.clicked.connect(self.vig_toggle)
        pos_x = self.width() - self.vig.width()
        self.vig.move(int(pos_x / 2), 240)

        self.mor.setText("Morse")
        self.mor.setGeometry(0, 0, 100, 40)
        self.mor.setFont(QFont("Helvetica", 15))
        self.mor.setStyleSheet("""QPushButton {
                                background-color: #042c18;
                                color: #dbf45c;
                                border: 2px solid black;
                                }
                                QPushButton::hover {
                                background-color: #8ac431;
                                color: black;
                                border: 4px solid black;
                                }""")
        self.mor.clicked.connect(self.mor_toggle)
        pos_x = self.width() - self.mor.width()
        self.mor.move(int(pos_x / 2), 300)

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
        pos_y = self.height() - self.ciphr_repo.height()
        margin = 15
        self.ciphr_repo.move(margin, pos_y-margin)

    def bin_toggle(self):
        self.switch_tab1.emit()

    def cae_toggle(self):
        self.switch_tab2.emit()

    def vig_toggle(self):
        self.switch_tab3.emit()

    def mor_toggle(self):
        self.switch_tab4.emit()

    def open_repo(self):
        import webbrowser
        webbrowser.open_new(self.url)


class BinaryTab(QWidget):

    switch_tab = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        self.backbutton = QPushButton(self)
        self.encodebutton = QPushButton(self)
        self.encodeinput = QLineEdit(self)
        self.decodebutton = QPushButton(self)
        self.decodeinput = QLineEdit(self)
        # self.numberVld = QIntValidator(self)
        # self.encodeinput.setValidator(self.numberVld)
        # self.decodeinput.setValidator(self.numberVld)
        self.result = QtWidgets.QLabel(self)
        self.setWindowTitle("Ciphr")
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(0, 0, 520, 400)
        self.move(qtRectangle.topLeft())
        self.setStyleSheet("background-color: #052321;")
        self.setFixedSize(self.size())
        self.binary_window()

    def binary_window(self):
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
        self.result.setGeometry(640, 410, 170, 20)
        self.result.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")
        self.result.setFont(QFont("Helvetica", 10))
        pos_x = self.width() - self.result.width()
        self.result.move(int(pos_x / 2), 200)

        self.encodeinput.setText("0")
        self.encodeinput.setGeometry(655, 280, 70, 30)
        self.encodeinput.setFont(QFont("Arial", 10))
        self.encodeinput.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")
        pos_x = (self.width() - self.encodeinput.width())
        self.encodeinput.move(int(pos_x / 2) - 40, 130)

        self.decodeinput.setText("0")
        self.decodeinput.setGeometry(655, 280, 70, 30)
        self.decodeinput.setFont(QFont("Arial", 10))
        self.decodeinput.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")
        pos_x = (self.width() - self.decodeinput.width())
        self.decodeinput.move(int(pos_x / 2) + 40, 130)

        self.encodebutton.setText("Encode")
        self.encodebutton.setGeometry(620, 360, 70, 30)
        self.encodebutton.setFont(QFont("Helvetica", 11))
        self.encodebutton.setStyleSheet("""QPushButton {
                                               background-color: #042c18;
                                               color: #dbf45c;
                                               border: 2px solid black;
                                               }
                                               QPushButton::hover {
                                               background-color: #8ac431;
                                               color: black;
                                               border: 4px solid black;
                                               }""")
        pos_x = self.width() - self.encodebutton.width()
        self.encodebutton.move(int(pos_x / 2) - 40, 165)
        self.encodebutton.clicked.connect(self.encodebinary)

        self.decodebutton.setText("Decode")
        self.decodebutton.setGeometry(720, 360, 70, 30)
        self.decodebutton.setFont(QFont("Helvetica", 11))
        self.decodebutton.setStyleSheet("""QPushButton {
                                                       background-color: #042c18;
                                                       color: #dbf45c;
                                                       border: 2px solid black;
                                                       }
                                                       QPushButton::hover {
                                                       background-color: #8ac431;
                                                       color: black;
                                                       border: 4px solid black;
                                                       }""")
        pos_x = self.width() - self.decodebutton.width()
        self.decodebutton.move(int(pos_x / 2) + 40, 165)
        self.decodebutton.clicked.connect(self.decodebinary)

    def encodebinary(self):
        from Binary.binary import binaryencoder

        decimal = self.encodeinput.text()
        if decimal != "":
            decimal = tools.process_int(decimal)
            out = binaryencoder(int(decimal))
            self.result.setText(str(out))
        else:
            self.result.setText("?")

    def decodebinary(self):
        from Binary.binary import binarydecoder

        decimal = self.decodeinput.text()
        if decimal != "":
            decimal = tools.process_int(decimal)
            out = binarydecoder(int(decimal))
            self.result.setText(str(out))
        else:
            self.result.setText("?")

    def menu_toggle(self):
        self.switch_tab.emit()


class CaesarTab(QWidget):

    switch_tab = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        self.backbutton = QPushButton(self)
        self.encodebutton = QPushButton(self)
        self.decodebutton = QPushButton(self)
        self.caesarinput = QLineEdit(self)
        self.caesarkey = QLineEdit(self)
        # self.numberVld = QIntValidator(self)
        # self.caesarkey.setValidator(self.numberVld)
        self.result = QtWidgets.QLabel(self)
        self.setWindowTitle("Ciphr")
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(0, 0, 520, 400)
        self.move(qtRectangle.topLeft())
        self.setStyleSheet("background-color: #052321;")
        self.setFixedSize(self.size())
        self.caesar_window()

    def caesar_window(self):
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
        self.result.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")
        self.result.setFont(QFont("Helvetica", 10))
        pos_x = self.width() - self.result.width()
        self.result.move(int(pos_x / 2), 200)

        self.caesarkey.setText("3")
        self.caesarkey.setGeometry(685, 320, 50, 30)
        self.caesarkey.setFont(QFont("Arial", 8))
        self.caesarkey.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")
        pos_x = self.width() - self.caesarkey.width()
        self.caesarkey.move(int(pos_x / 2), 120)

        self.caesarinput.setText("word")
        self.caesarinput.setGeometry(655, 280, 120, 30)
        self.caesarinput.setFont(QFont("Arial", 10))
        self.caesarinput.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")
        pos_x = self.width() - self.caesarinput.width()
        self.caesarinput.move(int(pos_x / 2), 80)

        self.encodebutton.setText("Encode")
        self.encodebutton.setGeometry(620, 360, 70, 30)
        self.encodebutton.setFont(QFont("Helvetica", 11))
        self.encodebutton.setStyleSheet("""QPushButton {
                                        background-color: #042c18;
                                        color: #dbf45c;
                                        border: 2px solid black;
                                        }
                                        QPushButton::hover {
                                        background-color: #8ac431;
                                        color: black;
                                        border: 4px solid black;
                                        }""")
        pos_x = self.width() - self.encodebutton.width()
        self.encodebutton.move(int(pos_x / 2) - 40, 160)
        self.encodebutton.clicked.connect(self.encodecaesar)

        self.decodebutton.setText("Decode")
        self.decodebutton.setGeometry(720, 360, 70, 30)
        self.decodebutton.setFont(QFont("Helvetica", 11))
        self.decodebutton.setStyleSheet("""QPushButton {
                                                background-color: #042c18;
                                                color: #dbf45c;
                                                border: 2px solid black;
                                                }
                                                QPushButton::hover {
                                                background-color: #8ac431;
                                                color: black;
                                                border: 4px solid black;
                                                }""")
        pos_x = self.width() - self.decodebutton.width()
        self.decodebutton.move(int(pos_x / 2) + 40, 160)
        self.decodebutton.clicked.connect(self.decodecaesar)

    def encodecaesar(self):
        from Caesar.caesar import caesarencoder

        word = self.caesarinput.text()
        word = tools.process_text(word)
        key = self.caesarkey.text()
        if key != "":
            key = tools.process_int(key)
            self.result.setText(caesarencoder(word, int(key)))
        else:
            self.result.setText("?")

    def decodecaesar(self):
        from Caesar.caesar import caesardecoder

        word = self.caesarinput.text()
        word = tools.process_text(word)
        key = self.caesarkey.text()
        if key != "":
            key = tools.process_int(key)
            self.result.setText(caesardecoder(word, int(key)))
        else:
            self.result.setText("?")

    def menu_toggle(self):
        self.switch_tab.emit()


class VigenereTab(QWidget):

    switch_tab = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        self.backbutton = QPushButton(self)
        self.result = QtWidgets.QLabel(self)
        self.vigenerekey = QLineEdit(self)
        self.vigenereinput = QLineEdit(self)
        self.encodebutton = QPushButton(self)
        self.decodebutton = QPushButton(self)
        self.setWindowTitle("Ciphr")
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(0, 0, 520, 400)
        self.move(qtRectangle.topLeft())
        self.setStyleSheet("background-color: #052321;")
        self.setFixedSize(self.size())
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
        self.result.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")
        self.result.setFont(QFont("Helvetica", 10))
        pos_x = self.width() - self.result.width()
        self.result.move(int(pos_x / 2), 200)

        self.vigenereinput.setText("word")
        self.vigenereinput.setGeometry(655, 280, 120, 30)
        self.vigenereinput.setFont(QFont("Arial", 10))
        self.vigenereinput.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")
        pos_x = self.width() - self.vigenereinput.width()
        self.vigenereinput.move(int(pos_x / 2), 80)

        self.vigenerekey.setText("key")
        self.vigenerekey.setGeometry(685, 320, 120, 30)
        self.vigenerekey.setFont(QFont("Arial", 10))
        self.vigenerekey.setStyleSheet("""background-color: #042c18; color: #dbf45c; border: 2px solid black;""")
        pos_x = self.width() - self.vigenerekey.width()
        self.vigenerekey.move(int(pos_x / 2), 120)

        self.encodebutton.setText("Encode")
        self.encodebutton.setGeometry(620, 360, 70, 30)
        self.encodebutton.setFont(QFont("Helvetica", 11))
        self.encodebutton.setStyleSheet("""QPushButton {
                                                background-color: #042c18;
                                                color: #dbf45c;
                                                border: 2px solid black;
                                                }
                                                QPushButton::hover {
                                                background-color: #8ac431;
                                                color: black;
                                                border: 4px solid black;
                                                }""")
        pos_x = self.width() - self.encodebutton.width()
        self.encodebutton.move(int(pos_x / 2) + 40, 160)
        self.encodebutton.clicked.connect(self.encodevigenere)

        self.decodebutton.setText("Decode")
        self.decodebutton.setGeometry(720, 360, 70, 30)
        self.decodebutton.setFont(QFont("Helvetica", 11))
        self.decodebutton.setStyleSheet("""QPushButton {
                                                        background-color: #042c18;
                                                        color: #dbf45c;
                                                        border: 2px solid black;
                                                        }
                                                        QPushButton::hover {
                                                        background-color: #8ac431;
                                                        color: black;
                                                        border: 4px solid black;
                                                        }""")
        pos_x = self.width() - self.decodebutton.width()
        self.decodebutton.move(int(pos_x / 2) - 40, 160)
        self.decodebutton.clicked.connect(self.decodevigenere)

    def encodevigenere(self):
        from Vigenere.vigenere import vigenereencoder

        word = self.vigenereinput.text()
        word = tools.process_text(word)
        key = self.vigenerekey.text()
        key = tools.process_text(key)
        if key != "":
            key = tools.newKey(word, key)
            self.result.setText(vigenereencoder(word.upper(), key.upper()))
        else:
            self.result.setText("?")

    def decodevigenere(self):
        from Vigenere.vigenere import vigeneredecoder

        word = self.vigenereinput.text()
        word = tools.process_text(word)
        key = self.vigenerekey.text()
        key = tools.process_text(key)
        if key != "":
            key = tools.newKey(word, key)
            self.result.setText(vigeneredecoder(word.upper(), key.upper()))
        else:
            self.result.setText("?")

    def menu_toggle(self):
        self.switch_tab.emit()


class MorseTab(QWidget):

    switch_tab = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        self.backbutton = QPushButton(self)
        self.result = QtWidgets.QLabel(self)
        self.setWindowTitle("Ciphr")
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(0, 0, 520, 400)
        self.move(qtRectangle.topLeft())
        self.setStyleSheet("background-color: #052321;")
        self.setFixedSize(self.size())
        self.morse_window()

    def morse_window(self):
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

    def menu_toggle(self):
        self.switch_tab.emit()


class Remote:
    def __init__(self):
        self.mwindow = MainUi()
        self.cae_tab = CaesarTab()
        self.vig_tab = VigenereTab()
        self.bin_tab = BinaryTab()
        self.mor_tab = MorseTab()

    def main_window(self):
        self.mwindow.switch_tab1.connect(self.binary_tab)
        self.mwindow.switch_tab2.connect(self.caesar_tab)
        self.mwindow.switch_tab3.connect(self.vigenere_tab)
        self.mwindow.switch_tab4.connect(self.morse_tab())
        self.bin_tab.close()
        self.cae_tab.close()
        self.vig_tab.close()
        self.mwindow.show()

    def binary_tab(self):
        self.bin_tab.switch_tab.connect(self.main_window)
        self.mwindow.close()
        self.bin_tab.show()

    def caesar_tab(self):
        self.cae_tab.switch_tab.connect(self.main_window)
        self.mwindow.close()
        self.cae_tab.show()

    def vigenere_tab(self):
        self.vig_tab.switch_tab.connect(self.main_window)
        self.mwindow.close()
        self.vig_tab.show()

    def morse_tab(self):
        self.mor_tab.switch_tab.connect(self.mwindow)
        self.mwindow.close()
        self.mor_tab.show()


def display():
    import sys
    w = QApplication(sys.argv)
    w.setStyle("Breeze")
    ui = Remote()
    ui.main_window()
    sys.exit(w.exec_())


display()

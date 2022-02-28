import tools
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit, QDesktopWidget, QGraphicsOpacityEffect


obj_list = ["Menu", "Backbutton", "Result", "Inputs", "Crypt", "Copy"]

class MainUi(QWidget):

    switch_tab1 = QtCore.pyqtSignal()
    switch_tab2 = QtCore.pyqtSignal()
    switch_tab3 = QtCore.pyqtSignal()
    switch_tab4 = QtCore.pyqtSignal()
    switch_tab5 = QtCore.pyqtSignal()

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
        self.hil = QPushButton(self)
        self.setWindowTitle("Ciphr")
        self.setObjectName(obj_list[0])
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(0, 0, 520, 400)
        self.move(qtRectangle.topLeft())
        self.setFixedSize(self.size())  # disable resizing
        self.menu()

    def menu(self):
        keyname = "FirstBtt"

        self.innic.setText("• CIPHR •")
        self.innic.setGeometry(0, 0, 190, 100)
        self.innic.setObjectName("Innic")
        self.innic.setAlignment(Qt.AlignCenter)
        pos_x = self.width() - self.innic.width()
        self.innic.move(int(pos_x / 2), 40)

        self.biny.setText("Binary")
        self.biny.setObjectName(keyname)
        self.biny.setGeometry(0, 0, 100, 40)
        self.biny.clicked.connect(self.bin_toggle)
        pos_x = self.width() - self.biny.width()
        self.biny.move(int(pos_x / 2) - 60, 140)

        self.cae.setText("Caesar")
        self.cae.setObjectName(keyname)
        self.cae.setGeometry(0, 0, 100, 40)
        self.cae.clicked.connect(self.cae_toggle)
        pos_x = self.width() - self.cae.width()
        self.cae.move(int(pos_x / 2) + 60, 140)

        self.vig.setText("Vigenere")
        self.vig.setObjectName(keyname)
        self.vig.setGeometry(0, 0, 100, 40)
        self.vig.clicked.connect(self.vig_toggle)
        pos_x = self.width() - self.vig.width()
        self.vig.move(int(pos_x / 2) - 60, 200)

        self.mor.setText("Morse")
        self.mor.setObjectName(keyname)
        self.mor.setGeometry(0, 0, 100, 40)
        self.mor.clicked.connect(self.mor_toggle)
        pos_x = self.width() - self.mor.width()
        self.mor.move(int(pos_x / 2) + 60, 200)

        self.hil.setText("Hill")
        self.hil.setObjectName(keyname)
        self.hil.setGeometry(0, 0, 100, 40)
        self.hil.clicked.connect(self.hil_toggle)
        pos_x = self.width() - self.hil.width()
        self.hil.move(int(pos_x / 2) - 60, 260)

        self.ciphr_repo.setGeometry(10, 800, 20, 20)
        self.ciphr_repo.setObjectName("Repo")
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

    def hil_toggle(self):
        self.switch_tab5.emit()

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
        self.copy_text = QPushButton(self)                                                                                                                                                                                                                                                      
        # self.numberVld = QIntValidator(self)
        # self.encodeinput.setValidator(self.numberVld)
        # self.decodeinput.setValidator(self.numberVld)
        self.result = QtWidgets.QLabel(self)
        self.setWindowTitle("Ciphr")
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(0, 0, 520, 400)
        self.move(qtRectangle.topLeft())
        self.setObjectName(obj_list[0])
        self.setFixedSize(self.size())
        self.binary_window()

    def binary_window(self):
        self.backbutton.setText("←")
        self.backbutton.setObjectName(obj_list[1])
        self.backbutton.setGeometry(10, 10, 60, 35)
        self.backbutton.clicked.connect(self.menu_toggle)

        self.result.setText("")
        self.result.setGeometry(640, 410, 170, 20)
        self.result.setObjectName(obj_list[2])
        pos_x = self.width() - self.result.width()
        self.result.move(int(pos_x / 2), 200)

        self.encodeinput.setText("0")
        self.encodeinput.setGeometry(655, 280, 70, 30)
        self.encodeinput.setObjectName(obj_list[3])
        pos_x = (self.width() - self.encodeinput.width())
        self.encodeinput.move(int(pos_x / 2) - 40, 130)

        self.decodeinput.setText("0")
        self.decodeinput.setGeometry(655, 280, 70, 30)
        self.decodeinput.setObjectName(obj_list[3])
        pos_x = (self.width() - self.decodeinput.width())
        self.decodeinput.move(int(pos_x / 2) + 40, 130)

        self.encodebutton.setText("Encode")
        self.encodebutton.setGeometry(620, 360, 70, 30)
        self.encodebutton.setObjectName(obj_list[4])
        pos_x = self.width() - self.encodebutton.width()
        self.encodebutton.move(int(pos_x / 2) - 40, 165)
        self.encodebutton.clicked.connect(self.encodebinary)

        self.decodebutton.setText("Decode")
        self.decodebutton.setGeometry(720, 360, 70, 30)
        self.decodebutton.setObjectName(obj_list[4])
        pos_x = self.width() - self.decodebutton.width()
        self.decodebutton.move(int(pos_x / 2) + 40, 165)
        self.decodebutton.clicked.connect(self.decodebinary)

        self.copy_text.setText("Copy")
        self.copy_text.setGeometry(620, 360, 50, 25)
        self.copy_text.setObjectName(obj_list[5])                                     
        pos_x = self.width() - self.copy_text.width()
        self.copy_text.move(int(pos_x / 2), 230)
        self.copy_text.clicked.connect(self.copy_to_clipboard)

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

    def copy_to_clipboard(self):
        tools.copy_to_pc(self.result.text())

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
        self.copy_text = QPushButton(self)
        # self.numberVld = QIntValidator(self)
        # self.caesarkey.setValidator(self.numberVld)
        self.result = QtWidgets.QLabel(self)
        self.setWindowTitle("Ciphr")
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(0, 0, 520, 400)
        self.move(qtRectangle.topLeft())
        self.setObjectName(obj_list[0])
        self.setFixedSize(self.size())
        self.caesar_window()

    def caesar_window(self):
        self.backbutton.setText("←")
        self.backbutton.setGeometry(10, 10, 60, 35)
        self.backbutton.setFont(QFont("Helvetica", 15))
        self.backbutton.setObjectName(obj_list[1])
        self.backbutton.clicked.connect(self.menu_toggle)

        self.result.setText("")
        self.result.setGeometry(640, 410, 150, 20)
        self.result.setObjectName(obj_list[2])
        pos_x = self.width() - self.result.width()
        self.result.move(int(pos_x / 2), 200)

        self.caesarinput.setText("text")
        self.caesarinput.setGeometry(655, 280, 120, 30)
        self.caesarinput.setObjectName(obj_list[3])
        pos_x = self.width() - self.caesarinput.width()
        self.caesarinput.move(int(pos_x / 2), 80)

        self.caesarkey.setText("3")
        self.caesarkey.setGeometry(685, 320, 50, 30)
        self.caesarkey.setObjectName(obj_list[3])
        pos_x = self.width() - self.caesarkey.width()
        self.caesarkey.move(int(pos_x / 2), 120)

        self.encodebutton.setText("Encode")
        self.encodebutton.setGeometry(620, 360, 70, 30)
        self.encodebutton.setObjectName(obj_list[4])
        pos_x = self.width() - self.encodebutton.width()
        self.encodebutton.move(int(pos_x / 2) - 40, 160)
        self.encodebutton.clicked.connect(self.encodecaesar)

        self.decodebutton.setText("Decode")
        self.decodebutton.setGeometry(720, 360, 70, 30)
        self.decodebutton.setObjectName(obj_list[4])
        pos_x = self.width() - self.decodebutton.width()
        self.decodebutton.move(int(pos_x / 2) + 40, 160)
        self.decodebutton.clicked.connect(self.decodecaesar)

        self.copy_text.setText("Copy")
        self.copy_text.setGeometry(620, 360, 50, 25)
        self.copy_text.setObjectName(obj_list[5])
        pos_x = self.width() - self.copy_text.width()
        self.copy_text.move(int(pos_x / 2), 230)
        self.copy_text.clicked.connect(self.copy_to_clipboard)

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

    def copy_to_clipboard(self):
        tools.copy_to_pc(self.result.text())

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
        self.copy_text = QPushButton(self)
        self.setWindowTitle("Ciphr")
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(0, 0, 520, 400)
        self.move(qtRectangle.topLeft())
        self.setObjectName(obj_list[0])
        self.setFixedSize(self.size())
        self.vigenere_window()

    def vigenere_window(self):
        self.backbutton.setText("←")
        self.backbutton.setGeometry(10, 10, 60, 35)
        self.backbutton.setObjectName(obj_list[1])
        self.backbutton.clicked.connect(self.menu_toggle)

        self.result.setText("")
        self.result.setGeometry(640, 410, 150, 20)
        self.result.setObjectName(obj_list[2])
        pos_x = self.width() - self.result.width()
        self.result.move(int(pos_x / 2), 200)

        self.vigenereinput.setText("text")
        self.vigenereinput.setGeometry(655, 280, 120, 30)
        self.vigenereinput.setObjectName(obj_list[3])
        pos_x = self.width() - self.vigenereinput.width()
        self.vigenereinput.move(int(pos_x / 2), 80)

        self.vigenerekey.setText("key")
        self.vigenerekey.setGeometry(685, 320, 120, 30)
        self.vigenerekey.setObjectName(obj_list[3])
        pos_x = self.width() - self.vigenerekey.width()
        self.vigenerekey.move(int(pos_x / 2), 120)

        self.encodebutton.setText("Encode")
        self.encodebutton.setGeometry(620, 360, 70, 30)
        self.encodebutton.setObjectName(obj_list[4])
        pos_x = self.width() - self.encodebutton.width()
        self.encodebutton.move(int(pos_x / 2) + 40, 160)
        self.encodebutton.clicked.connect(self.encodevigenere)

        self.decodebutton.setText("Decode")
        self.decodebutton.setGeometry(720, 360, 70, 30)
        self.decodebutton.setObjectName(obj_list[4])
        pos_x = self.width() - self.decodebutton.width()
        self.decodebutton.move(int(pos_x / 2) - 40, 160)
        self.decodebutton.clicked.connect(self.decodevigenere)

        self.copy_text.setText("Copy")
        self.copy_text.setGeometry(620, 360, 50, 25)
        self.copy_text.setObjectName(obj_list[5])
        pos_x = self.width() - self.copy_text.width()
        self.copy_text.move(int(pos_x / 2), 230)
        self.copy_text.clicked.connect(self.copy_to_clipboard)

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

    def copy_to_clipboard(self):
        tools.copy_to_pc(self.result.text())

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
        self.morseinput = QLineEdit(self)
        self.morsecrypt = QPushButton(self)
        self.copy_text = QPushButton(self)
        self.setWindowTitle("Ciphr")
        self.setWindowIcon(QIcon("icons/cr.png"))
        self.setGeometry(0, 0, 520, 400)
        self.move(qtRectangle.topLeft())
        self.setObjectName(obj_list[0])
        self.setFixedSize(self.size())
        self.morse_window()

    def morse_window(self):
        self.backbutton.setText("←")
        self.backbutton.setGeometry(10, 10, 60, 35)
        self.backbutton.setObjectName(obj_list[1])
        self.backbutton.clicked.connect(self.menu_toggle)

        self.result.setText("")
        self.result.setGeometry(640, 410, 150, 30)
        self.result.setObjectName(obj_list[2])
        pos_x = self.width() - self.result.width()
        self.result.move(int(pos_x / 2), 200)

        self.morseinput.setText("text")
        self.morseinput.setGeometry(655, 280, 150, 30)
        self.morseinput.setObjectName(obj_list[3])
        pos_x = self.width() - self.morseinput.width()
        self.morseinput.move(int(pos_x / 2), 120)

        self.morsecrypt.setText("Morse it")
        self.morsecrypt.setGeometry(620, 360, 70, 30)
        self.morsecrypt.setObjectName(obj_list[4])
        pos_x = self.width() - self.morsecrypt.width()
        self.morsecrypt.move(int(pos_x / 2), 160)
        self.morsecrypt.clicked.connect(self.morse_code)

        self.copy_text.setText("Copy")
        self.copy_text.setGeometry(620, 360, 50, 25)
        self.copy_text.setObjectName(obj_list[5])
        pos_x = self.width() - self.copy_text.width()
        self.copy_text.move(int(pos_x / 2), 240)
        self.copy_text.clicked.connect(self.copy_to_clipboard)

    def morse_code(self):
        from Morse.morse import morsecode

        word = self.morseinput.text()
        word = tools.process_morse(word)
        word = tools.remove_spaces(word)
        self.result.setText(morsecode(word.lower()))

    def copy_to_clipboard(self):
        tools.copy_to_pc(self.result.text())

    def menu_toggle(self):
        self.switch_tab.emit()


class HillTab(QWidget):

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
        self.setObjectName(obj_list[0])
        self.setFixedSize(self.size())
        self.hill_window()

    def hill_window(self):
        self.backbutton.setText("←")
        self.backbutton.setGeometry(10, 10, 60, 35)
        self.backbutton.setObjectName(obj_list[1])
        self.backbutton.clicked.connect(self.menu_toggle)

        self.result.setText("")
        self.result.setGeometry(640, 410, 150, 30)
        self.result.setObjectName(obj_list[2])
        pos_x = self.width() - self.result.width()
        self.result.move(int(pos_x / 2), 200)

    def menu_toggle(self):
        self.switch_tab.emit()


class Remote:
    def __init__(self):
        self.mwindow = MainUi()
        self.cae_tab = CaesarTab()
        self.vig_tab = VigenereTab()
        self.bin_tab = BinaryTab()
        self.mor_tab = MorseTab()
        self.hil_tab = HillTab()

    def main_window(self):
        self.mwindow.switch_tab1.connect(self.binary_tab)
        self.mwindow.switch_tab2.connect(self.caesar_tab)
        self.mwindow.switch_tab3.connect(self.vigenere_tab)
        self.mwindow.switch_tab4.connect(self.morse_tab)
        self.mwindow.switch_tab5.connect(self.hill_tab)
        self.bin_tab.close()
        self.cae_tab.close()
        self.vig_tab.close()
        self.mor_tab.close()
        self.hil_tab.close()
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
        self.mor_tab.switch_tab.connect(self.main_window)
        self.mwindow.close()
        self.mor_tab.show()

    def hill_tab(self):
        self.hil_tab.switch_tab.connect(self.main_window)
        self.mwindow.close()
        self.hil_tab.show()


def display():
    import sys
    w = QApplication(sys.argv)
    Interface = open("interface.qss", "r")
    with Interface:
        qss = Interface.read()
        w.setStyleSheet(qss)
    w.setStyle("Breeze")
    ui = Remote()
    ui.main_window()
    sys.exit(w.exec_())


display()

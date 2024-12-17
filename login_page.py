import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class LoginContent(QDialog):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.vbox1 = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.label1 = QLabel("Ting_Manager")
        self.font = QFont("Arial", 20, QFont.Bold )
        self.label1.setFont(self.font)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2 = QLabel("Please Enter Password")
        self.lineedit1 = QLineEdit()


        self.vbox1.addWidget(self.label1)
        self.vbox1.addStretch(10)
        self.hbox1.addWidget(self.label2)
        self.hbox1.addWidget(self.lineedit1)
        self.hbox1.addStretch()
        self.vbox1.addLayout(self.hbox1)
        self.setLayout(self.vbox1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_win = LoginContent()
    login_win.show()
    sys.exit(app.exec())
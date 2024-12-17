import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from stylesheet import default_stylesheet
from diary_main_content import DiaryMainContent

class LoginContent(QDialog):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.vbox1 = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.label1 = QLabel("Personal Manager")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2 = QLabel("Please Enter Password")
        self.enter_button = QPushButton("Enter")
        self.lineedit1 = QLineEdit()
        self.vbox1.addWidget(self.label1)
        self.vbox1.addStretch(10)
        self.hbox1.addWidget(self.label2)
        self.hbox1.addWidget(self.lineedit1)
        self.hbox1.addStretch()
        self.vbox1.addLayout(self.hbox1)
        self.vbox1.addWidget(self.enter_button)
        self.enter_button.clicked.connect(self.show_login_enter)
        self.setLayout(self.vbox1)
        self.setWindowTitle("Welcome!")

    def show_login_enter(self):
        self.login_enter = DiaryMainContent()
        self.login_enter.show()
        self.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(default_stylesheet)
    login_win = LoginContent()
    login_win.show()
    sys.exit(app.exec())
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from stylesheet import default_stylesheet

class MainContent(QDialog):
    def __init__(self):
        super().__init__()
        self.initui()


    def initui(self):

        self.grid = QGridLayout()
        self.hbox1 = QHBoxLayout()
        self.vbox1 = QVBoxLayout()

        # Button Dictionary
        self.btn_dict = {1: QPushButton("New Entry"),
                         2: QPushButton("Edit Entry"),
                         3: QPushButton("Delete Entry"),
                         4: QPushButton("Go Back"),
                         5: QPushButton("Exit")}

        # Create main content grid
        self.grid.addWidget(self.btn_dict[1], 1,1)
        self.grid.addWidget(self.btn_dict[2], 1, 2)
        self.grid.addWidget(self.btn_dict[3], 2, 1)
        self.grid.addWidget(self.btn_dict[4], 2, 2)

        # Make a settings page
        self.settings = QPushButton("Settings")


        self.vbox1.addLayout(self.grid)
        self.vbox1.addStretch()
        self.vbox1.addWidget(self.btn_dict[5])
        self.vbox1.addWidget(self.settings)

        self.setLayout(self.vbox1)

        self.setWindowTitle("Diary Entry")
        self.setGeometry(0,0,1000,400)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(default_stylesheet)
    main_win = MainContent()
    main_win.show()
    sys.exit(app.exec())


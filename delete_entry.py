import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from stylesheet import default_stylesheet



class DeleteEntry(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.setWindowTitle("New Entry")
        self.setGeometry(100,100,600,600)

        self.vbox1 = QVBoxLayout()
        self.label1 = QLabel("Delete Entry", self)
        self.label1.setAlignment(Qt.AlignCenter)
        self.line_edit = QLineEdit(self)

        self.back_button = QPushButton("Back", self)
        self.vbox1.addWidget(self.label1)
        self.vbox1.addWidget(self.line_edit)
        self.openbutton = QPushButton("Open Entry")
        self.openbutton.clicked.connect(self.open_file)
        self.vbox1.addWidget(self.openbutton)
        self.back_button.clicked.connect(self.show_main_content)
        self.delete_button = QPushButton("Delete Entry", self)
        self.delete_button.clicked.connect(self.delete_file)
        self.vbox1.addWidget(self.delete_button)
        self.vbox1.addWidget(self.back_button)
        self.setLayout(self.vbox1)

    def show_main_content(self):
        self.parent.show()
        self.hide()

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        file_name, _= QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files(*)", options = options)

        if file_name:
            self.line_edit.setText(file_name)
            QMessageBox.information(self, 'Success', f'File path "{file_name}" added successfully')
        else:
            QMessageBox.warning(self, 'Error', 'No file selected.')
    def delete_file(self):
        file_path = self.line_edit.text()
        if file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
                QMessageBox.information(self, 'Success', f'File"{file_path}" has been deleted!')
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Failed to delete File: {e}')
        else:
            QMessageBox.warning(self, 'Error', 'File not found or invalid path.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(default_stylesheet)
    Diary_entry = DeleteEntry()
    Diary_entry.show()
    sys.exit(app.exec())
import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from stylesheet import default_stylesheet



class EditEntry(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.setWindowTitle("New Entry")
        self.setGeometry(100,100,600,600)

        self.vbox1 = QVBoxLayout()
        self.label1 = QLabel("Edit Entry", self)
        self.label1.setAlignment(Qt.AlignCenter)
        self.line_edit = QLineEdit(self)

        self.back_button = QPushButton("Back", self)
        self.vbox1.addWidget(self.label1)
        self.vbox1.addWidget(self.line_edit)
        self.openbutton = QPushButton("Open Entry")
        self.openbutton.clicked.connect(self.open_file)
        self.vbox1.addWidget(self.openbutton)
        self.back_button.clicked.connect(self.show_main_content)
        self.save_button = QPushButton("Save Entry", self)
        self.save_button.clicked.connect(self.save_to_file)
        self.vbox1.addWidget(self.save_button)
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
            try:
                with open(file_name, 'r') as file:
                    content = file.read()
                    self.line_edit.clear()
                    self.line_edit.setText(content)
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Failed to read:{e}')
        else:
            pass
    def save_to_file(self):
        text = self.line_edit.text()
        if text:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog

            file_name, _ = QFileDialog.getSaveFileName(self, "Save Text File","","Text Files (*.txt);;All Files(*)", options=options)

            if file_name:
                if not file_name.endswith('.txt'):
                    file_name += '.txt'
                with open(file_name, 'w') as file:
                    file.write(text + '\n')
                QMessageBox.information(self, "Success", f'Text has been saved as {file_name}')
            else:
                QMessageBox.warning(self, "Error", " No folder selected.")
        else:
            QMessageBox.warning(self, 'Error', 'No text to save.')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(default_stylesheet)
    Diary_entry = EditEntry()
    Diary_entry.show()
    sys.exit(app.exec())
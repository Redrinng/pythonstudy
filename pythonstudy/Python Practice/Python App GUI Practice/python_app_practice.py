# Modules
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QComboBox
from googletrans import Translator
from languages import *


# Class
class Home(QWidget):
        # Constructor
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()


    # App Object and Design
    def initUI(self):
        self.input_box = QTextEdit()
        self.output_box = QTextEdit()
        self.reverse = QPushButton('Reverse')
        self.submit_button = QPushButton('Translate')
        self.reset = QPushButton('Reset')
        self.input_option = QComboBox()
        self.output_option = QComboBox()
        self.input_option.addItems(values)
        self.output_option.addItems(values)
        self.title = QLabel('Jelle is also gay But I love Him')

        self.master = QHBoxLayout() #H shaped Layout
        col1 = QVBoxLayout() # Column 1
        col2 = QVBoxLayout() # Column 2
        col1.addWidget(self.title) # Add title to column 1
        col1.addWidget(self.input_option) # Add input option box to column 1
        col1.addWidget(self.output_option) # Add output option box to column 1
        col1.addWidget(self.submit_button) # Add submit button to column 1
        col1.addWidget(self.reset)
        col2.addWidget(self.input_box) # Add input box to column 2
        col2.addWidget(self.reverse)
        col2.addWidget(self.output_box) # Add output box to column 2
        self.master.addLayout(col1, 20) # Add column 1 to master layout occupying 20% of the width
        self.master.addLayout(col2, 80) # Add column 2 to master layout occupying 80% of the width
        self.setLayout(self.master) # Set the master layout as the layout for the app

    # App Settings
    def settings(self):
        self.setWindowTitle("Marcus Is Gay hehe")
        self.setGeometry(250, 250, 600, 500)

    # Button Events
    def button_click(self):
        pass

    # Translate Click
    def translate_click(self):
        value_to_key1 = self.output_option.currentText()
        value_to_key2 = self.input_option.currentText()

        key_to_value1 = [k for k,v in LANGUAGES.items() if v == value_to_key1]
        key_to_value2 = [k for k,v in LANGUAGES.items() if v == value_to_key2]

        self.script = self.translate_text(self.input_box.toPlainText(), key_to_value1[0], key_to_value2[0])
        self.output_box.setText(self.script)

    # Reset App
    def reset_app(self):
        self.input_box.clear()
        self.output_box.clear()


    # Translate Text (Google)
    def translate_text(self, text, dest_lang, src_lang):
        speaker = Translator() # creating a speaker object to speak the text
        translation = speaker.translate(text, dest=dest_lang, src=src_lang)
        return translation.text
    

    # Reverse Translation
    def reverse_click(self):
        s1, l1 = self.input_box.toPlainText(),self.input_option.currentText()
        s2, l2 = self.output_box.toPlainText(),self.output_option.currentText()

        self.input_box.setText(s2)
        self.output_box.setText(s1)

        self.input_option.setCurrentText(l2)
        self.output_option.setCurrentText(l1)


# Main Run

if __name__ == '__main__':
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()


# tutorial video https://www.youtube.com/watch?v=RQOXVpaFYMU

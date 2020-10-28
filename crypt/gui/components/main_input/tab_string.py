from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from crypt.gui.components.main_input.input_string import InputString
from crypt.gui.components.main_input.input_mode import InputMode
from crypt.gui.encryption_parms import EncryptionParms
from crypt.engine.data import *


class TabString(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TabString, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.input_string = InputString()
        self.input_string.text_edit.setPlaceholderText(
            'Input your plain text (e.g. this is not tucil)'
        )
        self.output_string = InputString(enabled=False)
        self.input_mode = InputMode()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input_string)
        self.layout.addWidget(self.input_mode)
        self.layout.addWidget(self.output_string)

        self.setLayout(self.layout)

        self.output_string.btn_copy_field.clicked.connect(self.copy_output_to_input)

    def copy_output_to_input(self):
        output = self.output_string.text_edit.toPlainText()
        self.input_string.text_edit.setText(output)

    def build_data(self):
        text = self.input_string.text_edit.toPlainText()
        return Data(DataType.TEXT, text)
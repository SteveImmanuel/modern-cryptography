from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QSizePolicy, QSpacerItem, QHBoxLayout, QPushButton

from crypt.gui.components.configuration_box.base_keygen import BaseKeygen
from crypt.gui.components.configuration_box.edit_with_button import EditWithButton
from crypt.gui.components.main_input.input_file import InputFile
from crypt.engine.key import *


class RSAKeygen(BaseKeygen):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.p_value = EditWithButton('p value', 'Randomize')
        self.q_value = EditWithButton('q value', 'Randomize')
        self.output_file = InputFile('Output directory', 'Browse')
        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.p_value)
        self.layout.addWidget(self.q_value)
        self.layout.addSpacerItem(self.spacer)
        self.layout.addWidget(self.output_file)

        self.setLayout(self.layout)

    def build_key(self) -> Key:
        text = self.line_edit.text()
        return Key(KeyType.STRING, [text])

from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QSizePolicy, QSpacerItem, QHBoxLayout, QPushButton, QLabel

from crypt.gui.components.configuration_box.base_key_setup import BaseKeySetup
from crypt.gui.components.configuration_box.edit_with_button import EditWithButton
from crypt.gui.components.main_input.input_file import InputFile
from crypt.engine.key import *


class RSAKeySetup(BaseKeySetup):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.lbl_private = QLabel('Private Key')
        self.lbl_public = QLabel('Public Key')
        self.d_private = EditWithButton('d value', 'Load From File')
        self.n_private = EditWithButton('n value', 'Load From File')
        self.e_public = EditWithButton('e value', 'Load From File')
        self.n_public = EditWithButton('n value', 'Load From File')
        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_private)
        self.layout.addWidget(self.d_private)
        self.layout.addWidget(self.n_private)
        self.layout.addSpacerItem(self.spacer)
        self.layout.addWidget(self.lbl_public)
        self.layout.addWidget(self.e_public)
        self.layout.addWidget(self.n_public)

        self.setLayout(self.layout)

    def apply_key(self, key: Key):
        pass

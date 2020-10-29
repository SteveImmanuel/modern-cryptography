from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QSizePolicy, QSpacerItem, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog
from PyQt5 import QtCore

from crypt.gui.encryption_parms import EncryptionParms
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
        self.btn_browse_private = QPushButton('Load from File')
        self.btn_browse_private.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.btn_browse_public = QPushButton('Load from File')
        self.btn_browse_public.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.d_private = QLineEdit()
        self.d_private.setPlaceholderText('d value')
        self.n_private = QLineEdit()
        self.n_private.setPlaceholderText('n value')
        self.e_public = QLineEdit()
        self.e_public.setPlaceholderText('e value')
        self.n_public = QLineEdit()
        self.n_public.setPlaceholderText('n value')
        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.h_spacer_1 = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.h_spacer_2 = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.h_layout_1 = QHBoxLayout()
        self.h_layout_1.addWidget(self.lbl_private)
        self.h_layout_1.addSpacerItem(self.h_spacer_1)
        self.h_layout_1.addWidget(self.btn_browse_private)

        self.h_layout_2 = QHBoxLayout()
        self.h_layout_2.addWidget(self.lbl_public)
        self.h_layout_2.addSpacerItem(self.h_spacer_2)
        self.h_layout_2.addWidget(self.btn_browse_public)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.h_layout_1)
        self.layout.addWidget(self.d_private)
        self.layout.addWidget(self.n_private)
        self.layout.addSpacerItem(self.spacer)
        self.layout.addLayout(self.h_layout_2)
        self.layout.addWidget(self.e_public)
        self.layout.addWidget(self.n_public)

        self.setLayout(self.layout)
        self.btn_browse_private.clicked.connect(lambda: self.browse_key(is_private=True))
        self.btn_browse_public.clicked.connect(lambda: self.browse_key(is_private=False))

    def browse_key(self, is_private: bool):
        filepath, _ = QFileDialog.getOpenFileName(
            self, 'Single File', QtCore.QDir.currentPath(), '*.pub *.pri'
        )
        if filepath:
            key = EncryptionParms.get_instance().get_engine().load_key(filepath)
            self.apply_key(key, is_private)

    def build_key(self, is_private: bool) -> Key:
        if is_private:
            n_private = int(self.n_private.text())
            d_private = int(self.d_private.text())
            return Key([n_private, d_private])
        else:
            n_public = int(self.n_public.text())
            e_public = int(self.e_public.text())
            return Key([n_public, e_public])

    def apply_key(self, key: Key, is_private: bool):
        if is_private:
            n_private = key.value[0]
            d_private = key.value[1]
            self.n_private.setText(str(n_private))
            self.d_private.setText(str(d_private))
        else:
            n_public = key.value[0]
            e_public = key.value[1]
            self.n_public.setText(str(n_public))
            self.e_public.setText(str(e_public))

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QSpacerItem, QHBoxLayout, QPushButton, QLabel, QLineEdit, \
    QFileDialog

from crypt.engine.key import *
from crypt.gui.components.configuration_box.base_key_setup import BaseKeySetup
from crypt.gui.encryption_parms import EncryptionParms


class DHKeySetup(BaseKeySetup):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.lbl_session = QLabel('Session Key')
        self.btn_browse = QPushButton('Load from File')
        self.edit_value = QLineEdit()
        self.edit_value.setPlaceholderText('Session key value')
        self.spacer = QSpacerItem(30, 30, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.h_spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.lbl_session)
        self.h_layout.addSpacerItem(self.h_spacer)
        self.h_layout.addWidget(self.btn_browse)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.h_layout)
        self.layout.addWidget(self.edit_value)
        self.layout.addSpacerItem(self.spacer)

        self.setLayout(self.layout)
        self.btn_browse.clicked.connect(self.browse_key)

    def browse_key(self):
        filepath, _ = QFileDialog.getOpenFileName(
            self, 'Single File', QtCore.QDir.currentPath(), '*.ses'
        )
        if filepath:
            key = EncryptionParms.get_instance().get_engine().load_key(filepath)
            self.apply_key(key, True)

    def build_key(self, is_private: bool) -> Key:
        return Key([int(self.edit_value.text())])

    def apply_key(self, key: Key, is_private: bool):
        self.edit_value.setText(str(key.value[0]))

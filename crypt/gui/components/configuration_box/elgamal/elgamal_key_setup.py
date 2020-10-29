from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QSpacerItem, QHBoxLayout, QPushButton, QLabel, QLineEdit, \
    QFileDialog

from crypt.engine.key import *
from crypt.gui.components.configuration_box.base_key_setup import BaseKeySetup
from crypt.gui.encryption_parms import EncryptionParms


class ElgamalKeySetup(BaseKeySetup):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.lbl_private = QLabel('Private Key')
        self.lbl_public = QLabel('Public Key')
        self.btn_browse_private = QPushButton('Load From File')
        self.btn_browse_private.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.btn_browse_public = QPushButton('Load From File')
        self.btn_browse_public.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.x_private = QLineEdit()
        self.x_private.setPlaceholderText('x value')
        self.p_private = QLineEdit()
        self.p_private.setPlaceholderText('p value')
        self.y_public = QLineEdit()
        self.y_public.setPlaceholderText('y value')
        self.g_public = QLineEdit()
        self.g_public.setPlaceholderText('g value')
        self.p_public = QLineEdit()
        self.p_public.setPlaceholderText('p value')
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
        self.layout.addWidget(self.x_private)
        self.layout.addWidget(self.p_private)
        self.layout.addSpacerItem(self.spacer)
        self.layout.addLayout(self.h_layout_2)
        self.layout.addWidget(self.y_public)
        self.layout.addWidget(self.g_public)
        self.layout.addWidget(self.p_public)

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
            x_private = int(self.x_private.text())
            p_private = int(self.p_private.text())
            return Key([x_private, p_private])
        else:
            y_public = int(self.y_public.text())
            g_public = int(self.g_public.text())
            p_public = int(self.p_public.text())
            return Key([y_public, g_public, p_public])

    def apply_key(self, key: Key, is_private: bool):
        if is_private:
            x_private = key.value[0]
            p_private = key.value[1]
            self.x_private.setText(str(x_private))
            self.p_private.setText(str(p_private))
        else:
            y_public = key.value[0]
            g_public = key.value[1]
            p_public = key.value[2]
            self.y_public.setText(str(y_public))
            self.g_public.setText(str(g_public))
            self.p_public.setText(str(p_public))

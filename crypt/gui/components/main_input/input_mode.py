from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

from crypt.gui.encryption_parms import ModeType, EncryptionParms


class InputMode(QWidget):
    def __init__(self, parent=None):
        super(InputMode, self).__init__(parent)
        self.is_encrypt = False
        self.setup_ui()

    def setup_ui(self):
        self.btn_switch = QPushButton('Switch Mode')
        self.btn_execute = QPushButton('Execute')
        self.lbl_mode_title = QLabel('Mode')
        self.lbl_colon = QLabel(':')
        self.lbl_mode_value = QLabel('Encrypt')

        self.lbl_mode_title.setAlignment(Qt.AlignRight)
        self.lbl_colon.setAlignment(Qt.AlignCenter)
        self.lbl_mode_value.setAlignment(Qt.AlignLeft)

        self.spacer = QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.h_layout_1 = QHBoxLayout()
        self.h_layout_2 = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout_1.addWidget(self.lbl_mode_title)
        self.h_layout_1.addWidget(self.lbl_colon)
        self.h_layout_1.addWidget(self.lbl_mode_value)
        self.h_layout_2.addWidget(self.btn_switch)
        self.h_layout_2.addWidget(self.btn_execute)

        self.v_layout.addLayout(self.h_layout_1)
        self.v_layout.addLayout(self.h_layout_2)

        self.setLayout(self.v_layout)

        self.btn_switch.clicked.connect(self.switch_mode)
        self.btn_execute.clicked.connect(self.execute)
        self.btn_switch.animateClick()

    def switch_mode(self):
        self.is_encrypt = not self.is_encrypt
        if self.is_encrypt:
            mode = ModeType.ENCRYPT
        else:
            mode = ModeType.DECRYPT

        EncryptionParms.get_instance().mode = mode
        self.lbl_mode_value.setText(mode.value)

    def execute(self):
        EncryptionParms.get_instance().print_info()

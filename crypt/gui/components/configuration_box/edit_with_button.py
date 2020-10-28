from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QSizePolicy, QSpacerItem, QHBoxLayout, QPushButton


class EditWithButton(QWidget):
    def __init__(self, text_placeholder: str, text_btn: str, parent: QWidget = None):
        super().__init__(parent)
        self.text_placeholder = text_placeholder
        self.text_btn = text_btn
        self.setup_ui()

    def setup_ui(self):
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(self.text_placeholder)
        self.line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.btn_random = QPushButton(self.text_btn)
        self.btn_random.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.line_edit)
        self.h_layout.addWidget(self.btn_random)

        self.setLayout(self.h_layout)

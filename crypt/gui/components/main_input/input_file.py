from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import QSize


class InputFile(QWidget):
    def __init__(self, placeholder_text: str, btn_text: str, parent: QWidget = None):
        super(InputFile, self).__init__(parent=parent)
        self.btn_text = btn_text
        self.placeholder_text = placeholder_text
        self.setup_ui()

    def setup_ui(self):
        self.line_edit = QLineEdit()
        self.line_edit.setEnabled(False)
        self.line_edit.setPlaceholderText(self.placeholder_text)
        self.line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.btn_browse = QPushButton(self.btn_text)
        self.btn_browse.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.btn_browse)

        self.setLayout(self.layout)

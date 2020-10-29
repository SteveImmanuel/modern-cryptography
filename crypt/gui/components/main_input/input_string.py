from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QSizePolicy


class InputString(QWidget):
    def __init__(self, enabled: bool = True, parent: QWidget = None):
        super(InputString, self).__init__(parent=parent)
        self.enabled = enabled
        self.setup_ui()

    def setup_ui(self):
        self.text_edit = QTextEdit()
        self.text_edit.setEnabled(self.enabled)
        self.text_edit.setAcceptRichText(False)
        self.text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.btn_copy_clipboard = QPushButton('Copy to Clipboard')

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.text_edit)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.btn_copy_clipboard)
        self.v_layout.addLayout(self.h_layout)

        if not self.enabled:
            self.btn_copy_field = QPushButton('Copy to Input')
            self.h_layout.addWidget(self.btn_copy_field)

            self.btn_save_to_file = QPushButton('Save to File')
            self.v_layout.addWidget(self.btn_save_to_file)
        else:
            self.btn_load_from_file = QPushButton('Load from File')
            self.v_layout.addWidget(self.btn_load_from_file)

        self.setLayout(self.v_layout)

        self.btn_copy_clipboard.clicked.connect(self.copy_to_clipboard)

    def on_load_from_file(self, text: str):
        self.text_edit.setText(text)

    def copy_to_clipboard(self):
        text = self.text_edit.toPlainText()
        clip_board = QGuiApplication.clipboard()
        clip_board.clear(mode=clip_board.Clipboard)
        clip_board.setText(text, mode=clip_board.Clipboard)

    @pyqtSlot(object)
    def on_result_update(self, result: str):
        self.text_edit.setPlainText(result)

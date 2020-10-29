from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QFileDialog

from crypt.engine.data import *
from crypt.gui.components.main_input.input_file import InputFile
from crypt.gui.components.main_input.input_mode import InputMode


class TabFile(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TabFile, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.input_file = InputFile('Input file path', 'Import')
        self.output_file = InputFile('Output file path', 'Browse')
        self.input_mode = InputMode()

        self.layout = QVBoxLayout()
        self.layout.addSpacerItem(
            QSpacerItem(30, 30, QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        )
        self.layout.addSpacerItem(QSpacerItem(30, 50, QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.layout.addWidget(self.input_file)
        self.layout.addWidget(self.output_file)
        self.layout.addSpacerItem(QSpacerItem(30, 50, QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.layout.addWidget(self.input_mode)
        self.layout.addSpacerItem(
            QSpacerItem(30, 30, QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        )

        self.setLayout(self.layout)
        self.input_file.btn_browse.clicked.connect(lambda: self.get_directory(is_input=True))
        self.output_file.btn_browse.clicked.connect(lambda: self.get_directory(is_input=False))

    def get_directory(self, is_input: bool):
        if is_input:
            filepath, _ = QFileDialog.getOpenFileName(
                self, 'Single File', QtCore.QDir.currentPath(), '*'
            )
            if filepath:
                self.input_file.line_edit.setText(filepath)
        else:
            default_name = 'cipher_out'
            filepath, _ = QFileDialog.getSaveFileName(
                self, 'Save File',
                QtCore.QDir.currentPath() + '/' + default_name
            )
            if filepath:
                self.output_file.line_edit.setText(filepath)

    def build_data(self) -> Data:
        filepath = self.input_file.line_edit.text()
        output_path = self.output_file.line_edit.text()
        return Data(DataType.FILE, filepath, output_path)

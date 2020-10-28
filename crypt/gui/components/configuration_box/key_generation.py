from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout, QSizePolicy, QGroupBox, QPushButton, QFileDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

from crypt.gui.encryption_parms import EncryptionParms
from crypt.gui.components.configuration_box.key_widget_factory import *
from crypt.gui.components.main_input.input_file import InputFile
from crypt.engine.key import Key


class KeyGeneration(QGroupBox):
    def __init__(self, parent: QWidget = None):
        super(KeyGeneration, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.setTitle('Key Generation')

        self.key_input = KeyWidgetFactory.create_keygen_widget(EngineType.RSA)
        self.output_file = InputFile('Output directory', 'Browse')
        self.btn_generate = QPushButton('Generate Random Key')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.key_input)
        self.layout.addWidget(self.output_file)
        self.layout.addWidget(self.btn_generate)
        self.layout.setSpacing(20)

        self.setLayout(self.layout)

        self.btn_generate.clicked.connect(self.generate_key)
        self.output_file.btn_browse.clicked.connect(self.get_directory)

    def get_directory(self):
        dir_path = QFileDialog.getExistingDirectory(
            self, 'Select Directory', QtCore.QDir.currentPath()
        )

        if dir_path:
            self.output_file.line_edit.setText(dir_path)

    def generate_key(self):
        engine = EncryptionParms.get_instance().get_engine()
        key = engine.generate_random_key()
        self.key_input.apply_key(key)

    def apply_key(self, key: Key):
        self.key_input.apply_key(key)

    def get_key(self) -> Key:
        return self.key_input.build_key()

    @pyqtSlot(object)
    def on_update_key_widget(self, engine_type: EngineType):
        self.layout.removeWidget(self.key_input)
        self.layout.removeWidget(self.btn_generate)

        self.key_input.deleteLater()
        self.key_input = KeyWidgetFactory.create_widget(engine_type)

        self.layout.addWidget(self.key_input)
        self.layout.addWidget(self.btn_generate)

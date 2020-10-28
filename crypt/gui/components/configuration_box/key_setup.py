from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QSizePolicy, QSpacerItem, QGroupBox

from crypt.gui.encryption_parms import OutputType, EncryptionParms
from crypt.gui.components.configuration_box.key_widget_factory import *


class KeySetup(QGroupBox):
    def __init__(self, parent: QWidget = None):
        super(KeySetup, self).__init__(parent=parent)
        self.output_type_list = OutputType.list()
        self.setup_ui()

    def setup_ui(self):
        self.setTitle('Key Setup')
        self.layout = QVBoxLayout()

        self.key_input = KeyWidgetFactory.create_key_setup_widget(EngineType.RSA)

        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        self.layout.addWidget(self.key_input)
        self.layout.addSpacerItem(self.spacer)
        self.layout.setSpacing(20)
        self.setLayout(self.layout)
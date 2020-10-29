from PyQt5.QtWidgets import QWidget, QVBoxLayout, QButtonGroup, QRadioButton, QSizePolicy, QComboBox
from PyQt5.QtCore import QSize

from crypt.gui.components.configuration_box.keygen import Keygen
from crypt.gui.components.configuration_box.key_setup import KeySetup
from crypt.engine.engine_factory import EngineType
from crypt.gui.encryption_parms import EncryptionParms

class ConfigurationBox(QWidget):
    def __init__(self, parent: QWidget = None):
        super(ConfigurationBox, self).__init__(parent=parent)
        self.list_of_algorithm = EngineType.list()
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()

        self.combo_box = QComboBox()
        self.combo_box.addItems(map(lambda x: x.value, self.list_of_algorithm))

        self.keygen = Keygen()
        self.keygen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.key_setup = KeySetup()
        self.key_setup.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.keygen)
        self.layout.addWidget(self.key_setup)

        self.setLayout(self.layout)
        self.layout.setSpacing(20)

        self.combo_box.currentIndexChanged.connect(self.set_engine_type)

    def set_engine_type(self, idx:int):
        EncryptionParms.get_instance().update_engine_type(self.list_of_algorithm[idx])
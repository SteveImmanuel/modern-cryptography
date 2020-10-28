from PyQt5.QtWidgets import QWidget, QVBoxLayout, QButtonGroup, QRadioButton, QSizePolicy, QComboBox
from PyQt5.QtCore import QSize

from crypt.gui.components.configuration_box.key_generation import KeyGeneration
from crypt.gui.components.configuration_box.key_setup import KeySetup
from crypt.engine.engine_factory import EngineType


class ConfigurationBox(QWidget):
    def __init__(self, parent: QWidget = None):
        super(ConfigurationBox, self).__init__(parent=parent)
        self.list_of_algorithm = EngineType.list()
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()

        self.combo_box = QComboBox()
        self.combo_box.addItems(map(lambda x: x.value, self.list_of_algorithm))

        self.key_generation = KeyGeneration()
        self.key_generation.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.key_setup = KeySetup()
        self.key_setup.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.key_generation)
        self.layout.addWidget(self.key_setup)

        self.setLayout(self.layout)
        self.layout.setSpacing(20)
        # self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
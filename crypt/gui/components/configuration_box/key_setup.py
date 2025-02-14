from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox

from crypt.engine.key import *
from crypt.gui.components.configuration_box.key_widget_factory import *


class KeySetup(QGroupBox):
    def __init__(self, parent: QWidget = None):
        super(KeySetup, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.setTitle('Key Setup')
        self.layout = QVBoxLayout()

        self.key_input = KeyWidgetFactory.create_key_setup_widget(EngineType.RSA)
        self.layout.addWidget(self.key_input)
        self.layout.setSpacing(20)
        self.setLayout(self.layout)

    def get_key(self, is_private: bool) -> Key:
        return self.key_input.build_key(is_private)

    @pyqtSlot(object)
    def on_update_key_setup_widget(self, engine_type: EngineType):
        self.layout.removeWidget(self.key_input)

        self.key_input.deleteLater()
        self.key_input = KeyWidgetFactory.create_key_setup_widget(engine_type)

        self.layout.addWidget(self.key_input)

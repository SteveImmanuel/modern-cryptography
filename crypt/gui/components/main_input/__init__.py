from PyQt5.QtWidgets import QGroupBox, QWidget, QVBoxLayout, QTabWidget, QSizePolicy
from PyQt5.QtCore import QSize, pyqtSlot

from crypt.gui.components.main_input.tab_file import TabFile
from crypt.gui.components.main_input.tab_string import TabString
from crypt.engine.engine_factory import EngineType
from crypt.engine.data import Data


class MainInput(QTabWidget):
    def __init__(self, parent: QWidget = None):
        super(MainInput, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.tab_string = TabString()
        self.tab_file = TabFile()
        self.addTab(self.tab_string, 'String Input')
        self.addTab(self.tab_file, 'File Input')
        self.setCurrentIndex(0)
        self.currentChanged.connect(self.update_mode)

    def update_mode(self, idx:int):
        if idx==0:
            self.tab_string.input_mode.switch_mode()
            self.tab_string.input_mode.switch_mode()
        else:
            self.tab_file.input_mode.switch_mode()
            self.tab_file.input_mode.switch_mode()

    def get_data(self) -> Data:
        if self.currentWidget() == self.tab_string:
            return self.tab_string.build_data()
        else:
            return self.tab_file.build_data()


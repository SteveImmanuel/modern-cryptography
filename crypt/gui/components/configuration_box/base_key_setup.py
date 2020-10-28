from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget
from crypt.engine.key import *


class BaseKeySetup(QWidget):
    def __init__(self, parent: QWidget = None):
        super(BaseKeySetup, self).__init__(parent=parent)

    @abstractmethod
    def apply_key(self, key: Key):
        pass

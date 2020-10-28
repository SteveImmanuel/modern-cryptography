from abc import ABC, abstractmethod
from typing import List
from PyQt5.QtWidgets import QWidget
from crypt.engine.key import *


class BaseKeygen(QWidget):
    def __init__(self, parent: QWidget = None):
        super(BaseKeygen, self).__init__(parent=parent)

    @abstractmethod
    def build_params(self) -> List[int]:
        pass

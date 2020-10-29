from __future__ import annotations

from PyQt5.QtCore import pyqtSignal, QObject

from crypt.engine.base_engine import BaseEngine
from crypt.engine.data import *
from crypt.engine.engine_factory import *


class ParamsSignal(QObject):
    engine_type = pyqtSignal(object)


class ModeType(Enum):
    ENCRYPT = 'Encrypt'
    DECRYPT = 'Decrypt'


class EncryptionParms:
    __instance = None

    def __init__(self):
        if EncryptionParms.__instance is not None:
            raise Exception('Only allowed 1 instance')
        else:
            EncryptionParms.__instance = self
            self.signal = ParamsSignal()
            self.mode = None
            self.engine_type = EngineType.RSA

    def print_info(self):
        print('***Encryption Parameters***')
        print('Mode:', self.mode)
        print('Engine Type:', self.engine_type)
        print('***************************')

    def update_engine_type(self, engine_type: EngineType):
        self.engine_type = engine_type
        self.signal.engine_type.emit(engine_type)
        self.print_info()

    def get_engine(self) -> BaseEngine:
        return EngineFactory.create_engine(self.engine_type)

    @staticmethod
    def get_instance() -> EncryptionParms:
        if EncryptionParms.__instance is None:
            EncryptionParms()
        return EncryptionParms.__instance

from __future__ import annotations
from enum import Enum
from PyQt5.QtCore import pyqtSignal, QObject

from crypt.engine.engine_factory import *
from crypt.engine.base_engine import BaseEngine
from crypt.engine.data import *
from crypt.engine.key import *


class ParamsSignal(QObject):
    engine_type = pyqtSignal(object)
    output_type = pyqtSignal(object)


class ModeType(Enum):
    ENCRYPT = 'Encrypt'
    DECRYPT = 'Decrypt'


class OutputType(Enum):
    NO_SPACE = 'Remove whitespace'
    GROUP = 'Group in 5'

    @staticmethod
    def list():
        return list(map(lambda out_type: out_type, OutputType))


class EncryptionParms:
    __instance = None

    def __init__(self):
        if EncryptionParms.__instance is not None:
            raise Exception('Only allowed 1 instance')
        else:
            EncryptionParms.__instance = self
            self.signal = ParamsSignal()
            self.mode = None
            self.engine = None
            self.engine_type = EngineType.RSA
            self.old_engine_type = None
            self.output_conf = None

    def print_info(self):
        print('***Encryption Parameters***')
        print('Mode:', self.mode)
        print('Engine Type:', self.engine_type)
        print('Output Configuration:', self.output_conf)
        print('***************************')

    def update_engine_type(self, engine_type: EngineType):
        self.old_engine_type = self.engine_type
        self.engine_type = engine_type
        self.signal.engine_type.emit(engine_type)

    def update_output_type(self, output_type: OutputType):
        self.output_conf = output_type
        self.signal.output_type.emit(output_type)

    def is_parameter_valid(self) -> bool:
        return True

    def get_engine(self) -> BaseEngine:
        if self.engine_type == self.old_engine_type:
            return self.engine
        else:
            return EngineFactory.create_engine(self.engine_type)

    @staticmethod
    def get_instance() -> EncryptionParms:
        if EncryptionParms.__instance is None:
            EncryptionParms()
        return EncryptionParms.__instance

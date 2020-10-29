from enum import Enum

from crypt.engine.base_engine import BaseEngine
from crypt.engine.elgamal import Elgamal
from crypt.engine.rsa import RSA


class EngineType(Enum):
    RSA = 'RSA (Rivest-Shamir-Adleman)'
    ELGAMAL = 'El-Gamal'

    @staticmethod
    def list():
        return list(map(lambda engine: engine, EngineType))


class EngineFactory():
    @staticmethod
    def create_engine(engine_type: EngineType) -> BaseEngine:
        if engine_type == EngineType.RSA:
            return RSA()
        elif engine_type == EngineType.ELGAMAL:
            return Elgamal()
        else:
            raise Exception('Engine not found')
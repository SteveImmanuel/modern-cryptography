from abc import ABC, abstractmethod
from crypt.engine.key import *
from crypt.engine.data import *


class BaseEngine(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def encrypt(self, public_key: Key, plain_text: Data):
        pass

    @abstractmethod
    def decrypt(self, secret_key: Key, cipher_text: Data):
        pass

    @abstractmethod
    def generate_key(self, params: List[int], output_path: str):
        pass
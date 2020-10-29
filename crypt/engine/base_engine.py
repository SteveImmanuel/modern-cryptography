import pickle

from abc import ABC, abstractmethod
from crypt.engine.key import *
from crypt.engine.data import *


class BaseEngine(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def encrypt(self, public_key: Key, plain_text: Data) -> str:
        pass

    @abstractmethod
    def decrypt(self, secret_key: Key, cipher_text: Data) -> str:
        pass

    @abstractmethod
    def generate_key(self, params: List[int], output_path: str = '.') -> str:
        pass

    def load_key(self, key_path: str) -> Key:
        with open(key_path, 'rb') as key_file:
            key = pickle.load(key_file)
        return key
import pickle
from abc import ABC, abstractmethod
from typing import Tuple, Union

from crypt.engine.data import *
from crypt.engine.key import *


class BaseEngine(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def encrypt(self, public_key: Key, plain_text: Data) -> Union[str, Tuple[str, str]]:
        pass

    @abstractmethod
    def decrypt(self, secret_key: Key, cipher_text: Data) -> Union[str, Tuple[str, str]]:
        pass

    @abstractmethod
    def generate_key(self, params: List[int], output_path: str = '.') -> str:
        pass

    @staticmethod
    def get_exec_info(time_execution: float, size_before: int, size_after: int, save_location: str = None):
        formatted_time = '{:.5f}'.format(time_execution)
        info = 'Execution complete\n'
        info += f'Time execution: {formatted_time} s\n'
        info += f'Size before: {size_before} bytes\n'
        info += f'Size after: {size_after} bytes\n'
        if save_location:
            info += f'File saved in {save_location}\n'
        return info

    def load_key(self, key_path: str) -> Key:
        with open(key_path, 'rb') as key_file:
            key = pickle.load(key_file)
        return key

from typing import List
from enum import Enum


class DataType(Enum):
    TEXT = 'text'
    FILE = 'file'


class Data():
    def __init__(self, data_type: DataType, value: str):
        self.type = data_type
        self.value = value
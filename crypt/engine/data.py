from enum import Enum


class DataType(Enum):
    TEXT = 'text'
    FILE = 'file'


class Data():
    def __init__(self, data_type: DataType, value: str, output_path: str = None):
        self.data_type = data_type
        self.value = value
        if self.data_type == DataType.FILE:
            self.output_path = output_path
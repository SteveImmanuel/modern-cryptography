from abc import ABC, abstractmethod

class BaseEngine(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass
    
    @abstractmethod
    def generate_key(self, output_path:str):
        pass
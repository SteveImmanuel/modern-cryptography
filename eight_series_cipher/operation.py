import random
from abc import ABC, abstractmethod
from typing import List

from eight_series_cipher.cipher import BLOCK_SIZE, Cipher


class Operation(ABC):
    def __init__(self, key: str) -> None:
        Cipher.generate_internal_key(key)

    @staticmethod
    def grouping(input_val: str):
        bit_rep = Cipher.string_to_bits(input_val)
        for i in range(0, len(bit_rep), BLOCK_SIZE):
            one_block = bit_rep[i:i + BLOCK_SIZE]
            if len(one_block) < BLOCK_SIZE:
                one_block += [0] * (BLOCK_SIZE - len(one_block))
            yield one_block

    @abstractmethod
    def encipher(self, input_val: str) -> str:
        return input_val

    @abstractmethod
    def decipher(self, input_val: str) -> str:
        return input_val


class ECB(Operation):
    def encipher(self, input_val: str) -> str:
        out = []
        for block in Operation.grouping(input_val):
            out += Cipher.encipher(block)

        return Cipher.bits_to_string(out)

    def decipher(self, input_val: str) -> str:
        out = []
        for block in Operation.grouping(input_val):
            out += Cipher.decipher(block)

        return Cipher.bits_to_string(out)


class CBC(Operation):
    def __init__(self, key):
        super().__init__(key)
        self.prev_val = CBC.init_vector(BLOCK_SIZE)

    @staticmethod
    def init_vector(block_size: int) -> List[int]:
        init_vector = []
        for _ in range(block_size):
            init_vector.append(random.randint(0, 1))
        return init_vector

    def encipher(self, input_val: str) -> str:
        out = self.prev_val
        for block in Operation.grouping(input_val):
            self.prev_val = Cipher.encipher(
                [block[i] ^ self.prev_val[i] for i in range(BLOCK_SIZE)])
            out += self.prev_val
        return Cipher.bits_to_string(out)

    def decipher(self, input_val: str) -> str:
        out = []
        first = True
        for block in Operation.grouping(input_val):
            if first:
                self.prev_val = block
                first = False
                continue

            result = Cipher.decipher(block)
            out += [result[i] ^ self.prev_val[i] for i in range(BLOCK_SIZE)]
            self.prev_val = block
        return Cipher.bits_to_string(out)


class Counter(Operation):
    @staticmethod
    def init_counter(block_size: int) -> List[int]:
        random.seed(block_size)
        bit_rep = '{:0144b}'.format(random.randint(0, 2**144 - 1))
        return [int(bit) for bit in bit_rep]

    @staticmethod
    def increment_counter(counter: List[int]) -> List[int]:

        string_array = map(str, counter)
        string_array = ''.join(string_array)
        dec = '0b' + string_array
        int_counter = int(dec, 2)

        int_counter += 1
        int_counter %= (2**145 - 1)

        bit_rep = '{:0144b}'.format(int_counter)
        return [int(bit) for bit in bit_rep]

    def encipher(self, input_val: str) -> str:
        counter = Counter.init_counter(BLOCK_SIZE)
        out = []
        for block in Operation.grouping(input_val):
            result = Cipher.encipher(counter)
            out += [result[i] ^ block[i] for i in range(BLOCK_SIZE)]
            counter = Counter.increment_counter(counter)

        return Cipher.bits_to_string(out)

    def decipher(self, input_val: str) -> str:
        return self.encipher(input_val)

import random
import math

from typing import List
from crypt.engine.base_engine import BaseEngine
from crypt.engine.key import *
from crypt.engine.data import *
from crypt.utils.number_util import *
from crypt.utils.string_util import *

class Elgamal(BaseEngine):
    def encrypt(self, public_key: Key, plain_text: Data):
        y = public_key.value[0]
        g = public_key.value[1]
        p = public_key.value[2]

        block_size = get_block_size(p)

        if plain_text.type == DataType.TEXT:
            block_text = group_string(plain_text.value, block_size)
            block_text = map(string_to_int, block_text)
            result = []
            for text in block_text:
                k = random.randrange(1, p-1, 1)
                a = pow(g,k,p)

                b = (pow(y,k) * text) % p

                result.append(str(a))
                result.append(str(b))
            return ' '.join(result)
        else:
            raise NotImplementedError('Belum dibuat')

    def decrypt(self, secret_key: Key, cipher_text: Data):
        x = secret_key.value[0]
        p = secret_key.value[1]

        if cipher_text.type == DataType.TEXT:
            block_text = cipher_text.value.split(' ')
            block_text = map(int, block_text)
            result = []

            idx = 1
            a = 0
            b = 0
            
            for text in block_text:
                if (idx==1):
                    a = text
                    idx += 1
                else:
                    b = text
                    a_x_inverse = pow(a, p-1-x, p)
                    cipher = (b * a_x_inverse) % p
                    result.append(int_to_string(cipher))
                    idx = 1
            return ''.join(result)
        else:
            raise NotImplementedError('Belum dibuat')

    def generate_key(self, params: List[int], output_path: str):
        p, g, x = params
        y = pow(g,x,p)

        return g, p, x, y

if __name__ == "__main__":
    elgamal = Elgamal()
    data = Data(DataType.TEXT, 'abcdeajdkasdkakdsasdnoqjwneoqiwjeqowijeqwoiejqwoejio')
    g, p, x, y = elgamal.generate_key([2357, 2, 1751], 'a')
    public_key = Key([y, g, p])
    secret_key = Key([x,p])

    result = elgamal.encrypt(public_key, data)
    print(result)

    data = Data(DataType.TEXT, result)
    result = elgamal.decrypt(secret_key, data)
    print(result)
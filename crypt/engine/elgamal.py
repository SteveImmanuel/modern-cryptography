import pickle

from crypt.constant import MAX_CHUNK_SIZE
from crypt.engine.base_engine import BaseEngine
from crypt.engine.data import *
from crypt.engine.key import *
from crypt.utils.bytes_util import *
from crypt.utils.file_util import *
from crypt.utils.number_util import *

class Elgamal(BaseEngine):
    def encrypt(self, public_key: Key, plain_text: Data) -> str:
        y = public_key.value[0]
        g = public_key.value[1]
        p = public_key.value[2]

        block_size = get_block_size(p)
        max_digit = get_digit_count(p)

        if plain_text.data_type == DataType.TEXT:
            block_bytes = group_bytes(plain_text.value, block_size)
            block_bytes = map(lambda x: bytes_to_int(x, True), block_bytes)
            result = []

            for element in block_bytes:
                k = generate_random_number(1, p - 1)
                a = pow(g, k, p)
                b = (pow(y, k, p) * (element % p)) % p

                result.append(str(a).rjust(max_digit, '0'))
                result.append(str(b).rjust(max_digit, '0'))
            return ''.join(result)
        else:
            chunk_size = MAX_CHUNK_SIZE - (MAX_CHUNK_SIZE % block_size)
            with open(plain_text.output_path, 'w') as out:
                for chunk in load_file(plain_text.value, chunk_size):
                    block_bytes = group_bytes(chunk, block_size)
                    block_bytes = map(bytes_to_int, block_bytes)

                    for element in block_bytes:
                        k = generate_random_number(1, p - 1)
                        a = pow(g, k, p)
                        b = (pow(y, k, p) * (element % p)) % p
                        out.write(str(a).rjust(max_digit, '0'))
                        out.write(str(b).rjust(max_digit, '0'))
            return f'Execution complete. File saved in {plain_text.output_path}.'

    def decrypt(self, secret_key: Key, cipher_text: Data) -> str:
        x = secret_key.value[0]
        p = secret_key.value[1]

        block_size = get_block_size(p)
        max_digit = get_digit_count(p)

        if cipher_text.data_type == DataType.TEXT:
            block_bytes = group_bytes(cipher_text.value, max_digit)
            block_bytes = map(int, block_bytes)
            result = []

            next_element = True
            a = 0
            b = 0
            for element in block_bytes:
                if (next_element):
                    a = element
                    next_element = False
                else:
                    b = element
                    a_x_inverse = pow(a, p - 1 - x, p)
                    cipher = ((b % p) * (a_x_inverse % p)) % p
                    result.append(int_to_bytes(cipher, block_size, True))
                    next_element = True
            return ''.join(result)
        else:
            chunk_size = MAX_CHUNK_SIZE - (MAX_CHUNK_SIZE % max_digit)
            with open(cipher_text.output_path, 'wb') as out:
                for chunk in load_file(cipher_text.value, chunk_size):
                    block_bytes = group_bytes(chunk, max_digit)
                    block_bytes = map(int, block_bytes)

                    next_element = True
                    a = 0
                    b = 0
                    for element in block_bytes:
                        if (next_element):
                            a = element
                            next_element = False
                        else:
                            b = element
                            a_x_inverse = pow(a, p - 1 - x, p)
                            cipher = ((b % p) * (a_x_inverse % p)) % p
                            out.write(int_to_bytes(cipher, block_size))
                            next_element = True
            return f'Execution complete. File saved in {cipher_text.output_path}.'

    def generate_key(self, params: List[int], output_path: str = "."):
        p, g, x = params
        y = pow(g, x, p)

        public_key = Key([y, g, p])
        secret_key = Key([x, p])

        with open(f'{output_path}/elgamal.pub', 'wb') as out:
            pickle.dump(public_key, out)

        with open(f'{output_path}/elgamal.pri', 'wb') as out:
            pickle.dump(secret_key, out)

        return f'Keys elgamal.pub and elgamal.pri saved in {output_path}'


if __name__ == "__main__":
    elgamal = Elgamal()
    data = Data(DataType.TEXT, 'a b c d e r t g d w q a d r')
    p = generate_prime_number(15)
    print(p)
    g = generate_random_number(1, p - 1)
    print(g)
    x = generate_random_number(1, p - 1)
    print(x)
    elgamal.generate_key([p, g, x])
    public_key = elgamal.load_key('elgamal.pub')
    secret_key = elgamal.load_key('elgamal.pri')

    result = elgamal.encrypt(public_key, data)
    print(result)
    data = Data(DataType.TEXT, result)
    result = elgamal.decrypt(secret_key, data)
    print(result)
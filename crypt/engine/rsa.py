import pickle
import time

from crypt.engine.base_engine import BaseEngine
from crypt.engine.data import *
from crypt.engine.key import *
from crypt.utils.bytes_util import *
from crypt.utils.file_util import *
from crypt.utils.number_util import *


class RSA(BaseEngine):
    def encrypt(self, public_key: Key, plain_text: Data) -> str:
        n = public_key.value[0]
        e = public_key.value[1]
        block_size = get_block_size(n)
        max_digit = get_digit_count(n)

        if plain_text.data_type == DataType.TEXT:
            block_bytes = group_bytes(plain_text.value, block_size)
            block_bytes = map(lambda x: bytes_to_int(x, True), block_bytes)
            result = []
            for element in block_bytes:
                cipher = pow(element, e, n)
                result.append(str(cipher).rjust(max_digit, '0'))
            return ''.join(result)
        else:
            start_time = time.time()
            chunk_size = MAX_CHUNK_SIZE - (MAX_CHUNK_SIZE % block_size)
            with open(plain_text.output_path, 'w') as out:
                for chunk in load_file(plain_text.value, chunk_size):
                    block_bytes = group_bytes(chunk, block_size)
                    block_bytes = map(bytes_to_int, block_bytes)

                    for element in block_bytes:
                        cipher = pow(element, e, n)
                        out.write(str(cipher).rjust(max_digit, '0'))

            execution_time = time.time() - start_time
            return f'Execution complete. File saved in {plain_text.output_path}. \n Time execution  = {execution_time} seconds'

    def decrypt(self, secret_key: Key, cipher_text: Data) -> str:
        n = secret_key.value[0]
        d = secret_key.value[1]
        block_size = get_block_size(n)
        max_digit = get_digit_count(n)

        if cipher_text.data_type == DataType.TEXT:
            block_bytes = group_bytes(cipher_text.value, max_digit)
            block_bytes = map(int, block_bytes)
            result = []
            for element in block_bytes:
                cipher = pow(element, d, n)
                result.append(int_to_bytes(cipher, block_size, True))
            return ''.join(result)
        else:
            start_time = time.time()
            chunk_size = MAX_CHUNK_SIZE - (MAX_CHUNK_SIZE % max_digit)
            with open(cipher_text.output_path, 'wb') as out:
                for chunk in load_file(cipher_text.value, chunk_size):
                    block_bytes = group_bytes(chunk, max_digit)
                    block_bytes = map(int, block_bytes)

                    for element in block_bytes:
                        cipher = pow(element, d, n)
                        out.write(int_to_bytes(cipher, block_size))

            execution_time = time.time() - start_time
            return f'Execution complete. File saved in {cipher_text.output_path}. \n Time execution  = {execution_time} seconds'

    def generate_key(self, params: List[int], output_path: str = '.') -> str:
        p, q = params
        n = p * q
        toitent_n = toitent(p) * toitent(q)
        while True:
            e = random.randint(1, toitent_n - 2)
            if is_relative_prime(e, toitent_n):
                break

        d = mod_inverse(e, toitent_n)

        public_key = Key([n, e])
        secret_key = Key([n, d])

        with open(f'{output_path}/rsa.pub', 'wb') as out:
            pickle.dump(public_key, out)

        with open(f'{output_path}/rsa.pri', 'wb') as out:
            pickle.dump(secret_key, out)
        return f'Keys rsa.pub and rsa.pri saved in {output_path}'


if __name__ == '__main__':
    rsa = RSA()
    data = Data(DataType.TEXT, 'a b c d e r t g d w q a d r')
    p = generate_prime_number(10)
    q = generate_prime_number(10)
    rsa.generate_key([p, q])
    public_key = rsa.load_key('rsa.pub')
    secret_key = rsa.load_key('rsa.pri')
    result = rsa.encrypt(public_key, data)
    print(result)
    data = Data(DataType.TEXT, result)
    result = rsa.decrypt(secret_key, data)
    print(result)

    # data = Data(DataType.FILE, 'pdf_big.pdf', 'enctestread')
    # result = rsa.encrypt(public_key, data)
    # print(result)
    # data = Data(DataType.FILE, 'enctestread', 'decpdf_big.pdf')
    # result = rsa.decrypt(secret_key, data)
    # print(result)

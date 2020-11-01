import pickle
import time
from typing import List, Tuple, Union

from crypt.engine.base_engine import BaseEngine
from crypt.engine.data import Data, DataType
from crypt.engine.key import Key
from eight_series_cipher.operation import CBC


class DiffieHellman(BaseEngine):
    def encrypt(self, public_key: Key, plain_text: Data) -> Union[str, Tuple[str, str]]:
        start_time = time.time()
        key = public_key.value[0]
        if plain_text.data_type != DataType.TEXT:
            raise Exception('Current implementation only support string input')

        cbc = CBC(str(key))
        result = cbc.encipher(plain_text.value)
        execution_time = time.time() - start_time
        size_after = len(result)
        size_before = len(plain_text.value)
        info = BaseEngine.get_exec_info(execution_time, size_before, size_after)
        return info, result

    def decrypt(self, secret_key: Key, cipher_text: Data) -> Union[str, Tuple[str, str]]:
        start_time = time.time()
        key = secret_key.value[0]
        if cipher_text.data_type != DataType.TEXT:
            raise Exception('Current implementation only support string input')

        cbc = CBC(str(key))
        result = cbc.decipher(cipher_text.value)
        execution_time = time.time() - start_time
        size_after = len(result)
        size_before = len(cipher_text.value)
        info = BaseEngine.get_exec_info(execution_time, size_before, size_after)
        return info, result

    def generate_key(self, params: List[int], output_path: str = '.') -> str:
        n, g, x, y = params

        calculated_x = pow(g, x, n)
        calculated_y = pow(g, y, n)

        session_key = pow(calculated_y, x, n)
        session_key_2 = pow(calculated_x, y, n)
        assert session_key == session_key_2

        key = Key([session_key])

        with open(f'{output_path}/dh.ses', 'wb') as out:
            pickle.dump(key, out)

        return f'Session key dh.ses saved in {output_path}'

if __name__ == '__main__':
    dh = DiffieHellman()
    key = Key([1232345])
    data = Data(DataType.TEXT, 'test123123njakafs')
    result = dh.encrypt(key, data)
    result = dh.decrypt(key, Data(DataType.TEXT, result))
    print(result)

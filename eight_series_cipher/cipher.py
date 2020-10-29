from typing import ItemsView, List
from eight_series_cipher.constant import *

BLOCK_SIZE = 144
KEY_SIZE = 144
ITERATION = 8

INITIAL_PERMUTATION = [
    64, 63, 104, 67, 96, 78, 65, 11, 128, 3, 123, 66, 81, 120, 71, 125, 85, 45,
    90, 57, 46, 42, 51, 127, 137, 112, 122, 121, 68, 87, 129, 20, 55, 16, 119,
    43, 110, 101, 95, 49, 89, 91, 94, 126, 99, 53, 111, 102, 54, 108, 40, 50,
    48, 56, 80, 79, 83, 70, 75, 31, 26, 36, 114, 32, 8, 115, 124, 24, 44, 13,
    69, 118, 7, 59, 74, 133, 100, 88, 23, 98, 38, 97, 138, 107, 29, 106, 17,
    61, 92, 134, 109, 93, 10, 12, 0, 142, 58, 130, 37, 41, 30, 143, 84, 82, 34,
    2, 76, 60, 103, 105, 5, 35, 15, 132, 136, 140, 9, 28, 39, 86, 141, 131,
    139, 27, 73, 1, 22, 21, 47, 113, 18, 117, 77, 52, 19, 25, 14, 72, 4, 135,
    116, 33, 62, 6
]
INITIAL_PERMUTATION_INVERSE = [
    94, 125, 105, 9, 138, 110, 143, 72, 64, 116, 92, 7, 93, 69, 136, 112, 33,
    86, 130, 134, 31, 127, 126, 78, 67, 135, 60, 123, 117, 84, 100, 59, 63,
    141, 104, 111, 61, 98, 80, 118, 50, 99, 21, 35, 68, 17, 20, 128, 52, 39,
    51, 22, 133, 45, 48, 32, 53, 19, 96, 73, 107, 87, 142, 1, 0, 6, 11, 3, 28,
    70, 57, 14, 137, 124, 74, 58, 106, 132, 5, 55, 54, 12, 103, 56, 102, 16,
    119, 29, 77, 40, 18, 41, 88, 91, 42, 38, 4, 81, 79, 44, 76, 37, 47, 108, 2,
    109, 85, 83, 49, 90, 36, 46, 25, 129, 62, 65, 140, 131, 71, 34, 13, 27, 26,
    10, 66, 15, 43, 23, 8, 30, 97, 121, 113, 75, 89, 139, 114, 24, 82, 122,
    115, 120, 95, 101
]
S_BOX = [
    0, 41, 1, 127, 190, 17, 2, 248, 159, 151, 214, 51, 186, 3, 202, 229, 66,
    83, 115, 139, 132, 118, 188, 96, 4, 78, 93, 189, 34, 67, 251, 210, 108, 60,
    130, 191, 219, 211, 89, 57, 5, 245, 181, 88, 195, 140, 64, 11, 233, 136,
    54, 39, 37, 85, 168, 86, 91, 160, 117, 42, 119, 179, 6, 198, 182, 45, 99,
    141, 153, 165, 154, 29, 223, 121, 122, 92, 166, 237, 131, 184, 142, 14,
    242, 200, 81, 124, 30, 238, 44, 63, 107, 7, 28, 80, 176, 169, 212, 49, 147,
    16, 170, 221, 25, 171, 199, 46, 213, 206, 143, 21, 33, 65, 216, 20, 156,
    201, 125, 227, 148, 222, 48, 253, 215, 161, 209, 172, 128, 220, 8, 12, 174,
    116, 22, 197, 69, 112, 129, 133, 239, 106, 135, 19, 146, 31, 246, 113, 111,
    120, 208, 50, 27, 235, 100, 180, 68, 123, 254, 38, 247, 185, 244, 137, 144,
    175, 192, 94, 249, 163, 134, 243, 98, 231, 43, 110, 9, 207, 71, 228, 23,
    157, 252, 105, 224, 114, 164, 75, 73, 150, 203, 18, 177, 236, 250, 193, 77,
    230, 187, 173, 59, 217, 84, 58, 52, 47, 90, 240, 15, 232, 101, 152, 61,
    204, 87, 167, 56, 53, 183, 158, 149, 55, 104, 70, 13, 194, 109, 225, 82,
    138, 62, 205, 10, 32, 255, 162, 196, 155, 26, 226, 102, 79, 234, 103, 241,
    145, 35, 218, 97, 72, 95, 126, 74, 24, 36, 178, 40, 76
]


class Cipher():
    @staticmethod
    def string_to_bits(input_string: str) -> List[int]:
        result = []

        for char in input_string:
            binary_rep = bin(ord(char))
            result += [
                int(bit) for bit in binary_rep.lstrip('0b').rjust(8, '0')
            ]

        return result

    @staticmethod
    def bits_to_string(input_bits: List[int]) -> str:
        result = ''
        string_array = map(str, input_bits)
        string_array = ''.join(string_array)

        for i in range(0, len(string_array), 8):
            char = string_array[i:i + 8]
            char = '0b' + char
            char = chr(int(char, 2))
            result += char

        return result

    @staticmethod
    def int_to_bits(input_int: List[int]) -> List[int]:
        result = []

        for dec in input_int:
            binary_rep = bin(dec)
            result += [
                int(bit) for bit in binary_rep.lstrip('0b').rjust(8, '0')
            ]

        return result

    @staticmethod
    def bits_to_int(input_bits: List[int]) -> List[int]:
        result = []
        string_array = map(str, input_bits)
        string_array = ''.join(string_array)

        for i in range(0, len(string_array), 8):
            dec = string_array[i:i + 8]
            dec = '0b' + dec
            dec = int(dec, 2)
            result.append(dec)

        return result

    @staticmethod
    def shift(input_arr: List[int], n: int, is_left: bool) -> List[int]:
        if is_left:
            return input_arr[n:] + input_arr[:n]
        else:
            return input_arr[-n:] + input_arr[:-n]

    @classmethod
    def encipher(cls, input_val: List[int]) -> List[int]:  # bits
        temp = [0] * BLOCK_SIZE

        for idx, val in enumerate(input_val):
            temp[INITIAL_PERMUTATION[idx]] = val

        temp = Cipher.bits_to_int(temp)

        left = temp[:BLOCK_SIZE // 16]
        right = temp[BLOCK_SIZE // 16:]

        # do feistel
        for i in range(ITERATION):
            prev_right = right.copy()
            func_res = Cipher.function(cls.internal_keys[i], right, i)
            right = [left[i] ^ func_res[i] for i in range(len(left))]
            left = prev_right

        temp = left + right

        temp = Cipher.int_to_bits(temp)

        out = [0] * BLOCK_SIZE
        for idx, val in enumerate(temp):
            out[INITIAL_PERMUTATION_INVERSE[idx]] = val

        return out

    @classmethod
    def decipher(cls, input_val: List[int]) -> List[int]:
        temp = [0] * BLOCK_SIZE

        for idx, val in enumerate(input_val):
            temp[INITIAL_PERMUTATION[idx]] = val

        temp = Cipher.bits_to_int(temp)

        left = temp[:BLOCK_SIZE // 16]
        right = temp[BLOCK_SIZE // 16:]

        # do feistel
        for i in range(ITERATION - 1, -1, -1):
            prev_left = left.copy()
            func_res = Cipher.function(cls.internal_keys[i], left, i)
            left = [right[i] ^ func_res[i] for i in range(len(right))]
            right = prev_left

        temp = left + right

        temp = Cipher.int_to_bits(temp)

        out = [0] * BLOCK_SIZE
        for idx, val in enumerate(temp):
            out[INITIAL_PERMUTATION_INVERSE[idx]] = val

        return out

    @staticmethod
    def function(key: List[int], input_val: List[int], iter: int) -> List[int]:
        # returns list of int (decimal representation) with length 9 byte

        bit_rep = Cipher.int_to_bits(input_val)
        left = bit_rep[:len(bit_rep) // 2]
        right = bit_rep[len(bit_rep) // 2:]

        # shift left the left by sequence[iter]
        # shift right the right by sequence[iter]
        left = Cipher.shift(left, QUADRATIC[iter], is_left=True)
        right = Cipher.shift(right, QUADRATIC[iter], is_left=False)

        temp = Cipher.bits_to_int(left + right)
        # xor with key
        temp = [temp[i] ^ key[i] for i in range(len(temp))]
        # substitute with s-box
        temp = [S_BOX[val] for val in temp]

        bit_rep = Cipher.int_to_bits(temp)
        left = bit_rep[:len(bit_rep) // 2]
        right = bit_rep[len(bit_rep) // 2:]

        # shift right the left by sequence[iter]
        # shift left the right by sequence[iter]
        left = Cipher.shift(left, QUADRATIC[iter], is_left=False)
        right = Cipher.shift(right, QUADRATIC[iter], is_left=True)

        return Cipher.bits_to_int(left + right)

    @classmethod
    def generate_internal_key(cls, key: str) -> List[int]:
        last_idx = 0
        bit_key = Cipher.string_to_bits(key)
        key_len = len(bit_key)
        all_key = []
        for i in range(ITERATION):
            internal_key = []
            for val in SEQUENCES[i % ITERATION]:
                last_idx = (val + last_idx) % key_len
                internal_key.append(bit_key[last_idx])

            # do complex key
            left = internal_key[:len(internal_key) // 2]
            right = internal_key[len(internal_key) // 2:]
            left = Cipher.shift(left, i, is_left=True)
            right = Cipher.shift(right, i, is_left=False)

            if i % 2 == 1:
                temp = left
                left = right
                right = temp

            all_key.append(Cipher.bits_to_int(left + right))

        cls.internal_keys = all_key
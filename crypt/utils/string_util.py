import math
import textwrap

from typing import List


def string_to_int(plain_text: str) -> int:
    """Convert string into integer representation with certain block size.
    Block size is determined by the string length

    Args:
        plain_text (str): in block_size bytes

    Returns:
        int: integer representation
    """
    result = 0
    for i in range(len(plain_text)):
        result = result << 8
        result += ord(plain_text[i])

    return result


def int_to_string(encoded_int: int) -> str:
    """Convert integer representation back to string with certain block size.
    Block size is determined by the bit length

    Args:
        encoded_int (int)

    Returns:
        str: string from the integer representation
    """
    block_size = math.ceil(encoded_int.bit_length() / 8.0)
    mask = 0xFF

    result = []
    for i in range(block_size):
        char = encoded_int & mask
        result.insert(0, chr(char))
        encoded_int = encoded_int >> 8
    return ''.join(result)


def group_string(plain_text: str, block_size: int) -> List[str]:
    """Convert string into list of string. Each element is block_size bytes

    Args:
        plain_text (str)
        block_size (int)

    Returns:
        List[str]
    """
    return textwrap.wrap(plain_text, width=block_size, drop_whitespace=False)


if __name__ == '__main__':
    a = 'test123'
    a = group_string(a, 3)
    temp = []
    for el in a:
        temp.append(string_to_int(el))
    print(temp)
    temp2 = []
    for el in temp:
        temp2.append(int_to_string(el))
    print(temp2)
    print(''.join(temp2))
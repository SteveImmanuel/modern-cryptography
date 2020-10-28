import math

from typing import List, Union


def bytes_to_int(plain_text: bytes, is_string: bool = False) -> int:
    """
    Convert bytes into integer representation with certain block size.
    Block size is determined by plain_text length
    """
    result = 0
    for i in range(len(plain_text)):
        result = result << 8
        if is_string:
            result += ord(plain_text[i])
        else:
            result += plain_text[i]

    return result


def int_to_bytes(encoded_int: int, block_size: int, is_string: bool = False) -> Union[str, bytes]:
    """
    Convert integer representation back to bytes with certain block size.
    """
    mask = 0xFF

    if is_string:
        result = ''
    else:
        result = b''

    for i in range(block_size):
        char = encoded_int & mask
        if is_string:
            char = chr(char)
        else:
            char = bytes([char])

        result = char + result
        encoded_int = encoded_int >> 8

    return result


def group_bytes(plain_text: Union[bytes, str], block_size: int) -> List[Union[bytes, str]]:
    """
    Split bytes into chunks with size of block_size bytes
    """
    return [
        plain_text[i * block_size:(i + 1) * block_size]
        for i in range((len(plain_text) + block_size - 1) // block_size)
    ]


if __name__ == '__main__':
    a = 'test123'
    a = group_bytes(a, 3)
    print(a)
    temp = []
    for el in a:
        temp.append(bytes_to_int(el, True))
    print(temp)
    temp2 = []
    for el in temp:
        temp2.append(int_to_bytes(el, True))
    print(temp2)
    print(''.join(temp2))

    print()

    a = b'test123'
    a = group_bytes(a, 3)
    print(a)
    temp = []
    for el in a:
        temp.append(bytes_to_int(el))
    print(temp)
    temp2 = b''
    for el in temp:
        temp2 += int_to_bytes(el)
    print(temp2)
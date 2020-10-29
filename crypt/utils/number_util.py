import math
import random
from typing import List

from crypt.constant import *


def is_relative_prime(a: int, b: int) -> bool:
    """
    Check if two number relatively prime
    """
    return math.gcd(a, b) == 1


def generate_prime_number(n: int) -> int:
    """
    Generate prime number with n digits
    """
    start = 10**(n - 1) + 1  #make sure it's odd
    end = 10**(n) - 1
    while True:
        candidate = random.randrange(start, end, 2)
        if is_prime(candidate):
            return candidate

def generate_random_number(min: int, max: int) -> int:
    """
    Generate random number between range [min, max)
    """
    return random.randrange(min, max, 1)

def toitent(n: int) -> int:
    """
    Get toitent value of n. n must be a prime number
    """
    return n - 1


def is_prime(n: int) -> bool:
    """
    Check if number prime. Only handles positive number
    """
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_block_size(n: int) -> int:
    """
    Get biggest block size possible for n. Result will be clamped between 1 and MAX_BLOCK_SIZE
    """
    return min(MAX_BLOCK_SIZE, max(1, (n.bit_length() - 1) // 8))


def get_digit_count(n: int) -> int:
    """
    Returns digit count of a number
    """
    return len(str(n))


def egcd(a: int, b: int) -> List[int]:
    """
    Returns extended gcd of a and b in format gcd(a,b), x, y
    where ax + by = gcb(a,b)
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def mod_inverse(e: int, n: int) -> int:
    """
    Return inverse modulus of e in n so that ed = 1 mod n
    """
    g, x, y = egcd(e, n)
    if g != 1:
        raise Exception('e has no modulus inverse in n')
    return x % n


if __name__ == '__main__':
    p = 47
    q = 71
    e = 79
    n = p * q
    t_n = 46 * 70
    d = mod_inverse(e, t_n)
    print('p:', p)
    print('q:', q)
    print('n:', n)
    print('t_n:', t_n)
    print('e:', e)
    print('d:', d)
    print((d * e) % t_n)

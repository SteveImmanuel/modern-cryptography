import math

from crypt.constant import *


def is_relative_prime(a: int, b: int) -> bool:
    """Check if two number relatively prime

    Args:
        a (int): any integer
        b (int): any integer

    Returns:
        bool: is a and b relatively prime
    """
    return math.gcd(a, b) == 1


def toitent(n: int) -> int:
    """Get toitent value of n. n must be a prime number.

    Args:
        n (int): prime number

    Returns:
        int: toitent of n
    """
    return n - 1


def is_prime(n: int) -> bool:
    """Check if number prime. Only handles positive number.

    Args:
        n (int): any integer

    Returns:
        bool: is prime or not
    """
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_block_size(n: int) -> int:
    """Get biggest block size possible for n. Result will be clamped between 1 and MAX_BLOCK_SIZE

    Args:
        n (int): prime number

    Returns:
        int: block size in bytes
    """
    return max(MAX_BLOCK_SIZE, min(1, (n.bit_length() - 1) // 8))

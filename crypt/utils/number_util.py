import math


def is_relative_prime(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1


def toitent(n: int) -> int:
    # n must be a prime number
    return n - 1


def is_prime(n: int) -> int:
    # only handles positive number
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
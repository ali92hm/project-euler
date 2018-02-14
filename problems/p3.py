import math
from utils.factors import prime_factors


def answer(n):
    """
    Returns the largest prime factor of n
    ----------
    n : int
    Input number

    Returns
    -------
    max : int
    Maximum prime factor

    Doc Test
    ----------
    >>> answer(13195)
    29

    >>> answer(600851475143)
    6857
    """
    return max(prime_factors(n))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

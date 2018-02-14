import math
from utils import sum


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
    >>> answer(10)
    2640

    >>> answer(100)
    25164150
    """
    return sum.sum_n(n) ** 2 - sum.sum_n_squared(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

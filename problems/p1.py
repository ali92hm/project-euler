import math
from utils.sum import sum_n


def answer(n):
    """
    Sum of all the natural numbers below n that are multiples of 3 or 5.
    ----------
    n : int
    Upper bound (inclusive)

    Returns
    -------
    sum : int
    Sum of numbers

    Doc Test
    ----------
    >>> answer(2)
    0

    Doc Test
    ----------
    >>> answer(5)
    3

    Doc Test
    ----------
    >>> answer(6)
    8

    Doc Test
    ----------
    >>> answer(10)
    23

    Doc Test
    ----------
    >>> answer(15)
    45

    Doc Test
    ----------
    >>> answer(30)
    195

    >>> answer(1000)
    233168
    """
    return 3 * sum_n(math.ceil(n / 3) - 1) \
        + 5 * sum_n(math.ceil(n / 5) - 1) \
        - 15 * sum_n(math.ceil(n / 15) - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

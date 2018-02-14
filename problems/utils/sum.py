
def sum_n(n):
    """
    calculates sum of 1 + 2 + ... + n
    ----------
    n : int
    Upper bound (inclusive)

    Returns
    -------
    sum : int
    Sum of n numbers

    Doc Test
    ----------
    >>> sum_n(0)
    0

    >>> sum_n(3)
    6

    >>> sum_n(10)
    55

    >>> sum_n(-1)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert(n >= 0)
    return (n * (n + 1)) // 2


def sum_n_squared(n):
    """
    calculates sum of 1^2 + 2^2 + ... + n^2
    ----------
    n : int
    Upper bound (inclusive)

    Returns
    -------
    sum : int
    Sum of n^2 numbers

    Doc Test
    ----------
    >>> sum_n_squared(0)
    0

    >>> sum_n_squared(3)
    14

    >>> sum_n_squared(10)
    385

    >>> sum_n_squared(-1)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert(n >= 0)
    return (n * (n + 1) * (2 * n + 1)) // 6


if __name__ == "__main__":
    import doctest
    doctest.testmod()

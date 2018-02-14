from utils.prime import nth_prime


def answer(n):
    """
    Returns the nth prime
    ----------
    n : int
    Nth prime

    Returns
    -------
    prime : int
    Nth prime value

    Doc Test
    ----------
    >>> answer(1)
    2

    >>> answer(2)
    3

    >>> answer(6)
    13

    >>> answer(10001)
    104743
    """
    return nth_prime(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

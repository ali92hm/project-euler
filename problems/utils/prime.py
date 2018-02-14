import math


def is_prime(n):
    """
    Returns if the number is prime or not
    ----------
    n : int
    Natural number grater than 1

    Returns
    -------
    prime : bool
    True if the number is prime

    Doc Test
    ----------
    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(9)
    False

    >>> is_prime(10)
    False

    >>> is_prime(17)
    True

    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> is_prime(-1)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert(n > 1)
    if n % 2 is 0:
        return n == 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def nth_prime(n):
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
    >>> nth_prime(1)
    2

    >>> nth_prime(2)
    3

    >>> nth_prime(6)
    13
    """
    gen = gen_prime()
    for i in range(n):
        ans = next(gen)
    return ans


def gen_prime():
    """
    Returns a generator that generates prime numbers
    ----------

    Returns
    -------
    prime :
    True if the number is prime

    Doc Test
    ----------
    >>> gen_prime() #doctest: +ELLIPSIS
    <generator object gen_prime at 0x...>

    """
    yield 2

    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()

import math
from utils import constants


def answer(n):
    """
    Sum of even numbered Fibonacci numbers bellow n
    ----------
    n : int
    Upper bound (inclusive)

    Returns
    -------
    sum : int
    Sum of even Fibonacci numbers

    Doc Test
    ----------
    >>> answer(10)
    10

    >>> answer(4000000)
    4613732
    """
    sum_even = 0
    num_fib_seq = math.floor(
        math.log(n * constants.ROOT_FIVE + 0.5, constants.PHI))

    for i in range(0, num_fib_seq + 1, 3):
        sum_even += int(round(pow(constants.PHI, i) / constants.ROOT_FIVE))

    return sum_even


if __name__ == "__main__":
    import doctest
    doctest.testmod()

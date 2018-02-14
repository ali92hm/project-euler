import math


def prime_factors(n):
    if n == 1:
        return None

    root = int(math.sqrt(n))
    if root == 1:
        return [n]

    f1 = None
    f2 = None
    while root < n:
        if n % root == 0:
            f1 = root
            f2 = n/root
            break
        root += 1

    if not f1:
        return [n]
    else:
        return prime_factors(f1) + prime_factors(f2)

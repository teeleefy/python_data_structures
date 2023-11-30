def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    start_at = 2
    factors = {1, num}
    while start_at not in factors:
        if num % start_at == 0:
            factors.add(start_at)
            factors.add(int(num/start_at))
            start_at += 1
        else:
            start_at += 1
    factors = list(factors)
    factors.sort()
    return print(factors)
    
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
    return [factor for factor in range(1, num + 1) if num % factor == 0]

    # This is a math thing that would have been easier if I'd done a lot of math!
    # Main thing I missed is that both factors cannot be greater than the sqrt, so
    # I could have shortened my range significantly. Provided solution:
    # n_list = [n for n in range (1, num // 2 + 1) if num % n == 0]
    # n_list.append(num)
    # return n_list

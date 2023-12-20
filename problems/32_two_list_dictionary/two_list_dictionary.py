def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
    """
    # Just because, figured it's good to practice complex comprehensions!
    return {
        keys[i]: (values[i] if i < len(values) else None) for i in range(0, len(keys))
    }

    # Normal Solution
    # new_dict = {}
    # for i in range(0, len(keys)):
    #     key = keys[i]
    #     value = values[i] if i < len(values) else None
    #     new_dict[key] = value

    # return new_dict

    # Also, thanks to the provided solution, I learned you can
    # use enumerate() to get an index in your for loop!

def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

    >>> multiple_letter_count('yay')
    {'y': 2, 'a': 1}

    >>> multiple_letter_count('Yay')
    {'Y': 1, 'a': 1, 'y': 1}
    """
    frequency = {}
    for char in phrase:
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
    return frequency

    # For loop can be simplified!!
    # for char in phrase:
    #   frequency[char] = frequency.get(char, 0) + 1
    #
    # Remember, you can use .get() to provide a default value!

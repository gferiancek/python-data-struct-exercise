def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency(551122, 221515)
    True

    >>> same_frequency(321142, 3212215)
    False

    >>> same_frequency(1212, 2211)
    True
    """
    # Probably better to extract the frequency counting into
    # its own function, and just check the result of 
    # get_frequency(num1) == get_frequency(num2)
    # Not sure if problem was expected to be solved without additional funcs.
    num1_frequency = {}
    num2_frequency = {}

    for num in set(str(num1)):
        num1_frequency[num] = str(num1).count(num)

    for num in set(str(num2)):
        num2_frequency[num] = str(num2).count(num)

    return num1_frequency == num2_frequency
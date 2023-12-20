def valid_parentheses(parens):
    """Are the parentheses validly balanced?

    >>> valid_parentheses("()")
    True

    >>> valid_parentheses("()()")
    True

    >>> valid_parentheses("(()())")
    True

    >>> valid_parentheses(")()")
    False

    >>> valid_parentheses("())")
    False

    >>> valid_parentheses("((())")
    False

    >>> valid_parentheses(")()(")
    False
    """
    open_count = 0
    close_count = 0

    for char in parens:
        if char == "(":
            open_count += 1
        if char == ")":
            close_count += 1
        if close_count > open_count:
            return False

    return open_count == close_count

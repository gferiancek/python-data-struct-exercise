def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    reverse_str = ""
    vowels = []

    for char in s:
        if char in "aeiouAEIOU":
            vowels.append(char)
            reverse_str += "_"
        else:
            reverse_str += char

    vowels.reverse()
    for vowel in vowels:
        reverse_str = reverse_str.replace("_", vowel, 1)

    return reverse_str

    # My solution isn't works, but isn't optimal.
    # Provided solution is far more efficient as it has a single loop
    # Whereas mine has 3. (for char, vowels.reverse(), for vowel)
    # string = list(s)
    # i = 0
    # j = len(s) - 1

    # while i < j:
    #     if string[i].lower() not in vowels:
    #         i += 1
    #     elif string[j].lower() not in vowels:
    #         j -= 1
    #     else:
    #         string[i], string[j] = string[j], string[i]
    #         i += 1
    #         j -= 1

    # return "".join(string)

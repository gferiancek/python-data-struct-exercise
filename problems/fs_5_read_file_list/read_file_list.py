def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!
    file = open(filename, "r")
    next_line = file.readline()

    while next_line:
        next_line = next_line.strip()
        print(f"- {next_line}")
        next_line = file.readline()
    
    file.close()

    # Haven't covered Error Handling yet, so I didn't even think about try / catch
    # But the solution went a step further and introduced with !!
    # with makes tasks like above simplier. It open/closes and does some error handling!
    # 
    # with open(filename) as f:
    #     for line in f:
    #         line = line.strip()
    #         print(f"- {line}")

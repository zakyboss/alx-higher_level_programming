#!/usr/bin/python3
def uppercase(s):
    """
    Prints the input string in uppercase followed by a new line.

    Args:
    s (str): The string to be converted to uppercase and printed.
    """
    # Build the uppercase result string
    result = ''.join(
        chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        for char in s
    )

    # Print the result string followed by a newline
    print(result)

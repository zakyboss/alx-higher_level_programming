#!/usr/bin/python3
def uppercase(s):
    """
    Prints the input string in uppercase followed by a new line.

    Args:
    s (str): The string to be converted to uppercase and printed.
    """
    # Initialize an empty string to accumulate the result
    result = ""

    # Iterate through each character in the input string
    for char in s:
        # Convert lowercase letters to uppercase by adjusting ASCII value
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char

    # Print the final result string in uppercase
    print(result)

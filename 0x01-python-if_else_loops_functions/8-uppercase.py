#!/usr/bin/python3
def uppercase(s):
    """
    Prints the input string in uppercase followed by a new line.

    Args:
    s (str): The string to be converted to uppercase and printed.
    """
    result = ""
    
    for char in s:
        # Convert lowercase letters to uppercase
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    
    # Print the result string followed by a newline
    print(result)

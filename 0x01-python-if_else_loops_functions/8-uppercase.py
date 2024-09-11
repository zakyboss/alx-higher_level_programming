#!/usr/bin/python3
def uppercase(s):
    """
    Prints the input string in uppercase followed by a new line.

    Args:
    s (str): The string to be converted to uppercase and printed.
    """
    result = ""

    for char in s:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert to uppercase by subtracting 32 from ASCII value
            result += chr(ord(char) - 32)
        else:
            # Keep the character as is if it's not lowercase
            result += char

    # Print the result string followed by a newline
    print(result)


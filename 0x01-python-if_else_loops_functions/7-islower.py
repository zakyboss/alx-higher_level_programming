def islower(c):
    """
    Checks if the character c is a lowercase letter.

    Args:
    c (str): A single character to be checked.

    Returns:
    bool: True if c is a lowercase letter, False otherwise.
    """
    # Check if c is a single character
    if len(c) != 1:
        return False

    # Get the ASCII value of the character
    ascii_value = ord(c)

    # Check if the ASCII value falls in the range of lowercase letters
    return 97 <= ascii_value <= 122


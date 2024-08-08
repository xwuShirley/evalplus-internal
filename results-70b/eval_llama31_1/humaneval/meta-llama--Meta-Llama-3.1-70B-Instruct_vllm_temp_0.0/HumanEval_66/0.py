def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())
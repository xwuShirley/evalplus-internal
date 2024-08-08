def is_happy(s: str) -> bool:
    """
    Checks if a given string is happy.

    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is happy, False otherwise.
    """

    # A string is not happy if its length is less than 3
    if len(s) < 3:
        return False

    # Compare every 3 consecutive letters in the string
    for i in range(len(s) - 2):
        # If at least 2 out of 3 consecutive letters are the same, return False
        if len(set(s[i:i+3])) < 3:
            return False

    # If we haven't returned False by now, the string is happy
    return True
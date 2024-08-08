def any_int(x, y, z):
    """
    This function checks if one of the numbers is equal to the sum of the other two.
    It also checks if all numbers are integers.

    Args:
        x (int): The first number.
        y (int): The second number.
        z (int): The third number.

    Returns:
        bool: True if one of the numbers is equal to the sum of the other two and all numbers are integers.
    """

    # Check if all numbers are integers
    if not all(isinstance(num, int) for num in [x, y, z]):
        return False

    # Check if one of the numbers is equal to the sum of the other two
    if x == y + z or y == x + z or z == x + y:
        return True

    return False
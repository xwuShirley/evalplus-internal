def iscube(a):
    """
    Returns True if the integer a is a cube of some integer number.

    Args:
        a (int): The input integer.

    Returns:
        bool: True if a is a cube, False otherwise.
    """
    i = 0
    while True:
        # We calculate the cube of i and compare it with a
        if i ** 3 == a:
            return True
        # If i's cube is greater than a, a cannot be a cube
        elif i ** 3 > a:
            return False
        i += 1
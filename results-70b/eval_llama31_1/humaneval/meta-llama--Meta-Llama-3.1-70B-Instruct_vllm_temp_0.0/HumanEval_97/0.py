def multiply(a, b):
    """
    Returns the product of the unit digits of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of the unit digits of a and b.
    """
    # Get the unit digit of a and b using the modulus operator
    a_digit = a % 10
    b_digit = b % 10

    # Calculate the product of the unit digits
    product = a_digit * b_digit

    return product
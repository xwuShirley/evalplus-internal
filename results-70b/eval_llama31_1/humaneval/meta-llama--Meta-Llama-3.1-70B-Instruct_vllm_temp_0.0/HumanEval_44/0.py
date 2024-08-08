def change_base(x: int, base: int) -> str:
    """
    This function changes the numerical base of the input number x to the given base.
    
    Args:
        x (int): The input number to be converted.
        base (int): The base to which the number is to be converted.
    
    Returns:
        str: The string representation of the number after the conversion.
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Continue the process until the number becomes 0
    while x > 0:
        # Find the remainder of the number when divided by the base
        remainder = x % base
        
        # Prepend the remainder to the result
        result = str(remainder) + result
        
        # Update the number by performing integer division by the base
        x = x // base
    
    # Return the result
    return result
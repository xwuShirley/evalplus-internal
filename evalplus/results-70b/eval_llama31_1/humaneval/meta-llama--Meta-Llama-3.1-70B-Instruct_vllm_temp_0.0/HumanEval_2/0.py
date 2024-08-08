def truncate_number(number: float) -> float:
    """
    This function truncates the decimal part of a given floating point number.
    
    Args:
        number (float): A positive floating point number.
    
    Returns:
        float: The decimal part of the number.
    """
    
    # First, we import the math module which provides access to mathematical functions
    import math
    
    # We use the modulo operator to find the decimal part of the number
    # The modulo operator returns the remainder of the division of the number by 1
    # This effectively gives us the decimal part of the number
    decimal_part = number % 1
    
    # We return the decimal part
    return decimal_part
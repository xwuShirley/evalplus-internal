import math

def is_simple_power(x, n):
    """
    Checks if a number x is a simple power of n.
    
    Args:
        x (int): The number to check.
        n (int): The base number.
    
    Returns:
        bool: True if x is a simple power of n, False otherwise.
    """
    if x <= 0 or n <= 0:
        return False
    
    # Calculate the logarithm of x with base n
    log_x_base_n = math.log(x, n)
    
    # Check if the logarithm is an integer
    return log_x_base_n.is_integer()
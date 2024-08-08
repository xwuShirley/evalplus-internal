def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.
    
    The function uses the property of modular arithmetic that (a*b) % n = ((a % n) * (b % n)) % n.
    This property allows us to avoid large numbers and calculate the result directly modulo p.
    
    Parameters:
    n (int): The power of 2.
    p (int): The modulo.
    
    Returns:
    int: 2^n modulo p.
    """
    
    # Handle the special case where n is 0
    if n == 0:
        return 1
    
    # Initialize the result to 1 (2^0)
    result = 1
    
    # Calculate 2^n modulo p
    power_of_two = 2
    while n > 0:
        # If n is odd, multiply the result by the current power of two
        if n % 2 == 1:
            result = (result * power_of_two) % p
        
        # Square the current power of two and move to the next bit in n
        power_of_two = (power_of_two * power_of_two) % p
        n = n // 2
    
    return result
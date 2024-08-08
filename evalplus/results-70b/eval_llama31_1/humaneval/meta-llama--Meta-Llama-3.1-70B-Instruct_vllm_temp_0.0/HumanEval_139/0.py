def special_factorial(n):
    """
    This function calculates the Brazilian factorial of a number.
    
    The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0
    
    Args:
        n (int): The number to calculate the Brazilian factorial for.
    
    Returns:
        int: The Brazilian factorial of the input number.
    """
    
    # Initialize the result variable to 1. This variable will hold the final result.
    result = 1
    
    # Loop through all numbers from 1 to n.
    for i in range(1, n + 1):
        # For each number, calculate its factorial and multiply it with the result.
        # The factorial of a number is calculated by multiplying all numbers from 1 to that number.
        # This is done using the *= operator, which multiplies the result with the factorial of the current number.
        result *= factorial(i)
    
    # After the loop, result will hold the Brazilian factorial of the input number.
    return result

# This function is used to calculate the factorial of a number.
def factorial(n):
    """
    This function calculates the factorial of a number.
    
    The factorial of a number is the product of all positive integers less than or equal to that number.
    It is denoted by the symbol "!". For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.
    
    Args:
        n (int): The number to calculate the factorial for.
    
    Returns:
        int: The factorial of the input number.
    """
    
    # Initialize the result variable to 1. This variable will hold the final result.
    result = 1
    
    # Loop through all numbers from 1 to n.
    for i in range(1, n + 1):
        # For each number, multiply it with the result.
        # This is done using the *= operator, which multiplies the result with the current number.
        result *= i
    
    # After the loop, result will hold the factorial of the input number.
    return result
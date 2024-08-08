def fib4(n: int) -> int:
    """
    This function efficiently computes the n-th element of the fib4 number sequence.
    
    Parameters:
    n (int): The index of the fib4 number sequence.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the fib4 numbers
    fib4_numbers = [0, 0, 2, 0] + [0] * (n - 3)
    
    # Compute the fib4 numbers iteratively
    for i in range(4, n + 1):
        fib4_numbers[i - 1] = fib4_numbers[i - 2] + fib4_numbers[i - 3] + fib4_numbers[i - 4] + fib4_numbers[i - 5]
    
    # Return the n-th fib4 number
    return fib4_numbers[n - 1]
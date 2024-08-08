def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
        n (int): The position of the number in the sequence.
    
    Returns:
        int: The n-th number that is a Fibonacci number and it's also prime.
    """
    
    # Initialize the first two numbers in the sequence
    a, b = 0, 1
    
    # Initialize the count of prime Fibonacci numbers
    count = 0
    
    # Iterate over the sequence until we find the n-th prime Fibonacci number
    while True:
        # If a is prime and we've found n prime Fibonacci numbers, return it
        if is_prime(a) and count == n:
            return a
        
        # If a is prime, increment the count of prime Fibonacci numbers
        if is_prime(a):
            count += 1
        
        # Calculate the next number in the sequence
        a, b = b, a + b


def is_prime(num: int) -> bool:
    """
    is_prime checks if a number is prime.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    
    # If the number is less than 2, it's not prime
    if num < 2:
        return False
    
    # Check if the number is divisible by any number up to its square root
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    # If the number is not divisible by any number up to its square root, it's prime
    return True
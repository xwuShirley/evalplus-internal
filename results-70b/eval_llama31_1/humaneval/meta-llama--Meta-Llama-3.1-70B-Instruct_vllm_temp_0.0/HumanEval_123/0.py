def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    Args:
        n (int): A positive integer.

    Returns:
        list: A sorted list of odd numbers in the Collatz sequence of n.
    """
    # Initialize an empty set to store the odd numbers in the Collatz sequence
    odd_numbers = set()
    
    # Continue the sequence until we reach 1
    while n != 1:
        # If n is odd, add it to the set of odd numbers
        if n % 2 != 0:
            odd_numbers.add(n)
        
        # Calculate the next number in the Collatz sequence
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    # Add 1 to the set of odd numbers (because 1 is always an odd number in the sequence)
    odd_numbers.add(1)
    
    # Convert the set to a list, sort it, and return it
    return sorted(list(odd_numbers))
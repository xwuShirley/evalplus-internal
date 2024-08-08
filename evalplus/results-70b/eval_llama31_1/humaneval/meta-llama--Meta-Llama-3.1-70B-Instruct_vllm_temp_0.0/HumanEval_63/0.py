def fibfib(n: int):
    """
    This function calculates the n-th element of the FibFib number sequence.
    
    The FibFib number sequence is similar to the Fibonacci sequence, but each element is the sum of the three preceding ones.
    
    Args:
        n (int): The position of the element in the sequence.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    
    # Initialize the first three elements of the sequence
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize the list to store the sequence
    fibfib_seq = [0, 0, 1]
    
    # Calculate the sequence up to the n-th element
    for i in range(3, n + 1):
        # Calculate the next element as the sum of the three preceding ones
        next_element = fibfib_seq[i - 1] + fibfib_seq[i - 2] + fibfib_seq[i - 3]
        
        # Append the next element to the sequence
        fibfib_seq.append(next_element)
    
    # Return the n-th element of the sequence
    return fibfib_seq[n]
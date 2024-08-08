def solve(N):
    """
    This function calculates the sum of binary digits of a given number N and returns the result in binary format.
    
    Parameters:
    N (int): A positive integer.
    
    Returns:
    str: The sum of binary digits of N in binary format.
    """
    
    # Convert the number to binary and remove the '0b' prefix
    binary = bin(N)[2:]
    
    # Calculate the sum of the binary digits
    digit_sum = sum(int(digit) for digit in binary)
    
    # Convert the sum to binary and remove the '0b' prefix
    binary_sum = bin(digit_sum)[2:]
    
    return binary_sum
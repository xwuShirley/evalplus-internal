def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    :param n: A positive integer.
    :return: The count of n-digit positive integers that start or end with 1.
    """
    
    # Handle the special case when n is 1
    if n == 1:
        return 2
    
    # For n-digit numbers, there are 9 ways to choose the first digit (since it can't be 0)
    # and 10 ways to choose each of the remaining digits. So, there are 9 * 10^(n-1)
    # n-digit numbers. Among these, there are 1 * 10^(n-1) numbers that start with 1
    # (since the first digit is fixed to be 1), and 9 * 10^(n-2) numbers that end with 1
    # (since the last digit is fixed to be 1, and the first digit can be anything except 0).
    # However, we have counted numbers that start and end with 1 twice, so we need to subtract
    # 1 * 10^(n-2) once.
    
    # Calculate the total count of n-digit numbers that start or end with 1
    total_count = 1 * 10**(n-1) + 9 * 10**(n-2) - 1 * 10**(n-2)
    
    return total_count
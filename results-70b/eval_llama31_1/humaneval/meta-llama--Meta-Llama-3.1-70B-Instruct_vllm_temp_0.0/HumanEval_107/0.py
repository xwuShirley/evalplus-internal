def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Args:
        n (int): A positive integer.

    Returns:
        tuple: A tuple containing the number of even and odd integer palindromes respectively.

    """
    even_count = 0  # Initialize count for even palindromes
    odd_count = 0  # Initialize count for odd palindromes

    for i in range(1, n+1):  # Iterate through the range of 1 to n
        str_i = str(i)  # Convert the integer to a string for easy palindrome check
        if str_i == str_i[::-1]:  # Check if the string is the same when reversed
            if i % 2 == 0:  # Check if the number is even
                even_count += 1  # Increment the even count
            else:
                odd_count += 1  # Increment the odd count

    return even_count, odd_count  # Return the counts as a tuple
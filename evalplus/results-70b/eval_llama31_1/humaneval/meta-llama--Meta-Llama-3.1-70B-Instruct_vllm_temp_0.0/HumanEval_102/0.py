def choose_num(x, y):
    """
    This function takes two positive numbers x and y and returns the 
    biggest even integer number that is in the range [x, y] inclusive. 
    If there's no such number, then the function returns -1.

    Args:
        x (int): The start of the range (inclusive).
        y (int): The end of the range (inclusive).

    Returns:
        int: The biggest even integer number in the range [x, y] or -1 if not found.
    """

    # Check if y is less than x and return -1 if true
    if y < x:
        return -1

    # Initialize the max_even variable to -1
    max_even = -1
    
    # Iterate over the range from x to y (inclusive)
    for num in range(x, y + 1):
        # Check if the current number is even
        if num % 2 == 0:
            # If the current even number is greater than max_even, update max_even
            max_even = max(max_even, num)

    # Return the max_even
    return max_even


# Example use cases:
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
print(choose_num(10, 10))  # Output: 10
print(choose_num(11, 11))  # Output: -1
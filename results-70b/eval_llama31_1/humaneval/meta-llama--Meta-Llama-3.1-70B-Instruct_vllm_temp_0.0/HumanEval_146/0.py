def specialFilter(nums):
    """
    This function takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and 
    both first and last digits of a number are odd (1, 3, 5, 7, 9).
    
    Parameters:
    nums (list): A list of integers.
    
    Returns:
    int: The number of elements in the array that meet the specified conditions.
    """
    return len([num for num in nums if num > 10 and 
                 (num > 0 and num % 10 in [1, 3, 5, 7, 9] and 
                  int(str(abs(num))[0]) in [1, 3, 5, 7, 9])])

# Example usage:
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2
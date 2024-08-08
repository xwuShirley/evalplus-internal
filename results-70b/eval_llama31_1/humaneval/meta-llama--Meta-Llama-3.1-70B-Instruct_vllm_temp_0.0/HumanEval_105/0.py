def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list of strings representing the digit names.
    """
    # Filter out numbers outside the range 1-9
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    
    # Sort the filtered array
    sorted_arr = sorted(filtered_arr)
    
    # Reverse the sorted array
    reversed_arr = sorted_arr[::-1]
    
    # Map numbers to their corresponding names
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = [names[num - 1] for num in reversed_arr]
    
    return result
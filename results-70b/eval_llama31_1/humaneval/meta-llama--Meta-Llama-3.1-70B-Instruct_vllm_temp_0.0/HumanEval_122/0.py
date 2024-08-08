def add_elements(arr, k):
    """
    This function calculates the sum of the elements with at most two digits 
    from the first k elements of the given array.

    Parameters:
    arr (list): A non-empty array of integers.
    k (int): The number of elements to consider from the start of the array.

    Returns:
    int: The sum of the elements with at most two digits from the first k elements of arr.
    """
    
    # Initialize a variable to store the sum of the elements with at most two digits
    total = 0
    
    # Iterate over the first k elements of the array
    for i in range(k):
        # Check if the current element has at most two digits
        if len(str(arr[i])) <= 2:
            # Add the current element to the total sum
            total += arr[i]
    
    # Return the total sum
    return total
def pluck(arr):
    """
    This function plucks the node with the smallest even value from the given array.
    If multiple nodes with the same smallest even value are found, it returns the node with the smallest index.
    If there are no even values or the given array is empty, it returns an empty list.

    Args:
        arr (list): A list of non-negative integers representing a branch of a tree.

    Returns:
        list: A list containing the smallest even value and its index. If no even value is found, an empty list is returned.
    """
    
    # Initialize the smallest even value and its index with None
    smallest_even = None
    smallest_index = None
    
    # Iterate over the array with enumerate to get both the index and the value
    for i, value in enumerate(arr):
        # Check if the value is even
        if value % 2 == 0:
            # If smallest_even is None or the current value is smaller than smallest_even, update smallest_even and smallest_index
            if smallest_even is None or value < smallest_even:
                smallest_even = value
                smallest_index = i
                
    # If smallest_even is not None, return the smallest even value and its index, otherwise return an empty list
    if smallest_even is not None:
        return [smallest_even, smallest_index]
    else:
        return []
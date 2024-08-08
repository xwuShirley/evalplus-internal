def can_arrange(arr):
    """
    Returns the largest index of an element which is not greater than or equal to 
    the element immediately preceding it. If no such element exists then returns -1.

    Parameters:
    arr (list): The input list containing unique elements.

    Returns:
    int: The largest index of an element which is not greater than or equal to the element 
    immediately preceding it, or -1 if no such element exists.
    """
    
    # Initialize the answer as -1, assuming no such element exists
    answer = -1
    
    # Iterate over the list from the second element to the end
    for i in range(1, len(arr)):
        # If the current element is not greater than or equal to the previous element
        if arr[i] < arr[i-1]:
            # Update the answer as the current index
            answer = i
    
    # Return the answer
    return answer
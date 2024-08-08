def strange_sort_list(lst):
    """
    This function sorts a list of integers in a strange order. 
    The strange order is defined as starting with the minimum value, 
    then the maximum of the remaining integers, then the minimum and so on.

    Args:
        lst (list): A list of integers.

    Returns:
        list: The sorted list in strange order.
    """
    # Make a copy of the original list to avoid modifying it
    lst_copy = lst.copy()
    
    # Initialize an empty list to store the sorted elements
    sorted_lst = []
    
    # Continue the process until all elements are sorted
    while lst_copy:
        # Find the minimum element in the list and remove it
        min_val = min(lst_copy)
        lst_copy.remove(min_val)
        
        # Add the minimum element to the sorted list
        sorted_lst.append(min_val)
        
        # If there are still elements in the list, find the maximum element
        if lst_copy:
            # Find the maximum element in the list and remove it
            max_val = max(lst_copy)
            lst_copy.remove(max_val)
            
            # Add the maximum element to the sorted list
            sorted_lst.append(max_val)
    
    # Return the sorted list
    return sorted_lst
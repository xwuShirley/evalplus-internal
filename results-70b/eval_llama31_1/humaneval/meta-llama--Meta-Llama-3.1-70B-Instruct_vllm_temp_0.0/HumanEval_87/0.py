def get_row(lst, x):
    """
    This function finds the coordinates of a given integer x in a 2D list.
    
    Args:
    lst (list): A 2D list of integers.
    x (int): The integer to be searched in the list.
    
    Returns:
    list: A list of tuples, where each tuple contains the coordinates (row, column) of the integer x in the list.
    The coordinates are sorted first by row in ascending order, and then by column in descending order.
    """
    
    # Initialize an empty list to store the coordinates of x.
    coordinates = []
    
    # Iterate over each row in the list.
    for row_index, row in enumerate(lst):
        # Iterate over each element in the row.
        for col_index, element in enumerate(row):
            # Check if the element is equal to x.
            if element == x:
                # If it is, append the coordinates to the list.
                coordinates.append((row_index, col_index))
    
    # Sort the coordinates first by row in ascending order, and then by column in descending order.
    coordinates.sort(key=lambda x: (x[0], -x[1]))
    
    # Return the sorted list of coordinates.
    return coordinates
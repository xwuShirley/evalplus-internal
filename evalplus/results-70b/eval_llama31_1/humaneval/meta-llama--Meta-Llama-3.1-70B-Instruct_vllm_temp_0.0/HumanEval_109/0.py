def move_one_ball(arr):
    """
    This function checks if it is possible to get an array sorted in non-decreasing 
    order by performing right shift operation any number of times.
    
    Parameters:
    arr (list): The input list of integers.
    
    Returns:
    bool: True if it is possible to obtain the sorted array, False otherwise.
    """
    
    # If the array is empty, return True as per the problem statement
    if not arr:
        return True
    
    # Check if the array is already sorted
    if arr == sorted(arr):
        return True
    
    # Initialize a variable to store the minimum element in the array
    min_element = min(arr)
    
    # Find the index of the minimum element in the array
    min_index = arr.index(min_element)
    
    # Rotate the array to the right by 'min_index' positions
    rotated_arr = arr[-min_index:] + arr[:-min_index]
    
    # Check if the rotated array is sorted in non-decreasing order
    if rotated_arr == sorted(rotated_arr):
        return True
    
    # If none of the above conditions are met, return False
    return False
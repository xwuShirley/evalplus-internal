from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    This function filters a given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any python values.

    Returns:
        List[int]: A list containing only integers from the input list.
    """
    # Initialize an empty list to store the filtered integers
    filtered_list = []
    
    # Iterate over each value in the input list
    for value in values:
        # Check if the value is an integer
        if isinstance(value, int):
            # If the value is an integer, append it to the filtered list
            filtered_list.append(value)
    
    # Return the filtered list
    return filtered_list
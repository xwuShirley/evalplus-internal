from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    This function filters a list of strings and returns a new list containing only the strings that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings to be filtered.
        prefix (str): The prefix to filter the strings by.

    Returns:
        List[str]: A new list containing only the strings that start with the given prefix.
    """
    
    # Initialize an empty list to store the filtered strings
    filtered_strings = []
    
    # Iterate over each string in the input list
    for string in strings:
        # Check if the string starts with the given prefix
        if string.startswith(prefix):
            # If it does, add it to the filtered list
            filtered_strings.append(string)
    
    # Return the filtered list
    return filtered_strings
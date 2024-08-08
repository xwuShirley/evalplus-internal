from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    
    # Check if the input list is empty
    if not strings:
        # If the list is empty, return None
        return None
    
    # Initialize the longest string with the first string in the list
    longest_string = strings[0]
    
    # Iterate over the rest of the strings in the list
    for string in strings[1:]:
        # If the current string is longer than the longest string found so far
        if len(string) > len(longest_string):
            # Update the longest string
            longest_string = string
    
    # Return the longest string
    return longest_string
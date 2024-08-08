def how_many_times(string: str, substring: str) -> int:
    """
    This function finds how many times a given substring can be found in the original string.
    It counts overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    
    # Initialize a counter variable to store the number of occurrences
    count = 0
    
    # If the substring is empty, return 0
    if not substring:
        return 0
    
    # Iterate over the string with a sliding window of the length of the substring
    for i in range(len(string) - len(substring) + 1):
        # Check if the current window matches the substring
        if string[i:i+len(substring)] == substring:
            # If it matches, increment the counter
            count += 1
    
    # Return the total count
    return count
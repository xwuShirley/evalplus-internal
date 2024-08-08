from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    This function generates a list of all prefixes from shortest to longest of the input string.
    
    Args:
        string (str): The input string for which prefixes are to be generated.
    
    Returns:
        List[str]: A list of all prefixes from shortest to longest of the input string.
    """
    
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the string from the first character to the last
    for i in range(1, len(string) + 1):
        # Generate the prefix by slicing the string up to the current index
        prefix = string[:i]
        
        # Add the prefix to the list
        prefixes.append(prefix)
    
    # Return the list of prefixes
    return prefixes
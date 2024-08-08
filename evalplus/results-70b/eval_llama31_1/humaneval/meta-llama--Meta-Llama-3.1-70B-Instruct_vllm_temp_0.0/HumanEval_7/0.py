from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    This function filters an input list of strings and returns only the strings that contain a given substring.

    Args:
        strings (List[str]): The list of strings to be filtered.
        substring (str): The substring that the strings should contain.

    Returns:
        List[str]: The filtered list of strings.
    """
    # Use a list comprehension to iterate over the input list of strings
    # and include only the strings that contain the given substring
    return [string for string in strings if substring in string]
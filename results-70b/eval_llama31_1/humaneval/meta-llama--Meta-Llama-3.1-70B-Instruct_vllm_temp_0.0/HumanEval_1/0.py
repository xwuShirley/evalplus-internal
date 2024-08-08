from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string containing multiple groups of nested parentheses
    into separate strings and returns the list of those.

    :param paren_string: A string containing multiple groups of nested parentheses.
    :return: A list of strings, each containing a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to build a group of parentheses
    group = ''

    # Initialize a counter to keep track of open parentheses
    open_count = 0

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the counter
        if char == '(':
            open_count += 1
        # If the character is a close parenthesis, decrement the counter
        elif char == ')':
            open_count -= 1

        # Add the character to the group
        group += char

        # If the counter is zero, it means the group is complete, so add it to the list
        if open_count == 0:
            separate_groups.append(group)
            group = ''

    return separate_groups
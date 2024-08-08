from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it calculates the deepest level of nesting of parentheses.
    
    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.
    
    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group of parentheses.
    """
    
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum depth of each group
    max_depths = []
    
    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the maximum depth and current depth to 0
        max_depth = 0
        curr_depth = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current depth
            if char == '(':
                curr_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, curr_depth)
            # If the character is a closing parenthesis, decrement the current depth
            elif char == ')':
                curr_depth -= 1
        
        # Append the maximum depth of the current group to the list of maximum depths
        max_depths.append(max_depth)
    
    # Return the list of maximum depths
    return max_depths
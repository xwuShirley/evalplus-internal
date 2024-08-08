from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum element found until given moment in the sequence.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: A list of rolling maximum elements.
    """
    if not numbers:  # If the input list is empty, return an empty list.
        return []
    
    rolling_maxims = []  # Initialize an empty list to store the rolling maximums.
    max_so_far = numbers[0]  # Initialize the maximum element so far as the first element of the list.
    
    for num in numbers:  # Iterate through each number in the list.
        max_so_far = max(max_so_far, num)  # Update the maximum element so far.
        rolling_maxims.append(max_so_far)  # Append the maximum element so far to the list.
    
    return rolling_maxims

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
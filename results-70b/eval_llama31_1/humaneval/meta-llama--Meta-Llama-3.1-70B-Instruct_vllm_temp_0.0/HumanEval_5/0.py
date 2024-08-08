from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of numbers
    delimeter (int): The number to be inserted between every two consecutive elements

    Returns:
    List[int]: The resulting list with 'delimeter' inserted between every two consecutive elements
    """
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list with index
    for i, num in enumerate(numbers):
        # Append the current number to the result list
        result.append(num)
        
        # If it's not the last element, append the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    
    # Return the resulting list
    return result
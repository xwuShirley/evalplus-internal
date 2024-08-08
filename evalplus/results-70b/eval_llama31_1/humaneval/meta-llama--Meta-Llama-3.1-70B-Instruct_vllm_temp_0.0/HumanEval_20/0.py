from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    This function takes a list of numbers as input and returns a tuple of two numbers 
    that are closest to each other. The numbers in the tuple are in ascending order.

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple of two numbers that are closest to each other.
    """
    
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()  # Initialize with an empty tuple
    
    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is less than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    # Return the pair of numbers with the minimum difference
    return closest_pair
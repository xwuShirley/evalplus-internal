from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Count occurrences of each number
    counts = Counter(numbers)
    
    # Use a list comprehension to create a new list with only the numbers that occur once
    # The 'if counts[num] == 1' condition filters out numbers that occur more than once
    # The 'for num in numbers' loop ensures the order of numbers is preserved
    return [num for num in numbers if counts[num] == 1]
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    This function applies a linear transformation to the input list of numbers.
    The transformation scales the numbers such that the smallest number becomes 0 and the largest number becomes 1.

    Args:
        numbers: A list of numbers with at least two elements.

    Returns:
        A list of numbers that have been rescaled to the unit interval [0, 1].
    """

    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements.")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)  # Smallest number in the list
    max_val = max(numbers)  # Largest number in the list

    # Check if all numbers in the list are the same
    if min_val == max_val:
        return [0.0] * len(numbers)

    # Apply the linear transformation to each number in the list
    rescaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled_numbers
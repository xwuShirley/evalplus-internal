from typing import List
import statistics


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Initialize a list to store the absolute differences
    absolute_diff = []
    
    # Iterate over each number in the input list
    for num in numbers:
        # Calculate the absolute difference between the number and the mean
        diff = abs(num - mean)
        # Append the absolute difference to the list
        absolute_diff.append(diff)
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_diff)
    
    # Return the Mean Absolute Deviation
    return mad
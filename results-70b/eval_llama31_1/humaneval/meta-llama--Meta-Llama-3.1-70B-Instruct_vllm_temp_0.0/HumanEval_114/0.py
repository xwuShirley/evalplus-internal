def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The minimum sum of any non-empty sub-array.

    Example:
        >>> minSubArraySum([2, 3, 4, 1, 2, 4])
        1
        >>> minSubArraySum([-1, -2, -3])
        -6
    """
    min_sum = float('inf')
    current_sum = 0

    for num in nums:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)

    return min_sum
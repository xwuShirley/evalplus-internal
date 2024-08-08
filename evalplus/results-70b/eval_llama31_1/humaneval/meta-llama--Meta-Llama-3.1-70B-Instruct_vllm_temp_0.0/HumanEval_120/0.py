def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    :param arr: A list of integers
    :type arr: List[int]
    :param k: A positive integer
    :type k: int
    :return: A sorted list of length k with the maximum k numbers in arr
    :rtype: List[int]
    """

    # First, we sort the array in descending order to get the maximum numbers at the start
    arr.sort(reverse=True)
    
    # Then, we return the first k elements of the sorted array
    # This will be the maximum k numbers in the array
    return arr[:k]
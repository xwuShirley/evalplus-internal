def is_sorted(lst):
    """
    Returns True if the list is sorted in ascending order with no duplicates, False otherwise.
    
    :param lst: List of integers
    :return: Boolean
    """
    return lst == sorted(lst) and len(lst) == len(set(lst))
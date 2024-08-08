def total_match(lst1, lst2):
    """
    Returns the list with the total number of chars in all strings less than the other list.
    If both lists have the same number of chars, returns the first list.

    Args:
        lst1 (list[str]): The first list of strings.
        lst2 (list[str]): The second list of strings.

    Returns:
        list[str]: The list with fewer total chars.
    """
    def total_chars(lst):
        return sum(len(s) for s in lst)

    if total_chars(lst1) <= total_chars(lst2):
        return lst1
    else:
        return lst2
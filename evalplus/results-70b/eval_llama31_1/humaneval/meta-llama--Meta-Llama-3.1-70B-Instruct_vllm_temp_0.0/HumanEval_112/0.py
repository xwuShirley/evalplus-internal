def reverse_delete(s, c):
    """
    Delete all characters in s that are equal to any character in c, 
    then check if the result string is a palindrome.

    Args:
        s (str): The original string.
        c (str): The string containing characters to be deleted.

    Returns:
        tuple: A tuple containing the result string and a boolean indicating 
               whether the result string is a palindrome.
    """
    # delete all characters in s that are equal to any character in c
    result = ''.join([x for x in s if x not in c])
    
    # check if the result string is a palindrome
    is_palindrome = result == ''.join(reversed(result))
    
    return (result, is_palindrome)
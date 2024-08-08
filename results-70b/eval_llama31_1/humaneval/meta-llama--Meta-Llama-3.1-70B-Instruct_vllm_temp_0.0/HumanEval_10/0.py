def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:  # If the string is empty, return it as it is
        return string

    for i in range(len(string), 0, -1):  # Find the longest postfix that is a palindrome
        if is_palindrome(string[i - 1:]):
            return string + string[i - 1::-1]  # Append the reverse of the prefix to the string
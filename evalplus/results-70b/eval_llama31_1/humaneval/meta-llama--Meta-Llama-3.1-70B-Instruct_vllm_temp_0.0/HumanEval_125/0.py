def split_words(txt: str) -> list:
    """
    Splits a string into words based on whitespace or commas.
    If no whitespaces or commas are found, returns the count of lowercase letters with odd order in the alphabet.

    Args:
        txt (str): The input string to be split.

    Returns:
        list: A list of words if splitting is successful, otherwise an integer count of lowercase letters with odd order.

    Examples:
        >>> split_words("Hello world!")
        ["Hello", "world!"]
        >>> split_words("Hello,world!")
        ["Hello", "world!"]
        >>> split_words("abcdef")
        3
    """

    # First, try splitting on whitespace
    words = txt.split()
    if words:
        # If splitting on whitespace is successful, return the list of words
        return words

    # If no whitespaces are found, try splitting on commas
    words = txt.split(',')
    if words and any(words):
        # If splitting on commas is successful, return the list of words
        return words

    # If no commas are found, count the number of lowercase letters with odd order in the alphabet
    count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
    return count
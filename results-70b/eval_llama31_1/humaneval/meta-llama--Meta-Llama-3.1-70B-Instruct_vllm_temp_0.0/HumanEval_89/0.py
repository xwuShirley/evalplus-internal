def encrypt(s):
    """
    Encrypt a given string by rotating the alphabet.

    The alphabet is rotated in a manner such that the letters shift down 
    by two places.

    Parameters:
    s (str): The input string to be encrypted.

    Returns:
    str: The encrypted string.

    Example:
    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    >>> encrypt('gf')
    'kj'
    >>> encrypt('et')
    'ix'
    """
    shift = 4  # Two multiplied to two places equals four
    encrypted_string = ""

    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_string += encrypted_char
        else:
            encrypted_string += char

    return encrypted_string
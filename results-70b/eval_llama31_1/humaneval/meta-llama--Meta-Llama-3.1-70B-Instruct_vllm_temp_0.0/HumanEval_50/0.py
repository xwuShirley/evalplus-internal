def decode_shift(s: str):
    """
    Reverses the encoding done by the encode_shift function.
    
    Args:
    s (str): The encoded string.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
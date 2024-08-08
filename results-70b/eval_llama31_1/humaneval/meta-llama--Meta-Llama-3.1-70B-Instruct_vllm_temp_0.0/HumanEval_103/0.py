def rounded_avg(n, m):
    """
    Compute the rounded average of integers from n through m and convert to binary.

    Args:
        n (int): Start of the range (inclusive).
        m (int): End of the range (inclusive).

    Returns:
        str: Binary representation of the rounded average, or -1 if n > m.
    """
    if n > m:
        return -1

    # Calculate the sum of integers from n to m
    total = sum(range(n, m + 1))

    # Calculate the average and round to the nearest integer
    avg = round(total / (m - n + 1))

    # Convert the average to binary and return as a string
    return bin(avg)[2:]  # [2:] to remove the '0b' prefix
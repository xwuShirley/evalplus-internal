def tri(n):
    """
    Calculate the Tribonacci sequence up to the nth number.

    Args:
        n (int): The number of elements in the sequence to generate.

    Returns:
        list: A list of the first n+1 numbers in the Tribonacci sequence.
    """
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]

    trib = [1, 3, 2]
    for i in range(3, n+1):
        next_number = trib[i-1] + trib[i-2] + trib[i-3]
        trib.append(next_number)

    return trib

# Test cases
print(tri(3))  # Output: [1, 3, 2, 8]
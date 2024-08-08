def get_max_triples(n):
    """
    This function generates an array a of length n where each element a[i] = i * i - i + 1.
    It then returns the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Args:
        n (int): A positive integer.

    Returns:
        int: The number of triples (a[i], a[j], a[k]) where a[i] + a[j] + a[k] is a multiple of 3.
    """

    # Initialize an empty list to store the array a.
    a = []

    # Generate the array a.
    for i in range(1, n + 1):
        # Calculate the value of a[i] = i * i - i + 1.
        a.append(i * i - i + 1)

    # Initialize a variable to store the count of triples.
    count = 0

    # Iterate over the array a to find the triples.
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if the sum of the triple is a multiple of 3.
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    # If it is, increment the count.
                    count += 1

    # Return the count of triples.
    return count
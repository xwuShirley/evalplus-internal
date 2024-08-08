def count_up_to(n):
    """
    Returns an array of the first n integers that are prime numbers and less than n.

    Args:
        n (int): A non-negative integer.

    Returns:
        list: A list of prime numbers less than n.
    """
    def is_prime(num):
        """Checks if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
        if len(primes) == n:
            break
    return primes
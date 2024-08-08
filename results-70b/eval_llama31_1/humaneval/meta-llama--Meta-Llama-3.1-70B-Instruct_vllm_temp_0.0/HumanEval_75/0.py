def is_prime(n):
    """
    Helper function to check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_multiply_prime(a):
    """
    Returns True if the given number is the multiplication of 3 prime numbers, False otherwise.
    """
    # We know that a is less than 100, so we can limit our search to prime numbers up to a
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            remaining_factor = a // i
            for j in range(2, remaining_factor):
                if is_prime(j) and remaining_factor % j == 0:
                    last_factor = remaining_factor // j
                    if is_prime(last_factor):
                        return True
    return False


# Example usage:
print(is_multiply_prime(30))  # Output: True
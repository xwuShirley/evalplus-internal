def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return the value of x if n is a prime number and return the value of y otherwise."""
    if is_prime(n):
        return x
    else:
        return y
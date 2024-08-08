def skjkasdkd(lst):
    """
    Finds the largest prime value in the list and returns the sum of its digits.

    Args:
    lst (list): A list of integers.

    Returns:
    int: The sum of the digits of the largest prime number in the list.
    """
    def is_prime(n):
        """
        Checks if a number is prime.

        Args:
        n (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime_sum = 0
    for num in lst:
        if is_prime(num):
            digit_sum = sum(int(digit) for digit in str(num))
            max_prime_sum = max(max_prime_sum, digit_sum)
    
    return max_prime_sum
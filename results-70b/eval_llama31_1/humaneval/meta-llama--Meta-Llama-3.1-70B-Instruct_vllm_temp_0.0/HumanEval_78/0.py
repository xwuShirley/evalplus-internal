def hex_key(num):
    """
    Count the number of hexadecimal digits that are primes in a given string.

    Args:
    num (str): A string containing hexadecimal digits.

    Returns:
    int: The count of prime hexadecimal digits.

    Examples:
    >>> hex_key("AB")
    1
    >>> hex_key("1077E")
    2
    >>> hex_key("ABED1A33")
    4
    >>> hex_key("123456789ABCDEF0")
    6
    >>> hex_key("2020")
    2
    """

    # Define the mapping of hexadecimal digits to their decimal equivalents
    hex_to_decimal = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    # Define a function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Initialize a counter for prime hexadecimal digits
    prime_count = 0

    # Iterate over each character in the input string
    for char in num:
        # Convert the hexadecimal digit to its decimal equivalent
        decimal = hex_to_decimal[char]
        
        # Check if the decimal equivalent is a prime number
        if is_prime(decimal):
            # If it is a prime number, increment the counter
            prime_count += 1

    # Return the count of prime hexadecimal digits
    return prime_count
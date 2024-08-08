def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # First, ensure that a is less than or equal to b
    if a > b:
        a, b = b, a
    
    # Generate a list of even numbers between a and b
    even_numbers = [i for i in range(a, b+1) if i % 2 == 0]
    
    # Return the list of even numbers
    return even_numbers
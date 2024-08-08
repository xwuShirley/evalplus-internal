def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial.
    
    Args:
    xs (list): A list of coefficients of a polynomial, where xs[i] is the coefficient of x^i.
    
    Returns:
    list: A list of coefficients of the derivative of the polynomial.
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coefficients = []
    
    # The derivative of a constant is zero, so we can start from the second coefficient (i.e., the coefficient of x)
    for i in range(1, len(xs)):
        # The derivative of x^i is i * x^(i - 1), so we multiply the coefficient of x^i by i
        derivative_coefficients.append(xs[i] * i)
    
    # Return the coefficients of the derivative
    return derivative_coefficients
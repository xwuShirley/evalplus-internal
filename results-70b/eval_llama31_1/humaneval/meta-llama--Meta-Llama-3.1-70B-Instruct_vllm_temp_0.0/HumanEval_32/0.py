import math

def find_zero(xs: list):
    """
    Finds a zero of the polynomial with coefficients xs.
    Requires xs to have an even number of coefficients and
    the largest non-zero coefficient to be at an even index.
    Returns only one zero point, even if there are multiple.
    
    Parameters:
    xs (list): coefficients of the polynomial
    
    Returns:
    float: a zero of the polynomial
    """
    # Check if xs has an even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    
    # Find the largest non-zero coefficient and its index
    max_coeff_idx = max((i for i, coeff in enumerate(xs) if coeff != 0), key=lambda i: xs[i])
    
    # Check if the largest non-zero coefficient is at an even index
    if max_coeff_idx % 2 != 0:
        raise ValueError("Largest non-zero coefficient must be at an even index")
    
    # Use the fact that the polynomial is divisible by (x - (-coeffs[max_coeff_idx] / coeffs[max_coeff_idx - 1]))
    if max_coeff_idx == 0:
        return -xs[max_coeff_idx] / xs[max_coeff_idx - 1]
    else:
        return -xs[max_coeff_idx] / xs[max_coeff_idx - 1]
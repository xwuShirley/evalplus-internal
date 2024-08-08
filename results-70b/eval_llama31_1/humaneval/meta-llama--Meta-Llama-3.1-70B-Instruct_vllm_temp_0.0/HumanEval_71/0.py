import math

def triangle_area(a, b, c):
    """
    Calculate the area of a triangle given the lengths of its three sides.

    Args:
    a (float): The length of the first side.
    b (float): The length of the second side.
    c (float): The length of the third side.

    Returns:
    float: The area of the triangle rounded to 2 decimal points if the three sides form a valid triangle.
           Otherwise, returns -1.
    """
    
    # Check if the given sides can form a valid triangle
    if (a + b > c) and (a + c > b) and (b + c > a):
        # Calculate the semi-perimeter of the triangle
        s = (a + b + c) / 2
        
        # Calculate the area of the triangle using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        # Return the area rounded to 2 decimal points
        return round(area, 2)
    else:
        # Return -1 if the sides do not form a valid triangle
        return -1
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    This function calculates the sum and product of a given list of integers.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    The empty sum is considered to be 0 and the empty product is considered to be 1.
    """

    # Initialize sum and product with their respective identities
    sum_of_numbers = 0
    product_of_numbers = 1

    # Iterate over each number in the list
    for number in numbers:
        # Add the number to the sum
        sum_of_numbers += number
        # Multiply the product by the number
        product_of_numbers *= number

    # Return the sum and product as a tuple
    return sum_of_numbers, product_of_numbers
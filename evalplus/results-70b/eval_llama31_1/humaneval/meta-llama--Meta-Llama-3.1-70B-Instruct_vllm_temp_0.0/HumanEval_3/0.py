from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the operation
        balance += operation
        
        # If the balance is less than zero, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True by now, the balance never fell below zero
    return False
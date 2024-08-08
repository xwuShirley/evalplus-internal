def do_algebra(operator, operand):
    """
    Evaluates an algebraic expression built from the given operator and operand lists.

    Args:
    operator (list): A list of basic algebra operations.
    operand (list): A list of non-negative integers.

    Returns:
    int: The result of the evaluated algebraic expression.
    """

    # Check if the length of operator list is equal to the length of operand list minus one
    if len(operator) != len(operand) - 1:
        raise ValueError("The length of operator list must be equal to the length of operand list minus one")

    # Check if operator list has at least one operator, and operand list has at least two operands
    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("Operator list must have at least one operator, and operand list must have at least two operands")

    # Check if all operands are non-negative integers
    if not all(isinstance(x, int) and� >= 0 for x in operand):
        raise ValueError("All operands must be non-negative integers")

    # Check if all operators are valid
    valid_operators = ['+', '-', '*', '//', '**']
    if not all(op in valid_operators for op in operator):
        raise ValueError("Invalid operator. Only '+', '-', '*', '//', '**' are allowed")

    # Initialize the result with the first operand
    result = operand[0]

    # Iterate over the operator and operand lists to build the algebraic expression
    for i in range(len(operator)):
        op = operator[i]
        num = operand[i + 1]
        
        # Use a dictionary to map operator symbols to their corresponding functions
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '//': lambda x, y: x // y,
            '**': lambda x, y: x ** y
        }
        
        # Apply the operation to the current result and the next operand
        result = operations[op](result, num)

    return result
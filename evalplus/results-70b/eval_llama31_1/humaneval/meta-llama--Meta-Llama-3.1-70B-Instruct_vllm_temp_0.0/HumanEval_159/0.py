def eat(number, need, remaining):
    """
    This function calculates the total number of carrots eaten after the meals 
    and the number of carrots left after the meals.

    Args:
    number (int): The number of carrots already eaten.
    need (int): The number of carrots needed to eat.
    remaining (int): The number of remaining carrots in stock.

    Returns:
    list: A list containing the total number of carrots eaten and the number of carrots left.
    """
    
    # Calculate the total number of carrots needed to eat
    total_needed = number + need
    
    # Calculate the total number of carrots eaten
    total_eaten = min(total_needed, number + remaining)
    
    # Calculate the number of carrots left
    carrots_left = max(0, remaining - (total_eaten - number))
    
    # Return the total number of carrots eaten and the number of carrots left
    return [total_eaten, carrots_left]
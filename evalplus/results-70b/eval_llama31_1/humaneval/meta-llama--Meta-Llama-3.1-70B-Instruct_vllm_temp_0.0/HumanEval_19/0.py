from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a string of space-delimited numberals from 'zero' to 'nine',
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A string of space-delimited numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # First, we define a dictionary that maps number words to their numerical values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Then, we split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # We use the sorted function with a custom sorting key to sort the numbers
    # The custom key is a lambda function that returns the numerical value of a number word
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Finally, we join the sorted list back into a string with spaces in between
    sorted_str: str = ' '.join(sorted_list)
    
    return sorted_str
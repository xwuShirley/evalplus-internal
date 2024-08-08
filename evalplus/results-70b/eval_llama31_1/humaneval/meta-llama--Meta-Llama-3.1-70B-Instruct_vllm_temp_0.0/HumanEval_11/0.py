from typing import List


def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    Both strings should consist only of 1s and 0s.
    
    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if the lengths of the input strings are equal
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length")
    
    # Initialize an empty list to store the result of XOR operation
    result_list: List[str] = []
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Check if the characters are either '0' or '1'
        if char_a not in '01' or char_b not in '01':
            raise ValueError("Input strings must consist only of 1s and 0s")
        
        # Perform XOR operation using the '^' operator
        # Convert the result back to a string using str()
        # Append the result to the list
        result_list.append(str(int(char_a) ^ int(char_b)))
    
    # Join the list of strings into a single string using ''.join()
    result: str = ''.join(result_list)
    
    return result
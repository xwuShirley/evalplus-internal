def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    
    # Convert the string to lowercase to handle both lowercase and uppercase vowels
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Initialize a set of vowels
    vowels = set('aeiou')
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char in vowels:
            # If it is, increment the counter
            count += 1
        # Check if the character is 'y' and it's at the end of the string
        elif char == 'y' and i == len(s) - 1:
            # If it is, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count
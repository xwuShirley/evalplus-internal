def anti_shuffle(s):
    """
    This function takes a string and returns an ordered version of it.
    The ordered version of a string is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in ascending order 
    based on ascii value. The order of words and blank spaces in the sentence is kept.

    Parameters:
    s (str): The input string.

    Returns:
    str: The ordered version of the input string.
    """
    
    # Split the string into words
    words = s.split(' ')
    
    # Initialize an empty list to store the ordered words
    ordered_words = []
    
    # Iterate over each word in the list of words
    for word in words:
        # Order the characters in the word based on their ascii value
        ordered_word = ''.join(sorted(word))
        
        # Add the ordered word to the list of ordered words
        ordered_words.append(ordered_word)
    
    # Join the ordered words back into a string separated by spaces
    ordered_string = ' '.join(ordered_words)
    
    # Return the ordered string
    return ordered_string
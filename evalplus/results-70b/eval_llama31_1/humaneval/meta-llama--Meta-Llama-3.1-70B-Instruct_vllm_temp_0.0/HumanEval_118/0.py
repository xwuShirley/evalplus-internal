def get_closest_vowel(word):
    """
    This function finds the closest vowel that stands between two consonants from the right side of the word.

    Parameters:
    word (str): The input string.

    Returns:
    str: The closest vowel that stands between two consonants from the right side of the word. 
         Returns empty string if no such vowel is found.
    """
    
    # Define the vowels
    vowels = "aeiouAEIOU"
    
    # Iterate over the word from the right side
    for i in range(len(word) - 1, 0, -1):
        
        # Check if the current character is a vowel
        if word[i] in vowels:
            
            # Check if the previous and next characters are not vowels
            if word[i - 1] not in vowels and word[i + 1] not in vowels:
                
                # Return the found vowel
                return word[i]
    
    # If no such vowel is found, return an empty string
    return ""
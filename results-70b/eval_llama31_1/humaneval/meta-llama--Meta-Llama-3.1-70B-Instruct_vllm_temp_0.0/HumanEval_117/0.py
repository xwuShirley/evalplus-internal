def select_words(s, n):
    """
    Given a string s and a natural number n, returns a list of all words 
    from string s that contain exactly n consonants, in order these words 
    appear in the string s.

    Args:
        s (str): Input string.
        n (int): Natural number representing the number of consonants.

    Returns:
        list: List of words with exactly n consonants.
    """
    # Split the string into a list of words
    words = s.split()
    
    # Initialize an empty list to store the words with exactly n consonants
    result = []
    
    # Define the set of vowels
    vowels = set('aeiouAEIOU')
    
    # Iterate over each word in the list
    for word in words:
        # Initialize a counter for the number of consonants in the word
        consonant_count = 0
        
        # Iterate over each character in the word
        for char in word:
            # If the character is not a vowel and is an alphabet, increment the consonant count
            if char not in vowels and char.isalpha():
                consonant_count += 1
        
        # If the consonant count equals n, add the word to the result list
        if consonant_count == n:
            result.append(word)
    
    # Return the list of words with exactly n consonants
    return result

# Test cases
print(select_words("Mary had a little lamb", 4))  # ==> ["little"]
print(select_words("Mary had a little lamb", 3))  # ==> ["Mary", "lamb"]
print(select_words("simple white space", 2))  # ==> []
print(select_words("Hello world", 4))  # ==> ["world"]
print(select_words("Uncle sam", 3))  # ==> ["Uncle"]
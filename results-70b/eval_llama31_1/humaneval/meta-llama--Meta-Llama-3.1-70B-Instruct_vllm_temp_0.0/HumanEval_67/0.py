def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.
    
    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
             The string should be in the format "X apples and Y oranges" where X and Y are integers.
    n (int): The total number of fruits in the basket.
    
    Returns:
    int: The number of mango fruits in the basket.
    """
    # Split the string into parts based on the word "and"
    parts = s.split(" and ")
    
    # Extract the number of apples and oranges from the string
    apples = int(parts[0].split()[0])
    oranges = int(parts[1].split()[0])
    
    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Example use cases:
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
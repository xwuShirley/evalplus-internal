def unique_digits(x):
    def has_even_digit(n):
        return any(int(digit) % 2 == 0 for digit in str(n))
    
    return sorted([n for n in x if not has_even_digit(n)])